#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path

SPACING = 2
EXT = ".mem"

do_not_enter = [".git", ".github"]


def clean_path_in_mems(path: Path, execute, depth=0):
    spacing = SPACING * depth * " "
    path_printed = False
    for x in path.iterdir():
        if x.is_file():
            if x.suffix == EXT:
                if not path_printed:
                    print(f"{spacing}* {str(path)}")
                    path_printed = True
                if execute:
                    print(f"{spacing}  (R) {x}")
                    x.unlink()
                else:
                    print(f"{spacing}  - {x}")
    for x in path.iterdir():
        if x.is_dir():
            if x.stem not in do_not_enter:
                clean_path_in_mems(x, execute, depth + 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Recursively clean .mem files \
            from the specified directory."""
    )
    parser.add_argument("path", help="Path to clean")
    parser.add_argument("-e", "--execute", action="store_true", help="Execute cleanup")

    args = parser.parse_args()
    base_path = Path(args.path).resolve()
    clean_path_in_mems(base_path, execute=args.execute)
    if not args.execute:
        print(
            "[i] No files deleted. Use the -e (--execute) option to actually delete the identified files"
        )
