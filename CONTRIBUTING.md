To setup `getodo` for contributing, follow these steps

- [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the repository and then [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) it

- Navigate into the cloned repository

- Create a python [virtual environment](https://docs.python.org/3/tutorial/venv.html) [OPTIONAL]

- You can either use ```pip install -r requirements_dev.txt``` or `poetry install` to install the required libraries.

- It is recommended that you create a branch for the bug fix/feature ``` git branch feature_name``` and then work on it ```git checkout feature_name``` 

- After finishing the work, run the tests by simply using the pytest command
```pytest```

- Make sure tests pass and then make a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

> [!NOTE]
> If you feel stuck or confused, don't hesitate to open a new issue. :) I will be happy to help
