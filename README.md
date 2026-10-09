# harness-init-trial-py

Sample Python project for trying a project harness installer (P6 trial).

It contains a small command, `wordtally`, that prints the most frequent words of a text.
The code uses only the Python standard library.

## Usage

Requires Python 3.9 or later.

```sh
# from the repository root, without installing
PYTHONPATH=src python3 -m wordtally README.md -n 5

# or read standard input
echo "b a b c b a" | PYTHONPATH=src python3 -m wordtally -n 2
```

Each output line is the count and the word, separated by a tab.

## Tests

```sh
python3 -m unittest
```

The same command runs in CI (`.github/workflows/ci.yml`).
