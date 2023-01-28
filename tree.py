import pygame

pygame.init()

class Tree:
    value = -1
    name = "X"
    counter = -1
    text = ""

    def __init__(self, value, name):
        self.value = value
        self.name = name
        self.counter, self.text = 120, '120'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font = pygame.font.SysFont('Consolas', 30)

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    

    def drawTree(self, screen):
        self.counter -= 1
        text = str(self.counter).rjust(3) if self.counter > 0 else 'Growth Complete!'
        screen.blit(self.font.render(text, True, (0, 0, 0)), (32, 48))

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

    
    
