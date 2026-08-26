import unittest

from hello_app.greeter import greet, word_count


class GreeterTest(unittest.TestCase):
    def test_greet_default(self):
        self.assertEqual(greet(), "Hello, world!")

    def test_greet_with_name(self):
        self.assertEqual(greet("Nastya"), "Hello, Nastya!")

    def test_greet_strips_whitespace(self):
        self.assertEqual(greet("   "), "Hello, world!")

    def test_word_count(self):
        self.assertEqual(word_count("one two three"), 3)
        self.assertEqual(word_count(""), 0)


if __name__ == "__main__":
    unittest.main()
