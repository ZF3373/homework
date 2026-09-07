import pytest
import sys
from unittest.mock import patch
from greetlab.cli import main


def test_name_with_only_whitespace_exits_with_code_2():
    """当 name 只含空白字符时，main 应以 SystemExit(2) 结束"""
    test_args = ["prog", "--name", "   "]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 2
