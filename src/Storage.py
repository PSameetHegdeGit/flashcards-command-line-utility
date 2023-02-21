import os

directory = ".Flashcards"
sets_of_flashcards = []
current_state = []

def initialize_flashcard_store():
    '''
    Read current_state.txt for no_of_flashcards and counter
    :return: IDK
    '''

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
        c = map(lambda x: x.split(':'),  currentStatePtr.readlines())
        c = map(lambda x: {x[0]: x[1].strip()}, c)

    current_state.extend(list(c))
    populate_flashcards(int(current_state[0]["no_of_flashcards"]))

def populate_flashcards(no_of_flashcards: int):
    '''
    reads all flashcard files from .Flashcards and initializes sets_of_flashcards (represented as an array of
    dictionaries) to those flashcards

    :param no_of_flashcards:
    :return: None
    '''
    if no_of_flashcards == 0:
        sets_of_flashcards.append(dict())
    else:
        for i in range(no_of_flashcards):

            if not os.path.isfile(f"{directory}/flashcardset_{i}"):
                open(f"{directory}/flashcardset_{i}", "x")

            with open(fr"{directory}/flashcardset_{i}", 'r') as flashcard_ptr:
                flashcard_set = flashcard_ptr.readlines()
                fl = {}
                for flashcard in flashcard_set:
                    a, b = flashcard.split(':')
                    fl[a] = b.strip()
                sets_of_flashcards.append(fl)


def write_set_to_store(flashcard_set: dict, flashcard_idx: int):
    '''
    writes a flashcard set to its corresponding txt file under .Flashcards.
    Flashcard sets are ordered by when created. Will always be in that order

    :param flashcard_set: key value pairing corresponding to txt file
    :param flashcard_idx: IDK
    :return: None
    '''

    with open(fr"{directory}/flashcardset_{flashcard_idx}", 'w') as set_ptr:
        for word, definition in flashcard_set.items():
            set_ptr.write(f"{word}:{definition}\n")


def append_entry_to_set(flashcard_idx: int, word: str, definition: str):
    '''
    append entry to the file corresponding to a flashcard set

    :param flashcard_idx: set position
    :param word
    :param definition
    :return: None
    '''

    with open(fr"{directory}/flashcardset_{flashcard_idx}", 'a') as set_ptr:
        set_ptr.write(f"{word}:{definition}\n")



def update_current_state():
    '''
    Set number of flashcards in current_state.txt

    :return: None
    '''
    current_state[0]['no_of_flashcards'] = len(sets_of_flashcards)

    fl = current_state[0]
    d = current_state[1]

    print(fl + " " + d)
    with open(f"{directory}/current_state.txt", 'w') as current_state_ptr:
        current_state_ptr.write(f"no_of_flashcards:{fl['no_of_flashcards']}")
        current_state_ptr.write(f"day:{d['day']}")



def exit_flashcard_app():
    current_state[0]['no_of_flashcards'] = len(sets_of_flashcards)

    fl = current_state[0]
    d = current_state[1]

    with open(f"{directory}/current_state.txt", 'w') as current_state_ptr:
        current_state_ptr.write(f"no_of_flashcards:{fl['no_of_flashcards']}")
        current_state_ptr.write(f"day:{d['day']}")


