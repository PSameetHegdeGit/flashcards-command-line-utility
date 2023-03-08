import csv
import typing
from CommandLineInterface import *

#CSV Reading
def create_entries_from_csv_file(flashcardContext: FlashcardContext, csvfile: typing.IO):
    content = csv.reader(csvfile)

    #create sets_of_flashcards and merge sets_of_flashcards into flashcardContext?

    sets_of_flashcards = [dict()]

    for entry in content:
        NotImplementedError
        #Load entry into sets_of_flashcards in flashcardContext






