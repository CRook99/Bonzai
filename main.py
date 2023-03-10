import pygame
import os
from tree import *
from slot import *
from button import *
from market_slot import *
from seed import *
from sprites import SPRITES, CB_SPRITES, WB_SPRITES, EB_SPRITES, SB_SPRITES, RB_SPRITES
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

BEEPUS = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "beepus.png")), (150,150))
EXIT_ICON = pygame.image.load(os.path.join("Assets", "Exit Icon.png"))

fertilizeFont = pygame.font.SysFont("bahnschrift", 36)
sellFont = pygame.font.SysFont("bahnschrift", 24)
moneyFont = pygame.font.SysFont("bahnschrift", 30)

CLASSIC_ICON = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Classic Bonsai Seed.png")), (96,96))
WINTER_ICON = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Winter Bonsai Seed.png")), (96,96))
CHERRY_ICON = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Cherry Bonsai Seed.png")), (96,96))
ECLIPSE_ICON = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Eclipse Bonsai Seed.png")), (96,96))
SUNSET_ICON = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Sunset Bonsai Seed.png")), (96,96))
ROYAL_ICON = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Royal Bonsai Seed.png")), (96,96))

CLASSIC_SEED = ('classic', 120, 5, 10, CLASSIC_ICON)
WINTER_SEED = ('winter', 300, 25, 50, WINTER_ICON)
CHERRY_SEED = ('cherry', 1000, 100, 250, CHERRY_ICON)
ECLIPSE_SEED = ('eclipse', 2500, 500, 750, ECLIPSE_ICON)
SUNSET_SEED = ('sunset', 10000, 2000, 5000, SUNSET_ICON)
ROYAL_SEED = ('royal', 50000, 20000, 50000, ROYAL_ICON)

FRAMERATE = 60

BUTTONS = []

MONEY = 10


TREES = []
SLOT_GRID = [[], [], []]

SLOT_COORDS = [[(100, 100), (300, 100), (500, 100)],
               [(100, 300), (300, 300), (500, 300)],
               [(100, 500), (300, 500), (500, 500)]]


SEEDS = []
SEED_TUPLES = [CLASSIC_SEED, WINTER_SEED, CHERRY_SEED, ECLIPSE_SEED, SUNSET_SEED, ROYAL_SEED]
SEED_SPRITE_DICT = {'classic': SPRITES, 'winter': WB_SPRITES, 'cherry': CB_SPRITES, 
                    'eclipse': EB_SPRITES, 'sunset': SB_SPRITES, 'royal': RB_SPRITES}

MARKET_GRID = [[], []]

MARKET_COORDS = [[(900, 100), (1050, 100), (1200, 100)],
                 [(900, 250), (1050, 250), (1200, 250)]]


def drawWindow():
    WIN.fill(SAND_COLOR)
    WIN.blit(BEEPUS, (700, 500))

    for tree in TREES:
        if not tree.button == None:
            (tree.button).draw(WIN)

    for button in BUTTONS:
        button.draw(WIN)
        

    moneyText = moneyFont.render(f"${str(MONEY)}", True, (0, 0, 0))
    WIN.blit(moneyText, (950, 600))

    for row in SLOT_GRID:
        for slot in row:
            slot.drawSlot(WIN)
            if slot.tree != None:
                if slot.tree.sold == False:
                    slot.tree.updateImage()
                    slot.tree.drawTree(WIN)
                else:
                    slot.image.set_alpha(255)


    for row in MARKET_GRID:
        for slot in row:
            if slot.seed != None:
                slot.seed.draw(WIN)
            else:
                slot.drawSlot(WIN)

    if cursor_icon != None:
        cursor_img_rect = cursor_icon.get_rect()
        cursor_img_rect.center = pygame.mouse.get_pos()
        WIN.blit(cursor_icon, cursor_img_rect.center)

    pygame.display.update()

def changeCursor(icon):
    pygame.mouse.set_visible(False)
    return icon

def defaultCursor():
    pygame.mouse.set_visible(True)
    return None


def main():

    global MONEY
    global cursor_icon
    cursor_icon = None

    for i in range(3):
        for j in range(3):
            SLOT_GRID[i].append(Slot(*(SLOT_COORDS[i][j])))


    count = 0
    for i in range(2):
        for j in range(3):
            MARKET_GRID[i].append(MarketSlot(*(MARKET_COORDS[i][j])))
            seed = Seed(*(SEED_TUPLES[count]))
            SEEDS.append(seed)
            MARKET_GRID[i][j].giveSeed(seed)
            count += 1

    BEEPUS.set_alpha(0)


    pygame.time.set_timer(pygame.USEREVENT, 1000)
    fertilizeButton = TextButton(1100, 550, 200, 50, "Fertilize!", fertilizeFont, (255, 255, 255))
    exitButton = ImageButton(WIDTH - 100, 20, EXIT_ICON)
    BUTTONS.append(fertilizeButton)
    BUTTONS.append(exitButton)

    heldSeed = None

    run = True
    while run:
        pygame.time.Clock().tick(FRAMERATE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # May use later

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_m:
                    MONEY += 10000
                elif event.key == pygame.K_b:
                    BEEPUS.set_alpha(255)

            elif event.type == pygame.USEREVENT:
                for tree in TREES:
                    tree.updateCounter()
                    if tree.getCounter() <= 0 and not tree.sold:
                        tree.createSellButton()

            if heldSeed != None:
                for row in SLOT_GRID:
                    for slot in row:
                        if slot.drawSlot(WIN):
                            if MONEY >= heldSeed.cost:
                                slot.plantTree(Tree(heldSeed.value, heldSeed.growthTime, SEED_SPRITE_DICT[heldSeed.name]))
                                MONEY -= heldSeed.cost
                                TREES.append(slot.tree)
                            else:
                                pass
                            heldSeed = None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if cursor_icon != None:
                    cursor_icon = defaultCursor()
                    heldSeed = None

            
            if fertilizeButton.draw(WIN):
                for tree in TREES:
                    tree.fertilize(2)

            
                    

            if exitButton.draw(WIN):
                run = False

            
            for seed in SEEDS:
                if seed.draw(WIN):
                    cursor_icon = changeCursor(seed.image)
                    heldSeed = seed
            

            for tree in TREES:
                if tree.button:
                    if tree.button.draw(WIN):
                        tree.button = None
                        MONEY += tree.value
                        tree.sold = True
                        del tree

                  

        drawWindow()

    pygame.quit()


if __name__ == "__main__":
    main()
