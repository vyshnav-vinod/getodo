# Contains the main parser of getodo 

try:
    from getodo import utils
except ImportError:
    import utils

from os import path, scandir
from colorama import Fore, Style, init

class TodoParser:

    def __init__(self, parse_path, out_file, print_to_term) -> None:
        
        init() # Colorama

        self._todo = ['TODO:', 'TODO :']
        self._comments = utils.load_comments()
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
            # Right now, while printing to terminal, TODO(s) will also be stored in the output file
            # TODO: Give option to only print to terminal
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
        try:
            with open(file) as f:
                # Parse TODO from the file
                current_comment_syntax = utils.get_comment_syntax(f.name, self._comments)
                
                if not current_comment_syntax:
                    print(f"File type of {f.name} is not yet implemented [ADD TO IGNORE FILES]")
                
                else:
                    line_num = 0
                    file_todo = {}
                    for line in f.readlines():
                        line = line.strip()
                        line_num += 1

                        if any(line.startswith(syntax) for syntax in current_comment_syntax):
                            line = line[utils.get_first_letter_index(line):]
                            
                            if any(line.startswith(todo) for todo in self._todo):
                                file_todo[line_num] = line
                    
                    if file_todo:
                        self.output[f.name] = file_todo
        except Exception as e:
            utils.print_error(e)


    def print_to_terminal(self):
        for key,value in self.output.items():
            print(Fore.GREEN + Style.BRIGHT + "\n[FILE] "+Fore.LIGHTRED_EX+f"{key}\n"+Style.RESET_ALL)
            for line_num, content in value.items():
                print(Fore.CYAN + Style.BRIGHT + f"[Line {line_num}] " + Style.RESET_ALL + Fore.WHITE + f"{content}" + Style.RESET_ALL)


    def write_out_file(self):
        #TODO: output file is being saved in folder when getodo is run
        # Change it to folder of parse_path
        try:
            with open(self.out_file, "w+") as f:
                for key, value in self.output.items():
                    f.write(f"[FILE] {key}\n")
                    for line_num, content in value.items():
                        f.write(f"\n[Line {line_num}] {content}")
                    f.write("\n--------------------------------------------------------------------------------\n")
            print(Fore.GREEN + Style.BRIGHT + f"\nTODO(s) written to {path.abspath(self.out_file)}" + Style.RESET_ALL)
            utils.add_to_gitignore(self.parse_path, self.out_file)
        except Exception as e:
            utils.print_error(e)


# TODO: IDEA: Find a way to support multi line TODO's without having to type TODO in each line