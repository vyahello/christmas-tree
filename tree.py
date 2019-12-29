from christmas.tree import Tree, ChristmasTree


def _launch_tree(tree: Tree) -> None:
    """Runs tree in an infinite loop."""
    while True:
        tree.launch()


if __name__ == "__main__":
    _launch_tree(ChristmasTree(name="Slider", type_="real"))
