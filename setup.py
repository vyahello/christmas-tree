from typing import IO
from setuptools import setup, find_packages


def _description() -> str:
    """Returns project description."""
    with open("README.md", "r") as readme:  # type: IO
        return readme.read()


setup(
    name="christmas-tree",
    version="0.3.0",
    author="Volodymyr Yahello",
    author_email="vyahello@gmail.com",
    description="A simple cli christmas tree, made just for christmas mood :)",
    long_description=_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/vyahello/christmas-tree",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
