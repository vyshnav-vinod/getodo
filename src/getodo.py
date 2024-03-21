# CLI functionality code


from os import path
from todoparser import TodoParser

import argparse
import questionary
import toml


class ParseKeyValue(argparse.Action):

    # https://stackoverflow.com/a/68829190/23381273

    def __call__(self, parser, args, values, option_string=None):
        try:
            # TODO: Raise error when user does --add_filetypes and passes something like txt, without a comment syntax it comment syntax as empty string and causes error so check if user has passed a comment syntax
            d = dict(map(lambda x: x.split(","), values))
            d = {
                path.basename(x)[path.basename(x).rindex(".") :]: y
                for x, y in d.items()
            }  # This is done to extract only the filetype when the directory is also mentioned
        except ValueError as err:
            raise argparse.ArgumentError(
                self,
                f"Could not parse arguments {values} as format filetype,commentsyntax",
            )
        setattr(args, self.dest, d)


def main():
    parser = argparse.ArgumentParser(
        description="Scan a file or a directory and extract all the TODO into a file/stdout"
    )

    # Required argument

    parser.add_argument("input_path", help="Directory or file to scan for TODO's")

    # Optional arguments

    parser.add_argument("-o", "--output", help="Output file to store the TODO's")

    parser.add_argument(
        "-t", "--term", action="store_true", help="Print the TODO's to terminal"
    )

    parser.add_argument(
        "-i", "--ignore", nargs="+", help="Ignore specific directories or files"
    )
    parser.add_argument(
        "--add_filetypes",
        metavar="filetype,comment-syntax",
        nargs="+",
        dest="add_filetypes",
        action=ParseKeyValue,
        help="Parse the custom filetype(s) passed as argument along with their comment syntax to parse the TODO's isnide that file",
    )
    parser.add_argument(
        "-c",
        "--config",
        action="store_true",
        help="Add a configuration for this project",
    )
    parser.add_argument(
        "--override_config",
        action="store_true",
        help="Do not use the custom config for this project and run getodo with its defaults",
    )

    args = parser.parse_args()

    input_path = args.input_path
    output_file = args.output
    print_to_terminal = args.term
    ignore_paths = args.ignore
    add_filetypes = args.add_filetypes  # dict
    config = args.config
    use_defaults = args.override_config

    if config:
        create_config(".getodo_config.toml")

    if ignore_paths:
        for i in range(len(ignore_paths)):
            if path.isfile(ignore_paths[i]):
                ignore_paths[i] = path.basename(ignore_paths[i])
            else:
                ignore_paths[i] = path.basename(path.abspath(ignore_paths[i]))

    TodoParser(
        base_dir=input_path,
        out_file=output_file,
        print_to_term=print_to_terminal,
        user_ignore_paths=ignore_paths, 
        user_add_filetypes=add_filetypes,
    )  # Prolly will be put inside if use_defaults:


def create_config(config_file_name):
    out_file = ""
    user_ignore_paths = []
    user_add_filetypes = {}
    
    out_file = questionary.text("Specify file to save the getodo output [Press ENTER for default]", default="todo.txt").ask()
    confirm = questionary.confirm("Do you want to add files/folders to be ignored while parsing? ", default= False).ask()

    while confirm:
        user_ignore_paths.append(questionary.path("Specify file/dir to ignore while parsing", validate=lambda x : True if x else False).ask())
        confirm = questionary.confirm("Do you want to continue?", default=True).ask()
    confirm = questionary.confirm("Do you want to add custom filetypes to be parsed? ", default= False).ask()

    while confirm:
        user_input : str = questionary.text("Specify the filetype and its comment syntax in this order [filetype,commentsyntax]", validate=lambda x : True if x else False).ask()
        split_values = user_input.split(",")
        user_add_filetypes[split_values[0]] = split_values[1]
        confirm = questionary.confirm("Do you want to continue?", default=True).ask()

    toml_content = {
        "out_file":out_file,
        "user_ignore_paths":user_ignore_paths,
        "user_add_filetypes":user_add_filetypes
    }

    try:
        with open(config_file_name, "w+") as f:
            toml.dump(toml_content, f)
    except Exception as e:
        print(e)

    try:
        with open(".gitignore", "a") as f:
            f.write(f"\n{config_file_name}")
    except Exception as e:
        print(e)


    # TODO : Create a .getodo_config.toml in the project directory and add these into it. Also automatically add this to .gitignore
    
def load_config(config_file_name):
    # Will always look for the config file in the folder getodo is being called
    pass



if __name__ == "__main__":
    main()
