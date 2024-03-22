from io import TextIOWrapper
from os import path, scandir
from colorama import Fore, Style, init


class TodoParser:
    def __init__(
        self,
        base_dir,
        out_file,
        user_ignore_paths,
        user_add_filetypes,
        print_to_term=False,
    ) -> None:
        self.out_file_contents = ""
        self.base_dir = base_dir
        self.out_file = out_file or "todo.txt"
        self.print_to_term = print_to_term
        self.valid_file = {
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
            ".php": "//",  # TODO: php also supports another comment syntax, So add parsing for that as well
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
        self.ignored_paths = [
            ".git",
            "__pycache__",
            ".vscode",
            ".idea",
            ".project",
            ".metadata",
            ".vs",
        ]
        self.ignore_paths = user_ignore_paths
        self.add_filetypes = user_add_filetypes

        self.found_todo = False
        self.main()

    def main(self):
        init()  # colorama.init()
        is_dir = path.isdir(self.base_dir)

        if (
            self.ignore_paths
        ):  # if user provided ignored paths then append it to ignored_paths
            self.ignored_paths.extend(self.ignore_paths)
        if (
            self.add_filetypes
        ):  # if user provided filetypes along with their comment syntax so TODO's inside those can be parsed
            for key, value in self.add_filetypes.items():
                if (
                    not key in self.valid_file and not f".{key}" in self.valid_file
                ):  # Prevents user from overriding valid_file
                    if value:
                        if not key.startswith("."):
                            self.valid_file[f".{key}"] = value
                        else:
                            self.valid_file[key] = value
                    else:
                        print(
                            Fore.RED
                            + Style.BRIGHT
                            + f"Please add a comment syntax for {key}"
                            + Style.RESET_ALL
                        )
                        exit(1)

        if is_dir:
            self.parse_dir(self.base_dir)

        else:
            self.parse_file(self.base_dir)

        if not self.print_to_term:
            if self.out_file_contents:
                with open(self.out_file, "w+") as file:
                    file.write(self.out_file_contents)
                    print(
                        Fore.GREEN
                        + Style.BRIGHT
                        + f"TODO(s) written to {self.out_file}"
                        + Style.RESET_ALL
                    )
            else:
                print(Fore.RED + Style.BRIGHT + "NO TODO (s) found" + Style.RESET_ALL)
        else:
            if not self.found_todo:
                print(Fore.RED + Style.BRIGHT + "NO TODO (s) found" + Style.RESET_ALL)

    def parse_TODO_from_file(self, file: TextIOWrapper):

        has_todo = False
        file_content = file.readlines()
        comment_syntax = self.get_comment_syntax(
            file.name
        )  # Get the comment syntax of that file
        line_num = 0
        if comment_syntax:
            for line in file_content:
                line_num += 1
                if line.startswith(comment_syntax) or line.__contains__(comment_syntax):
                    line_content = line[
                        line.rindex(comment_syntax[0]) + 1 :
                    ].strip()  # Get the contents of the comment
                    if line_content.startswith("TODO:") or line_content.startswith(
                        "TODO :"
                    ):
                        self.found_todo = True
                        if (
                            not has_todo
                        ):  # This is done to not print the file name when there is no todo present in that file
                            if self.print_to_term:
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
                                self.out_file_contents += f"\n{file.name} : \n\n"
                        has_todo = True
                        if self.print_to_term:
                            line_content = (
                                line_content[line_content.index(":") + 1 :]
                                .strip()
                                .capitalize()
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
                            self.out_file_contents += (
                                f"Line {line_num} - {line_content.strip()}\n"
                            )

    def parse_file(self, file):
        with open(file) as file:
            self.parse_TODO_from_file(file)

    def parse_dir(self, dir):
        # if not path.basename(path.abspath(dir)) in self.ignored_paths:
        if not dir in self.ignored_paths:
            dir_content = scandir(dir)

            for dir_or_file in dir_content:
                if dir_or_file.is_dir():
                    if not self.is_ignored(dir_or_file):
                        self.parse_dir(dir_or_file)
                if dir_or_file.is_file():
                    if self.is_allowed_file(dir_or_file.name) and not self.is_ignored(
                        dir_or_file
                    ):
                        self.parse_file(dir_or_file.path)
            dir_content.close()

    def is_ignored(self, file_dir_path):

        if file_dir_path.is_file():
            return file_dir_path.name in self.ignored_paths
        else:
            is_virtual_env = path.join(
                self.base_dir, file_dir_path, "pyvenv.cfg"
            )  # All virtual environments created with venv contains a pyenv.cfg file
            return file_dir_path.name in self.ignored_paths or path.exists(
                is_virtual_env
            )  # Check if it is a ignored dir or a virtual env dir

    def is_allowed_file(self, file: str):
        # Check if it is of a valid file type

        file_type = ""

        if file.__contains__(".") and not file.startswith(
            "."
        ):  # Extract file type extension
            file_type = file[file.rindex(".") :]
        return file_type in self.valid_file and not file == self.out_file

    def get_comment_syntax(self, file: str):
        # Get the comment syntax of the corresponding file

        file_type = file[file.rindex(".") :]

        return self.valid_file[file_type]
