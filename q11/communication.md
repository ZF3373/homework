# Issue: `sdt-greet --name " "` 未校验空白输入

**环境**：Windows 10, Python 3.14 (WSL), greetlab-25020007186 0.1.0
**复现命令**：`sdt-greet --name " "`
**期望结果**：拒绝空白姓名，以非零退出码（如2）终止并输出错误提示。
**实际结果**：输出 `Hello,   !` 并以退出码0正常结束。
**待确认**：是否需在 macOS/Linux 原生环境验证；是否需同时拦截纯制表符/换行输入。

---

# 提交信息

Fix whitespace-only name validation in CLI

空白字符作为 `--name` 参数时程序未做校验，直接输出问候并以退出码0
退出，导致调用方无法区分有效/无效输入。

添加 `_non_blank_name()` 作为 argparse type 钩子，空白时抛
ArgumentTypeError，argparse 自动以 SystemExit(2) 终止。正常输入行为不变。

---

# 评审意见

**Blocking**：`--name " "` 仍输出 `Hello,   !` 且退出码为0。CI/脚本调用
方依赖退出码判断成败，此行为会导致静默错误传播。合入前必须修复。

**Suggestion**：该校验逻辑可抽取为公共工具函数，便于其他 CLI 参数复用。

**Nit**：错误提示中可注明姓名的最小长度要求，提升用户体验。# Issue: `sdt-greet --name " "` 未校验空白输入

**环境**：Windows 10, Python 3.14 (WSL), greetlab-25020007186 0.1.0
**复现命令**：`sdt-greet --name " "`
**期望结果**：拒绝空白姓名，以非零退出码（如2）终止并输出错误提示。
**实际结果**：输出 `Hello,   !` 并以退出码0正常结束。
**待确认**：是否需在 macOS/Linux 原生环境验证；是否需同时拦截纯制表符/换行输入。

---

# 提交信息

Fix whitespace-only name validation in CLI

空白字符作为 `--name` 参数时程序未做校验，直接输出问候并以退出码0
退出，导致调用方无法区分有效/无效输入。

添加 `_non_blank_name()` 作为 argparse type 钩子，空白时抛
ArgumentTypeError，argparse 自动以 SystemExit(2) 终止。正常输入行为不变。

---

# 评审意见

**Blocking**：`--name " "` 仍输出 `Hello,   !` 且退出码为0。CI/脚本调用
方依赖退出码判断成败，此行为会导致静默错误传播。合入前必须修复。

**Suggestion**：该校验逻辑可抽取为公共工具函数，便于其他 CLI 参数复用。

**Nit**：错误提示中可注明姓名的最小长度要求，提升用户体验。
