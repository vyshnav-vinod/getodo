# Currently only supports Python Files

from io import TextIOWrapper
import sys
from os import path


# TODO: Add CLI args and flags

out_file_contents = ""


def main():
    args = sys.argv[1:] # Remove the starting file name
    is_dir = path.isdir(args[0])
    out_file = "todo.txt" # TODO: Ask for output file from User
    if is_dir:
        # TODO: Recursively visit every file and folder inside
        pass 
    else: # TODO: Check which file type and then get its corresponding comment syntax ( Prolly make a new func and check file type and call parse_TODO inside there) 
        with open(args[0]) as file:
            parse_TODO(file)
    
    with open(out_file, "w+") as file:
        file.write(out_file_contents)


def parse_TODO(file: TextIOWrapper):
        file_content = file.readlines()
        global out_file_contents 
        out_file_contents = f"{file.name} : \n"
        line_num = 0
        for line in file_content:
            line_num += 1
            if line.startswith("#") or line.__contains__("#"):
                line_content = line[line.index("#")+1:] # Get the contents of the comment
                # Check if it is starts with TODO or TODO:
                if line_content.__contains__("TODO"):
                    out_file_contents += f"Line {line_num} - {line_content.strip()}\n"


if __name__ == "__main__":
    main()
            
