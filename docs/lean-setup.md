# 固定版本与实际构建

版本：Lean `leanprover/lean4:v4.31.0`；Mathlib 提交
`fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`。`lake-manifest.json` 固定其传递依赖。
原来的 Lean4.15/README4.35/未固定 Mathlib 配置已替换。无需修改全局 Codex 或 Git 配置。

## 标准联网路径

在已有 elan 且能获取固定工具链及 GitHub 依赖的环境中，从 `formalization/` 运行：

```powershell
lake exe cache get
lake build
python validate.py
```

这是供具备联网环境者复现的路径，本次没有重新下载所有依赖来运行它。
`validate.py` 读取最近构建的公理输出；本次输出由下述离线目标保存到 `evidence/lake-build.log`。
若使用标准联网路径，需把完整构建输出与退出码保存到该日志，或独立运行 AxiomAudit.lean 并保留记录。

## 本机实际运行路径

本机已有 Lean4.31 和相同提交的 Mathlib 及缓存，原有项目保持只读。实际运行：

```powershell
.\build.ps1 -LeanBin 'C:\Users\HuangZY\.elan\toolchains\leanprover--lean4---v4.31.0\bin' `
  -MathlibCache 'F:\LaTeX\BVE research\lean-proof\.lake\packages\mathlib'
python validate.py
```

脚本检查 Mathlib HEAD，设置只读缓存搜索路径，并调用
`lake -f lakefile.offline.lean build`。该目标依次用 Lean 编译四个物理源文件，
所有本项目生成物写到本项目 `.lake/`。不是仅运行 `#check`，也不是用 Python 替代 Lean。
每个定理另有 `#print axioms`，包括递归依赖。实际通过的声明与尚未完成的一般目标
以 `../formalization/PROGRESS.md` 和独立审计为准。

`setup.ps1` 是保留的局部工具链获取辅助脚本；已有环境不需要重装。
本次没有安装全局 Lean、改变其他研究项目或声称测试了全部联网下载流程。
