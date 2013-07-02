"""Automated tests for the combinations_distance_summarizer project.

Automated tests for a command-line-based utility to find
the combinations of words and return the average distance.

@author: Sam Pottinger, 2013
@license: MIT
"""

import unittest

import summarizer


class SummarizerTests(unittest.TestCase):
    """Test case for summarizer."""

    def setUp(self):
        """Create common testing objects."""
        distances = [
            {'word': 'a', 'b': 0.2, 'c': 0.4},
            {'word': 'b', 'a': 0.2, 'c': 0.5},
            {'word': 'c', 'a': 0.4, 'b': 0.5}
        ]
        self.distance_finder = summarizer.WordDistanceFinder(distances)

    def test_word_distance_finder(self):
        """Test finding the distance between words."""
        self.assertEqual(self.distance_finder.find_distance('a', 'b'), 0.2)

    def test_word_distance_finder_list(self):
        """Test finding the distance between words in a list."""
        result = self.distance_finder.find_distance_list(['a', 'b'])
        self.assertEqual(result, 0.2)

    def test_find_combinations_and_distances(self):
        """Test finding the combinations and distances between them."""
        combinations, distances = summarizer.find_combiantions_and_distances(
            self.distance_finder,
            ['a', 'b', 'c']
        )
        
        expected = (('a', 'b'), ('a', 'c'), ('b', 'c'))
        self.assertItemsEqual(expected, combinations)

        expected = (0.2, 0.4, 0.5)
        self.assertItemsEqual(expected, distances)

    def test_arithmetic_mean(self):
        """Test finding the arithmetic mean of a sequence of numbers."""
        mean = summarizer.arithmetic_mean([1, 2, 3])
        self.assertAlmostEqual(mean, 2)


if __name__ == '__main__':
    unittest.main()