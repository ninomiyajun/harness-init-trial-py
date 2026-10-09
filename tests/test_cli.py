import io
import os
import tempfile
import unittest
from contextlib import redirect_stderr

from wordtally.cli import main


class CliTest(unittest.TestCase):
    def run_cli(self, argv, stdin_text=""):
        stdout = io.StringIO()
        code = main(argv, stdin=io.StringIO(stdin_text), stdout=stdout)
        return code, stdout.getvalue()

    def test_reads_standard_input(self):
        code, output = self.run_cli(["-n", "2"], "b a b c b a")
        self.assertEqual(code, 0)
        self.assertEqual(output, "3\tb\n2\ta\n")

    def test_reads_a_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "sample.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write("red green red")
            code, output = self.run_cli([path])
        self.assertEqual(code, 0)
        self.assertEqual(output, "2\tred\n1\tgreen\n")

    def test_rejects_limit_below_one(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                self.run_cli(["-n", "0"], "text")
        self.assertEqual(raised.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
