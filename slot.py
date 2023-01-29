import pygame
import os

class Slot(pygame.sprite.Sprite):
    filled = False
    tree = None
    xPos = -1
    yPos = -1

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Empty Slot.png")), (128, 128))
        self.filled = False
        self.xPos = x
        self.yPos = y

    def drawSlot(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos))


    def plantTree(self, tree):
        self.tree = tree
        self.tree.setPos(self.xPos, self.yPos)
        self.filled = True
        self.image.set_alpha(0) # Transparent

    def sellTree(self):
        print(f"Sold {self.tree.name} for ${self.tree.value}")
        self.image.set_alpha(255)
        
