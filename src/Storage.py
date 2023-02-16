import os


directory = ".Flashcards"
flashcards = []

def initialize_flashcard_store():
    '''
    Read current_state.txt for latest flashcard file ... Wait do I need this?
    :return: IDK
    '''


    if not os.path.isdir(directory):
        os.mkdir(directory)

    # set current state
    with open(fr"{directory}/current_state.txt", "r+") as currentState:
        if os.path.getsize(f"{directory}/current_state.txt") == 0:
            # indicates fresh flashcard db
            currentState.write("no_of_flashcards:0\n")

    with open(fr"{directory}/current_state.txt", "r") as currentState:
        currentFile = currentState.read().split(':')
        currentFile = {currentFile[0]: currentFile[1].strip()}

    populate_flashcards(currentFile["no_of_flashcards"])


def populate_flashcards(no_of_flashcards):

    for i in no_of_flashcards:

        with open(fr"{directory}/flashcardset_{}")
    flashcards = self.flashcardStore.readlines()
    fl = {}
    for item in flashcards:
        a, b = item.split(':')
        fl[a] = b.strip()

    return fl












