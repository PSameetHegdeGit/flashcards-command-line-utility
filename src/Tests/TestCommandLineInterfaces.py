import unittest
from unittest.mock import Mock, patch
from src.CommandLineInterface import *
from src.FlashcardContext import *

class TestCommandLineInterfaces(unittest.TestCase):


    #Mock FlashcardContext
    def setUp(self):
        self.mock_flashcard_context = patch('Storage.FlashcardContext').start()
        self.flashcard_context = self.mock_flashcard_context.return_value

        self.flashcard_context.no_of_flashcards = 1
        self.flashcard_context.sets_of_flashcards = [{'word1': 'definition1'}]

    def tearDown(self) -> None:
        self.mock_flashcard_context.stop()

    @patch('CommandLineInterface.find_set_idx_of_entry')
    @patch('Storage.write_set_to_store')
    @patch('CommandLineInterface.update_current_state')
    @patch('CommandLineInterface.append_entry_to_set')
    def test_put_entry_add_entry(self, mock_append_entry, mock_update_state, mock_write_store, mock_find_idx):
        mock_find_idx.return_value = 0
        mock_write_store.return_value = "ADDED ENTRY"
        mock_update_state.return_value = "UPDATED STATE"
        mock_append_entry.return_value = "APPENDED ENTRY"

        result = put_entry(self.mock_flashcard_context, 'word', 'definition')

        self.assertEqual(result, "ADDED ENTRY")


