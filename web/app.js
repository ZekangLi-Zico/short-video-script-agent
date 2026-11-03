"use strict";
const $ = (id) => document.getElementById(id);
const actionNames = {
  search_materials: "检索素材",
  write_script: "生成 / 修订脚本",
  estimate_duration: "估算时长",
  check_rules: "检查事实与规则",
  finish: "结束任务",
  model_error: "模型调用失败",
  invalid_model_action: "修正无效动作",
};
const statusNames = {
  completed: "检查通过",
  needs_input: "需要补充",
  blocked: "未完成",
  step_limit: "达到步数上限",
  invalid_input: "输入无效",
  cancelled: "已停止",
  running: "运行中",
  error: "运行失败",
  idle: "待运行",
};
const presetHints = {
  normal: "检索产品资料，生成并检查一份脚本。",
  missing_information: "目标时长留空，预期提示补充关键信息。",
  no_material: "使用没有资料的产品，预期补查后请求补充。",
  tool_failure: "素材检索持续失败，预期明确停止。",
  recoverable_failure: "第一次检索失败，观察模型是否恢复。",
  over_duration: "已载入 38 秒旧稿，观察检查、修订和复检。",
  rule_revision: "旧稿含“效率提升80%”，观察模型发现并删除无依据宣传。",
  impossible_duration: "1 秒无法满足最短镜头要求，预期明确说明缺口。",
};
let config,
  currentId = null,
  currentJob = null,
  pollTimer = null,
  timerInterval = null,
  busy = false,
  traceLength = -1,
  pollError = false;

function node(tag, className, text) {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text !== undefined) element.textContent = text;
  return element;
}
function error(message) {
  $("global-error").textContent = message;
  $("global-error").hidden = !message;
}
async function request(path, options = {}) {
  const response = await fetch(path, options);
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || "服务请求失败");
  return data;
}
function post(path, body) {
  return request(path, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-Local-Token": config.token,
    },
    body: JSON.stringify(body),
  });
}
function setBusy(value) {
  busy = value;
  $("form-fields").disabled = value;
  $("history").disabled = value;
  $("cancel-button").hidden = !value;
  $("offline-demo").disabled = value;
  $("run-button").querySelector("span").textContent = value
    ? "正在生成与检查…"
    : "生成并检查";
}
function switchTab(name) {
  document.querySelectorAll("[data-tab]").forEach((button) => {
    const active = button.dataset.tab === name;
    button.setAttribute("aria-selected", String(active));
    button.tabIndex = active ? 0 : -1;
    $("panel-" + button.dataset.tab).hidden = !active;
  });
}
function providerHint() {
  const mode = $("provider").value;
  $("provider-hint").textContent =
    mode === "mock"
      ? "立即体验固定流程，不消耗模型额度；不证明真实模型决策。"
      : mode === "api"
        ? "使用服务启动时配置的模型 API，密钥不进入页面。"
        : "调用本机已登录的 Codex，通常需要一到数分钟。";
  $("run-note").textContent =
    mode === "mock"
      ? "离线演练不会调用真实模型。"
      : "真实模型运行会使用当前账号的额度。";
}
function populateFields(r, failures = {}) {
  for (const [field, key] of [
    ["topic", "topic"],
    ["audience", "audience"],
    ["platform", "platform"],
    ["target-seconds", "target_seconds"],
    ["style", "style"],
    ["product", "product_id"],
  ])
    $(field).value = r[key] ?? "";
  $("initial-script").value = r.initial_script
    ? JSON.stringify(r.initial_script, null, 2)
    : "";
  const fault = Object.entries(failures)[0];
  $("fault").value = fault ? fault.join(":") : "none";
  $("advanced").open = Boolean(r.initial_script || fault);
}
function applyPreset(id) {
  const preset = config.presets.find((p) => p.id === id);
  if (!preset) {
    $("preset-hint").textContent = "填写自己的需求，或选择一个预设场景。";
    return;
  }
  populateFields(preset.request, preset.failures);
  $("preset-hint").textContent = presetHints[id];
  error("");
}
function restoreForm(job) {
  populateFields(job.request, job.failures);
  $("preset").value = job.scenario_id || "custom";
  $("preset-hint").textContent = "已载入这条记录的原始需求，可修改后重新运行。";
  $("provider").value = job.provider;
  providerHint();
}
function collect() {
  const r = {
    topic: $("topic").value.trim(),
    audience: $("audience").value.trim(),
    platform: $("platform").value,
    style: $("style").value.trim(),
    product_id: $("product").value,
  };
  if ($("target-seconds").value !== "")
    r.target_seconds = Number($("target-seconds").value);
  if ($("initial-script").value.trim()) {
    try {
      r.initial_script = JSON.parse($("initial-script").value);
    } catch {
      throw new Error("旧稿 JSON 格式有误，请检查括号、引号和逗号。");
    }
  }
  const [name, count] = $("fault").value.split(":");
  return {
    request: r,
    provider: $("provider").value,
    scenario_id: $("preset").value,
    failures: name === "none" ? {} : { [name]: Number(count) },
  };
}

