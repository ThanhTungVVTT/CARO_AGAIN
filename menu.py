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
        self.board_buttons=[ Button(image=volume_image_on, pos=(WIDTH + board.ADD_WIDTH - 150, HEIGHT - 50),
                                    text_input=None, font=get_font(40),base_color="black", hovering_color=(0, 0, 200)),
                            Button(image=volume_image_off, pos=(WIDTH + board.ADD_WIDTH - 150, HEIGHT - 50),
                                    text_input=None, font=get_font(40),base_color="black", hovering_color=(0, 0, 200)),
                            Button(image=None, pos=(WIDTH + board.ADD_WIDTH - 150, HEIGHT - 100),
                                  text_input="MENU", font=get_font(40), base_color="black", hovering_color=(0, 0, 200))
        ]

        self.main_menu_buttons=[Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2-50),text_input="PLAY",font=get_font(40),base_color="#d7fcd4",hovering_color=(0,0,200)),
                                Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+70),text_input="OPTIONS",font=get_font(40),base_color="#d7fcd4",hovering_color=(0,200,0)),
                                Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+190),text_input="QUIT",font=get_font(40),base_color="#d7fcd4",hovering_color=(200,0,0))
                                ]

        self.option_buttons=[
            Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2-50),text_input="3x3",font=get_font(40),base_color="#d7fcd4",hovering_color=(0,0,200)),
            Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+70),text_input="7x7",font=get_font(40),base_color="#d7fcd4",hovering_color=(0,200,0)),
            Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+190),text_input="15x15",font=get_font(40),base_color="#d7fcd4",hovering_color=(200,0,0)),
            Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+310),text_input="BACK",font=get_font(40),base_color="#d7fcd4",hovering_color=(200,0,0))
        ]

        self.confirm_buttons = [
            Button(image=None, pos=(WIDTH // 2, HEIGHT // 2), text_input="YES", font=get_font(30), base_color="black", hovering_color=(0, 0, 200)),
            Button(image=None, pos=(WIDTH // 2, HEIGHT // 2 + 60), text_input="NO", font=get_font(30), base_color="black", hovering_color=(0, 0, 200))
        ]
        self.winner_buttons = [
            Button(image=None, pos=(WIDTH // 2, HEIGHT // 2 ), text_input="PLAY AGAIN", font=get_font(30), base_color="black", hovering_color=(0, 0, 200)),
            Button(image=None, pos=(WIDTH // 2, HEIGHT // 2+60), text_input="MENU", font=get_font(30), base_color="black", hovering_color=(0, 0, 200))
        ]

    def confirm_quit(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.confirm_buttons[0].checkForInput(pygame.mouse.get_pos()):
                        return True
                    if self.confirm_buttons[1].checkForInput(pygame.mouse.get_pos()):
                        return False

            # pygame.draw.rect(self.screen, WHITE, (WIDTH // 4, HEIGHT // 3, WIDTH // 1.5, HEIGHT // 3))
            # pygame.draw.rect(self.screen, BLACK, (WIDTH // 4, HEIGHT // 3, WIDTH // 1.5, HEIGHT // 3), 2)
            pygame.draw.rect(self.screen, WHITE, (110, 220, 480, 240))
            pygame.draw.rect(self.screen, BLACK, (110, 220, 480, 240), 2)
            confirm_text = get_font(35).render("ARE YOU SURE?", True, BLACK)
            self.screen.blit(confirm_text, (WIDTH // 2 - confirm_text.get_width() // 2, HEIGHT // 3 + 20))
            for button in self.confirm_buttons:
                button.update(self.screen)
            pygame.display.update()
            pygame.time.Clock().tick(60)

    def show_winner(self, winner):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.winner_buttons[0].checkForInput(pygame.mouse.get_pos()):
                        return "PLAY"
                    if self.winner_buttons[1].checkForInput(pygame.mouse.get_pos()):
                        return "MENU"

            # rect_x = WIDTH // 4
            # rect_y = HEIGHT // 3
            # rect_width = WIDTH // 2
            # rect_height = HEIGHT // 3

            # pygame.draw.rect(self.screen, WHITE, (rect_x, rect_y, rect_width, rect_height))
            # pygame.draw.rect(self.screen, BLACK, (rect_x, rect_y, rect_width, rect_height), 2)
            # winner_text = get_font(35).render(f"{winner} WINS!", True, BLACK)
            # text_rect = winner_text.get_rect(center=(rect_x + rect_width / 2, rect_y + rect_height / 2 - 30))
            # self.screen.blit(winner_text, text_rect)
            pygame.draw.rect(self.screen, WHITE, (110, 220, 480, 240))
            pygame.draw.rect(self.screen, BLACK, (110, 220, 480, 240), 2)

            winner_text = get_font(33).render(f"{winner} WINS!", True, BLACK)
            text_rect=winner_text.get_rect(topleft=(130,240))
            self.screen.blit(winner_text,text_rect)
            for button in self.winner_buttons:
                button.update(self.screen)
            
            pygame.display.update()
            pygame.time.Clock().tick(60)

    def draw_option_menu(self):
        self.screen.blit(back_ground_image,(0,0))
        OPTION_TEXT=get_font(50).render("OPTIONS",True,(255,255,255))
        OPTION_RECT=OPTION_TEXT.get_rect(center=(((WIDTH+board.ADD_WIDTH)//2),HEIGHT//2-200))
        self.screen.blit(OPTION_TEXT,OPTION_RECT)    
        for button in self.option_buttons:
            button.changeColor(pygame.mouse.get_pos())
            button.update(self.screen)

    def draw_main_menu(self):
        self.screen.blit(back_ground_image,(0,0))
        MENU_TEXT=get_font(50).render("CARO GAME",True,(255,255,255))
        MENU_RECT=MENU_TEXT.get_rect(center=(((WIDTH+board.ADD_WIDTH)//2),HEIGHT//2-200))
        self.screen.blit(MENU_TEXT,MENU_RECT)

        for button in self.main_menu_buttons:
            button.changeColor(pygame.mouse.get_pos())
            button.update(self.screen)

    def draw_board_buttons(self):
        self.board_buttons[2].changeColor(pygame.mouse.get_pos())
        self.board_buttons[2].update(self.screen)
        if self.state_volume:
            self.board_buttons[0].update(self.screen)
        else:
            self.board_buttons[1].update(self.screen)
