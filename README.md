# GETODO
> A python program to collect all your TODO(s)

`getodo` is a python program that collects all your TODO(s) from a folder/file and list them for you as a file or in the terminal screen. `getodo` makes it easy to keep track of your TODO(s)

## Installation

 - You can install `getodo` via `pip`

```
pip install getodo
```

- You can also check out the [releases](https://github.com/vyshnav-vinod/getodo/releases) page to download the latest version of `getodo`. Note that it downloads the source code of `getodo` and you might need to check out this [guide](https://github.com/vyshnav-vinod/getodo/blob/main/README.md#running-from-the-source-code) to run the source code.

- You can also [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository.Cloning the repository can give you access to unreleased versions and might not be stable. Check out this [guide](https://github.com/vyshnav-vinod/getodo/blob/main/README.md#running-from-the-source-code) to run `getodo` if you have cloned it.

```
git clone https://github.com/vyshnav-vinod/getodo.git
```

### Running from the source code

If you have either downloaded from the [releases](https://github.com/vyshnav-vinod/getodo/releases) or cloned this repository, you might need to setup a few different things.

- Go into the getodo folder

- It is recommended to create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) before installing the packages.
```
python3 -m venv venv
```

- Install the required packages from `requirements.txt`
>[!NOTE]
>Use can you either `poetry` or `pip` to install the required packages.

``` 
pip install -r requirements.txt
```

- Run `getodo` using python
``` python cli.py input_path ```

## Usage

If you have downloaded via `pip`
```
getodo input_path [options]
```

else

```
python cli.py input_path [options]
```

Replace `input_path` with the path to the folder/file you want to parse. You can just type `.` to parse the current directory for TODO(s)

### Options

`-h, --help` : Display the help command

`-c, --config` : Create a custom config file for getodo. [More Info](https://github.com/vyshnav-vinod/getodo/blob/main/README.md#config)

`--override_config` : Run getodo with the default configs 

`-o, --output` : Write to the file provided here. If no file is specified, the program will write to `todo.txt`

`-t, --term` : Display the TODO's in the terminal with colors

`--add_filetypes` : If you have a filetype that is not currently supported by `getodo` you can use this to specify the filetype and the comment syntax and `getodo` will parse the TODO's

`-i, --ignore` : Ignore parsing the directories/files provided as arguments to this option


### Config

when running `getodo`, it will first look for a `getodo_config.toml` file in the root of the directory meant to be parsed. If found, getodo will use the options inside the `getodo_config.toml` file. It includes the path to the output file , the folders and files meant to be ignored by `getodo` and also if any custom filetype is to be parsed as well.

```bash
python3 getodo.py . -c
```
This will start a interactive interface to create the `getodo_config.toml` file and store it in the , in this case, the current directory. Then next time whenever you run `getodo` in that directory, you need not specify any options as `.getodo_config.toml` file will already have them. You can create different config files for different projects, making it easy to just type `getodo.py .` and get your TODO(s).

If there comes a circumstance where you need to ignore some other directories/files or add new filetypes you can use the `--override_config` flag along with the other flags. This will not load the configs from `.getodo_config.toml` and only use the arguments passed. 


## Contributing

All contributions are welcome. You can submit a issue/bug or request for a feature or ask for help in the [issues](https://github.com/vyshnav-vinod/getodo/issues) tab.

If you like to add a new feature or fix a bug, please checkout [CONTRIBUTING]() guidelines.
