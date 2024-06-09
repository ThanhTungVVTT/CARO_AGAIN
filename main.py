import pygame
from config import *
pygame.init()

screen=pygame.display.set_mode((500,500))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill(WHITE)
    
   
    avatar_X_pos=avatar_X.get_rect()
    
    screen.blit(avatar_X,avatar_X_pos)
    pygame.display.update()