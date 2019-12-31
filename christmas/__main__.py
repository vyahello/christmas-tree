import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from typing import NamedTuple
from christmas.tree import Tree, ChristmasTree


class _TreeArguments(NamedTuple):
    name: str
    type: str
    speed: float


class _Arguments(NamedTuple):
    action: str
    tree: _TreeArguments


def _arguments() -> _Arguments:
    parser = ArgumentParser(
        description="Allows to manipulate with christmas tree", formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "tree",
        metavar="tree",
        type=str,
        nargs="+",
        help="Choose tree to launch (along with 'name', 'type' and 'speed' parameters)",
    )
    return _Arguments(sys.argv[1], _TreeArguments(*vars(parser.parse_args())["tree"][1:]))


def _launch_tree(tree: Tree, speed: float) -> None:
    while True:
        tree.launch(speed)


def _run_christmas(arguments: _Arguments) -> None:
    if arguments.action == "tree":
        _launch_tree(ChristmasTree(arguments.tree.name, arguments.tree.type), float(arguments.tree.speed))


if __name__ == "__main__":
    _run_christmas(_arguments())
