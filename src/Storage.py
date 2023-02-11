import os

class Storage:

    flashcards = None

    def __init__(self):
        self.flashcards = self.init_storage()

    def init_storage(self):
        path = "../.Flashcards"
        if not os.path.isdir(path):
            os.mkdir(path)

        return open(r"../.Flashcards/flashcard_main.txt", "w+")







