import pygame

class Tree:
    value = -1
    name = "X"

    def __init__(self, value, name):
        self.value = value
        self.name = name

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    timer = pygame.time.Clock()