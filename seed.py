import pygame
import os

class Seed:
    xPos = -1
    yPos = -1

    def __init__(self, name, growthTime, cost, value, image):
        self.name = name
        self.growthTime = growthTime
        self.cost = cost
        self.value = value
        self.image = image
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont("bahnschrift", 18)
        self.clicked = False

    def setPos(self, x, y):
        self.xPos = x
        self.yPos = y
        self.rect.topleft = (x - 50,y - 20)
        self.rect.width = self.rect.width * 2
        self.rect.height = self.rect.height * 2

    def draw(self, surface):
        text = self.font.render(f"${self.cost}", True, (0,0,0))
        surface.blit(self.image, (self.xPos, self.yPos))
        surface.blit(text, (self.xPos - 15, self.yPos + 75))

        action = False

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action


        '''
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.MOUSEBUTTONDOWN and dragging == False:
                dragging = True
                mouse_x, mouse_y = pos
                offset_x = self.rect.x - mouse_x
                offset_y = self.rect.y - mouse_y

        elif pygame.MOUSEBUTTONUP:
            dragging = False

        elif pygame.MOUSEMOTION:
            if dragging:
                mouse_x, mouse_y = pygame.mouse.getpos
                self.rect.x = mouse_x + offset_x
                self.rect.y = mouse_y + offset_y
        '''

    