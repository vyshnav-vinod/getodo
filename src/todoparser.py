from io import TextIOWrapper
from os import path, scandir
from colorama import Fore, Style


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
    ".rb": "#",
    ".js": "//",
    ".cs": "//",
    ".lua": "--",
    ".php": "//",  # TODO: php also supports # as a single line comment, So add parsing for that as well
    ".kt": "//",
    ".swift": "//",
    ".r": "#",
    ".pl": "#",
    ".sc": "//",
    ".ex": "#",
    ".exs": "#",
    ".dart": "//",
    ".clj": ";",
}

ignored_paths = [
    ".git",
    "__pycache__",
    ".vscode",
    ".idea",
    ".project",
    ".metadata",
    ".vs",
]


def main(base, outfile, print_to_terminal, ignore_paths, add_filetypes):
    global base_dir
    global out_file
    global print_to_term
    global ignored_paths

    print_to_term = print_to_terminal
    is_dir = path.isdir(base)
    base_dir = base
    out_file = outfile or "todo.txt"

    if ignore_paths:  # if user provided ignored paths then append it to ignored_paths
        ignored_paths.extend(ignore_paths)

    if (
        add_filetypes
    ):  # if user provided filetypes along with their comment syntax so TODO's inside those can be parsed
        for key, value in add_filetypes.items():
            if (
                not key in valid_file and not f".{key}" in valid_file
            ):  # Prevents user from overriding valid_file
                if not key.startswith("."):
                    valid_file[f".{key}"] = value
                else:
                    valid_file[key] = value

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
                        print(
                            Fore.GREEN
                            + Style.BRIGHT
                            + "[FILE] "
                            + Fore.LIGHTRED_EX
                            + f"{file.name}\n"
                            + Style.RESET_ALL
                        )
                    else:
                        out_file_contents += f"\n{file.name} : \n\n"
                has_todo = True
                if print_to_term:
                    line_content = (
                        line_content[line_content.index(":") + 1 :].strip().capitalize()
                    )
                    print(
                        Fore.CYAN
                        + Style.BRIGHT
                        + f"[Line {line_num}] "
                        + Style.RESET_ALL
                        + Fore.WHITE
                        + f"{line_content}"
                        + Style.RESET_ALL
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
            if not is_ignored(dir_or_file):
                parse_dir(dir_or_file)
        if dir_or_file.is_file():
            if is_allowed_file(dir_or_file.name) and not is_ignored(dir_or_file):
                parse_file(dir_or_file.path)
    dir_content.close()


def is_ignored(file_dir_path):
    global base_dir
    global ignored_paths

    if file_dir_path.is_file():
        return file_dir_path.name in ignored_paths
    else:
        is_virtual_env = path.join(
            base_dir, file_dir_path, "pyvenv.cfg"
        )  # All virtual environments created with venv contains a pyenv.cfg file
        return file_dir_path.name in ignored_paths or path.exists(
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
# TODO: Config file [set output file, ignored dirs, ]
