# v7 whole-change review — 2026-11-05

One fresh read-only review of the v6 archive comparison and current owning source. No source edits, model calls, campaign runs, or subagents. This report is the only file written by the reviewer.

## Scope and evidence

Read the implementation plan, progress ledger, frozen protocol, review-diff.patch, archived/current provider and requirements differences, all changed runtime/UI/test sections, and the surrounding schema, agent, persistence, HTTP and duration paths. The saved final offline test evidence reports **133 tests, 0 failures, 0 errors** (`development-tests/final/summary.json` and `unittest.txt`). These tests were inspected, not rerun by this reviewer.

## Strengths

- `src/listening.py:18–26` preserves shot order, stably sorts audible blocks by beat, excludes screen-only blocks, and does not alter the script. The new test explicitly covers unordered and equal-numbered beats plus title/visual/notes exclusion.
- `src/providers.py:120–125` sends the exact shared listening projection through the existing review call. No added model stage, refusal gate, case-specific rewrite, or second naturalness review call was introduced. Revision feedback still flows through the existing requirements state and writer payload.
- `src/requirements.py:36` directs the existing reviewer to judge continuous meaning with quoted evidence, distinguish silent/legacy scripts, and avoid failing personal wording preferences.
- Web display and Markdown correctly distinguish legacy combined text from known voice. Silent and empty projections do not invent narration. New results/checkpoints record their producing app version; config exposes the running backend's imported version, rather than presenting the static frontend version as backend proof.

## Issues

### Critical

None found.

### Important

1. **[P2] Legacy combined text is still offered as an unqualified voice download.**
   - Locations: `web/app.js:471–472`, `web/index.html:314`, `src/reporting.py:105–107`.
   - Trigger: a new v7 run retains or produces a valid legacy script. This is explicitly exercised by `tests/test_natural_v7.py:39–49`: its result has `app_version=v7-natural-voice` while `listening.json.kind=legacy_unspecified`.
   - The button is shown solely because the run has a version and is saved. It always says “下载旁白”; `voice.txt` contains all legacy blocks with no legacy/unknown-channel indication. Thus the correctly qualified read-through panel loses that qualification at the exact export action, and the recipient can read screen-only/unknown-channel copy as verified narration. This violates the explicit legacy review focus, and is not merely a historical-run issue.
   - Fix: make the download affordance depend on listening kind. Offer known voice as voice; label any legacy export as combined text with unknown channels (or keep legacy users on the already-qualified script export). Preserve exact extraction; do not invent channel assignments or rewrite copy. Cover the legacy download decision, not only the helper's JSON kind.

### Minor

None worth blocking this work for.

## Operational verification still required

At review time, a read-only GET to `http://127.0.0.1:8765/api/config` returned `app=short-video-script-agent`, **no app_version**, and `active_id=null`. The default service is still old. The new frontend can warn about this, but that does not update the writer process. This is the already-planned Task 3 handoff work, not an additional source-code defect: replace the idle workspace-owned process and verify the default URL returns `v7-natural-voice` before using it for the campaign or handing it back. Do not infer a v7 campaign from current files alone.

## Declined to judge

- Whether v7 actually improves naturalness/direct voice readiness across the 20 briefs: the formal real-model campaign has not yet run at this review stage; prompt wording and offline extraction tests cannot establish that outcome.
- Recorded/TTS fluency: explicitly outside the frozen protocol; the planned evaluation is developer AI text read-through.
- Final archive/hash replay and preservation of all historical artifacts after the campaign: deferred to planned final evidence verification, which has not yet happened.
- Broader production-system features and new defensive gates: outside this change and explicitly excluded by the user.

## Assessment

**Ready for final freeze: with the legacy download fix.** The core implementation matches the planned architecture and is appropriately small. Resolve the concrete export mislabelling, then verify the live backend version and complete the separately planned 20-case campaign before claiming the user's overall task complete. No additional review/model stage is recommended.
