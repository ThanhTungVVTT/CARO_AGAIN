from board import Board
from game import Game
from config import *

import pygame,sys
pygame.init()

board=Board()
game=Game()
screen=pygame.display.set_mode((WIDTH+board.ADD_WIDTH,HEIGHT))
pygame.display.set_caption('Game Caro')

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            row,col=y//game.board.SQ_SIZE,x//game.board.SQ_SIZE
            game.handle_click(row,col)
            
            
    
    game.draw_on_board(screen)
    pygame.display.update()