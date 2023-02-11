import os
from Storage import *

class CommandLineInterface:
    '''
    Manages I/O with command line
    '''

    def __init__(self, store):
        self.flashcards = {}
        self.storage = store

    def start(self):
        while True:
            print("What command would you like to run?")
            cmd = input()
            if cmd == "help":
                print("list of available commands: put entry, remove entry, list entries")
            if cmd == "put entry":
                self.put_entry()
            if cmd == "remove entry":
                pass
            if cmd == "list entries":
                pass

    def put_entry(self):
        word = input("Enter word: ")
        definition = input("Enter definition: ")
        if input(f"would you like to register following? {word} : {definition} ") == "yes":
            self.flashcards[word] = definition
        else:
            if input("would you like to reenter?") == "yes":
                self.put_entry()


    def list_entries(self):
        print(self.flashcards)



