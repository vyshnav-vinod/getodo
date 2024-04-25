# Contains all utility functions required for getodo

from os import path
from json import loads
from colorama import Fore, Style


def load_getodo_cfg() -> dict:
    # Loads the content of getodo_cfg.json
    try:
        with open(path.join(path.dirname(__file__), "getodo_cfg.json"), "r") as f:
            json_data = f.read()
        return loads(json_data)
    except Exception as e:
        print_error(e)


def get_comment_syntax(file: str, _comments: dict) -> list | None:
    file_type = file[file.rindex('.'):]
    return _comments.get(file_type, '')


def get_first_letter_index(s: str) -> int:
    for c in s:
        if c.isalpha():
            return s.index(c)
        

def print_error(e: Exception) -> None:
    print(Fore.RED + Style.BRIGHT + "Encountered Error" + Style.RESET_ALL)
    print(e)
    exit(-1)


def add_to_gitignore(parse_path: str, out_file: str) -> None:
    # Assume .gitignore is in the root of the input_path
    gitignore_root = path.abspath(path.dirname(parse_path))
    gitignore_file = path.join(gitignore_root, ".gitignore")
    
    if path.exists(gitignore_file):
        try:
            with open(gitignore_file, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip() == out_file:
                        exit(0)
            with open(gitignore_file, "a") as f:
                f.write(out_file + "\n")
                # TODO: Make this configurable (Maybe user doesnot want us to write to gitignore)
                print(Fore.GREEN + Style.BRIGHT + f"Appended {out_file} to .gitignore" + Style.RESET_ALL)
        except Exception as e:
            print_error(e)

    else:
        # TODO: Make this configurable (maybe allow user to specify where the gitignore is)
        print(Fore.RED + Style.BRIGHT + f"No .gitignore found in {gitignore_root} to append the output file name to it" + Style.RESET_ALL)
