import unittest
from FlashcardApi import *
import csv
import os
import glob

class TestFetchApi(unittest.TestCase):


    def create_csv_test_file(self, filepath):
        '''
        Creates a testing file in CSV to test fetchApi

        :param filepath: relative path from src to csv file
        :return: csvfie of type typing.IO
        '''

        data = [
            ["word", "definition"],
            ["happy", "feeling or showing pleasure"],
            ["sad", "feeling or showing sorrow"],
            ["excited","very enthusiastic and eager"]
        ]

        csv_file_path = filepath

        with open(csv_file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def delete_all_csv_files_in_dir(self, directory):
        csv_pattern = os.path.join(directory, "*.csv")
        csv_files = glob.glob(csv_pattern)

        for csv_file in csv_files:
            try:
                os.remove(csv_file)
                print(f"removed: {csv_file}")
            except Exception as e:
                print(f"Error removing {csv_file}: {e}")

    def setUp(self):
        csv_file_path = "test.csv"

        self.create_csv_test_file(csv_file_path)
        self.csvfile = open(csv_file_path)


    def tearDown(self) -> None:
        self.csvfile.close()
        #using relative path
        self.delete_all_csv_files_in_dir("")

    def test_integration_create_entries_from_csv_file(self):

        expected = {'word': 'definition',
                    'happy': 'feeling or showing pleasure',
                    'sad': 'feeling or showing sorrow',
                    'excited': 'very enthusiastic and eager'}

        actual = get_entries_from_csv_file(self.csvfile)

        self.assertEqual(expected, actual)


