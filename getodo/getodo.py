from os import path, scandir
from json import loads
from colorama import Fore, Style, init

class TodoParser:

    def __init__(self, parse_path, out_file, print_to_term) -> None:
        
        init() # Colorama

        self._todo = ['TODO:', 'TODO :']
        with open(path.join(path.dirname(__file__), "comment_syntax.json"), "r") as f:
            json_data = f.read()
        self._comments = loads(json_data)
        self.output = {}

        self.parse_path = parse_path
        # Create a out file specified by user or a default "todo.txt" in the folder where `getodo` is run
        self.out_file = out_file or "todo.txt" 
        self.print_to_term = print_to_term

        if path.isdir(parse_path):
            # User provided a directory to parse
            self.parse_dir(parse_path)
            pass

        else:
            # User provided a file to parse
            self.parse_file(parse_path)
            pass
        
        if not self.output:
            print(Fore.RED + Style.BRIGHT + "NO TODO (s) found" + Style.RESET_ALL)
            exit(0)

        if self.print_to_term:
            self.print_to_terminal()
            self.write_out_file()
        
        else:
            # Only write to output file
            self.write_out_file()


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


    def print_to_terminal(self):
        for key,value in self.output.items():
            print(Fore.GREEN + Style.BRIGHT + "\n[FILE] "+Fore.LIGHTRED_EX+f"{key}\n"+Style.RESET_ALL)
            for line_num, content in value.items():
                print(Fore.CYAN + Style.BRIGHT + f"[Line {line_num}] " + Style.RESET_ALL + Fore.WHITE + f"{content}" + Style.RESET_ALL)


    def write_out_file(self):
        pass    
# TODO: After completing this, write tests before moving to next portion of the flags
