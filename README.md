
# GETODO

STILL IN EARLY DEVELOPMENT

A python program that collects all the comments starting with TODO and list it all in a text file. Easy to keep track of your TODO's

## Installation

You can either download the `zip/tar.gz` from the [releases](https://github.com/vyshnav-vinod/getodo/releases) or 

 Clone this repository to your local machine. Cloning might give extra features which have not been released yet and might be unstable

```bash
git clone https://github.com/vyshnav-vinod/getodo.git
```

Navigate to the directory

```bash
cd getodo/src/
```

Install the required dependencies
>[!NOTE]
>`requirements_dev.txt` is only meant for people who wish to contribute as it includes extra packages mainly for testing

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

`-c, --config` : Create a custom config file for getodo. [More Info](https://github.com/vyshnav-vinod/getodo/blob/main/README.md#config-file)

`--override_config` : Run getodo with the default configs 

`-o, --output` : Write to the file provided here. If no file is specified, the program will write to `todo.txt`

`-t, --term` : Display the TODO's in the terminal with colors

`--add_filetypes` : If you have a filetype that is not currently supported by `getodo` you can use this to specify the filetype and the comment syntax and `getodo` will parse the TODO's

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
python3 getodo.py . --add_filetypes .kk,-- .txt,//
```
This will also parse files with the extension `kk` and `txt` and parse all the TODO's inside it.Please note that whatever value you pass along with the filetype will be considered as the comment syntax of that filetype

```bash
python3 getodo.py . -i test.py
```
This will parse all the files and sub directories in the current folder except `test.py` and write all the TODO's to `todo.txt`

### Config File

when running `getodo`, it will first look for a `getodo_config.toml` file in the root of the directory meant to be parsed. If found, getodo will use the options inside the `getodo_config.toml` file. It includes the path to the output file , the folders and files meant to be ignored by `getodo` and also if any custom filetype is to be parsed as well.

```bash
python3 getodo.py . -c
```
This will start a interactive interface to create the `getodo_config.toml` file and store it in the , in this case, the current directory. Then next time whenever you run `getodo` in that directory, you need not specify any options as `.getodo_config.toml` file will already have them. You can create different config files for different projects, making it easy to just type `getodo.py .` and get your TODO(s).

If there comes a circumstance where you need to ignore some other directories/files or add new filetypes you can use the `--override_config` flag along with the other flags. This will not load the configs from `.getodo_config.toml` and only use the arguments passed. 

