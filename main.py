from Storage import *
from CommandLineInterface import *

if __name__ == "__main__":
    storageapi = Storage()
    cli = CommandLineInterface(storageapi)
    cli.start()

