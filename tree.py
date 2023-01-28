import pygame

font = pygame.font.SysFont('Consolas', 30)

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

    screen = pygame.display.set_mode((128, 128))
    counter, text = 120, '120'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    def drawTree(self, screen):
        counter -= 1
        text = str(counter).rjust(3) if counter > 0 else 'Growth Complete!'
        #screen.fill((255, 255, 255))
        screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        #pygame.display.flip()

    '''
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT:
                # do stuff
                print("pass")
            elif e.type == pygame.QUIT:
                run = False
    pygame.display.flip()
    timer.tick(60)
    '''

    
    
