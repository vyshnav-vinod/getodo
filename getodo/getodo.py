import os


class TodoParser:

    def __init__(self, parse_path, out_file, print_to_term) -> None:
        
        self.parse_path = parse_path
        self.out_file = out_file
        self.print_to_term = print_to_term

        if os.path.isdir(parse_path):
            # User provided a directory to parse
            pass

        else:
            # User provided a file to parse
            pass
    

    def parse_dir(self):
        # Recursively walk the directory and when the file is encountered, parse it
        pass


    def parse_file(self, file):
        with open(file) as f:
            # Parse TODO from the file
            pass


# TODO: After completing this, write tests before moving to next portion of the flags