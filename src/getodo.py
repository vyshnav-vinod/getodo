# CLI functionality code


from os import path
from todoparser import TodoParser

import argparse


class ParseKeyValue(argparse.Action):

    # https://stackoverflow.com/a/68829190/23381273

    def __call__(self, parser, args, values, option_string=None):
        try:
            d = dict(map(lambda x: x.split(","), values))
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

    args = parser.parse_args()

    input_path = args.input_path
    output_file = args.output
    print_to_terminal = args.term
    ignore_paths = args.ignore
    add_filetypes = args.add_filetypes  # dir

    if ignore_paths:
        ignore_paths = list(map(path.basename, ignore_paths))

    TodoParser(base_dir=input_path, out_file=output_file, print_to_term=print_to_terminal, user_ignore_paths=ignore_paths, user_add_filetypes=add_filetypes)


if __name__ == "__main__":
    main()
