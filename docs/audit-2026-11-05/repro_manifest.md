# Reproducibility manifest

Baseline: upstream commit f8f7235dca197933cd97ac74b6d35d64f67e693d, clean clone,
branch audit/lean-a1-2026-11-05. No existing user changes were overwritten.
Audited source/artifact commit: `e6be224ab4928b5be317f4b367451600b8de3f54`.
The worktree was clean immediately after that commit. The following provenance
commit changes only this manifest and the source-commit field in run-manifest.json;
all tested mathematical, Lean and Python sources are restored by the audited commit.
The final PR head and post-submission clean state are recorded in the task-local
submission receipt and final delivery, avoiding a self-referential commit hash.

Inputs: original arXiv:1811.10137v2 Appendix A; repository report/source,
verification scripts, existing Lean layer; no omitted attachments were accessible.
Material source hashes and the frozen independent audits bind the accepted bytes.
Raw evidence paths are exempt from Git line-ending conversion. Main report hash
51072a56fb99886bc19dc7f35889876b4b50e9c4ab2fe0f786b11fea9daa8d84;
companion source hash907fa82ee4fb735b6350d0bc102b9c4ac2a115ad62e54f5271b72d08d2b02c4c.

Python: CPython3.10.11, standard-library fractions/integers. Actual final command:
`C:\Users\HuangZY\AppData\Local\Programs\Python\Python310\python.exe verification/run_all.py`.
All nine child scripts exited0. Six regression groups include runner nonzero/timeout
propagation, the false one-sided lemma and explicit B4 membership certificate.
Final result manifest hash7ed28e668b257a0792e2d3d6940d4cb8ce05a727e0f3b5ad3973f9dc080ccde4;
it binds each script and transcript. Finite parameter scopes are in verification/README.md.

Lean: native4.31.0, compiler commit68218e876d2a38b1985b8590fff244a83c321783.
Mathlib fabf563a7c95a166b8d7b6efca11c8b4dc9d911f and eight dependencies pinned
in formalization/lake-manifest.json. Existing prebuilt dependency caches are trusted
read-only imports; they were not rebuilt. The actual offline Lake command and
exact paths are in formalization/PROGRESS.md and evidence/build-context.log.
Twenty theorem/lemma axiom queries are in evidence/lake-build.log; no axiom outside
propext,Classical.choice,Quot.sound was accepted. The final normalized four source
modules were also compiled in a fresh directory by an independent agent; source,
signature,scan,axiom,exit and dependency checks are bound in lean-audit/.
Ordinary online dependency-managed lake build was not run.

Formalizer: actual local CLI0.166.0-alpha.6, session
01a1ac05-20d8-7ed2-9686-94b4fe1d7a66, model gpt-6.1-sol from turn_context.
The observed process command contains service_tier=priority; the local catalog
maps priority to Fast. Backend tier echo/latency guarantee: unavailable, not inferred.
Only selected runtime evidence is retained; no credentials or unrelated task logs.

Overall verification is layered: corrected written general proof and sharpness;
bounded exact computation; kernel-accepted partial Lean development with independent
semantic audit. Full Lean generality, expert novelty review and human final semantic
approval are not claimed. A draft PR supplies the requested reviewable artifact.
Existing PDF binaries were not regenerated. No canonical knowledge-base integration,
merge or global installation was performed. Network/CLI/cache issues were resolved;
no permission action remains pending or uncertain.
