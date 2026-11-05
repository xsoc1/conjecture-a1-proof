# 实际形式化范围与陈述差异

本次在 Lean 4.31.0、Mathlib `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f` 下完成了
范围明确的部分形式化。详细命令、输入、失败修正、版本和日志见
`../formalization/PROGRESS.md`；独立审计见 `audit-2026-11-05/lean-audit-report.md`。

| 内容 | Lean 对应 | 范围 |
|---|---|---|
| 交换子导子性质与幂递推 | `ad_*` | 一般环；原基线 `ad_pow_succ` 编译失败已修复 |
| 一般交换子幂公式 | `ad_pow_of_commute`, `ad_pow_eq` | 只要求 y 与 [x,y] 交换，含 n=0 边界 |
| 一次正规序换位 | `mul_pow_normal_order`, `pow_mul_normal_order` | 任意非负参数，局部交换性 |
| 有限的左侧证书 | `two_mul_add_pow_three`, `two_mul_add_pow_five` | Lean 核验的非交换环恒等式，X²、Y² 等湮灭元始终在最右端 |
| 原猜想四个向量特例 | `vector_p_zero_q_zero`, `vector_p_one_q_zero`, `vector_p_zero_q_one`, `vector_p_one_q_one` | 任意维特征零域向量空间；仅原猜想的局部交换性 |
| 四例合并 | `vector_parameters_le_one` | 0≤p,q≤1；保留一般目标形式及所需指数 |
| 一般猜想 | `def VectorConjecture` | 忠实定义命题，**尚无一般证明** |

20 个引理/定理的实际公理查询仅出现 Lean/Mathlib 标准的 `propext`、`Classical.choice`、
`Quot.sound`（不同声明使用其子集）。代码扫描没有 `sorry`、`admit`、用户公理或
`unsafe`/`native_decide`。这些检查不能代替陈述保真审计；本次另有独立审计。

## 保真的关键修正

1. 旧的 `def ConjectureA1` 被保留并标明历史范围。其 section 中未使用的 `Algebra ℚ R`
   被 Lean 自动删去，实际类型缺少该特征约束；它还要求 z 与整个 R 交换。
   新的 `VectorConjecture` 用显式 Field/CharZero 绑定和 `Module.End K V`，只要求
   X、Y 分别与 [X,Y] 交换。旧定义不是原猜想的完成证明。
2. 向量湮灭 `X^(p+1)v=0` 与算子湮灭 `X^(p+1)=0` 严格区分。
   有限恒等式在最右端保留向量湮灭元，代入后才作用于 v。
3. 旧注释中的三项式公式确实漏了 n!，已更正；x=1,y=z=0,n=2 可检测此错误。
   注释路线不计作已证明声明。

## 一般证明尚缺的形式化义务

一般正规序有限和、所有参数的直线递推与边界、标量少项式重数界、向量多项式支撑论证、
三类直线的组装和主定理，以及一般张量最优性构造，都尚未形成完整 Lean 证明。
可直接采用端同态和向量关系路线，完整 PBW 代数未被本次证明为必需基础设施。
原稿“需要若干人月”的估计未验证，本次不沿用。

本次书面主证明通过独立数学审稿，有限 Python 检查通过，部分 Lean 声明经内核编译；
三者的范围不同。不得把四个特例或目标的 `def` 描述成完整一般形式化。
