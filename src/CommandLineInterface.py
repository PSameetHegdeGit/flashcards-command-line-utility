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
        flashcard_set = sets_of_flashcards[-1]
        if len(flashcard_set) == 10:
            sets_of_flashcards.append(dict())
        sets_of_flashcards[-1][word] = [definition]
        write_set_to_store(sets_of_flashcards[-1], len(sets_of_flashcards) - 1)
    else:
        if input("would you like to reenter?: ") == "yes":
            put_entry()

def list_entries():
    print(sets_of_flashcards)







