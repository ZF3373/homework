import argparse


def _non_blank_name(value):
    """argparse 的 type 校验钩子：拒绝只含空白字符的 --name。

    抛出 argparse.ArgumentTypeError 后，argparse 会自行捕获并调用
    parser.error()，由它打印用法与错误信息并以 SystemExit(2) 结束，
    因此这里无需手动调用 sys.exit()。

    校验通过时原样返回 value，不做 strip()，以免改变原有输出。
    """
    if not value.strip():
        raise argparse.ArgumentTypeError(
            "参数 --name 不能为空，也不能只包含空白字符（空格、制表符、换行等）"
        )
    return value


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True, type=_non_blank_name)
    a = p.parse_args()
    print(f"Hello, {a.name}!")
