from Storage import *


default_mode = "10_per_day"

def start():

    flashcardContext = FlashcardContext()

    if default_mode == "10_per_day":
        mode_10_per_day(flashcardContext)
        exit_flashcard_app(flashcardContext)

    while True:
        print("What command would you like to run?")
        cmd = input()
        if cmd == "help":
            print("list of available commands: put entry, remove entry, list entries")
        if cmd == "put entry":
            put_entry(flashcardContext)
        if cmd == "remove entry":
            pass
        if cmd == "list entries":
            list_entries(flashcardContext)
        if cmd == "exit":
            exit(0)

def put_entry(flashcardContext: FlashcardContext):

    sets_of_flashcards = flashcardContext.setsOfFlashcards

    word = input("Enter word: ")
    definition = input("Enter definition: ")

    if input(f"would you like to register following? {word} : {definition}\n") == "yes":

        setIdxOfSetToAddIn = check_if_entry_exists(flashcardContext, word)
        flashcard_set = sets_of_flashcards[setIdxOfSetToAddIn]

        if setIdxOfSetToAddIn != -1:
            flashcard_set[word] = definition
            write_set_to_store(flashcardContext, flashcard_set, setIdxOfSetToAddIn)

        else:
            if len(flashcard_set) == 10:
                sets_of_flashcards.append(dict())
                update_current_state(flashcardContext)

            sets_of_flashcards[-1][word] = definition
            append_entry_to_set(flashcardContext, len(sets_of_flashcards) - 1, word, definition)

    else:
        if input("would you like to reenter?: ") == "yes":
            put_entry()


def list_entries(flashcardContext: FlashcardContext):

    sets_of_flashcards = flashcardContext.setsOfFlashcards

    for flashcard_set in sets_of_flashcards:
        for word, definition in flashcard_set.items():
            print(f"{word} : {definition}")

def check_if_entry_exists(flashcardContext: FlashcardContext, word: str):

    sets_of_flashcards = flashcardContext.setsOfFlashcards

    for idx, flashcard_set in enumerate(sets_of_flashcards):
        if word in flashcard_set:
            return idx

    return -1


def review_set(flashcard_set):

    for word, definition in flashcard_set.items():
        print(f"{word}")
        input("Press enter for definition")
        print(f"{definition}\n")

    print("\nreviewed set\n")

### MODES ###


def mode_10_per_day(flashcardContext: FlashcardContext):
    '''
    Enter 10 cards per day and review all cards based on day.
    Counter refreshes every 5 days

    :return: None
    '''

    day = flashcardContext.day
    sets_of_flashcards = flashcardContext.setsOfFlashcards
    place = day % 5

    #check current_state.txt to see what day we are on
    print("Enter words for set")
    for _ in range(10):
        put_entry(flashcardContext)

    if place == 0:
        review_set(sets_of_flashcards[-1])
    elif place == 1:
        for i in range(-2, 0):
            review_set(sets_of_flashcards[i])
    elif place == 2:
        for i in range(-3, 0):
            review_set(sets_of_flashcards[i])
    elif place == 3:
        for i in range(-4, 0):
            review_set(sets_of_flashcards[i])
    elif place == 4:
        for i in range(-5, 0):
            review_set(sets_of_flashcards[i])

    print("completed today's session. See you tomorrow!\n")



