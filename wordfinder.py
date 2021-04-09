"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, file_path):
        """initialize new wordfinder with a filepath, empty list, and run read method on it"""
        self.file_path = file_path
        self.list = []
        self.read()

    def read(self):
        """read file from file_path, append each line of words to list excluding the new line symbol"""
        with open(self.file_path) as reader:
            for line in reader:
                self.list.append(line[:len(line)-2])
        print(f"{len(self.list)} words read")
        
    def random(self):
        """return a random word from list"""
        return self.list[random.randint(0, len(self.list)-1)]


class SpecialWordFinder(WordFinder):
    def __init__(self, file_path):
        """initialize new specialwordfinder with the wordfinder init method, but makes a special list and runs special read method on it"""
        super().__init__(file_path)
        self.special_list = []
        self.special_read()
    
    def special_read(self):
        """read file from file_path, append each line of words excluding the new line symbol but only with lines that aren't empty or start with #"""
        with open(self.file_path) as reader:
            for line in reader:
                if line[0] != "\n" and line[0] != "#":
                    self.special_list.append(line.replace("\n", ""))
        print(f"{len(self.list)} words read")