import pygame 
from pygame.locals import QUIT
import sys

# 기본 변수
pygame.init()
Surface = pygame.display.set_mode((600, 400)) 
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Template')

def main():
    while True:
        Surface.fill(color='black')  # Surface.fill((0,0,0))
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(30) 

if __name__ == '__main__':
    main()