function elapsed() {
  if (!currentJob) return;
  const seconds = Math.max(
    0,
    Math.floor((Date.now() - Date.parse(currentJob.created_at)) / 1000),
  );
  if (currentJob.state === "running")
    $("run-detail").textContent =
      `第 ${currentJob.step || 1} / 12 步 · 已等待 ${seconds} 秒`;
}
function renderScript(job) {
  const script = job.script;
  $("script-empty").hidden = !!script;
  $("script-content").hidden = !script;
  $("summary-bar").hidden = !script;
  if (!script) return;
  $("script-title").textContent = script.title;
  const successful = job.result?.status === "completed";
  $("draft-label").textContent = successful
    ? "当前稿 · 检查通过"
    : "草稿 · 尚未通过完整检查";
  const duration = job.duration;
  $("duration-value").textContent = duration?.ok
    ? `${duration.total_seconds} / ${duration.target_seconds} 秒`
    : "待检查";
  const checked = job.rules_check;
  $("rule-value").textContent = checked?.ok
    ? checked.passed
      ? "通过"
      : "待修订"
    : checked
      ? "工具失败"
      : "待检查";
  const citations = checked?.citations || [];
  $("source-value").textContent = String(
    new Set(citations.map((c) => c.source_id)).size,
  );
  $("shots").replaceChildren();
  let cursor = 0;
  script.shots.forEach((shot, i) => {
    const item = node("article", "shot");
    const time = node("div", "shot-time");
    time.append(node("b", "", `分镜 ${i + 1}`));
    const seconds = duration?.shots?.[i]?.estimated_seconds;
    if (seconds !== undefined) {
      time.append(
        node(
          "span",
          "",
          `${cursor.toFixed(1)}–${(cursor + seconds).toFixed(1)}s`,
        ),
      );
      cursor += seconds;
    } else time.append(node("span", "", "待估时"));
    const content = node("div", "shot-body");
    content.append(
      node("h3", "", shot.visual),
      node("p", "narration", shot.blocks.map((b) => b.text).join("")),
    );
    const sources = shot.blocks.filter((b) => b.source_id);
    const holder = node("div", "citations");
    sources.forEach((b) => {
      const cite = node("span", "citation", `${b.source_id} · ${b.fact_id}`);
      cite.title = b.text;
      holder.append(cite);
    });
    if (!sources.length)
      holder.append(
        node(
          "span",
          "creative-note",
          checked?.passed ? "已检查的非事实连接语" : "未标注事实来源的文案",
        ),
      );
    content.append(holder);
    item.append(time, content);
    $("shots").append(item);
  });
  $("risks").replaceChildren();
  $("risks").hidden = !checked?.issues?.length;
  if (checked?.issues?.length) {
    $("risks").append(node("strong", "", "本次检查发现的问题"));
    const list = node("ul");
    checked.issues.forEach((issue) =>
      list.append(
        node(
          "li",
          "",
          `${issue.location || "文案"}：${issue.code}${issue.text ? " · " + issue.text : ""}${issue.phrase ? " · " + issue.phrase : ""}`,
        ),
      ),
    );
    $("risks").append(list);
  }
}
function observationSummary(entry) {
  const o = entry.observation;
  if (!o.ok) return o.message || o.error || "工具未成功返回";
  if (entry.action === "search_materials")
    return `检索“${entry.arguments.query}”：找到 ${o.count} 条素材`;
  if (entry.action === "estimate_duration")
    return `预计 ${o.total_seconds} 秒 / 上限 ${o.target_seconds} 秒${o.passed ? "，符合上限" : "，需要压缩脚本"}`;
  if (entry.action === "check_rules")
    return o.passed
      ? `检查通过，核对 ${o.citations.length} 处事实引用`
      : `发现 ${o.issues.length} 项风险，需要修订或补充`;
  if (entry.action === "finish") return statusNames[o.status] || o.status;
  return o.message || "执行完成";
}
function renderTrace(job) {
  const trace = job.trace || [];
  $("trace-count").textContent = trace.length;
  if (trace.length !== traceLength) {
    const open = new Set(
      [...$("timeline").querySelectorAll("details[open]")].map(
        (x) => x.dataset.step,
      ),
    );
    $("timeline").replaceChildren();
    trace.forEach((entry) => {
      const li = node("li", "trace-step");
      li.append(node("span", "step-number", String(entry.step)));
      const header = node("div", "step-header");
      header.append(
        node("strong", "", actionNames[entry.action] || entry.action),
      );
      const warning =
        !entry.observation.ok || entry.observation.passed === false;
      header.append(
        node(
          "span",
          "step-outcome" + (warning ? " warning" : ""),
          warning ? "需要处理" : "已执行",
        ),
      );
      if (entry.elapsed_ms)
        header.append(
          node("small", "", `${(entry.elapsed_ms / 1000).toFixed(1)} s`),
        );
      li.append(
        header,
        node("p", "step-basis", entry.decision_basis),
        node("p", "step-summary", observationSummary(entry)),
      );
      const details = node("details");
      details.dataset.step = String(entry.step);
      details.open = open.has(String(entry.step));
      details.append(
        node("summary", "", "查看参数与返回结果"),
        node(
          "pre",
          "",
          JSON.stringify(
            { arguments: entry.arguments, observation: entry.observation },
            null,
            2,
          ),
        ),
      );
      li.append(details);
      $("timeline").append(li);
    });
    traceLength = trace.length;
  }
  $("trace-empty").hidden = trace.length > 0 || job.state === "running";
  $("trace-empty").textContent = "本次在执行工具前结束，原因见上方提示。";
  $("thinking").hidden = job.state !== "running";
  $("thinking-title").textContent = job.cancel_requested
    ? "正在等待当前调用结束"
    : "模型正在决定下一步";
  $("thinking-detail").textContent = job.cancel_requested
    ? "不会执行下一步动作，已有结果会保留。"
    : job.provider === "mock"
      ? "离线桩正在执行本地工具。"
      : "当前调用完成后，将显示实际执行结果。";
}
function humanMessage(message) {
  const labels = {
    target_seconds: "目标时长",
    topic: "主题",
    audience: "给谁看",
    platform: "发布平台",
    style: "表达风格",
    product_id: "产品资料",
  };
  return message.replace(
    /target_seconds|product_id|audience|platform|topic|style/g,
    (key) => labels[key],
  );
}
function render(job) {
  currentJob = job;
  const status =
    job.state === "running"
      ? "running"
      : job.state === "error"
        ? "error"
        : job.result?.status || "idle";
  $("status-badge").className = "status-badge " + status;
  $("status-badge").textContent = statusNames[status] || status;
  $("offline-banner").hidden = job.provider !== "mock";
  $("result-message").hidden = !job.result?.message && !job.error;
  $("result-message").textContent = humanMessage(
    job.error || job.result?.message || "",
  );
  $("result-message").className =
    "result-message" + (status !== "completed" ? " problem" : "");
  $("run-detail").textContent =
    job.state === "running"
      ? "准备模型调用…"
      : `${job.provider === "mock" ? "离线演练" : "真实模型"} · ${job.trace.length} 个执行步骤`;
  $("cancel-button").disabled = job.cancel_requested;
  $("cancel-button").textContent = job.cancel_requested
    ? "等待当前调用结束…"
    : "停止后续步骤";
  renderScript(job);
  renderTrace(job);
  $("raw-output").textContent = JSON.stringify(
    job.result || {
      status: job.state,
      script: job.script,
      duration: job.duration,
      rules_check: job.rules_check,
    },
    null,
    2,
  );
  $("downloads").hidden = !job.saved;
  for (const [id, file] of [
    ["download-script", "script.md"],
    ["download-trace", "trace.jsonl"],
    ["download-result", "output.json"],
  ])
    $(id).href = `/api/runs/${job.id}/download/${file}`;
  $("save-note").textContent = job.saved
    ? `记录已保存 · ${job.id.slice(0, 8)}`
    : "运行记录会保存在本机，便于复验。";
  elapsed();
}
async function recent() {
  const jobs = await request("/api/runs");
  $("history").replaceChildren(
    node("option", "", jobs.length ? "选择一条记录" : "暂无记录"),
  );
  $("history").firstChild.value = "";
  jobs.forEach((job) => {
    const option = node(
      "option",
      "",
      `${new Date(job.created_at).toLocaleString("zh-CN", { month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit" })} · ${job.provider === "mock" ? "演练" : "模型"} · ${statusNames[job.status || job.state]} · ${job.topic.slice(0, 15)}`,
    );
    option.value = job.id;
    $("history").append(option);
  });
  if (currentId) $("history").value = currentId;
}
async function watch(id, restore = false) {
  if (currentId !== id) return;
  clearTimeout(pollTimer);
  try {
    const job = await request(`/api/runs/${id}`);
    if (currentId !== id) return;
    if (pollError) {
      error("");
      pollError = false;
    }
    if (restore) restoreForm(job);
    render(job);
    setBusy(job.state === "running");
    if (job.state === "running") pollTimer = setTimeout(() => watch(id), 900);
    else {
      clearInterval(timerInterval);
      await recent();
    }
  } catch (e) {
    if (currentId !== id) return;
    pollError = true;
    error(`暂时无法读取进度：${e.message}。若服务仍在运行，将自动重试。`);
    pollTimer = setTimeout(() => watch(id, restore), 3000);
  }
}
async function start(event) {
  event?.preventDefault();
  if (busy || !config) return;
  try {
    const body = collect();
    error("");
    setBusy(true);
    const answer = await post("/api/runs", body);
    currentId = answer.id;
    traceLength = -1;
    pollError = false;
    localStorage.setItem("script-agent-last-run", currentId);
    switchTab("trace");
    clearInterval(timerInterval);
    timerInterval = setInterval(elapsed, 1000);
    await recent();
    await watch(currentId);
    if (matchMedia("(max-width:760px)").matches)
      document
        .querySelector(".result-panel")
        .scrollIntoView({ behavior: "smooth", block: "start" });
  } catch (e) {
    error(e.message);
    setBusy(false);
  }
}

