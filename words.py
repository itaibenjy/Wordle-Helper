import copy


class Word(object):
    def __init__(self):
        self.letters = ["" for i in range(5)]
        self.curLetter = 0

    def writeLetter(self, letter):
        if self.curLetter == 5:
            return
        self.letters[self.curLetter] = letter.upper()
        self.curLetter += 1

    def backspaceLetter(self):
        if self.curLetter != 0:
            self.curLetter -= 1
        self.letters[self.curLetter] = ""

    def newLine(self):
        self.letters = ["" for i in range(5)]
        self.curLetter = 0


class Words(object):
    def __init__(self):
        self.words = self.getWords()
        self.currentWords = copy.deepcopy(self.words)

    def getWords(self):
        words = []
        with open("words5.txt") as file:
            data = file.readlines()
            words = data

        for word in words:
            word = word.replace("\n", "")

        return words

    def sort(self, word, colors):
        for i in range(5):
            if colors[i] == 1:
                self.letterNotIn(word[i].lower())
            elif colors[i] == 2:
                self.letterInNotRight(word[i].lower(), i)
            else:
                self.letterInRight(word[i].lower(), i)

    def letterNotIn(self, letter):
        words = copy.deepcopy(self.currentWords)
        self.currentWords = []
        for word in words:
            if letter not in word:
                self.currentWords.append(word)

    def letterInNotRight(self, letter, index):
        words = copy.deepcopy(self.currentWords)
        self.currentWords = []
        for word in words:
            if letter in word:
                if word[index] != letter:
                    self.currentWords.append(word)

    def letterInRight(self, letter, index):
        words = copy.deepcopy(self.currentWords)
        self.currentWords = []
        for word in words:
            if word[index] == letter:
                self.currentWords.append(word)

    def reset(self):
        self.currentWords = copy.deepcopy(self.words)
