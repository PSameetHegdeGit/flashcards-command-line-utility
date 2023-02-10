import os


def init_storage():
    path = ".Flashcards"
    if not os.path.isdir(path):
        os.mkdir(path)

    global flashcardStore
    flashcardStore = open(r".Flashcards/flashcard_main.txt", "w+")


def put_entry(store):
    word = input("Enter word: ")
    definition = input("Enter definition: ")
    print(f"would you like to register following? {word} : {definition}")
    toregister = input()
    if toregister == "yes":
        # register into dictionary and into file
        pass
    else:
        # ask if you would like to do something else
        pass