$("brief-form").addEventListener("input", (event) => {
  if (["preset", "provider"].includes(event.target.id)) return;
  $("preset").value = "custom";
  $("preset-hint").textContent = "需求已修改，将按当前内容运行。";
});
$("brief-form").addEventListener("submit", start);
$("provider").addEventListener("change", providerHint);
$("preset").addEventListener("change", () => applyPreset($("preset").value));
$("reset-button").addEventListener("click", () => {
  $("preset").value = "normal";
  applyPreset("normal");
});
$("offline-demo").addEventListener("click", () => {
  $("provider").value = "mock";
  providerHint();
  start();
});
$("cancel-button").addEventListener("click", async () => {
  if (!currentId) return;
  try {
    await post(`/api/runs/${currentId}/cancel`, {});
    await watch(currentId);
  } catch (e) {
    error(e.message);
  }
});
$("history").addEventListener("change", () => {
  if (!$("history").value) return;
  currentId = $("history").value;
  traceLength = -1;
  localStorage.setItem("script-agent-last-run", currentId);
  watch(currentId, true);
});
document.querySelectorAll("[data-tab]").forEach((button, index) => {
  button.addEventListener("click", () => switchTab(button.dataset.tab));
  button.addEventListener("keydown", (event) => {
    if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
    event.preventDefault();
    const tabs = [...document.querySelectorAll("[data-tab]")];
    const next =
      event.key === "Home"
        ? 0
        : event.key === "End"
          ? tabs.length - 1
          : (index + (event.key === "ArrowRight" ? 1 : -1) + tabs.length) %
            tabs.length;
    switchTab(tabs[next].dataset.tab);
    tabs[next].focus();
  });
});
async function init() {
  try {
    config = await request("/api/config");
    $("preset").replaceChildren();
    const custom = node("option", "", "自定义需求");
    custom.value = "custom";
    $("preset").append(custom);
    config.presets.forEach((p) => {
      const option = node("option", "", p.name);
      option.value = p.id;
      $("preset").append(option);
    });
    config.materials.forEach((material) => {
      const block = node("div", "material-item");
      block.append(node("strong", "", `${material.id} · ${material.title}`));
      material.facts.forEach((fact) => block.append(node("p", "", fact.text)));
      $("materials").append(block);
    });
    $("provider").querySelector("[value=api]").disabled = !config.api_available;
    if (!config.codex_available) $("provider").value = "mock";
    providerHint();
    $("preset").value = "normal";
    applyPreset("normal");
    await recent();
    const saved = localStorage.getItem("script-agent-last-run");
    const known = [...$("history").options].map((o) => o.value);
    currentId = config.active_id || (known.includes(saved) ? saved : null);
    if (currentId) {
      traceLength = -1;
      timerInterval = setInterval(elapsed, 1000);
      await watch(currentId, true);
    }
  } catch (e) {
    error(
      `无法连接本地服务：${e.message}。请重新启动“启动网页.cmd”，再刷新页面。`,
    );
    $("run-button").disabled = true;
  }
}
init();
