#!/usr/bin/env python3
import argparse
import sys
from typing import Set


def read_file(filename: str) -> str:
    raise NotImplementedError  # TODO


# You can use something else than a set!
def get_variables(template: str) -> Set[str]:
    raise NotImplementedError  # TODO


def main(template_filename: str) -> int:
    template = read_file(template_filename)

    # Find the required variables
    required_variables = get_variables(template)

    # Ask the user for required variables' value, except for "today"
    ...

    # Render filename
    filename = ""

    # Check if filename exists, exit if it does
    ...

    # Write to file
    with open(filename, "w") as f:
        f.write(...)

    print(f"\n./{filename}")

    # Returning 0 is just good practice for CLI commands, 0 means success
    return 0


# Why? https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Doc: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description="render a template file")
    parser.add_argument("template", help="template filename")
    args = parser.parse_args()

    # Doc: https://docs.python.org/3/library/sys.html#sys.exit
    sys.exit(main(args.template))
