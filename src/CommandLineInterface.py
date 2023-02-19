from Storage import *


def start():

    initialize_flashcard_store()

    while True:
        print("What command would you like to run?")
        cmd = input()
        if cmd == "help":
            print("list of available commands: put entry, remove entry, list entries")
        if cmd == "put entry":
            put_entry()
        if cmd == "remove entry":
            pass
        if cmd == "list entries":
            list_entries()
        if cmd == "exit":
            exit(0)

def put_entry():
    word = input("Enter word: ")
    definition = input("Enter definition: ")

    if input(f"would you like to register following? {word} : {definition}\n") == "yes":

        setIdxOfSetToAddIn = check_if_entry_exists(word)
        flashcard_set = sets_of_flashcards[setIdxOfSetToAddIn]

        if setIdxOfSetToAddIn != -1:
            flashcard_set[word] = definition
            write_set_to_store(flashcard_set, setIdxOfSetToAddIn)

        else:
            if len(flashcard_set) == 10:
                sets_of_flashcards.append(dict())
                update_current_state()

            sets_of_flashcards[-1][word] = definition
            append_entry_to_set(len(sets_of_flashcards) - 1, word, definition)

    else:
        if input("would you like to reenter?: ") == "yes":
            put_entry()

def list_entries():
    for flashcard_set in sets_of_flashcards:
        for word, definition in flashcard_set.items():
            print(f"{word} : {definition}")

def check_if_entry_exists(word):

    for idx, flashcard_set in enumerate(sets_of_flashcards):

        if word in flashcard_set:
            return idx

    return -1


###############################

# mode 10 per day

def mode_10_per_day():
    '''

    :return: None
    '''

    while True:





