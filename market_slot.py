import pygame
import os

class MarketSlot(pygame.sprite.Sprite):
    seed = None
    xPos = -1
    yPos = -1

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Empty Market Slot.png")), (96, 96))
        self.xPos = x
        self.yPos = y

    def giveSeed(self, seed):
        self.seed = seed
        self.seed.setPos(self.xPos, self.yPos)

    def drawSlot(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos))