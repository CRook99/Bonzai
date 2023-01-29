import pygame
from main import Button

pygame.init()


class Tree:
    value = -1
    name = "X"
    counter = -1
    text = ""
    button = None
    sold = False

    def __init__(self, value, name):
        self.value = value
        self.name = name
        self.counter, self.text = 120, '120'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font = pygame.font.SysFont('Consolas', 12)

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    def drawTree(self, screen):
        text = str(self.counter).rjust(
            3) if self.counter > 0 else 'Growth Complete!'
        screen.blit(self.font.render(text, True, (0, 0, 0)), (32, 48))

    def updateCounter(self):
        if self.counter > 0:
            self.counter -= 1

    def fertilize(self, amount):
        self.counter -= amount

    def getCounter(self):
        return self.counter

    def createSellButton(self):
        self.button = Button(100, 100, 50, 50, 'Sell!')
        sold = True

    '''
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT:
                # do stuff
                print("pass")
            elif e.type == pygame.QUIT:
                run = False
    pygame.display.flip()
    timer.tick(60)
    '''
