"""Command line entry point: print the most frequent words of a text."""

import argparse
import sys
from typing import List, Optional, TextIO

from wordtally.core import top_words


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wordtally",
        description="Print the most frequent words of a text file (or standard input).",
    )
    parser.add_argument("file", nargs="?", help="text file to read; reads standard input when omitted")
    parser.add_argument("-n", "--limit", type=int, default=10, help="how many words to print (default: 10)")
    return parser


def main(argv: Optional[List[str]] = None, stdin: TextIO = sys.stdin, stdout: TextIO = sys.stdout) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.limit < 1:
        parser.error("--limit must be 1 or more")

    if args.file:
        with open(args.file, encoding="utf-8") as handle:
            text = handle.read()
    else:
        text = stdin.read()

    for word, count in top_words(text, args.limit):
        stdout.write(f"{count}\t{word}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
