"""
Section 12 Challenge - Map
Wrap each of the 4 blocks of code in function definitions, then use the timeit module to time each one.

Remember to import timeit at the start of the file.

My solution will use a slightly different approach, to save time in the video.
The test of whether your solution works is if it successfully times all 4 approaches to capitalising the
characters and words in text.
"""
import timeit

text = "what have the romans ever done for us"


def comp_capitals():
    return [char.upper() for char in text]


def map_capitals():
    return list(map(str.upper, text))


def comp_words():
    return [word.upper() for word in text.split(' ')]


def map_words():
    return list(map(str.upper, text.split(' ')))


if __name__ == "__main__":
    print("comp_capitals: {}".format(timeit.timeit(comp_capitals, number=10000)))
    print("map_capitals: {}".format(timeit.timeit(map_capitals, number=10000)))
    print("comp_words: {}".format(timeit.timeit(comp_words, number=10000)))
    print("map_words: {}".format(timeit.timeit(map_words, number=10000)))
