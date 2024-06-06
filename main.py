from board import Board
from game import Game
from config import *
from button import Button
from menu import *
import pygame,sys
pygame.init()

board_size=15


screen=pygame.display.set_mode((WIDTH+board.ADD_WIDTH,HEIGHT))
pygame.display.set_caption('Game Caro')
clock=pygame.time.Clock()
menu=Menu(screen,board)


def game_board():
    global game
    game=Game(screen,board_size)  
    pause=False
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==game.TIME_EVENT and not pause:
                game.check_time()   
            if event.type==pygame.MOUSEBUTTONDOWN and not pause:
                x,y=pygame.mouse.get_pos()
                row,col=y//game.board.SQ_SIZE,x//game.board.SQ_SIZE
                if 0 <= row < game.board.size and 0 <= col < game.board.size:                    
                    game.handle_click(row,col)
                           
                if menu.board_buttons[1].checkForInput((x,y)):
                    pause=True
                    if menu.confirm_quit():
                        main()
                        return
                    else:
                        pause=False
                if menu.board_buttons[0].checkForInput((x,y)):
                    print('Volume')
                

                
        game.draw_on_board(screen)
        menu.draw_board_buttons()
        pygame.display.update()
        clock.tick(60) 


def option_menu():
    global board_size
    while True:
        menu.draw_option_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.option_buttons[0].checkForInput(pygame.mouse.get_pos()):
                    board_size = 3
                    main()
                if menu.option_buttons[1].checkForInput(pygame.mouse.get_pos()):
                    board_size = 7
                    main()
                if menu.option_buttons[2].checkForInput(pygame.mouse.get_pos()):
                    board_size = 15
                    main()
                if menu.option_buttons[3].checkForInput(pygame.mouse.get_pos()):
                    main()
                

        pygame.display.update()
        clock.tick(60)

def main():
    
    while True:
        menu.draw_main_menu()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                
                if menu.main_menu_buttons[0].checkForInput(pygame.mouse.get_pos()):
                    game_board()
                    return
                if menu.main_menu_buttons[1].checkForInput(pygame.mouse.get_pos()):
                    option_menu()
                    return
                if menu.main_menu_buttons[2].checkForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)

main()