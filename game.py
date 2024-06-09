import pygame
import sys
from player import Player
from board import Board
from menu import Menu
from config import *

# Khởi tạo pygame
pygame.init()

board=Board()
board_size=15
screen = pygame.display.set_mode((WIDTH + board.ADD_WIDTH, HEIGHT))
pygame.display.set_caption('Game Caro')
clock = pygame.time.Clock()

menu=Menu(screen,board)

# Hàm tiện ích để tải phông chữ


class Game:
    def __init__(self, screen, board_size): 
        self.screen = screen
        self.board = Board(board_size)
        self.players = [Player('Player 1', 'X'), Player('Player 2', 'O')]
        self.current_player_index = 0
        self.winner = None
        self.timers = {0: self.players[0].time, 1: self.players[1].time}
        self.menu = Menu(screen, self.board)
        self.sound_state=True
        self.sound_menu_state=True
        self.sound_menu_played=False
        self.TIME_EVENT=pygame.USEREVENT+1
        pygame.time.set_timer(self.TIME_EVENT,1000)
 
        # self.turn_start_time=pygame.time.get_ticks()

    def reset_timer(self):
        self.timers = {0: self.players[0].time, 1: self.players[1].time}

    def switch_player(self):
        self.current_player_index = 1-self.current_player_index
        self.reset_timer()

    def get_current_player(self):
        return self.players[self.current_player_index]

    def handle_click(self, row, col):
        player = self.get_current_player()
        if self.board.temp_mark == (row, col):
            if self.board.update(row, col, player.symbol):
                self.board.temp_mark = None
                self.draw_on_board(self.screen)
                pygame.display.update()

                if self.board.check_win():
                    if self.sound_state:
                        sound_win.play()
                    pygame.time.wait(1000)
                    self.winner = player
                    result = self.menu.show_winner(self.winner.name)
                    if result == "PLAY":
                        self.reset()
                    elif result == "MENU":
                        self.run()
                        return True
                else:
                    self.switch_player()                  
        else:
            self.board.temp_mark = (row, col)
        return False
    
    def check_time(self):
        if self.winner:
            self.timers[self.current_player_index] = self.players[self.current_player_index].time
        if not self.winner:
            self.timers[self.current_player_index] -= 1
            if self.timers[self.current_player_index] <= 0:
                self.switch_player()

    def draw_on_board(self, screen):
        
        self.board.draw_board(screen)
        self.board.draw_player(screen, self.players, self.get_current_player().symbol, self.timers)

    def reset(self):
        self.board = Board(self.board.size)
        self.current_player_index = 0
        self.winner = None
        self.reset_timer()

    def game_board(self, board_size):
        self.__init__(self.screen, board_size)
        pause=False
        while True:
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==self.TIME_EVENT and not pause:
                    self.check_time()
                if event.type == pygame.MOUSEBUTTONDOWN and not pause:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // self.board.SQ_SIZE, x // self.board.SQ_SIZE
                    if 0 <= row < self.board.size and 0 <= col < self.board.size:
                        if self.sound_state:
                            sound_click_X_O.play()
                        self.handle_click(row, col)
                        
                    if board_buttons[2].checkForInput((x, y)):
                        pause = True
                        self.pause_game=True
                        if self.menu.confirm_quit():
                            self.run()
                            return
                        else:
                            pause = False                 
                                                      
                    if self.menu.state_volume:
                        if board_buttons[0].checkForInput((x, y)):
                            self.menu.state_volume=False
                            self.sound_state=False 
                                                   
                    else:
                        if board_buttons[1].checkForInput((x, y)):
                            self.menu.state_volume=True
                            self.sound_state=True
                       
            
            self.draw_on_board(self.screen)
            board_buttons=self.menu.draw_board_buttons()
            pygame.display.update()
            clock.tick(60)

    def option_menu(self):
        while True:
            option_buttons=self.menu.draw_option_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sound_click.play()
                    if option_buttons[0].checkForInput(pygame.mouse.get_pos()):
                        self.choose_board_size()
                    if option_buttons[1].checkForInput(pygame.mouse.get_pos()):
                        self.show_help()
                    if option_buttons[2].checkForInput(pygame.mouse.get_pos()):
                        self.run()
                        

            pygame.display.update()
            clock.tick(60)

    def show_help(self):
        while True:
            help_buttons=self.menu.show_help_button()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sound_click.play()
                    if help_buttons[0].checkForInput(pygame.mouse.get_pos()):
                        self.option_menu()
            pygame.display.update()
            clock.tick(60)    

    def choose_board_size(self):
        global board_size
        while True:
            grid_buttons=self.menu.draw_choose_board_size()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sound_click.play()
                    if grid_buttons[0].checkForInput(pygame.mouse.get_pos()):
                        board_size = 3
                        self.run()
                    if grid_buttons[1].checkForInput(pygame.mouse.get_pos()):
                        board_size = 7
                        self.run()
                    if grid_buttons[2].checkForInput(pygame.mouse.get_pos()):
                        board_size = 15
                        self.run()          
            pygame.display.update()
            clock.tick(60)


    def run(self):
        if not pygame.mixer.get_busy():
            sound_menu.play(-1)
        while True:
            main_menu_buttons=self.menu.draw_main_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sound_click.play()
                    if main_menu_buttons[0].checkForInput(pygame.mouse.get_pos()):
                        sound_menu.stop()
                        self.game_board(board_size)
                        return
                    if main_menu_buttons[1].checkForInput(pygame.mouse.get_pos()):
                        self.option_menu()
                        return
                    if main_menu_buttons[2].checkForInput(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
                    
                    if self.menu.state_volume_menu:
                        if main_menu_buttons[3].checkForInput(pygame.mouse.get_pos()):
                            self.menu.state_volume_menu=False
                            self.sound_menu_state=False
                            sound_menu.stop()
                    else:
                        if main_menu_buttons[4].checkForInput(pygame.mouse.get_pos()):
                            self.menu.state_volume_menu=True
                            self.sound_menu_state=True
                            sound_menu.play(-1)
                        
            
            pygame.display.update()
            clock.tick(60)


if __name__ == "__main__":
    game = Game(screen, board_size)
    game.run()
