import pytest
from getodo import getodo


def test_get_comment_syntax():
    _comments = getodo.utils.load_getodo_cfg()['comment_syntax']

    files = {
        "supported_file1": ["file1.py", ["#"]],
        "supported_file2": ["file2.php", ["//", "#"]],
        "supported_file3": ["file3.clj", [";"]],
        "unsupported_file1": ["file1.txt", ""],
        "unsupported_file2": ["file2.json", ""],
    }

    for key, value in files.items():
        assert getodo.utils.get_comment_syntax(value[0], _comments) == value[1]
