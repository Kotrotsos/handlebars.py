#!/usr/bin/env python3

import argparse
import sys
import yaml
from pybars import Compiler

def render_template(template, variables):
    compiler = Compiler()
    template = compiler.compile(template)
    return template(variables)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str)
    args, unknown = parser.parse_known_args()

    variables = {}

    # Load variables from YAML file if provided
    if args.file:
        with open(args.file, 'r') as f:
            variables = yaml.safe_load(f)

    # Parse the unknown args into a dictionary and merge with existing variables
    variables.update(dict(zip(unknown[::2], unknown[1::2])))
    # Remove '--' from keys
    variables = {k.lstrip('--'): v for k, v in variables.items()}

    template = sys.stdin.read().strip()

    result = render_template(template, variables)
    print(result)

if __name__ == "__main__":
    main()
