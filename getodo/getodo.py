from os import path, scandir
from json import loads

class TodoParser:

    def __init__(self, parse_path, out_file, print_to_term) -> None:
        self._todo = ['TODO:', 'TODO :']
        with open("comment_syntax.json", "r") as f:
            json_data = f.read()
        self._comments = loads(json_data)

        self.parse_path = parse_path
        self.out_file = out_file
        self.print_to_term = print_to_term

        if path.isdir(parse_path):
            # User provided a directory to parse
            self.parse_dir(parse_path)
            pass

        else:
            # User provided a file to parse
            self.parse_file(parse_path)
            pass
    

    def parse_dir(self, dir):
        # Recursively walk the directory and when the file is encountered, parse it
        dir_contents = scandir(dir)
        
        for contents in dir_contents:
            if contents.is_dir():
                self.parse_dir(contents)
            
            if contents.is_file():
                self.parse_file(contents)



    def parse_file(self, file):
        with open(file) as f:
            # Parse TODO from the file
            for line in f.readlines():
                pass



# TODO: After completing this, write tests before moving to next portion of the flags