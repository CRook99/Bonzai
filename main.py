import pygame
import os
from tree import *
from slot import *
from pygame import mixer


pygame.init()

mixer.init()
mixer.music.load('Assets/onion_song.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()


WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Bonzai")

SAND_COLOR = pygame.Color("#C2B280")
DARK_SAND_COLOR = pygame.Color("#85671C")

BEEPUS = pygame.image.load(os.path.join("Assets", "beepus.png"))
EXIT_ICON = pygame.image.load(os.path.join("Assets", "Exit Icon.png"))



FRAMERATE = 60

 
'''
class Button:
    def __init__(self, x, y, width, height, label):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.clicked = False

    def draw(self, WIN, font, color=(255, 255, 255)):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)
        text = font.render(self.label, True, color)
        surface.blit(text, (self.x + self.width // 2 - text.get_width() // 2, self.y + self.height // 2 - text.get_height() // 2))

    def is_clicked(self, pos):
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            self.clicked = True
'''

TREES = []


        

def drawWindow():
    WIN.fill(SAND_COLOR)
    WIN.blit(BEEPUS, (400,400))
    WIN.blit(EXIT_ICON, (WIDTH - 50, 20))
    for tree in TREES:
        tree.drawTree(WIN)
    pygame.display.update()

def main():
    tree1 = Tree(5, "Bonsai")
    TREES.append(tree1)

    pygame.time.set_timer(pygame.USEREVENT, 1000)


    run = True
    while run:
        pygame.time.Clock().tick(FRAMERATE)

        tree1.drawTree(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False # May use later
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


            elif event.type == pygame.USEREVENT:
                print("UE")
                for tree in TREES:
                    tree.updateCounter()


        drawWindow()

    pygame.quit()


if __name__ == "__main__":
    main()

