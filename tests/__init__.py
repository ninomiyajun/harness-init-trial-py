"""Make the package under src/ importable when running `python3 -m unittest` from the repository root."""

import pathlib
import sys

_SRC = pathlib.Path(__file__).resolve().parent.parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
