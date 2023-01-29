import pygame
import os
from tree import *
from slot import *
from market_slot import *
from pygame import mixer


pygame.init()

mixer.init()
mixer.music.load('Assets/onion_song.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()


WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Bonzai")

SAND_COLOR = pygame.Color("#C2B280")
DARK_SAND_COLOR = pygame.Color("#85671C")

BEEPUS = pygame.image.load(os.path.join("Assets", "beepus.png"))
EXIT_ICON = pygame.image.load(os.path.join("Assets", "Exit Icon.png"))

font = pygame.font.Font(None, 36)

FRAMERATE = 60

BUTTONS = []

MONEY = 0


class Button:
    def __init__(self, x, y, width, height, label):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.clicked = False
        BUTTONS.append(self)

    def draw(self, surface, font, color=(255, 255, 255)):
        pygame.draw.rect(surface, (255, 255, 255),
                         (self.x, self.y, self.width, self.height), 2)
        text = font.render(self.label, True, color)
        WIN.blit(text, (self.x + self.width // 2 - text.get_width() //
                 2, self.y + self.height // 2 - text.get_height() // 2))

    def is_clicked(self, pos):
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            self.clicked = True


TREES = []
SLOT_GRID = [[], [], []]

SLOT_COORDS = [[(100, 100), (300, 100), (500, 100)],
               [(100, 300), (300, 300), (500, 300)],
               [(100, 500), (300, 500), (500, 500)]]


SEEDS = []
MARKET_GRID = [[], []]

MARKET_COORDS = [[(900, 100), (1000, 100), (1100, 100)],
                 [(900, 200), (1000, 200), (1100, 200)]]


def drawWindow():
    WIN.fill(SAND_COLOR)
    WIN.blit(BEEPUS, (400, 400))
    WIN.blit(EXIT_ICON, (WIDTH - 50, 20))

    for tree in TREES:
        #tree.updateImage()
        #tree.drawTree(WIN)
        if not tree.button == None:
            (tree.button).draw(WIN, font)

    for button in BUTTONS:
        button.draw(WIN, font)

    moneyText = font.render(str(MONEY), True, (0, 0, 0))
    WIN.blit(moneyText, (400, 400))

    for row in SLOT_GRID:
        for slot in row:
            slot.drawSlot(WIN)
            if slot.tree != None:
                if slot.tree.sold == False:
                    slot.tree.updateImage()
                    slot.tree.drawTree(WIN)
                    #slot.tree.button.draw(WIN, font)
                else:
                    slot.image.set_alpha(255)


    # for seed in SEEDS:
    #    seed.drawSeeds(WIN)
    for row in MARKET_GRID:
        for slot in row:
            slot.drawSlot(WIN)
    pygame.display.update()


def main():

    global MONEY
    tree1 = Tree(5, "Bonsai", 120)
    TREES.append(tree1)

    tree2 = Tree(6, "Elm", 300)
    TREES.append(tree2)


    for i in range(3):
        for j in range(3):
            SLOT_GRID[i].append(Slot(*(SLOT_COORDS[i][j])))

    SLOT_GRID[0][0].plantTree(tree1)
    SLOT_GRID[1][2].plantTree(tree2)

    for i in range(2):
        for j in range(3):
            MARKET_GRID[i].append(MarketSlot(*(MARKET_COORDS[i][j])))

    print(MARKET_GRID)

    pygame.time.set_timer(pygame.USEREVENT, 1000)
    fertlizeButton = Button(1100, 550, 200, 50, "Fertilize!")

    run = True
    while run:
        pygame.time.Clock().tick(FRAMERATE)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # May use later

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                fertlizeButton.is_clicked(event.pos)
                if fertlizeButton.clicked:
                    for tree in TREES:
                        tree.fertilize(5)

            elif event.type == pygame.USEREVENT:
                print("UE")
                for tree in TREES:
                    tree.updateCounter()
                    if tree.getCounter() <= 0 and not tree.sold:
                        # create button
                        tree.createSellButton()
            
            for tree in TREES:
                if not tree.button == None:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        tree.button.is_clicked(event.pos)
                        if (tree.button).clicked:
                            tree.button = None
                            MONEY += 5
                            tree.sold = True
                            del tree
                            
            '''
            for row in SLOT_GRID:
                for slot in row:
                    if slot.tree != None:
                        if not slot.tree.button == None:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                slot.tree.button.is_clicked(event.pos)
                                if (slot.tree.button).clicked:
                                    MONEY += 5
                                    tree.sold = True
                                    del tree
            '''

        drawWindow()

    pygame.quit()


if __name__ == "__main__":
    main()
