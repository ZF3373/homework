from merge_sort import merge_sort


def test_given_input():
    """测试题目给定的输入"""
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_duplicates():
    """测试含重复元素的列表"""
    assert merge_sort([5, 2, 5, 1, 2, 0, 5]) == [0, 1, 2, 2, 5, 5, 5]
