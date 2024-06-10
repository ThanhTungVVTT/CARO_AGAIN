from config import *
from button import Button
from board import Board
board=Board()
import pygame,sys
pygame.init()

class Menu:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board
        self.state_volume=True
        self.state_menu_volume=True
        

    def create_button(self, image, pos, text_input, font, base_color, hovering_color):
        return Button(image, pos, text_input, font, base_color, hovering_color)
    
    def confirm_quit(self):
        confirm_buttons=[
            self.create_button(None,(WIDTH//2,HEIGHT//2),"YES",get_font(40,"Designer","otf"),BLACK,(0,0,200)),
            self.create_button(None,(WIDTH//2,HEIGHT//2+60),"NO",get_font(40,"Designer","otf"),BLACK,(0,0,200))
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
            confirm_text = get_font(45,"Designer","otf").render("ARE YOU SURE?", True, BLACK)
            self.screen.blit(confirm_text, (WIDTH // 2 - confirm_text.get_width() // 2, HEIGHT // 3 + 20))
            for button in confirm_buttons:
                button.update(self.screen)
            pygame.display.update()
            pygame.time.Clock().tick(60)

    def show_winner(self, winner):
        winner_buttons=[
            self.create_button(None,(WIDTH//2,HEIGHT//2),"PLAY AGAIN",get_font(40,"Designer","otf"),BLACK,(0,0,200)),
            self.create_button(None,(WIDTH//2,HEIGHT//2+60),"MENU",get_font(40,"Designer","otf"),BLACK,(0,0,200))
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

            winner_text = get_font(45,"Designer","otf").render(f"{winner} WINS", True, BLACK)
            
            self.screen.blit(winner_text,(WIDTH//2-winner_text.get_width()//2,HEIGHT//2-100))
            for button in winner_buttons:
                button.update(self.screen)
            
            pygame.display.update()
            pygame.time.Clock().tick(60)
        

    def draw_option_menu(self):
        option_buttons=[
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2-50),"GRID",get_font(40,"font","ttf"),BUTTON_COLOR,GRAY),
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+50),"HELP",get_font(40,"font","ttf"),BUTTON_COLOR,GRAY),
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+150),"BACK",get_font(40,"font","ttf"),BUTTON_COLOR,GRAY)
        ]

        self.screen.blit(back_ground_image,(0,0))
        OPTION_TEXT=get_font(50,"font","ttf").render("OPTIONS",True,TITLE_COLOR)
        OPTION_RECT=OPTION_TEXT.get_rect(center=(((WIDTH+board.ADD_WIDTH)//2),HEIGHT//2-200))
        self.screen.blit(OPTION_TEXT,OPTION_RECT)    
        for button in option_buttons:
            button.changeColor(pygame.mouse.get_pos())
            button.zoom_in_text(pygame.mouse.get_pos(),self.screen)
        return option_buttons
    
    def show_help_button(self):
        help_buttons=[
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT-70),"BACK",get_font(40,"font","ttf"),BUTTON_COLOR,GRAY)
        ]
        self.screen.blit(back_ground_image,(0,0))
        HELP_TEXT=get_font(50,"font","ttf").render("GAME RULES",True,TITLE_COLOR)
        HELP_RECT=HELP_TEXT.get_rect(center=(((WIDTH+board.ADD_WIDTH)//2),HEIGHT//2-250))
        font_help=pygame.font.Font(None,30)

        instruction_text1=font_help.render(instructions[0],True,(255,255,255))
        instruction_text2=font_help.render(instructions[1],True,(255,255,255))
        instruction_text3=font_help.render(instructions[2],True,(255,255,255))
        instruction_text4=font_help.render(instructions[3],True,(255,255,255))
        instruction_text5=font_help.render(instructions[4],True,(255,255,255))
        instructions_help=[instruction_text1,instruction_text2,instruction_text3,instruction_text4,instruction_text5]
        for instruction in instructions_help:
            instruction_rect=instruction.get_rect(center=((WIDTH+board.ADD_WIDTH)//2+200,HEIGHT//2-100+instructions_help.index(instruction)*50))
            self.screen.blit(instruction,instruction_rect) 

        self.screen.blit(HELP_TEXT,HELP_RECT)
        self.screen.blit(help_image,(50,HEIGHT//2-150))
        for button in help_buttons:
            button.changeColor(pygame.mouse.get_pos())
            button.zoom_in_text(pygame.mouse.get_pos(),self.screen)

        return help_buttons


    def draw_choose_grid(self):
        grid_buttons=[
            self.create_button(board_3x3,(182,HEIGHT//2+50),None,get_font(40,"font","ttf"),BUTTON_COLOR,(0,0,200)),
            self.create_button(board_7x7,(498,HEIGHT//2+50),None,get_font(40,"font","ttf"),BUTTON_COLOR,(0,200,0)),
            self.create_button(board_15x15,(812,HEIGHT//2+50),None,get_font(40,"font","ttf"),BUTTON_COLOR,(200,0,0)),
        ]
        self.screen.blit(back_ground_image,(0,0))
        GRID_TEXT=get_font(50,"font","ttf").render("CHOOSE A GRID",True,TITLE_COLOR)
        GRID_RECT=GRID_TEXT.get_rect(center=(((WIDTH+board.ADD_WIDTH)//2),HEIGHT//2-200))
        self.screen.blit(GRID_TEXT,GRID_RECT)
        for button in grid_buttons:
            button.changeColor(pygame.mouse.get_pos())
            button.update(self.screen)
        return grid_buttons
    
    def draw_main_menu(self):
        board_buttons=[
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2-30),"PLAY",get_font(40,"font","ttf"),BUTTON_COLOR,GRAY),
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+80),"OPTIONS",get_font(40,"font","ttf"),BUTTON_COLOR,GRAY),
            self.create_button(None,((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+190),"QUIT",get_font(40,"font","ttf"),BUTTON_COLOR,GRAY),
            self.create_button(volume_image_menu_on,(WIDTH + board.ADD_WIDTH - 60, 50),None,get_font(40,"font","ttf"),BLACK,(0,0,200)),
            self.create_button(volume_image_menu_off,(WIDTH + board.ADD_WIDTH - 60, 50),None,get_font(40,"font","ttf"),BLACK,(0,0,200))
        ]
        self.screen.blit(back_ground_image,(0,0))
        MENU_TEXT=get_font(70,"font","ttf").render("CARO GAME",True,TITLE_COLOR)
        MENU_RECT=MENU_TEXT.get_rect(center=(((WIDTH+board.ADD_WIDTH)//2),HEIGHT//2-200))
        self.screen.blit(MENU_TEXT,MENU_RECT)
        
        for button in board_buttons[0:3]:
            button.changeColor(pygame.mouse.get_pos())
            button.zoom_in_text(pygame.mouse.get_pos(),self.screen)
            
            
        if self.state_menu_volume:
            board_buttons[3].update(self.screen)
        else:
            board_buttons[4].update(self.screen)

        return board_buttons

    def draw_button_in_board(self):
        board_buttons=[
            self.create_button(volume_image_on,(WIDTH + 80, HEIGHT - 50),None,get_font(40,"font","ttf"),BLACK,(0,0,200)),
            self.create_button(volume_image_off,(WIDTH + 80, HEIGHT - 50),None,get_font(40,"font","ttf"),BLACK,(0,0,200)),
            self.create_button(home_image,(WIDTH + board.ADD_WIDTH-80, HEIGHT - 50),None,get_font(40,"font","ttf"),BLACK,(0,0,200))
        ]
        board_buttons[2].changeColor(pygame.mouse.get_pos())
        board_buttons[2].update(self.screen)
        if self.state_volume:
            board_buttons[0].update(self.screen)
        else:
            board_buttons[1].update(self.screen)
        return board_buttons
