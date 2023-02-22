import os


class FlashcardContext:


    def __init__(self, directory='.Flashcards'):
        '''
        Read current_state.txt for no_of_flashcards and counter
        :return: IDK
        '''

        self.directory = directory

        if not os.path.isdir(directory):
            os.mkdir(directory)

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
            self.noOfFlashcards = int(current_state[0]['no_of_flashcards'])
            self.day = int(current_state[1]['day'])

        self.setsOfFlashcards = self.populate_flashcards(self.noOfFlashcards)

    def populate_flashcards(self, no_of_flashcards: int):
        '''
        reads all flashcard files from .Flashcards and initializes sets_of_flashcards (represented as an array of
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

def write_set_to_store(flashcardContext: FlashcardContext, flashcardSet: dict, flashcardIdx: int):
    '''
    writes a flashcard set to its corresponding txt file under .Flashcards.
    Flashcard sets are ordered by when created. Will always be in that order

    :param flashcardSet: key value pairing corresponding to txt file
    :param flashcard_idx: IDK
    :return: None
    '''

    with open(fr"{flashcardContext.directory}/flashcardset_{flashcardIdx}", 'w') as set_ptr:
        for word, definition in flashcardSet.items():
            set_ptr.write(f"{word}:{definition}\n")


def append_entry_to_set(flashcardContext: FlashcardContext, flashcardIdx: int, word: str, definition: str):
    '''
    append entry to the file corresponding to a flashcard set

    :param flashcard_idx: set position
    :param word
    :param definition
    :return: None
    '''

    with open(fr"{flashcardContext.directory}/flashcardset_{flashcardIdx}", 'a') as set_ptr:
        set_ptr.write(f"{word}:{definition}\n")


def update_current_state(flashcardContext: FlashcardContext):
    '''
    Updates current_state.txt

    :return: None
    '''

    noOfFlashcards = len(flashcardContext.setsOfFlashcards)
    day = flashcardContext.day

    with open(f"{flashcardContext.directory}/current_state.txt", 'w') as current_state_ptr:
        current_state_ptr.write(f"no_of_flashcards:{noOfFlashcards}")
        current_state_ptr.write(f"day:{day}")


def exit_flashcard_app(flashcardContext: FlashcardContext):

    update_current_state(flashcardContext)
    exit()


