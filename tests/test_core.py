import unittest

from wordtally.core import count_words, tokenize, top_words


class TokenizeTest(unittest.TestCase):
    def test_lowercases_and_splits_on_punctuation(self):
        self.assertEqual(tokenize("Hello, world! HELLO."), ["hello", "world", "hello"])

    def test_keeps_apostrophes_and_digits(self):
        self.assertEqual(tokenize("It's 2 o'clock"), ["it's", "2", "o'clock"])

    def test_empty_text_has_no_words(self):
        self.assertEqual(tokenize("  ... \n"), [])


class CountWordsTest(unittest.TestCase):
    def test_counts_each_word(self):
        counts = count_words("a b a c a b")
        self.assertEqual(counts["a"], 3)
        self.assertEqual(counts["b"], 2)
        self.assertEqual(counts["c"], 1)


class TopWordsTest(unittest.TestCase):
    def test_orders_by_count_then_alphabetically(self):
        self.assertEqual(
            top_words("pear apple pear fig apple kiwi", limit=3),
            [("apple", 2), ("pear", 2), ("fig", 1)],
        )

    def test_limit_larger_than_vocabulary(self):
        self.assertEqual(top_words("one two", limit=5), [("one", 1), ("two", 1)])

    def test_rejects_limit_below_one(self):
        with self.assertRaises(ValueError):
            top_words("text", limit=0)


if __name__ == "__main__":
    unittest.main()
