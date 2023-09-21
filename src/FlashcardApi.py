from src.FlashcardContexts.FlashcardContext import *
from src.FlashcardCsv.FlashcardCsvManager import *

class FlashcardApi:
    # Todo: determine better way to pass status codes

    def __init__(self, flashcardContext):
        self.flashcard_context = flashcardContext
        self.flashcard_csv_manager = FlashcardCsvManager()

    def put_entry(self, word: str, definition: str):
        '''
        Add or update entry in FlashcardContext.sets_of_flashcards

        :return: None
        '''

        setsOfFlashcards = self.flashcard_context.sets_of_flashcards
        idxOfSetToAddIn = self.find_set_idx_of_entry(word)
        flashcardSet = setsOfFlashcards[idxOfSetToAddIn]

        if idxOfSetToAddIn != -1:
            flashcardSet[word] = definition
            return self.flashcard_context.write_set_to_store(flashcardSet, idxOfSetToAddIn)

        else:
            if len(flashcardSet) == 10:
                setsOfFlashcards.append(dict())
                self.flashcard_context.update_current_state()

            setsOfFlashcards[-1][word] = definition
            self.flashcard_context.append_entry_to_set(len(setsOfFlashcards) - 1, word, definition)
            return 1

    def delete_entry(self, word: str):
        NotImplementedError

    def list_entries(self):

        sets_of_flashcards = self.flashcard_context.sets_of_flashcards

        for flashcard_set in sets_of_flashcards:
            for word, definition in flashcard_set.items():
                print(f"{word} : {definition}")

    def find_set_idx_of_entry(self, word: str):
        '''
        Finds the idx of set in FlashcardContext.sets_of_flashcards that word exists in

        :return: set idx if word exists; -1 if does not exist
        '''

        sets_of_flashcards = self.flashcard_context.sets_of_flashcards

        for idx, flashcard_set in enumerate(sets_of_flashcards):
            if word in flashcard_set:
                return idx

        return -1

    def close_flashcard_app(flashcardContext: FlashcardContext):

        noOfFlashcards = len(flashcardContext.sets_of_flashcards)
        day = flashcardContext.day + 1

        with open(f"{flashcardContext.directory}/current_state.txt", 'w') as current_state_ptr:
            current_state_ptr.write(f"no_of_flashcards:{noOfFlashcards}\n")
            current_state_ptr.write(f"day:{day}")

        exit()













