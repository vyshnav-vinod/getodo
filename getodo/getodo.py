from os import path, scandir
from json import loads

class TodoParser:

    def __init__(self, parse_path, out_file, print_to_term) -> None:
        
        self._todo = ['TODO:', 'TODO :']
        with open(path.join(path.dirname(__file__), "comment_syntax.json"), "r") as f:
            json_data = f.read()
        self._comments = loads(json_data)
        self.output = {}

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
            current_comment_syntax = self.get_comment_syntax(f.name)
            
            if not current_comment_syntax:
                print(f"File type of {f.name} is not yet implemented [ADD TO IGNORE FILES]")
            
            else:
                line_num = 0
                file_todo = {}
                for line in f.readlines():
                    line = line.strip()
                    line_num += 1

                    if any(line.startswith(syntax) for syntax in current_comment_syntax):
                        line = line[self.get_first_letter_index(line):]
                        
                        if any(line.startswith(todo) for todo in self._todo):
                            # Decide what to do with the TODO's (either print directly or store in variable to reduce code for printing to term or writing to file or both.. just reduce code)
                            file_todo[line_num] = line
                
                if file_todo:
                    self.output[f.name] = file_todo


    def get_comment_syntax(self, file):
        file_type = file[file.rindex('.'):]
        return self._comments.get(file_type, '')


    def get_first_letter_index(self, s: str):
        for c in s:
            if c.isalpha():
                return s.index(c)
            
# TODO: After completing this, write tests before moving to next portion of the flags
