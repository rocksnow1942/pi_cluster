#!/usr/bin/env python
"""Find corrupted photos files in a directory.

The files have almost all bytes set to 0.
"""
import argparse
import os
import pathlib
from collections.abc import Iterator


def walk_dir(directory: pathlib.Path) -> Iterator[pathlib.Path]:
    for root, _, files in os.walk(directory):
        for file in files:
            yield pathlib.Path(root) / file


def is_bad_photo(file: pathlib.Path) -> bool:
    # check if the file is a JPEG
    data = file.open("rb").read(1000)
    # if all bytes are 0, it's a bad file
    return all(b == 0 for b in data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=pathlib.Path)
    args = parser.parse_args()
    for file in walk_dir(args.directory):
        if is_bad_photo(file):
            print(file)
