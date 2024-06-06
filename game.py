import pygame
import sys
from player import Player
from board import Board
from menu import Menu
from button import Button
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
def get_font(size):
    return pygame.font.Font("assets/images/font.ttf", size)

class Game:
    def __init__(self, screen, board_size):
        self.screen = screen
        self.board = Board(board_size)
        self.players = [Player('Player 1', 'X'), Player('Player 2', 'O')]
        self.current_player_index = 0
        self.winner = None
        self.timers = {0: self.players[0].time, 1: self.players[1].time}
        self.menu = Menu(screen, self.board)
        self.TIME_EVENT = pygame.USEREVENT
        pygame.time.set_timer(self.TIME_EVENT, 1000)

    def reset_timer(self):
        self.timers = {0: self.players[0].time, 1: self.players[1].time}

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
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
                    pygame.time.wait(500)
                    self.winner = player
                    result = self.menu.show_winner(self.winner.name)
                    if result == "PLAY":
                        self.reset()
                    elif result == "MENU":
                        main()
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

# Tạo cửa sổ hiển thị


# Khởi tạo Menu
menu = Menu(screen, Board())

def game_board(board_size):
    global game
    game = Game(screen, board_size)
    pause = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == game.TIME_EVENT and not pause:
                game.check_time()
            if event.type == pygame.MOUSEBUTTONDOWN and not pause:
                x, y = pygame.mouse.get_pos()
                row, col = y // game.board.SQ_SIZE, x // game.board.SQ_SIZE
                if 0 <= row < game.board.size and 0 <= col < game.board.size:
                    game.handle_click(row, col)

                if menu.board_buttons[1].checkForInput((x, y)):
                    pause = True
                    if menu.confirm_quit():
                        main()
                        return
                    else:
                        pause = False
                if menu.board_buttons[0].checkForInput((x, y)):
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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.main_menu_buttons[0].checkForInput(pygame.mouse.get_pos()):
                    game_board(board_size)
                    return
                if menu.main_menu_buttons[1].checkForInput(pygame.mouse.get_pos()):
                    option_menu()
                    return
                if menu.main_menu_buttons[2].checkForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)


