import pygame
import os
import math

pygame.init()


class Tree:
    value = -1
    name = "X"
    counter = -1
    text = ""
    xPos = -1
    yPos = -1
    
    DIRT = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Dirt Pile.png")), (128, 128))
    S1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Stage 1.png")), (128, 128))
    S2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Stage 2.png")), (128, 128))
    S3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Stage 3.png")), (128, 128))
    S4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Stage 4.png")), (128, 128))
    COMPLETE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Complete.png")), (128, 128))

    SPRITES = [DIRT, S1, S2, S3, S4, COMPLETE]

    def __init__(self, value, name):
        self.value = value
        self.name = name
        self.counter, self.text = 120, '120'.rjust(3)
        self.totalTime = self.counter
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font = pygame.font.SysFont('Consolas', 12)
        self.image = self.DIRT

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    def setPos(self, x, y):
        self.xPos = x
        self.yPos = y
    
    def updateImage(self):
        self.image = self.SPRITES[5 - (math.ceil((self.counter/self.totalTime) * 6) - 1)]

    def drawTree(self, screen):
        text = str(self.counter).rjust(
            3) if self.counter > 0 else 'Growth Complete!'
        screen.blit(self.font.render(text, True, (0, 0, 0)), (self.xPos, self.yPos + 25))
        screen.blit(self.image, (self.xPos, self.yPos))

    def updateCounter(self):
        self.counter -= 1

    def fertilize(self, amount):
        self.counter -= amount

