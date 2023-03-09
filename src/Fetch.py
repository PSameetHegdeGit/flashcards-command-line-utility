import csv
import typing
from CommandLineInterface import *


'''
File lists functions that grab entries from a source 

'''


def get_entries_from_csv_file(flashcardContext: FlashcardContext, csvfile: typing.IO):

    content = csv.reader(csvfile)

    #create sets_of_flashcards and merge sets_of_flashcards into flashcardContext?



    for entry in content:
        put
        NotImplementedError
        #Load entry into sets_of_flashcards in flashcardContext






