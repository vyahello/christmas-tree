import pytest
from christmas.tree import Garland, Tree, ChristmasTree


@pytest.fixture(scope="module")
def garland() -> Garland:
    return Garland()


@pytest.fixture(scope="module")
def tree() -> Tree:
    return ChristmasTree("foo", "real")


def test_dollar(garland: Garland) -> None:
    assert garland.dollar == "$"


def test_loop(garland: Garland) -> None:
    assert garland.loop == "&"


def test_star(garland: Garland) -> None:
    assert garland.star == "*"


def test_ring(garland: Garland) -> None:
    assert garland.ring == "o"


def test_tree_name(tree: Tree) -> None:
    assert tree.name() == "foo"


def test_tree_type(tree: Tree) -> None:
    assert tree.type() == "real"
