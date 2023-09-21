from FlashcardApi import *


'''
File lists functions that interact with command line and any helper functions associated with those functions  
'''

def start():

    flashcards = FlashcardApi(FlashcardContext())

    default_mode = "10_per_day"

    #Todo: how do we set modes
    if default_mode == "10_per_day":
        mode_10_per_day()

    #Todo: Replace below with argparse
    while True:
        print("What command would you like to run?")
        cmd = input()
        if cmd == "help":
            print("list of available commands: put entry, remove entry, list entries")
        if cmd == "put entry":
            word = input("enter word: ")
            definition = input("enter definition: ")
            flashcards.put_entry(word, definition)
        if cmd == "remove entry":
            word = input("enter word: ")
            flashcards.delete_entry(word)
        if cmd == "list entries":
            flashcards.list_entries()
        if cmd == "exit":
            flashcards.close_flashcard_app()
            exit(0)

def get_entry_from_input_stream(flashcards: FlashcardApi):
    '''
    gets ent

    :param flashcardContext: flashcard config values
    :return: 0 on update, 1 on add, and -1 if failed to add or update
    '''

    word = input("Enter word: ")
    definition = input("Enter definition: ")

    if input(f"would you like to register following? {word} : {definition}\n") == "yes":
        return flashcards.put_entry(word, definition)

    else:
        if input("would you like to reenter?: ") == "yes":
            get_entry_from_input_stream(flashcards)

    return "success"


def review_set(flashcard_set):

    for word, definition in flashcard_set.items():
        print(f"{word}")
        input("Press enter for definition")
        print(f"{definition}\n")

    print("\nreviewed set\n")


### MODES ###


def mode_10_per_day(flashcards: FlashcardApi):
    '''
    Enter 10 cards per day and review all cards based on day.
    Counter refreshes every 5 days

    :return: None
    '''

    day = flashcards.flashcard_context.day
    sets_of_flashcards = flashcards.flashcard_context.sets_of_flashcards
    place = day % 5

    # check current_state.txt to see what day we are on
    print("Enter words for set")
    new_entry_ctr = 0
    while new_entry_ctr < 10:
        #must be 10 new entries
        if get_entry_from_input_stream(flashcards) == 1:
            new_entry_ctr += 1

    print(flashcards.flashcard_context.sets_of_flashcards)

    try:
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
    except IndexError:
        # Ignore idx error
        pass

    print("completed today's session. See you tomorrow!\n")


def quiz(flashcardContext, noOfProblems):

    for _ in range(noOfProblems/5):
        setsOfFlashcards = flashcardContext.sets_of_flashcards
        flashcardSet = setsOfFlashcards[random.randint(0, len(setsOfFlashcards) - 1)]

        for _ in range(noOfProblems/5):
            flashcard = random.choice(list(flashcardSet))
            input(f"what is the definition of: {flashcard}. Press Enter for answer")
            print(flashcardSet[flashcard])

