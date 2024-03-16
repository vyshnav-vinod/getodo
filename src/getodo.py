# CLI functionality code


# OPTION FOR CLI
# getodo.py dir/file
# getodo.py dir/file -o output.txt
# getodo.py dir/file -term
# getodo.py dir/file -i ignoredir/file ignoredir/file ignoredir/file [Maybe make this a one-time option only and store it in a .cfg maybe???]

import todoparser

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Scan a file or a directory and extract all the TODO into a file/stdout"
    )

    # Required argument
    parser.add_argument("input_path", help="Directory or file to scan for TODO's")

    # Optional arguments
    parser.add_argument("-o", "--output", help="Output file to store the TODO's")
    # parser.add_argument("-t", "--term", action="store_true", help="Print the TODO's to terminal")
    # parser.add_argument("-i", "--ignore", nargs="+", help="Ignore specific directories or files")

    args = parser.parse_args()

    input_path = args.input_path
    output_file = args.output
    # print_to_terminal = args.term
    # ignore_paths = args.ignore

    todoparser.main(input_path, output_file)


if __name__ == "__main__":
    main()
