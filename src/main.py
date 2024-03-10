# Currently only supports Python Files

from io import TextIOWrapper
import sys
from os import path, scandir


# TODO: Add CLI args and flags
# TODO: Add option to print to terminal(if user dont want to write to a output file)
# TODO: Check if args is given or not

out_file_contents = ""
base_dir = ""
out_file = ""


def main():
    global base_dir
    global out_file
    args = sys.argv[1:]  # Remove the starting file name
    is_dir = path.isdir(args[0])
    base_dir = args[0]
    out_file = "todo.txt"  # TODO: Ask for output file from User
    if is_dir:
        # TODO: Recursively visit every file and folder inside
        parse_dir(args[0])

    else:  # TODO: Check which file type and then get its corresponding comment syntax ( Prolly make a new func and check file type and call parse_TODO_from_file inside there)
        parse_file(args[0])

    with open(out_file, "w+") as file:
        file.write(
            out_file_contents
        )  # TODO : If file does not contain any TODO , do no write it to the output file


def parse_TODO_from_file(file: TextIOWrapper):
    # TODO : Check todo.txt and see that when the comment sign is used like in the if line.startswith... below, then it starts to parse from there.. Maybe make it so that only parse comments that start with TODO
    file_content = file.readlines()
    global out_file_contents
    out_file_contents += f"\n{file.name} : \n\n"
    line_num = 0
    for line in file_content:
        line_num += 1
        if line.startswith("#") or line.__contains__(
            "#"
        ):  # TODO : Replace # with a variable which contains the comment syntax of the given file type
            line_content = line[
                line.index("#") + 1 :
            ]  # Get the contents of the comment
            # Check if it is starts with TODO or TODO:
            if line_content.__contains__("TODO"):
                out_file_contents += f"Line {line_num} - {line_content.strip()}\n"


def parse_file(file):
    with open(file) as file:
        parse_TODO_from_file(file)


def parse_dir(dir):
    dir_content = scandir(dir)
    for dir_or_file in dir_content:
        if dir_or_file.is_dir():
            if not is_ignored_dir(dir_or_file.name):
                # print(dir_or_file.name)
                parse_dir(dir_or_file)
        if dir_or_file.is_file():
            if is_allowed_file(dir_or_file.name):
                # print(dir_or_file.name)
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
    return dir in ignored_dirs or path.exists(is_virtual_env)


def is_allowed_file(file):
    # Check if it is of a valid file type
    global out_file
    valid_file = [
        ".py",
        ".rs",
        ".txt",
        ".java",
        ".c",
        ".cpp",
        ".go",
    ]  # Planning to add support for these files
    return (
        any(type in file for type in valid_file)
        and not file.startswith(".")
        and not file == out_file
    )


if __name__ == "__main__":
    main()

# TODO : tests
