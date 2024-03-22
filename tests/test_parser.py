import pytest
import sys

sys.path.append("../getodo")
from getodo import todoparser


class TestParser:
    def test_parser(self, tmp_path):
        with open("tests/py_content.py", "r") as file:
            self.py_content = file.read()
        with open("tests/cpp_content.cpp", "r") as file:
            self.cpp_content = file.read()
        with open("tests/other_content.txt", "r") as file:
            self.other_content = file.read()
        with open("tests/todo_test.txt", "r") as file:
            self.expected_output = file.read()

        self.file1 = tmp_path / "file1.py"
        self.file2 = tmp_path / "file2.cpp"
        self.file3 = tmp_path / "file3_ignore.py"
        self.file4 = tmp_path / "file4_custom.kk"
        self.folder1 = tmp_path / "folder1"
        self.folder1.mkdir()
        self.folder2 = tmp_path / "folder2_ignore"
        self.folder2.mkdir()
        self.file5 = self.folder1 / "ffile1.py"
        self.file6 = self.folder1 / "ffile2.cpp"
        self.file7 = self.folder2 / "ffile1.cpp"
        self.file1.write_text(self.py_content, encoding="utf-8")
        self.file2.write_text(self.cpp_content, encoding="utf-8")
        self.file3.write_text(self.py_content, encoding="utf-8")
        self.file4.write_text(self.other_content, encoding="utf-8")
        self.file5.write_text(self.py_content, encoding="utf-8")
        self.file6.write_text(self.cpp_content, encoding="utf-8")
        self.file7.write_text(self.cpp_content, encoding="utf-8")

        parser = todoparser.TodoParser(
            base_dir=tmp_path,
            out_file=tmp_path / "tmp_todo.txt",
            user_ignore_paths=[self.file3.name, self.folder2.name],
            user_add_filetypes={"kk": "/"},
            print_to_term=False,
        )

        self.expected_output = self.expected_output.format(
            self.file2, self.file1, self.file4, self.file5, self.file6
        )
        self.actual_output = parser.out_file_contents
        assert self.expected_output == self.actual_output
