# Contains all utility functions required for getodo

from os import path
from json import loads
from colorama import Fore, Style

def load_comments()  -> dict:
    with open(path.join(path.dirname(__file__), "comment_syntax.json"), "r") as f:
        json_data = f.read()
    return loads(json_data)


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