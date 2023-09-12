import os

'''
File lists functions and classes that interact with storage 

'''

class FlashcardContext:

    def __init__(self, directory='%USERPROFILE%/.Flashcards'):
        '''
        Represents the current directory where flashcards and metadata is stored

        :param directory: path to flashcard directory; defaults to %USERPROFILE%/.Flashcards; set to '' for testing

        Attributes:

        noOfFlashcards: total number of flashcards across all sets
        day: day we are inputting flashcards in
        setsOfFlashcards: sets of 10 flashcards (except last flashcard set)
        '''

        # don't save state
        if directory == '':
            self.no_of_flashcards = 0
            self.sets_of_flashcards = [dict()]
        else:

            self.directory = directory

            ## initialize directory
            if not os.path.isdir(directory):
                os.mkdir(directory)

            # create metadata for flashcard store
            if not os.path.isfile(f"{directory}/current_state.txt"):
                open(f"{directory}/current_state.txt", "x")

            # set current state if nothing exists in current state
            with open(fr"{directory}/current_state.txt", "r+") as currentStatePtr:
                if os.path.getsize(f"{directory}/current_state.txt") == 0:
                    # indicates fresh flashcard db
                    currentStatePtr.write("no_of_flashcards:0\n")
                    currentStatePtr.write("day:0")


            with open(fr"{directory}/current_state.txt", "r") as currentStatePtr:
                current_state = map(lambda x: x.split(':'),  currentStatePtr.readlines())
                current_state = list(map(lambda x: {x[0]: x[1].strip()}, current_state))
                self.no_of_flashcards = int(current_state[0]['no_of_flashcards'])
                self.day = int(current_state[1]['day'])

            self.sets_of_flashcards = self.populate_flashcards(self.no_of_flashcards)


    def generate_metadata_folder(self):

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

                if not os.path.isfile(f"{self.directory}/flashcardset_{i}"):
                    open(f"{self.directory}/flashcardset_{i}", "x")

                with open(fr"{self.directory}/flashcardset_{i}", 'r') as flashcard_ptr:
                    flashcard_set = flashcard_ptr.readlines()
                    fl = {}
                    for flashcard in flashcard_set:
                        a, b = flashcard.split(':')
                        fl[a] = b.strip()
                    sets_of_flashcards.append(fl)

        return sets_of_flashcards

    def write_set_to_store(self, flashcardSet: dict, flashcardIdx: int):
        '''
        writes a flashcard set to its corresponding txt file under .Flashcards.
        Flashcard sets are ordered by when created. Will always be in that order

        :param flashcardSet: key value pairing corresponding to txt file
        :param flashcard_idx: IDK
        :return: None
        '''

        with open(fr"{self.directory}/flashcardset_{flashcardIdx}", 'w') as set_ptr:
            for word, definition in flashcardSet.items():
                set_ptr.write(f"{word}:{definition}\n")


    def append_entry_to_set(self, flashcardIdx: int, word: str, definition: str):
        '''
        append entry to the file corresponding to a flashcard set

        :param flashcard_idx: set position
        :param word
        :param definition
        :return: None
        '''

        with open(fr"{self.directory}/flashcardset_{flashcardIdx}", 'a') as set_ptr:
            set_ptr.write(f"{word}:{definition}\n")


    def update_current_state(self):
        '''
        Updates current_state.txt

        :return: None
        '''

        noOfFlashcards = len(self.sets_of_flashcards)
        day = self.day

        with open(f"{self.directory}/current_state.txt", 'w') as current_state_ptr:
            current_state_ptr.write(f"no_of_flashcards:{noOfFlashcards}\n")
            current_state_ptr.write(f"day:{day}")



