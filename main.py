from board import Board
from game import Game
from config import *
from button import Button
from menu import *
import pygame,sys
pygame.init()

board_size=15

game=Game(board_size)
screen=pygame.display.set_mode((WIDTH+board.ADD_WIDTH,HEIGHT))
pygame.display.set_caption('Game Caro')
clock=pygame.time.Clock()

VOLUME_BUTTON=Button(image=None,pos=(WIDTH+board.ADD_WIDTH-150,HEIGHT-50),text_input="VOLUME",font=get_font(40),base_color="black",hovering_color=(0,0,200))
MENU_BUTTON=Button(image=None,pos=(WIDTH+board.ADD_WIDTH-150,HEIGHT-100),text_input="MENU",font=get_font(40),base_color="black",hovering_color=(0,0,200))

buttons=create_button()
option_button=size_board()


def game_board():
    global game
    game=Game(board_size)  
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
                if MENU_BUTTON.checkForInput((x,y)):
                    pause=True
                    if confirm_quit():
                        main()
                        return
                    else:
                        pause=False
                if VOLUME_BUTTON.checkForInput((x,y)):
                    print('Volume')

                
        game.draw_on_board(screen)
        VOLUME_BUTTON.update(screen)
        MENU_BUTTON.update(screen)
        pygame.display.update()
        clock.tick(60) 

def confirm_quit():
    confirm_button=[
        Button(image=None,pos=(WIDTH//2,HEIGHT//2-30),text_input="YES",font=get_font(40),base_color="black",hovering_color=(0,0,200)),
        Button(image=None,pos=(WIDTH//2,HEIGHT//2+30),text_input="NO",font=get_font(40),base_color="black",hovering_color=(0,0,200))
    ]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if confirm_button[0].checkForInput(pygame.mouse.get_pos()):
                    return True
                if confirm_button[1].checkForInput(pygame.mouse.get_pos()):
                    return False

        pygame.draw.rect(screen, WHITE, (WIDTH // 4, HEIGHT // 3, WIDTH // 2, HEIGHT // 3))
        pygame.draw.rect(screen, BLACK, (WIDTH // 4, HEIGHT // 3, WIDTH // 2, HEIGHT // 3), 2)
        confirm_text = get_font(40).render("ARE YOU SURE?", True, BLACK)
        screen.blit(confirm_text, (WIDTH // 2 - confirm_text.get_width() // 2, HEIGHT // 3 + 20))
        for button in confirm_button:
            button.update(screen)
        pygame.display.update()
        clock.tick(60)


def option_menu():
    global board_size
    while True:
        draw_option_menu(screen,option_button,back_ground_image)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if option_button[0].checkForInput(pygame.mouse.get_pos()):
                    board_size = 3
                    main()
                if option_button[1].checkForInput(pygame.mouse.get_pos()):
                    board_size = 7
                    main()
                if option_button[2].checkForInput(pygame.mouse.get_pos()):
                    board_size = 15
                    main()
                if option_button[3].checkForInput(pygame.mouse.get_pos()):
                    main()
                

        pygame.display.update()
        clock.tick(60)

def main():
    
    while True:
        draw_main_menu(screen,buttons,back_ground_image)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                
                if buttons[0].checkForInput(pygame.mouse.get_pos()):
                    game_board()
                    return
                if buttons[1].checkForInput(pygame.mouse.get_pos()):
                    option_menu()
                    return
                if buttons[2].checkForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)

main()