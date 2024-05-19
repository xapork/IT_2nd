import random


class Crossword:
    def __init__(self, width, height, word_list):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.word_list = word_list

    def display(self):
        for row in self.grid:
            print(' '.join(row))

    def can_place_word_horizontally(self, word, row, col):
        if col + len(word) > self.width:
            return False
        if col > 0 and self.grid[row][col - 1] != ' ':
            return False
        if col + len(word) < self.width and self.grid[row][col + len(word)] != ' ':
            return False
        for i in range(len(word)):
            if self.grid[row][col + i] not in (' ', word[i]):
                return False
        return True

    def can_place_word_vertically(self, word, row, col):
        if row + len(word) > self.height:
            return False
        if row > 0 and self.grid[row - 1][col] != ' ':
            return False
        if row + len(word) < self.height and self.grid[row + len(word)][col] != ' ':
            return False
        for i in range(len(word)):
            if self.grid[row + i][col] not in (' ', word[i]):
                return False
        return True

    def place_word_horizontally(self, word, row, col):
        for i in range(len(word)):
            self.grid[row][col + i] = word[i]

    def place_word_vertically(self, word, row, col):
        for i in range(len(word)):
            self.grid[row + i][col] = word[i]

    def generate(self):
        for word in self.word_list:
            placed = False
            attempts = 0
            while not placed and attempts < 100:
                row = random.randint(0, self.height - 1)
                col = random.randint(0, self.width - 1)
                if random.choice([True, False]):
                    if self.can_place_word_horizontally(word, row, col):
                        self.place_word_horizontally(word, row, col)
                        placed = True
                else:
                    if self.can_place_word_vertically(word, row, col):
                        self.place_word_vertically(word, row, col)
                        placed = True
                attempts += 1

        self.fill_empty_spaces()

    def fill_empty_spaces(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == ' ':
                    self.grid[row][col] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


word_list = ['PYTHON', 'JAVA', 'HTML', 'CSS', 'JAVASCRIPT', 'CPLUSPLUS']
crossword = Crossword(15, 15, word_list)
crossword.generate()
crossword.display()
