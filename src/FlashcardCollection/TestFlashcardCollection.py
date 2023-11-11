import unittest
from FlashcardCollection import *

class TestFlashcardContext(unittest.TestCase):

    def setUp(self):

        self.metadata = {
            "dump_file" : {
                "path_to_dump" : "n/a",
                "line_pointer" : 0
            },
            "flashcards" : {
                "path_to_flashcards": "n/a",
                "no_of_flashcards": 10,
                "review_cycle": 5,
            }
        }

        new = FlashcardCollection()






