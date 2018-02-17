import unittest

def max_word_count(file_name):
    freq = {}
    for piece in open(file_name).read().lower().split():
        # only consider alphabetic character within this piece
        word = ''.join(c for c in piece if c.isalpha())
        if word:    # require at least one alphabetic character
            freq[word] = 1 + freq.get(word, 0)

    max_word = ''
    max_count = 0
    for (w, c) in freq.items():     # (key, value) tuples represent (word, count)
        if c > max_count:
            max_word = w
            max_count = c
    print('The most frequent word is', max_word)
    print('Its number of occurrences is', max_count)
    return max_word, max_count

class WordOccurrencesTests(unittest.TestCase):

    def test_most_occurrences(self):
        # file_name = '/Users/zhijunsheng/dev_learn_py/tictactoe-py/LICENSE'
        # or
        # file_name = './LICENSE'
        # or
        file_name = 'LICENSE'
        w, c = max_word_count(file_name)
        self.assertEqual(w, 'the')
        self.assertEqual(c, 14)


if __name__ == '__main__':
    unittest.main()
