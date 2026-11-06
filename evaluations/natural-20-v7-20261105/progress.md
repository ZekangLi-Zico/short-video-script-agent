# SDD ledger — plan: docs/superpowers/plans/2026-11-05-v7-natural-voice.md

Preserved v6 source/docs/examples: 825 files. Historical evidence baseline: 12006 files. Archive SHA256 2ced085b0524fd67b3ce8449315790b9f9137e4268ca6c444da0fcf12f994b28.
Ruling: execute in authorized workspace with immutable archive, no git worktree/commit/reset; .git read-only and existing modifications retained. Cost: local snapshot needs final user GitHub commit.
Ruling: 20 cases supersedes 50. Reuse a diverse fixed v6 subset for exact pairing, excluding the screenshot's v3 runtime from v6 statistics. Cost: no claim about all possible scenarios.
Ruling: naturalness has no honest deterministic unit-test seam. Use saved real utterances and explicit text read-through; unit tests cover listening projection and integration, not semantic quality. No fake regex fluency gate. Cost: subjective AI review, separately labelled.
Pre-flight: shared listening projection consumed by model reviewer, saved artifacts and web display; old channel-less input labelled legacy, never silently treated as known voice.
Diagnosis: screenshot run efcc96a70bf4485db882c7cc6aba2722 is v3 completion policy, not current v6. Existing v6 prompt still starts from shots/functions and describes blocks as separate facts; existing review focuses individual requirements/expressions rather than a continuous listening track.
Hypotheses: (1) shot-first writing creates disconnected functions/scene sentences; narrative-first wording should reduce patching. (2) reviewer sees full formatted script but no continuous listening view; exact voice projection should expose missing referents and false transitions without another review stage. (3) inherited source statements anchor instruction-manual language; permit each supported fact to live naturally inside a scene sentence. (4) active old service masks improvements; show actual app version and replace idle workspace-owned default process at handoff.

Task 1: complete — narration-first prompt and exact listening projection. RED→GREEN evidence saved; full suite133/133.
Task 2: complete — read-through display, export, producing-version metadata. Fresh review P2 legacy export labelling fixed; test_saved_run_exposes_exact_listening_artifact_and_current_version RED→GREEN; review-fixed suite133/133.
Final: Ruling: reviewer declined semantic improvement/TTS/preservation conclusions before experiments; assess20actualoutputs and verifyhashes after campaign, no TTS claim. Cost: subjective text-readiness remains subjective. Broader production features remain out of requested scope.

Task 3: all20UI runs captured,121real responses;20evidence replays valid;47frozen files and12006historical hashes unchanged.19spoken texts graded:8→13direct-readiness,6remaining local edits,1silent excluded.10improve/7same/2regress/1silent. Median141.36→184.98s.133tests passed. Current documentation and7copied examples verified; finalZIP check next.
Default service: prior owned idlePID35564 replaced withv7PID39812; UIheader andproducing metadata verified; screenshothandoff-v7.png.
Final: minor (deferred): none from code review. Remaining semantic defects enumerated per actualcase, not concealed or retested away.
Ruling: retain this plan andledger because user requires alltestrecords preserved; do notdelete skill workspace/evidence. Cost: larger localarchive, explicit navigational indexprovided.
