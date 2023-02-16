from src.CommandLineInterface import *



if __name__ == "__main__":
    storageapi = Storage()
    cli = CommandLineInterface(storageapi)
    cli.start()














'''
TODO

(1) Flashcard set as Class
(2) Storage API needs more transactional I/O operations
    - Access all flashcards in flashcard_main.txt
    - Extend fxnality to be able to access flashcards across all flash_card_XX.txt files
    - 
(3)  


'''