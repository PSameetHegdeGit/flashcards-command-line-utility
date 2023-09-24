from src.FlashcardContexts.FlashcardContext import *
from src.FlashcardCsv.FlashcardCsvManager import *

class FlashcardApi:
    # Todo: determine better way to pass status codes

    def __init__(self, flashcardContext: FlashcardContext):
        self.flashcard_context = flashcardContext
        self.flashcard_csv_manager = FlashcardCsvManager()


    ######  COMMAND LINE INTERFACE FXNALITY  ######

    def put_entry(self, word: str, definition: str):
        '''
        Add or update entry in FlashcardContext.sets_of_flashcards

        :return: None
        '''

        sets_of_flashcards = self.flashcard_context.sets_of_flashcards
        idx_of_set_to_add_in = self.find_set_idx_of_entry(word)
        flashcard_set = sets_of_flashcards[idx_of_set_to_add_in]

        ## update word
        if idx_of_set_to_add_in != -1:
            flashcard_set[word] = definition
            return self.write_set_to_store(flashcard_set, idx_of_set_to_add_in)

        ## add word
        else:
            if len(flashcard_set) == 10:
                sets_of_flashcards.append(dict())
                self.update_current_state()

            sets_of_flashcards[-1][word] = definition
            self.append_entry_to_set(len(sets_of_flashcards) - 1, word, definition)
            return 1

    def delete_entry(self, word: str):
        NotImplementedError

    def list_entries(self):

        for flashcard_set in self.flashcard_context.sets_of_flashcards:
            for word, definition in flashcard_set.items():
                print(f"{word} : {definition}")


    def find_set_idx_of_entry(self, word: str):
        '''
        Finds the idx of set in FlashcardContext.sets_of_flashcards that word exists in

        :return: set idx if word exists; -1 if does not exist
        '''

        for idx, flashcard_set in enumerate(self.flashcard_context.sets_of_flashcards):
            if word in flashcard_set:
                return idx

        return -1

    ######  Disk Interface for Flashcard Context  ######


    def write_set_to_store(self, flashcardSet: dict, flashcardIdx: int):
        '''
        writes a flashcard set to its corresponding txt file under .FlashcardContexts.
        Flashcard sets are ordered by when created. Will always be in that order

        :param flashcardSet: key value pairing corresponding to txt file
        :param flashcard_idx: IDK
        :return: None
        '''

        with open(fr"{self.flashcard_context.path_to_flashcards}/flashcardset_{flashcardIdx}", 'w') as set_ptr:
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

        with open(fr"{self.flashcard_context.path_to_flashcards}/flashcardset_{flashcardIdx}", 'a') as set_ptr:
            set_ptr.write(f"{word}:{definition}\n")

    def update_current_state(self):
        '''
        Updates current_state.txt

        :return: None
        '''

        noOfFlashcards = len(self.flashcard_context.sets_of_flashcards)
        day = self.day

        with open(f"{self.directory}/current_state.txt", 'w') as current_state_ptr:
            current_state_ptr.write(f"no_of_flashcards:{noOfFlashcards}\n")
            current_state_ptr.write(f"day:{day}")

    def close_flashcard_app(flashcardContext: FlashcardContext):

        noOfFlashcards = len(flashcardContext.sets_of_flashcards)
        day = flashcardContext.day + 1

        with open(f"{flashcardContext.directory}/current_state.txt", 'w') as current_state_ptr:
            current_state_ptr.write(f"no_of_flashcards:{noOfFlashcards}\n")
            current_state_ptr.write(f"day:{day}")

        exit()













