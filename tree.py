import pygame

pygame.init()


class Tree:
    value = -1
    name = "X"
    counter = -1
    text = ""
    xPos = -1
    yPos = -1

    def __init__(self, value, name):
        self.value = value
        self.name = name
        self.xPos = 0
        self.yPos = 0
        self.counter, self.text = 120, '120'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font = pygame.font.SysFont('Consolas', 12)

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    def setPos(self, x, y):
        self.xPos = x
        self.yPos = y

    

    def drawTree(self, screen):
        text = str(self.counter).rjust(
            3) if self.counter > 0 else 'Growth Complete!'
        screen.blit(self.font.render(text, True, (0, 0, 0)), (32, 48))

    def updateCounter(self):
        self.counter -= 1
        
    def fertilize(self, amount):
        self.counter -= amount
    
