import os

directory = ".Flashcards"
sets_of_flashcards = [dict()]

def initialize_flashcard_store():
    '''
    Read current_state.txt for latest flashcard file ... Wait do I need this?
    :return: IDK
    '''

    if not os.path.isdir(directory):
        os.mkdir(directory)

    if not os.path.isfile(f"{directory}/current_state.txt"):
        open(f"{directory}/current_state.txt", "x")

    # set current state if nothing exists in current state
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
        with open(fr"{directory}/flashcardset_{i}", 'r') as flashcard_ptr:
            flashcard_set = flashcard_ptr.readlines()
            fl = {}
            for flashcard in flashcard_set:
                a, b = flashcard.split(':')
                fl[a] = b.strip()
            sets_of_flashcards.append(fl)


def write_set_to_store(flashcard_set: dict, flashcard_idx: int):
    with open(fr"{directory}/flashcardset_{flashcard_idx}", 'w') as set_ptr:
        for word, definition in flashcard_set.items():
            set_ptr.write(f"{word}:{definition}\n")












