"""Utility to find the combinations of words and return the average distance.

Utility program to find the combinations of words in a given list, the distances
between those combination pairs, and the average of those distances. The final
return value is that average.

@author: Ariel Aguilar, 2013
@author: Sam Pottinger, 2013
@license: MIT
"""

import csv
import itertools
import sys


class WordDistanceFinder:
    """Wrapper around a list of dictionaries with distances between words.

    Wrapper around a list of dictionaries with the distances between words
    loaded CSV or other structured data.
    """

    def __init__(self, distances):
        """Create a new word distance finder.

        @param distances: Description of the distances between words. Should
            be a list with dictionaries. The dictionaries should have a 'word'
            key with a value indicating what word the dictionary is for. The
            rest of the keys should be other words with distances to those
            words.
        @type distances: list of dict
        """
        self.__distances = distances

    def find_distance_list(self, words):
        """Find the distance between the two words in the given parameter.

        @param words: The list of two words to find the distance between.
        @type words: List of str.
        @return: The distances between those words.
        @rtype: list of float
        """
        if len(words) != 2:
            raise ValueError('Can only find distance between two words.')
        return self.find_distance(words[0], words[1])

    def find_distance(self, word_1, word_2):
        """Find the distance between two words.

        @param word_1: The first word in the pair of words to find the distance
            between.
        @type word_1: str
        @param word_2: The second word in the pair of words to find the distance
            between.
        @type: word_2: str
        @return: The distance between word_1 and word_2
        @rtype: float
        """
        word_rows = filter(lambda x: x['word'] == word_1, self.__distances)
        
        if len(word_rows) == 0:
            raise ValueError('%s not found.' % word_1)
        elif len(word_rows) > 1:
            raise ValueError('Multiple entries for %s found.' % word_1)

        word_row = word_rows[0]
        if word_2 in word_row:
            return float(word_row[word_2])
        else:
            raise ValueError('Distance %s to %s not found.' % (word_1, word_2))


def load_distances_csv(loc):
    """Load a CSV file containing word distances.

    @param loc: The path or file name of the CSV file to load.
    @type loc: str
    @return: WordDistanceFinder from contents of the given CSV file.
    @rtype: WordDistanceFinder
    """
    with open(loc, 'rb') as f:
        dialect = csv.Sniffer().sniff(f.readline())
        f.seek(0)
        values = list(csv.DictReader(f, dialect=dialect))

    return WordDistanceFinder(values)


def load_words_to_summarize(loc):
    with open(loc, 'rb') as f:
        words = f.read().split('\n')
    return filter(lambda x: x != '', words)


def find_combiantions_and_distances(distance_finder, words):
    # Find distances for all combinations
    word_combinations = list(itertools.combinations(words, 2))
    word_distances = map(distance_finder.find_distance_list, word_combinations)

    return (word_combinations, word_distances)


def arithmetic_mean(target):
    return sum(target) / float(len(target))


def run_cli():
    """Run the command line interface driver for this program.

    @return: The average distance between the combination of user-provided
        words or None if error.
    @rtype: float
    """

    # Check correct number of arguments supplied
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        with open('usage.txt') as f:
            sys.stderr.write(f.read())
        return None

    # Parse command line arguments and load distances
    words_loc = sys.argv[1]
    distances_csv_loc = sys.argv[2]

    if len(sys.argv) == 4:
        display_pairs = sys.argv[3].lower() == 'y'
    else:
        display_pairs = False

    words = load_words_to_summarize(words_loc)
    distance_finder = load_distances_csv(distances_csv_loc)

    word_combinations, word_distances = find_combiantions_and_distances(
        distance_finder, words)

    # Display individual pairs
    if display_pairs:
        for (pair, distance) in zip(word_combinations, word_distances):
            print "%s: %s" % (pair, distance)

    return arithmetic_mean(word_distances)


if __name__ == '__main__':
    result = run_cli()

    if result:
        sys.stdout.write(str(result))
        sys.stdout.write('\n')
        sys.exit(0)
    else:
        sys.exit(1)
