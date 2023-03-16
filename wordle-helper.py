
import pygame
import sys
from graphics import Graphics
from buttons import SquareButtons
from words import Word, Words
import math


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((700, 200))
pygame.display.set_caption("Wordle Helper")

graphics = Graphics()
squareButtons = SquareButtons()
word = Word()
words = Words()

displayWords = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                word.backspaceLetter()
            elif event.key == pygame.K_ESCAPE:
                words.reset()
                word.newLine()
                graphics.newLine()
                displayWords = False
                screen = pygame.display.set_mode((700, 200))
            elif event.key == pygame.K_RETURN:
                words.sort(word.letters, graphics.squareColors)
                graphics.newLine()
                word.newLine()
                displayWords = True
                height = math.ceil(len(words.currentWords) / 3)*22 + 250
                screen = pygame.display.set_mode((700, height))
            elif event.unicode.isalpha():
                word.writeLetter(event.unicode)

    screen.fill((18, 18, 18))
    graphics.drawSquares(screen, squareButtons.buttons,
                         squareButtons.getPressed())
    graphics.drawLetters(screen, word.letters, squareButtons.buttons)

    if displayWords:
        graphics.displayWords(screen, words.currentWords)

    pygame.display.update()
    clock.tick(30)
