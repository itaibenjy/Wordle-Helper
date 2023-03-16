import pygame


class Graphics(object):

    def __init__(self):
        self.colors = [(255, 255, 255), (58, 58, 60),
                       (181, 159, 58), (82, 141, 77)]
        self.squareColors = [1 for i in range(5)]
        self.squareCycle = (1, 3)
        self.lettersFont = pygame.font.Font(
            'RobotoMono-VariableFont_wght.ttf', 80)
        self.wordsFont = pygame.font.Font(
            'RobotoMono-VariableFont_wght.ttf', 20)

    def drawSquares(self, screen, squareButtons, pressedSquares):
        self.updateSquareColors(pressedSquares)
        for i, button in enumerate(squareButtons):
            pygame.draw.rect(
                screen, self.colors[self.squareColors[i]], button.rect)
            # pygame.draw.rect(
            #    screen, self.colors[0], button.rect, width=4, border_radius=4)

    def updateSquareColors(self, pressedSquares):
        for i in range(5):
            if pressedSquares[i]:
                if self.squareColors[i] == self.squareCycle[1]:
                    self.squareColors[i] = self.squareCycle[0]
                else:
                    self.squareColors[i] += 1

    def drawLetters(self, screen, word, squareButtons):
        for i in range(5):
            topleft = squareButtons[i].rect.topleft
            cords = (topleft[0] + squareButtons[i].rect.width/4, topleft[1]-5)
            letter_render = self.lettersFont.render(
                word[i], True, self.colors[0])
            screen.blit(letter_render, cords)

    def newLine(self):
        self.squareColors = [1 for i in range(5)]

    def displayWords(self, screen, words):
        columnLength = len(words) // 3
        if len(words) % 3 != 0:
            columnLength += 1

        columnWidth = screen.get_width()/3 - 40

        currentColumn = 0
        currentRow = 0
        for word in words:
            word_render = self.wordsFont.render(word, True, self.colors[0])
            screen.blit(word_render, (columnWidth *
                                      currentColumn + 20 + columnWidth//2, currentRow*20 + 200))
            currentRow += 1
            if currentRow >= columnLength:
                currentColumn += 1
                currentRow = 0
