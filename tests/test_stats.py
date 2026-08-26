import unittest

from hello_app.stats import summarize


class StatsTest(unittest.TestCase):
    def test_summarize(self):
        result = summarize([1, 2, 3, 4])
        self.assertEqual(result["count"], 4)
        self.assertEqual(result["sum"], 10)
        self.assertEqual(result["mean"], 2.5)
        self.assertEqual(result["min"], 1)
        self.assertEqual(result["max"], 4)

    def test_summarize_single_value(self):
        result = summarize([7])
        self.assertEqual(result["count"], 1)
        self.assertEqual(result["mean"], 7.0)

    def test_summarize_empty_raises(self):
        with self.assertRaises(ValueError):
            summarize([])


if __name__ == "__main__":
    unittest.main()
