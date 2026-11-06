# v7.3.1 公开交付

项目：第4题“短视频脚本Agent”。目标仓库为`ZekangLi-Zico/short-video-script-agent`，采用公开可读方式；版本标识为`v7.3.1-submission`。

## 从干净目录复现

Python 3.11或以上；仅使用标准库，没有第三方Python运行依赖。

```bash
git clone https://github.com/ZekangLi-Zico/short-video-script-agent.git
cd short-video-script-agent
python -m scripts.run_tests
python -m scripts.verify_evidence
python -m src.cli --provider mock --input examples/inputs/normal.json --output outputs/my-demo
python -m src.web --open
```

真实模型运行需使用自己的Codex登录或API配置，见README。网页在本机监听，GitHub仓库本身不是在线服务。

## 随仓库交付的内容

代码、网页、测试、合成产品和漫剧文字资料、提交文档、历次报告、examples、历史网页产物及源码备份均随仓库提交。原有两个Git提交保留，当前发布在其上新增提交。为避免跨平台换行转换改变证据哈希，`.gitattributes`保留文件原始字节。

原始本地工作区及旧记录均保留。公开副本只对10份旧诊断日志中的个人Windows用户目录前缀作替换，输入、生成脚本、工具返回和Trace未因发布而重写。`PUBLICATION-MANIFEST.json`记录原文件与公开副本哈希；原有保存核验中的哈希描述未脱敏本地记录，不能直接当作脱敏副本哈希。

未发布登录文件、密钥、`.runtime`、Python缓存、临时工作目录及根目录重复交付ZIP；需要复核的历次源码ZIP保留在`archives/`，素材ZIP也保留。公开版本没有附带个人GitHub登录凭证。

## 验证与实际结果

- 当前功能验证：161项自动测试通过。
- 四类真实网页验收：正常生成24.8秒、超时旧稿38秒改为7.3秒、无素材时补查后请求资料、工具持续失败后明确停止。共18次真实模型响应、0次超时。故障案例通过网页注入业务工具错误，模型为真实调用。
- 证据复算：当前4组和原始16组共20组通过。复算验证保存的本地工具与状态，不会再次调用模型。
- 详细文件：[验收索引](examples/current/evaluation.md)、[本轮报告](evaluations/submission-v7.3.1-20261106/README.md)、[发布副本离线核验](release-checks/summary.json)。

时长为文本和动作估算，未做实际配音或成片测量。超时旧稿转换为新格式后，修订统计可能显示没有完全相同的结构块，但两句台词实际保留。历史实验保留发生时的版本和结论，不重新标成当前实验。

候选人贡献与AI辅助说明见[docs/04](docs/04-ai-usage.md)；个人累计投入时间尚待本人提供。GitHub发布不代替笔试平台交卷，最终SHA由真实Git提交产生，不预填或编造。
