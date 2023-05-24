import csv
import typing
from CommandLineInterface import *
import random



def get_entries_from_csv_file(csvfile: typing.IO):

    return [Entry(row[0], row[1]) for row in csv.reader(csvfile)]




class Entry:
    def __init__(self, word: str, definition: str):
        self.word = word
        self.definition = definition

