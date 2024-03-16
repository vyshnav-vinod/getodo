# Currently only supports Python Files

from io import TextIOWrapper
import sys
from os import path, scandir


# TODO: Add CLI args and flags
# TODO: Add option to print to terminal(if user dont want to write to a output file)
# TODO: Check if args is given or not
# TODO: Add colors
# TODO: Config [set output file, ignored dirs, ]

out_file_contents = ""
base_dir = ""
out_file = ""

valid_file = {
    ".py":'#',
    ".rs":"//",
    ".java":"//",
    ".c":"//",
    ".cpp":"//",
    ".go":'//'
}


def main():
    global base_dir
    global out_file
    args = sys.argv[1:]  # Remove the starting file name
    is_dir = path.isdir(args[0])
    base_dir = args[0]
    out_file = "todo.txt"  # TODO: Ask for output file from User
    if is_dir:
        parse_dir(args[0])

    else:
        parse_file(args[0])

    with open(out_file, "w+") as file:
        file.write(out_file_contents)


def parse_TODO_from_file(file: TextIOWrapper):
    global out_file_contents
    has_todo = False
    file_content = file.readlines()
    comment_syntax = get_comment_syntax(file.name) # Get the comment syntax of that file
    line_num = 0
    for line in file_content:
        line_num += 1
        if line.startswith(comment_syntax) or line.__contains__(
            comment_syntax
        ):  
            line_content = line[
                line.rindex(comment_syntax[0]) + 1:
            ].strip()  # Get the contents of the comment 
            # Check if it is starts with TODO or TODO:
            if line_content.startswith("TODO"):
                if (
                    not has_todo
                ):  # This is done to not print the file name when there is no todo present in that file
                    out_file_contents += f"\n{file.name} : \n\n"
                has_todo = True
                out_file_contents += f"Line {line_num} - {line_content.strip()}\n"


def parse_file(file):
    with open(file) as file:
        parse_TODO_from_file(file)


def parse_dir(dir):
    dir_content = scandir(dir)
    for dir_or_file in dir_content:
        if dir_or_file.is_dir():
            if not is_ignored_dir(dir_or_file.name):
                parse_dir(dir_or_file)
        if dir_or_file.is_file():
            if is_allowed_file(dir_or_file.name):
                parse_file(dir_or_file.path)
    dir_content.close()


def is_ignored_dir(dir):
    global base_dir
    ignored_dirs = [
        ".git",
        "__pycache__",
    ]
    # TODO : Add option for user to add directory or files to be ignored
    is_virtual_env = path.join(
        base_dir, dir, "pyvenv.cfg"
    )  # All virtual environments created with venv contains a pyenv.cfg file
    return dir in ignored_dirs or path.exists(
        is_virtual_env
    )  # Check if it is a ignored dir or a virtual env dir


def is_allowed_file(file):
    # Check if it is of a valid file type
    global out_file
    global valid_file

    return (
        any(type in file for type in valid_file)
        and not file.startswith(".")
        and not file == out_file
    )


def get_comment_syntax(file: str):
    # Get the comment syntax of the corresponding file
    global valid_file
    file_type = file[file.rindex(".") :]
    return valid_file[file_type]


if __name__ == "__main__":
    main()

# TODO : tests
