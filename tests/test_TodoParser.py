# Main TodoParser class test

import pytest
from os import path
from getodo import getodo

def test_TodoParser(tmp_path):
    # NOTE: As more and more flags are added, remember to update the expected output
    expected_output = {
            path.abspath('tests/data/cpp_file.cpp'): {
                1: 'TODO: Todo1',
                2: 'TODO: Todo2'
            }, 
            path.abspath('tests/data/py_file.py'): {
                1: 'TODO: Todo1',
                2: 'TODO: Todo2'
            }
        }
    actual_output = getodo.TodoParser(path.abspath("tests/data/"), tmp_path / "todo.txt", False).output
    assert actual_output == expected_output