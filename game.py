from player import Player
from board import Board

class Game:
    def __init__(self):
        '''
        Khởi tạo game với bảng chơi, danh sách người chơi và các thuộc tính cần thiết
        '''
        self.board=Board()
        self.players=[Player('Player 1','X'),Player('Player 2','O')]
        self.current_player_index=0
        self.winner=None
    def switch_player(self):
        '''
        Chuyển đổi lượt chơi giữa 2 người chơi và cập nhật thông tin người chơi hiện tại
        '''
        self.current_player_index=1-self.current_player_index

    def get_current_player(self):   
        '''
        Lấy người chơi hiện tại
        '''
        return self.players[self.current_player_index]
    

    
    def handle_click(self,row,col):
        '''
        Xử lí sự kiện khi nhấn vào bảng chơi
        '''
        player=self.get_current_player()
        if self.board.temp_mark==(row,col):
            if self.board.update(row,col,player.symbol):
                self.board.temp_mark=None
                if self.board.check_win():
                    
                    self.winner=player                  
                    return True
                self.switch_player()
        else:
            self.board.temp_mark=(row,col)
        return False
    
    def handle_time(self):
        '''
        Xử lí thời gian chơi
        '''
        player=self.get_current_player()
        player.time-=1
        if player.time==0:
            self.switch_player()
            player.time=5
    def update_time(self):
        '''
        Cập nhật thời gian còn lại của người chơi hiện tại
        '''
        self.get_current_player().time-=1
    def reset_time(self):
        '''
        Reset thời gian còn lại của người chơi hiện tại
        '''
        self.get_current_player().time=5

    def draw_on_board(self,screen):
        '''
        Vẽ game lên màn hình
        '''
        self.board.draw_board(screen)
        self.board.draw_player(screen,self.players,self.get_current_player().symbol)
        
        


    def reset(self):
        
        '''
        Reset game để bắt đầu một ván mới
        '''
        self.board=Board()
        self.current_player_index=0
        self.winner=None