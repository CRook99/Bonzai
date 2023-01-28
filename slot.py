import pygame
import os

class Slot(pygame.sprite.Sprite):
    filled = False
    tree = None
    #DEFAULT_IMAGE = pygame.image.load(os.path.join("Assets", "Empty Slot.png"))

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("Assets", "Empty Slot.png"))
        self.filled = False

    def drawSlot(self, screen):
        screen.blit(self.image, self.rect)


    def plantTree(self, tree):
        self.tree = tree
        self.filled = True

    def sellTree(self):
        print(f"Sold {self.tree.name} for ${self.tree.value}")
