import pygame


class Button(object):

    def __init__(self, topleft, width, height, colors_cycle=0):
        self.rect = pygame.Rect(topleft, (width, height))
        self.colorCycle = colors_cycle
        self.currentColor = 0
        self.currentPressed = False

    def isButtonHover(self):
        mousePos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mousePos)

    def isButtonPressed(self):
        mousePos = pygame.mouse.get_pos()
        isPressed = pygame.mouse.get_pressed()[0]
        if not isPressed:
            self.currentPressed = False
            return False
        if not self.currentPressed and self.rect.collidepoint(mousePos):
            self.currentPressed = True
            return isPressed  # return true if collide isPressed and not currentPressed
        return False


class SquareButtons(object):

    def __init__(self):
        self.start = (50, 50)
        self.end = (650, 150)
        self.squareSize = self.end[1] - self.start[1]
        self.squareSpacing = (
            self.end[0] - self.start[0] - (self.squareSize*5)) / 4.0
        self.buttons = self.initButtons()

    def initButtons(self):
        squareButtons = []
        leftTop = [self.start[0], self.start[1]]
        for i in range(5):
            button = Button(leftTop, self.squareSize,
                            self.squareSize)
            squareButtons.append(button)
            leftTop[0] = leftTop[0] + self.squareSize + self.squareSpacing
        return squareButtons

    def getPressed(self):
        pressed = []
        for button in self.buttons:
            pressed.append(button.isButtonPressed())
        return pressed

    def update(self):
        for button in self.buttons:
            button.update()
