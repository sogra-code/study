import io
import unittest
from contextlib import redirect_stdout

from hello_app.cli import main


class CliTest(unittest.TestCase):
    def test_main_prints_greeting(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main(["--name", "Jenkins"])
        self.assertEqual(code, 0)
        self.assertEqual(buf.getvalue().strip(), "Hello, Jenkins!")

    def test_main_default_name(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main([])
        self.assertEqual(code, 0)
        self.assertEqual(buf.getvalue().strip(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
