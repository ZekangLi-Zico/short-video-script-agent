# v7 Natural Voice Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Preserve all evidence; user already authorized execution.

**Goal:** Improve speakable narration and cross-shot logic, then run 20 real-model webpage tasks and compare exact original briefs.
**Architecture:** Write a continuous spoken argument before splitting it into shots; give the existing reviewer an exact listening-only projection alongside full evidence. No extra reviewer call, new refusal gate, banned-word list or scripted rewriting. Show the same projection in the UI and export for human review.
**Tech Stack:** Python standard library, existing JS UI and Codex adapter.
**Spec:** User's latest request; frozen protocol `evaluations/natural-20-v7-20261105/protocol.json`.

## Global Constraints
- 20 real-model UI tasks (user reduced from 50), no input revision from expected results.
- Preserve v6 and all old records. Keep source frozen throughout formal campaign.
- Default medium effort, 180s per attempt, one timeout recovery, 12 steps; no new model stage.
- Existing factual, duration and original-brief obligations remain; no production-system expansion.

## Review Focus
- Mixed voice/screen and unordered beats: listening copy follows actual audible order only.
- Silent script: no invented narration; empty listening copy clearly shown.
- Legacy script: channels unknown, labelled legacy combined copy, not claimed verified voice.
- Revision feedback: existing reviewer uses actual continuous text, no duplicated extra model calls.
- Stale process: live app version visible; default page must run current code at handoff.

### Task 1: narration-first generation and listening projection
Files: new `src/listening.py`, modify `src/providers.py`, `src/requirements.py`, tests `tests/test_natural_v7.py`.
Interfaces: `listening_copy(script) -> dict(kind, text, shots)` exact text extraction; no content rewriting.
- [ ] RED: public model review payload lacks listening_copy; assert order, excluded screen/title/notes and unchanged source.
- [ ] GREEN: shared extraction helper; payload and existing style/continuity assessment use it.
- [ ] Replace writer-first instructions with continuous listener-oriented narration then shot allocation; keep evidence schema.
- [ ] Tests for silent, legacy and empty input; full suite.

### Task 2: human read-through and version handoff
Files: `src/reporting.py`, `src/web.py`, `src/version.py`, `src/agent.py`, `web/app.js`, `web/index.html`, tests above.
- [ ] RED: saved run has no listening artifact / current app version.
- [ ] GREEN: exact listening JSON/text export, read-through UI section; backend build label, per-run writer version.
- [ ] Existing routes/current result continue to work; static UI visually verified.
- [ ] One fresh-context whole-change reviewer; important defects fixed with regressions.

### Task 3: frozen real experiment and deliverable
- [ ] Freeze 20 unchanged v6 briefs before implementation; label screenshot example correctly as older v3, outside pairing.
- [ ] Freeze final source after tests/review. Submit each case through webpage real Codex only and preserve all artifacts.
- [ ] Read each audible copy and compare old/new on direct voice readiness, naturalness, continuity and required content; quote actual defects.
- [ ] Replay evidence, verify all old hashes, update docs/report and checked ZIP. Keep default webpage on tested v7.
