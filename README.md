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

``` 
pip install -r requirements.txt
```

- Run `getodo` using python
``` python getodo_cli.py input_path ```

## Usage

If you have downloaded via `pip`
```
getodo input_path [options]
```

else

```
python getodo_cli.py input_path [options]
```

Replace `input_path` with the path to the folder/file you want to parse. You can just type `.` to parse the current directory for TODO(s)

### Options

`-h, --help` : Display the help command

`-o, --output` : Write to the file provided here. If no file is specified, the program will write to `todo.txt`

`-t, --term` : Display the TODO's in the terminal with colors

`-i, --ignore` : Ignore parsing the directories/files provided as arguments to this option

## Additional Configurations

Right now, `getodo` only supports editing the `getodo_cfg.json` directly to add some additional configs. In the future, a `-c,--config` command will be added so that anyone can add more configs(especially those who downloaded from `pip`). To add more comment syntax, change the default output file name, to add more default ignored folders and files and to even change the word to be parsed(i.e, If you want to parse comments beginning with `NOTE:` or `IMPORTANT:` , etc), go to `getodo_cfg.json` and add or remove the configs as you wish. Please note that you must stick to the given syntax or else the program will break. `getodo_cfg.json` can be found in the `getodo/` directory for those who cloned the repo. For those who installed via `pip`, please refer to this [link](https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages) and find out where the `getodo` folder is present and make your changes in there. You can always ask for help by raising an [issue](https://github.com/vyshnav-vinod/getodo/issues) and i will be glad to help.

## Contributing

All contributions are welcome. You can submit a issue/bug or request for a feature or ask for help in the [issues](https://github.com/vyshnav-vinod/getodo/issues) tab.

If you like to add a new feature or fix a bug, please checkout [CONTRIBUTING](https://github.com/vyshnav-vinod/getodo/blob/main/CONTRIBUTING.md) guidelines.
