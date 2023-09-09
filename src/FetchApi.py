import csv
import typing
import random


class Entry:
    def __init__(self, word: str, definition: str):
        self.word = word
        self.definition = definition



def get_entries_from_csv_file(csvfile: typing.IO):

    return {row[0]: row[1] for row in csv.reader(csvfile)}


def get_random_set(entries: list[Entry]):
    '''
    randomly picks entries from list to generate a set consisting of 10 word, definition tuples

    :param entries: list of words and their definition
    :return: dict structured as word : definition
    '''

    noOfEntries = len(entries)
    setOfFlashcards = {}

    for _ in range(10):

        entryIdx = random.randint(0, noOfEntries - 1)
        entry = entries[entryIdx]
        setOfFlashcards[entry.word] = entry.definition

        entries[entryIdx], entries[-1] = entries[-1], entries[entryIdx]

        entries = entries[:-1]

    return setOfFlashcards






