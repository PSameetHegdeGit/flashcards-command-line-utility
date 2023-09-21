class Metadata:
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