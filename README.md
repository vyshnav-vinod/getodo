
# GETODO

STILL IN EARLY DEVELOPMENT

A python program that collects all the comments starting with TODO and list it all in a text file. Easy to keep track of your TODO's

## Installation

You can either download the `zip/tar.gz` from the [releases](https://github.com/vyshnav-vinod/getodo/releases) or Clone this repository to your local machine.

```bash
git clone https://github.com/vyshnav-vinod/getodo.git
```

Navigate to the directory

```bash
cd getodo/src/
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Run the following command
```bash
python3 getodo.py input_path
```
Replace `input_path` with the path to the directory or file you want to parse for TODO's


## Usage



```bash
python3 getodo.py input_path
```
Replace `input_path` with the path to the directory or file you want to parse for TODO's

### Options ###

`-h, --help` : Display the help command

`-o, --output` : Write to the file provided here. If no file is specified, the program will write to `todo.txt`

`-t, --term` : Display the TODO's in the terminal with colors

`-i, --ignore` : Ignore parsing the directories/files provided as arguments to this option

### Examples ###

```bash
python3 getodo.py . 
```
This will parse all the files and sub directories in the current folder and write all the TODO's to `todo.txt`

```bash
python3 getodo.py . -o mytodo.txt 
```
This will parse all the files and sub directories in the current folder and write all the TODO's to `mytodo.txt`

```bash
python3 getodo.py . -t
```
This will parse all the files and sub directories in the current folder and display it in the terminal with colors

```bash
python3 getodo.py . -i test.py
```
This will parse all the files and sub directories in the current folder except `test.py` and write all the TODO's to `todo.txt`
