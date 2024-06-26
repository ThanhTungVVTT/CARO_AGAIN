import pygame
import sys
from player import Player
from board import Board
from menu import Menu
from config import *

pygame.init()

board = Board()
board_size = 15
screen = pygame.display.set_mode((WIDTH + board.ADD_WIDTH, HEIGHT))
pygame.display.set_caption("GAME CARO")
clock = pygame.time.Clock()


menu = Menu(screen, board)


class Game:
    '''
    Lớp Game quản lý trạng thái và logic của trò chơi cờ caro.
    '''
    def __init__(self, screen, board_size):
        '''
        Khởi tạo trạng thái của trò chơi
        '''
        self.screen = screen
        self.board = Board(board_size)
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player_index = 0
        self.winner = None
        self.timers = {0: self.players[0].time, 1: self.players[1].time}
        self.menu = Menu(screen, self.board)
        self.sound_state = True
        self.TIME_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.TIME_EVENT, 1000)

    def reset_timer(self):
        '''
        Đặt lại thời gian cho người chơi
        '''
        self.timers = {0: self.players[0].time, 1: self.players[1].time}

    def increase_score(self, player):
        '''
        Tăng điểm cho người chơi chiến thắng
        '''
        player.score += 1

    def switch_player(self):
        '''
        Chuyển lượt chơi cho người chơi khác
        '''
        self.current_player_index = 1 - self.current_player_index
        self.reset_timer()

    def get_current_player(self):
        '''
        Lấy người chơi hiện tại
        '''
        return self.players[self.current_player_index]

    def handle_click(self, row, col):
        '''
        Xử lý sự kiện click chuột
        '''
        player = self.get_current_player()
        if self.board.temp_mark == (row, col):
            if self.board.update(row, col, player.symbol):
                self.board.temp_mark = None
                self.draw_on_board(self.screen)
                pygame.display.update()
                if self.board.check_win():
                    if self.menu.state_board_volume:
                        sound_win.play()
                    pygame.time.wait(1000)
                    self.winner = player
                    self.increase_score(self.winner)
                    result = self.menu.show_winner(self.winner.name)
                    if result == "PLAY":
                        self.reset()
                    elif result == "MENU":
                        sound_win.stop()
                        self.run()
                        return True

                elif self.board.is_full():
                    self.reset()

                else:
                    self.switch_player()
        else:
            self.board.temp_mark = (row, col)
        return False

    def check_time(self):
        '''
        Kiểm tra thời gian chơi còn lại của người chơi
        '''
        if self.winner:
            self.timers[self.current_player_index] = self.players[
                self.current_player_index
            ].time
        if not self.winner:
            self.timers[self.current_player_index] -= 1
            if self.timers[self.current_player_index] <= 0:
                self.switch_player()

    def draw_on_board(self, screen):
        '''
        Vẽ trạng thái của bảng chơi và thông tin người chơi lên màn hình 
        '''
        self.board.draw_board(screen)
        self.board.draw_info_player(
            screen,
            self.players,
            self.get_current_player().symbol,
            self.timers,
        )
        if not self.winner:
            self.menu.draw_button_in_board()

    def reset(self):
        '''
        Đặt lại trạng thái của trò chơi
        '''
        self.board = Board(self.board.size)
        self.current_player_index = 0
        self.winner = None
        self.reset_timer()

    def game_board(self, board_size):
        '''
        Chạy trò chơi cờ caro
        '''
        self.__init__(self.screen, board_size)
        pause = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.TIME_EVENT and not pause:
                    self.check_time()
                if event.type == pygame.MOUSEBUTTONDOWN and not pause:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // self.board.SQ_SIZE, x // self.board.SQ_SIZE
                    if 0 <= row < self.board.size and 0 <= col < self.board.size:
                        if self.menu.state_board_volume:
                            sound_click_X_O.play()
                        self.handle_click(row, col)

                    if board_buttons[2].checkForInput((x, y)):
                        pause = True
                        self.pause_game = True
                        if self.menu.confirm_quit():
                            self.run()
                            return
                        else:
                            pause = False

                    if self.menu.state_board_volume:
                        if board_buttons[0].checkForInput((x, y)):
                            self.menu.state_board_volume = False
                            self.sound_state = False

                    else:
                        if board_buttons[1].checkForInput((x, y)):
                            self.menu.state_board_volume = True
                            self.sound_state = True

            self.draw_on_board(self.screen)
            board_buttons = self.menu.draw_button_in_board()
            pygame.display.update()
            clock.tick(60)

    def show_option_menu(self):
        '''
        Hiển thị menu tùy chọn
        '''
        while True:
            option_buttons = self.menu.draw_option_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sound_click.play()
                    if option_buttons[0].checkForInput(pygame.mouse.get_pos()):
                        self.choose_grid()
                    if option_buttons[1].checkForInput(pygame.mouse.get_pos()):
                        self.show_help()
                    if option_buttons[2].checkForInput(pygame.mouse.get_pos()):
                        self.run()

            pygame.display.update()
            clock.tick(60)

    def show_help(self):
        '''
        Hiển thị hướng dẫn luật chơi cờ caro
        '''
        while True:
            help_buttons = self.menu.show_help_button()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sound_click.play()
                    if help_buttons[0].checkForInput(pygame.mouse.get_pos()):
                        self.show_option_menu()
            pygame.display.update()
            clock.tick(60)

    def choose_grid(self):
        '''
        Chọn kích thước bàn cờ
        '''
        global board_size
        while True:
            grid_buttons = self.menu.draw_choose_grid()
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
        '''
        Chạy trò chơi
        '''
        if not pygame.mixer.get_busy():
            sound_menu.play(-1)
        while True:
            main_menu_buttons = self.menu.draw_main_menu()
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
                        self.show_option_menu()
                        return
                    if main_menu_buttons[2].checkForInput(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()

                    if self.menu.state_menu_volume:
                        if main_menu_buttons[3].checkForInput(pygame.mouse.get_pos()):
                            self.menu.state_menu_volume = False
                            sound_menu.stop()
                    else:
                        if main_menu_buttons[4].checkForInput(pygame.mouse.get_pos()):
                            self.menu.state_menu_volume = True
                            sound_menu.play(-1)

            pygame.display.update()
            clock.tick(60)


if __name__ == "__main__":
    game = Game(screen, board_size)
    game.run()

