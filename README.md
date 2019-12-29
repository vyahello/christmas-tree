[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Build Status](https://travis-ci.org/vyahello/christmas-tree.svg?branch=master)](https://travis-ci.org/vyahello/christmas-tree)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

# Christmas tree
This tool will launch christmas tree right in your terminal, use it just for fun :)

## Tools
- python 3.6, 3.7, 3.8
- [black](https://black.readthedocs.io/en/stable/)
- [pylint](https://www.pylint.org/)
- [pytest](https://pypi.org/project/pytest/)

## Usage

Please run following script to obtain latest package from PYPI:
```bash
➜ pip install christmas-tree
```
Then please execute instructions below to launch game from your environment:
```python
from christmas.tree import Tree, ChristmasTree


tree: Tree = ChristmasTree(name="awesome", type_="real")
tree.launch(speed=.2)
```

### Demo
![Screenshot](christmas/img/image.png)


## Development notes

### Launch source code
To be able to run source code please execute command below:
```bash
~ python tree.py
``` 

### CI 

Project has Travis CI integration thus code analysis (`black`, `pylint`) and unittests (`pytest`) will be run automatically
after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
~ ./run-code-analysis.sh
```

### Meta

Author – Volodymyr Yahello

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
3. `pip install -r requirements-dev.txt` to install all development project dependencies