#! /usr/bin/env python3

# jinja_run.py

import sys
import logging
import argparse
import datetime

from jinja2 import Template

import init_logging

log = logging.getLogger(__name__)

def main():
    init_logging.init_logging()
    args = parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    log.debug("running...")

    datestring = datetime.datetime.now().strftime("%Y-%m-%d")


    if args.template:
        instream = open(args.template, "r")
    else:
        instream = sys.stdin

    if args.output:
        outstream = open(args.output, "w")
    else:
        outstream = sys.stdout

    file_contents = instream.read()

    template = Template(file_contents)

    expanded = template.render(datestring=datestring)

    outstream.write(expanded)

def parse_args():
    parser = argparse.ArgumentParser(
            description="expand a jinja2 template",
            allow_abbrev=False)
    parser.add_argument("--debug", help="turn on debugging output", action="store_true")
    parser.add_argument("--template", help="template-file (stdin if missing)" )
    parser.add_argument("--output", help="output-file (stdout if missing)" )

    args = parser.parse_args()
    return args



if __name__ == "__main__":
    main()

