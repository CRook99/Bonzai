import pygame
import os
import math
from main import Button, sellFont

pygame.init()


class Tree:
    value = -1
    name = "X"
    counter = -1
    text = ""
    xPos = -1
    yPos = -1
    growthTime = -1
    
    # Sprites
    DIRT = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Dirt Pile.png")), (128, 128))
    S1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Stage 1.png")), (128, 128))
    S2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Stage 2.png")), (128, 128))
    S3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Stage 3.png")), (128, 128))
    S4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Stage 4.png")), (128, 128))
    COMPLETE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Complete.png")), (128, 128))
    SPRITES = [DIRT, S1, S2, S3, S4, COMPLETE]

    # Graphics
    button = None
    sold = False
    font = pygame.font.SysFont("bahnschrift", 20)

    def __init__(self, value, name, growthTime):
        self.value = value
        self.name = name
        self.counter = growthTime - 1
        self.growthTime = growthTime
        self.text = str(self.counter - 1).rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.image = self.DIRT

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    def setPos(self, x, y):
        self.xPos = x
        self.yPos = y
    
    def updateImage(self):
        x = self.growthTime // 6
        THENUMBER = self.growthTime - self.counter
        
        list_a = [range(0, x), range(x, 2*x), range(2*x, 3*x), range(3*x, 4*x), range(4*x, 5*x), range(5*x, self.growthTime)]

        for i in range(6):
            if THENUMBER in list_a[i]:
                self.image = self.SPRITES[i]

        
    def drawTree(self, screen):
        text = str(self.counter).rjust(
            3) if self.counter > 0 else 'Growth Complete!'
        screen.blit(self.font.render(text, True, (0, 0, 0)), (self.xPos - 10, self.yPos - 10))
        screen.blit(self.image, (self.xPos, self.yPos))

    def updateCounter(self):
        if self.counter > 0:
            self.counter -= 1

    def fertilize(self, amount):
        self.counter -= amount

    def getCounter(self):
        return self.counter

    def createSellButton(self):
        self.button = Button(self.xPos + 20, self.yPos + 110, 100, 60, 'Sell!', sellFont, (255, 255, 255))
        sold = True