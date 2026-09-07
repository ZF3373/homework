# 系统开发工具基础 · 第一周实验

- 姓名：周峰　学号：25020007186
- 日期：2026-08-24（第一周 第 5—8 节）
- 环境：Windows 11 + WSL2（Ubuntu, bash）、Git、TeX Live（XeLaTeX/latexmk）
- 说明：实验全部在 WSL 内完成并按过程分次提交；q03 按题目要求"从零创建"了独立 Git 仓库，
  其完整分支历史以 q03-main / q03-feature-a / q03-feature-b 三个分支推送至本仓库，
  可在 GitHub 分支切换或 Insights → Network 中查看分叉与合并图谱。

## 实验内容与提交对照

| 题号 | 主题 | 对应提交 |
| ---- | ---- | -------- |
| q01  | Shell 批量整理：空格/隐藏文件、750/640 权限、inventory.txt | q01 前缀 3 次提交 |
| q02  | 日志统计 analyze.sh：awk/sort/head 管道、stderr 与非零退出码 | q02 前缀 2 次提交 |
| q03  | 从零建仓、feature-a/feature-b 分支、合并冲突解决 | q03 前缀 4 次提交 + q03-* 分支 |
| q04  | LaTeX 补全与构建：公式/表格 label-ref 交叉引用、latexmk 构建 | q04 前缀 2 次提交 |
| q05  | 命令行环境：worker.sh 后台任务控制、信号捕获与 CLEAN_EXIT | q05 前缀提交 |
| q06  | 语义重构：total_price→calculate_total 重命名 + ruff/pytest | q06 前缀提交 |
| q07  | Debugging：pdb 定位归并排序 merge 缺陷（right[i]→right[j]） | q07 前缀提交 |
| q08  | Profiling：cProfile 分析词频程序 + set 优化去重 | q08 前缀提交 |
| q09  | Packaging：构建 greetlab wheel 并验证安装 | q09 前缀提交 |
| q10  | 智能体编程：TDD 空白姓名校验 + ai_log | add q10 TDD agent fix loop |
| q11  | 不止于代码：协作材料改写（Issue/提交信息/评审意见） | add q11 communication rewrite |
| q12  | PyTorch：CPU 线性回归训练循环 SGD 收敛至 loss<0.001 | add q12 pytorch linear regression |
| q13  | 代码质量：本地质量门禁 ruff + pytest + check.sh | （待完成） |
| q14  | 构建系统：Makefile 依赖管理 | （待完成） |
| q15  | 大杂烩：curl + jq API 数据转 Markdown 报告 | （待完成） |
| q16  | 综合测试：修复陌生工具仓库 + Makefile + wheel 交付 | （待完成） |