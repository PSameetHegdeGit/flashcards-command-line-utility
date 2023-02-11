import os

class Storage:

    def __init__(self):

        path = ".Flashcards"

        # set current state
        self.currentState = open(fr"{path}/current_state.txt")
        print(self.currentState.read())

        # set flash card store
        if not os.path.isdir(path):
            os.mkdir(path)

        self.flashcardStore = open(fr"{path}/flashcard_main.txt", "w+")



    #TODO: Refactor this
    def write(self, entry):
        self.flashcardStore.write(entry)

    #TODO: Refactor this... pretty useless
    def close(self):
        self.flashcardStore.close()







