from abc import ABC, abstractmethod
from random import randint
from time import sleep
from typing import NamedTuple, Union
from christmas.support import reset_terminal


_random_static: int = randint(1, 30)


def tree_length(from_: int, to_: int = _random_static) -> int:
    return randint(from_, to_)


def format_tree(character: Union[int, str]) -> None:
    print("{:^50}".format(character))


class Tree(ABC):
    @abstractmethod
    def type(self) -> str:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def launch(self, speed: float = 0.2) -> None:
        pass


class Garland(NamedTuple):
    dollar: str = "$"
    ring: str = "o"
    loop: str = "&"
    star: str = "*"


class ChristmasTree(Tree):
    def __init__(self, name: str, type_: str) -> None:
        self._name: str = name
        self._type: str = type_
        self._garland: Garland = Garland()

    def type(self) -> str:
        return self._type

    def name(self) -> str:
        return self._name

    def launch(self, speed: float = 0.2) -> None:
        reset_terminal()
        for iteration in range(1, 30, 2):
            if iteration == 1:
                character = self._garland.dollar
            elif tree_length(from_=1) % 4 == 0:
                character = self._garland.ring
            elif tree_length(from_=1) % 3 == 0:
                character = self._garland.loop
            else:
                character = self._garland.star
            format_tree(character * iteration)
        format_tree("|||")
        format_tree("|||")
        sleep(speed)
