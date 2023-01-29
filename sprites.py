import pygame
import os

DIRT = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Dirt Pile.png")), (128, 128))

S1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Stage 1.png")), (128, 128))
S2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Stage 2.png")), (128, 128))
S3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Stage 3.png")), (128, 128))
S4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Stage 4.png")), (128, 128))
COMPLETE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Complete.png")), (128, 128))
SPRITES = [DIRT, S1, S2, S3, S4, COMPLETE]

CB_STAGE1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "CB_Stage1.png")), (128, 128))
CB_STAGE2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "CB_Stage2.png")), (128, 128))
CB_STAGE3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "CB_Stage3.png")), (128, 128))
CB_STAGE4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "CB_Stage4.png")), (128, 128))
CB_COMPLETE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "CB_Complete.png")), (128, 128))

CB_SPRITES = [DIRT, CB_STAGE1, CB_STAGE2, CB_STAGE3, CB_STAGE4, CB_COMPLETE]

WB_STAGE1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "WB_Stage1.png")), (128, 128))
WB_STAGE2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "WB_Stage2.png")), (128, 128))
WB_STAGE3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "WB_Stage3.png")), (128, 128))
WB_STAGE4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "WB_Stage4.png")), (128, 128))
WB_COMPLETE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "WB_Complete.png")), (128, 128))

WB_SPRITES = [DIRT, WB_STAGE1, WB_STAGE2, WB_STAGE3, WB_STAGE4, WB_COMPLETE]

EB_STAGE1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "EB_Stage1.png")), (128, 128))
EB_STAGE2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "EB_Stage2.png")), (128, 128))
EB_STAGE3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "EB_Stage3.png")), (128, 128))
EB_STAGE4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "EB_Stage4.png")), (128, 128))
EB_COMPLETE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "EB_Complete.png")), (128, 128))

EB_SPRITES = [DIRT, EB_STAGE1, EB_STAGE2, EB_STAGE3, EB_STAGE4, EB_COMPLETE]

SB_STAGE1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "SB_Stage1.png")), (128, 128))
SB_STAGE2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "SB_Stage2.png")), (128, 128))
SB_STAGE3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "SB_Stage3.png")), (128, 128))
SB_STAGE4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "SB_Stage4.png")), (128, 128))
SB_COMPLETE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "SB_Complete.png")), (128, 128))

SB_SPRITES = [DIRT, SB_STAGE1, SB_STAGE2, SB_STAGE3, SB_STAGE4, SB_COMPLETE]

RB_STAGE1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "RB_Stage1.png")), (128, 128))
RB_STAGE2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "RB_Stage2.png")), (128, 128))
RB_STAGE3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "RB_Stage3.png")), (128, 128))
RB_STAGE4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "RB_Stage4.png")), (128, 128))
RB_COMPLETE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "RB_Complete.png")), (128, 128))

RB_SPRITES = [DIRT, RB_STAGE1, RB_STAGE2, RB_STAGE3, RB_STAGE4, RB_COMPLETE]