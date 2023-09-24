import json
import os



#Todo: Should I take out non disk-write fxns or keep them in; ie keep everything under flashcard context
class FlashcardContext:

    # Todo: Find better ways to organize attributes; Do I load config to a class?
    def __init__(self, directory='%USERPROFILE%/.FlashcardContexts'):
        '''
        Represents the current directory where flashcards and metadata is stored

        :param directory: path to flashcard directory; defaults to %USERPROFILE%/.FlashcardContexts; set to '' for testing

        Attributes:

        noOfFlashcards: total number of flashcards across all sets
        day: day we are inputting flashcards in
        setsOfFlashcards: sets of 10 flashcards (except last flashcard set)
        '''

        ## initialize directory if directory doesn't exist
        if not os.path.isdir(directory):
            os.mkdir(directory)

        #if metadata.json doesn't exist it
        if not os.path.isfile(f"{directory}/metadata.json"):
            self.generate_metadata_folder(directory)

        self.path_to_flashcards = f"{directory}/flashcards"
        self.path_to_dump = f"{directory}/dump_file"

        ## if flashcard directory doesn't exist, create it
        if not os.path.isdir(self.path_to_flashcards):
            os.mkdir(self.path_to_flashcards)

        ## if dump directory doesn't exist, create it
        if not os.path.isdir(self.path_to_dump):
            os.mkdir(self.path_to_dump)

        ## get values from metadata
        with open(fr"{directory}/metadata.json", "r") as metadata_ptr:
            metadata = json.loads(metadata_ptr.read())
            self.no_of_flashcards = int(metadata["flashcards"]["no_of_flashcards"])
            self.review_cycle = int(metadata["flashcards"]["review_cycle"])
            self.line_pointer = int(metadata["dump_file"]["line_pointer"])

        ## create array of dictionaries for sets of flashcards
        self.sets_of_flashcards = self.populate_flashcards(self.no_of_flashcards)

    def generate_metadata_folder(self, directory):
        '''
        Generates a metadata folder in specified path

        :param directory: path to directory
        '''

        metadata = {
            "dump_file": {
                "path_to_dump": f"{directory}/dump_file.txt",
                "line_pointer": 0
            },
            "flashcards": {
                "path_to_flashcards": f"{directory}/.FlashcardContexts/",
                "no_of_flashcards": 0,
                "review_cycle": 5,
            }
        }

        with open(f"{directory}/metadata.json", "x") as metadata_ptr:
            json.dump(metadata, metadata_ptr)

    def populate_flashcards(self, no_of_flashcards: int):
        '''
        reads all flashcard files when a valid directory is specified (i.e. not '') and initializes sets_of_flashcards (represented as an array of
        dictionaries) to those flashcards

        :param no_of_flashcards:
        :return: a list of the sets of flashcards
        '''

        sets_of_flashcards = []

        if no_of_flashcards == 0:
            sets_of_flashcards.append(dict())
        else:
            for i in range(no_of_flashcards):

                if not os.path.isfile(f"{self.}/flashcardset_{i}"):
                    open(f"{self.path_to_flashcards}/flashcardset_{i}", "x")

                with open(fr"{self.path_to_flashcards}/flashcardset_{i}", 'r') as flashcard_ptr:
                    flashcard_set = flashcard_ptr.readlines()
                    fl = {}
                    for flashcard in flashcard_set:
                        a, b = flashcard.split(':')
                        fl[a] = b.strip()
                    sets_of_flashcards.append(fl)

        return sets_of_flashcards


