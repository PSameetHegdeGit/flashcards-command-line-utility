import os

class Storage:

    def __init__(self):

        path = ".Flashcards"

        # set current state
        with open(fr"{path}/current_state.txt", "r+") as currentState:
            if os.path.getsize(f"{path}/current_state.txt") == 0:
                # indicates fresh flashcard store
                currentState.write("current_file:None\n")

        with open(fr"{path}/current_state.txt", "r") as currentState:
            currentFile = currentState.read().split(':')
            self.currentFile = {currentFile[0]:currentFile[1].strip()}

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








