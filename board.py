from player import Player
import pygame
from config import *



class Board:
    def __init__(self,size=15):
        '''
        Khởi tạo bàn cờ với kích thước mặc định 15x15,grid là ma trận để lưu trữ các dấu X,O
        '''
        self.size=size
        self.grid=[['' for _ in range(size)] for _ in range(size)]
        self.temp_mark=None
        self.last_mark=None
        self.SQ_SIZE=WIDTH//self.size
        self.ADD_WIDTH=300
    def draw_board(self,screen):
        '''
        Vẽ bảng chơi lên màn hình
        '''
        screen.fill(WHITE)
        for row in range(self.size):
            for col in range(self.size):
                rect=pygame.Rect(col*self.SQ_SIZE,row*self.SQ_SIZE,self.SQ_SIZE,self.SQ_SIZE)
                pygame.draw.rect(screen,(159,161,165),rect,1)
                if self.temp_mark==(row,col):
                    row,col=self.temp_mark
                    pygame.draw.rect(screen,HIGHTLIGHT_COLOR,(col*self.SQ_SIZE+1,row*self.SQ_SIZE+1,self.SQ_SIZE-2,self.SQ_SIZE-2),0)
                elif self.last_mark==(row,col):
                    pygame.draw.rect(screen,HIGHTLIGHT_COLOR,(col*self.SQ_SIZE+1,row*self.SQ_SIZE+1,self.SQ_SIZE-2,self.SQ_SIZE-2),0)
                if self.grid[row][col]=='X':
                    screen.blit(X_image,(col*self.SQ_SIZE+self.SQ_SIZE//2-X_image.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-X_image.get_height()//2))
                elif self.grid[row][col]=='O':
                    screen.blit(O_image,(col*self.SQ_SIZE+self.SQ_SIZE//2-O_image.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-O_image.get_height()//2))
        if self.check_win():
            winning_squares=self.check_win()
            self.draw_when_win(screen,winning_squares)


    def draw_when_win(self,screen,winning_squares):
        for row,col in winning_squares:
            if self.grid[row][col]=='X':
                pygame.draw.rect(screen,X_COLOR_WIN,(col*self.SQ_SIZE+1,row*self.SQ_SIZE+1,self.SQ_SIZE-2,self.SQ_SIZE-2))
                screen.blit(X_image_win,(col*self.SQ_SIZE+self.SQ_SIZE//2-X_image.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-X_image.get_height()//2))
            else:
                pygame.draw.rect(screen,O_COLOR_WIN,(col*self.SQ_SIZE+1,row*self.SQ_SIZE+1,self.SQ_SIZE-2,self.SQ_SIZE-2))
                screen.blit(O_image_win,(col*self.SQ_SIZE+self.SQ_SIZE//2-O_image.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-O_image.get_height()//2))
    
    def draw_player(self,screen,player,current_player_symbol,timers):
        '''
        Vẽ thông tin người chơi lên màn hình
        '''
        for i,player in enumerate(player):
            y_offset=30+i*100

            font=pygame.font.SysFont(None, 36)
            name_text=font.render(f"{player.name}",True,(0,0,0))
            screen.blit(name_text,(WIDTH+30,y_offset))
            symbol_text=font.render(f"Symbol: {player.symbol}",True,(0,0,0))
            screen.blit(symbol_text,(WIDTH+30,y_offset+30))

            # thời gian còn lại
            elapsed_time=timers[i]
            time_text=font.render(f"Time: {elapsed_time} s",True,(0,0,0))
            screen.blit(time_text,(WIDTH+30,y_offset+60))

            if player.symbol==current_player_symbol:
                pygame.draw.rect(screen,(255,0,0),(WIDTH+25,y_offset-5,OFFSET-30,95),2)

    def update(self,row,col,player_symbol):
        '''
        Cập nhật bảng với ký hiệu của người chơi tại vị trí chỉ định
        '''
        if self.grid[row][col]=='':
            self.grid[row][col]=player_symbol
            self.last_mark=(row,col)
            return True
        return False
    
    def check_win(self):
        '''
        Kiểm tra xem có người chơi nào thắng chưa
        '''
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col]!='':
                    winning_squares=self.check_five(row,col)
                    if winning_squares:
                        return winning_squares
                    
        return []
    
    def check_five(self,row,col):
        '''
        Kiểm tra xem có 5 ký hiệu liên tiếp theo hàng ngang, hàng dọc,đường chéo không
        '''
        directions=[(0,1),(1,0),(1,1),(1,-1)]
        for d in directions:
            count,winning_squares=self.count_direction(row,col,d)
            if count>=5:
                return winning_squares
        return []        

    def count_direction(self,row,col,direction):
        '''
        Đếm số lượng ký hiệu liên tiếp theo một hướng nhất định
        '''
        count=1
        winning_squares=[(row,col)]
        for i in range(1,self.size):
            new_row=row+i*direction[0]
            new_col=col+i*direction[1]
            if 0<=new_row<self.size and 0<=new_col<self.size and self.grid[new_row][new_col]==self.grid[row][col]:
                count+=1
                winning_squares.append((new_row,new_col))
            else:
                break
        for i in range(1,self.size):
            new_row=row-i*direction[0]
            new_col=col-i*direction[1]
            if 0<=new_row<self.size and 0<=new_col<self.size and self.grid[new_row][new_col]==self.grid[row][col]:
                count+=1
                winning_squares.append((new_row,new_col))
            else:
                break
        return count,winning_squares
