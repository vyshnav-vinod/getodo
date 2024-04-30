import pytest
from getodo import getodo

cfg = getodo.utils.load_getodo_cfg()

def test_get_comment_syntax():
    _comments = cfg['comment_syntax']

    files = {
        "supported_file1": ["file1.py", ["#"]],
        "supported_file2": ["file2.php", ["//", "#"]],
        "supported_file3": ["file3.clj", [";"]],
        "unsupported_file1": ["file1.txt", ""],
        "unsupported_file2": ["file2.json", ""],
    }

    for _, value in files.items():
        assert getodo.utils.get_comment_syntax(value[0], _comments) == value[1]


def test_is_ignored():
    _ignored: list = cfg['default_ignored']

    expected_output: dict = {
        "config.json": True,
        "test.txt": True,
        ".gitignore": True,
        ".git": True,
        "test": False,
        "test.py": False
    }

    for key, value in expected_output.items():
        assert getodo.utils.is_ignored(key, _ignored) == value