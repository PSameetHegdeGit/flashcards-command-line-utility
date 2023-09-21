
#Todo: Should I take out non disk-write fxns or keep them in; ie keep everything under flashcard context
class FlashcardContext():
    class Flashcards:
        def __init__(self, path_to_flashcards, no_of_flashcards, review_cycle):
            self.path_to_flashcards = path_to_flashcards
            self.no_of_flashcards = no_of_flashcards
            self.review_cycle = review_cycle
    class DumpFile:
        def __init__(self, path_to_dump, line_pointer):
            self.path_to_dump = path_to_dump
            self.line_pointer = line_pointer
    def __init__(self, dump_file: DumpFile, flashcards: Flashcards):
        self.dump_file = dump_file
        self.flashcards = flashcards



def generate_metadata_folder(self, directory):
    '''
    Generates a metadata folder in specified path

    :param directory: path to directory
    '''

    metadata = {
        "dump_file": {
            "path_to_dump": f"{directory}/dump_file.txt",
            "line_pointer": 0
        },
        "flashcards": {
            "path_to_flashcards": f"{directory}/.FlashcardContexts/",
            "no_of_flashcards": 0,
            "review_cycle": 5,
        }
    }

    with open(f"{directory}/metadata.json", "x") as metadata_ptr:
        json.dump(metadata, metadata_ptr)

def get_flashcard_context_from_source(directory: str):
