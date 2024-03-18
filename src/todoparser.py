from io import TextIOWrapper
from os import path, scandir
import print_color

# TODO: Add CLI args and flags [Half done]
# TODO: Add option to parse TODO as well along with TODO: and TODO :
# TODO: Config [set output file, ignored dirs, ]

out_file_contents = ""
base_dir = ""
out_file = ""
print_to_term = False

valid_file = {
    ".py": "#",
    ".rs": "//",
    ".java": "//",
    ".c": "//",
    ".cpp": "//",
    ".go": "//",
}


def main(base, outfile, print_to_terminal):
    global base_dir
    global out_file
    global print_to_term
    print_to_term = print_to_terminal
    is_dir = path.isdir(base)
    base_dir = base
    out_file = outfile or "todo.txt"
    if is_dir:
        parse_dir(base_dir)

    else:
        parse_file(base_dir)

    if not print_to_term:
        with open(out_file, "w+") as file:
            file.write(out_file_contents)


def parse_TODO_from_file(file: TextIOWrapper):
    global out_file_contents
    global print_to_term
    has_todo = False
    file_content = file.readlines()
    comment_syntax = get_comment_syntax(
        file.name
    )  # Get the comment syntax of that file
    line_num = 0
    for line in file_content:
        line_num += 1
        if line.startswith(comment_syntax) or line.__contains__(comment_syntax):
            line_content = line[
                line.rindex(comment_syntax[0]) + 1 :
            ].strip()  # Get the contents of the comment
            if line_content.startswith("TODO:") or line_content.startswith("TODO :"):
                if (
                    not has_todo
                ):  # This is done to not print the file name when there is no todo present in that file
                    if print_to_term:
                        print("\n")
                        print_color.print(
                            f"{file.name} : \n\n",
                            tag="FILE",
                            tag_color="green",
                            color="white",
                            format="bold",
                        )
                    else:
                        out_file_contents += f"\n{file.name} : \n\n"
                has_todo = True
                # Find a way to only bold the tags [maybe fork the print_color and add it]
                if print_to_term:
                    line_content = line_content.strip()[line_content.index(":") + 1 :]
                    print_color.print(
                        f"{line_content}\n",
                        tag=f"Line {line_num}",
                        tag_color="cyan",
                        color="white",
                    )
                else:
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


def is_allowed_file(file: str):
    # Check if it is of a valid file type
    global out_file
    global valid_file
    file_type = ""
    if file.__contains__(".") and not file.startswith(
        "."
    ):  # Extract file type extension
        file_type = file[file.rindex(".") :]
    return file_type in valid_file and not file == out_file


def get_comment_syntax(file: str):
    # Get the comment syntax of the corresponding file
    global valid_file
    file_type = file[file.rindex(".") :]
    return valid_file[file_type]


# TODO : tests
