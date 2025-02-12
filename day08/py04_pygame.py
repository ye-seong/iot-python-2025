import pygame 
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEWHEEL, MOUSEMOTION
import sys


# 기본 변수
pygame.init()
Surface = pygame.display.set_mode((600, 400)) 
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Mouse')

def main():
    pos = []
    check = mousebutton = False
    while True:
        Surface.fill(color='black')  # Surface.fill((0,0,0))
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # pos.append(event.pos)
                check = True
                mousebutton = True
            elif event.type == MOUSEMOTION:
                if mousebutton: pos.append(event.pos)
            elif event.type == MOUSEBUTTONUP:
                mousebutton = False
                check = False
                pos.clear()

        # for mpos in pos:
        #     pygame.draw.circle(Surface, 'white', mpos, 5)
        if check:
            if len(pos) > 1:
                pygame.draw.line(Surface, 'white', False, pos)

        pygame.display.update()
        FPSCLOCK.tick(30) 

if __name__ == '__main__':
    main()

