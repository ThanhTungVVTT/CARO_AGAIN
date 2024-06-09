from config import *
from button import Button
from board import Board
board=Board()
import pygame,sys
pygame.init()


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/font.ttf", size)


class Menu:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board
        self.state_volume=True
        self.state_volume_menu=True

    def create_button(self, image, pos, text_input, font, base_color, hovering_color):
        return Button(image, pos, text_input, font, base_color, hovering_color)
    
    def confirm_quit(self):
        confirm_buttons=[
            self.create_button(None,(WIDTH//2,HEIGHT//2),"YES",get_font(30),"black",(0,0,200)),
            self.create_button(None,(WIDTH//2,HEIGHT//2+60),"NO",get_font(30),"black",(0,0,200))
        ]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if confirm_buttons[0].checkForInput(pygame.mouse.get_pos()):
                        return True
                    if confirm_buttons[1].checkForInput(pygame.mouse.get_pos()):
                        return False
            pygame.draw.rect(self.screen, WHITE, (110, 220, 480, 240))
            pygame.draw.rect(self.screen, BLACK, (110, 220, 480, 240), 2)
            confirm_text = get_font(35).render("ARE YOU SURE?", True, BLACK)
            self.screen.blit(confirm_text, (WIDTH // 2 - confirm_text.get_width() // 2, HEIGHT // 3 + 20))
            for button in confirm_buttons:
                button.update(self.screen)
            pygame.display.update()
            pygame.time.Clock().tick(60)

    def show_winner(self, winner):
        winner_buttons=[
            self.create_button(None,(WIDTH//2,HEIGHT//2),"PLAY AGAIN",get_font(30),"black",(0,0,200)),
            self.create_button(None,(WIDTH//2,HEIGHT//2+60),"MENU",get_font(30),"black",(0,0,200))
        ]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if winner_buttons[0].checkForInput(pygame.mouse.get_pos()):
                        return "PLAY"
                    if winner_buttons[1].checkForInput(pygame.mouse.get_pos()):
                        return "MENU"
            pygame.draw.rect(self.screen, WHITE, (110, 220, 480, 240))
            pygame.draw.rect(self.screen, BLACK, (110, 220, 480, 240), 2)

            winner_text = get_font(33).render(f"{winner} WINS!", True, BLACK)
            text_rect=winner_text.get_rect(topleft=(130,240))
            self.screen.blit(winner_text,text_rect)
            for button in winner_buttons:
                button.update(self.screen)
            
            pygame.display.update()
            pygame.time.Clock().tick(60)
        

    def draw_option_menu(self):
        option_buttons=[
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2-50),"GRID",get_font(40),"#d7fcd4",(0,0,200)),
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+190),"HELP",get_font(40),"#d7fcd4",(0,0,200)),
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+310),"BACK",get_font(40),"#d7fcd4",(200,0,0))
        ]

        self.screen.blit(back_ground_image,(0,0))
        OPTION_TEXT=get_font(50).render("OPTIONS",True,(255,255,255))
        OPTION_RECT=OPTION_TEXT.get_rect(center=(((WIDTH+board.ADD_WIDTH)//2),HEIGHT//2-200))
        self.screen.blit(OPTION_TEXT,OPTION_RECT)    
        for button in option_buttons:
            button.changeColor(pygame.mouse.get_pos())
            button.update(self.screen)
        return option_buttons
    
    def show_help_button(self):
        help_buttons=[
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+200),"BACK",get_font(40),"#d7fcd4",(200,0,0))
        ]
        self.screen.blit(back_ground_image,(0,0))
        HELP_TEXT=get_font(50).render("RULE THE GAME",True,(255,255,255))
        HELP_RECT=HELP_TEXT.get_rect(center=(((WIDTH+board.ADD_WIDTH)//2),HEIGHT//2-200))
        self.screen.blit(HELP_TEXT,HELP_RECT)
        for button in help_buttons:
            button.changeColor(pygame.mouse.get_pos())
            button.update(self.screen)
        return help_buttons


    def draw_choose_board_size(self):
        grid_buttons=[
            self.create_button(board_3x3,(182,HEIGHT//2+50),None,get_font(40),"#d7fcd4",(0,0,200)),
            self.create_button(board_7x7,(498,HEIGHT//2+50),None,get_font(40),"#d7fcd4",(0,200,0)),
            self.create_button(board_15x15,(812,HEIGHT//2+50),None,get_font(40),"#d7fcd4",(200,0,0)),
        ]
        self.screen.blit(back_ground_image,(0,0))
        GRID_TEXT=get_font(50).render("CHOOSE A GRID",True,(255,255,255))
        GRID_RECT=GRID_TEXT.get_rect(center=(((WIDTH+board.ADD_WIDTH)//2),HEIGHT//2-200))
        self.screen.blit(GRID_TEXT,GRID_RECT)
        for button in grid_buttons:
            button.changeColor(pygame.mouse.get_pos())
            button.update(self.screen)
        return grid_buttons
    
    def draw_main_menu(self):
        board_buttons=[
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2-50),"PLAY",get_font(40),"#d7fcd4",(0,0,200)),
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+70),"OPTIONS",get_font(40),"#d7fcd4",(0,200,0)),
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+190),"QUIT",get_font(40),"#d7fcd4",(200,0,0)),
            self.create_button(volume_image_on,(WIDTH + board.ADD_WIDTH - 150, HEIGHT - 50),None,get_font(40),"black",(0,0,200)),
            self.create_button(volume_image_off,(WIDTH + board.ADD_WIDTH - 150, HEIGHT - 50),None,get_font(40),"black",(0,0,200))
        ]
        self.screen.blit(back_ground_image,(0,0))
        MENU_TEXT=get_font(50).render("CARO GAME",True,(255,255,255))
        MENU_RECT=MENU_TEXT.get_rect(center=(((WIDTH+board.ADD_WIDTH)//2),HEIGHT//2-200))
        self.screen.blit(MENU_TEXT,MENU_RECT)

        for button in board_buttons[0:3]:
            button.changeColor(pygame.mouse.get_pos())
            button.update(self.screen)
        if self.state_volume_menu:
            board_buttons[3].update(self.screen)
        else:
            board_buttons[4].update(self.screen)

        return board_buttons

    def draw_board_buttons(self):
        board_buttons=[
            self.create_button(volume_image_on,(WIDTH + board.ADD_WIDTH - 150, HEIGHT - 50),None,get_font(40),"black",(0,0,200)),
            self.create_button(volume_image_off,(WIDTH + board.ADD_WIDTH - 150, HEIGHT - 50),None,get_font(40),"black",(0,0,200)),
            self.create_button(None,(WIDTH + board.ADD_WIDTH - 150, HEIGHT - 100),"MENU",get_font(40),"black",(255,0,0))
        ]
        board_buttons[2].changeColor(pygame.mouse.get_pos())
        board_buttons[2].update(self.screen)
        if self.state_volume:
            board_buttons[0].update(self.screen)
        else:
            board_buttons[1].update(self.screen)
        return board_buttons
    