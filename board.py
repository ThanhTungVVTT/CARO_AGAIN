from player import Player
from timer_countdown import CountdownTimer
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
        self.time1=CountdownTimer(total_time=30,position=(100,100))
        self.time2=CountdownTimer(total_time=30,position=(100,100))
    def draw_board(self,screen):
        '''
        Vẽ bảng chơi lên màn hình
        '''
        screen.fill(WHITE)
        pygame.draw.rect(screen, BG_BOARD, (WIDTH, 0, self.ADD_WIDTH, HEIGHT))
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
                    if self.size==3:
                        screen.blit(X_image_3x3,(col*self.SQ_SIZE+self.SQ_SIZE//2-X_image_3x3.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-X_image_3x3.get_height()//2))
                    elif self.size==7:
                        screen.blit(X_image_7x7,(col*self.SQ_SIZE+self.SQ_SIZE//2-X_image_7x7.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-X_image_7x7.get_height()//2))
                    elif self.size==15:
                        screen.blit(X_image_15x15,(col*self.SQ_SIZE+self.SQ_SIZE//2-X_image_15x15.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-X_image_15x15.get_height()//2))
                elif self.grid[row][col]=='O':
                    if self.size==3:
                        screen.blit(O_image_3x3,(col*self.SQ_SIZE+self.SQ_SIZE//2-O_image_3x3.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-O_image_3x3.get_height()//2))
                    elif self.size==7:
                        screen.blit(O_image_7x7,(col*self.SQ_SIZE+self.SQ_SIZE//2-O_image_7x7.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-O_image_7x7.get_height()//2))
                    elif self.size==15:
                        screen.blit(O_image_15x15,(col*self.SQ_SIZE+self.SQ_SIZE//2-O_image_15x15.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-O_image_15x15.get_height()//2))
        if self.check_win():
            winning_squares=self.check_win()
            self.draw_when_win(screen,winning_squares)


    def draw_when_win(self,screen,winning_squares):
        for row,col in winning_squares:
            if self.grid[row][col]=='X':
                pygame.draw.rect(screen,X_COLOR_WIN,(col*self.SQ_SIZE+1,row*self.SQ_SIZE+1,self.SQ_SIZE-2,self.SQ_SIZE-2))
                if self.size==3:
                    screen.blit(X_image_win_3x3,(col*self.SQ_SIZE+self.SQ_SIZE//2-X_image_win_3x3.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-X_image_win_3x3.get_height()//2))
                elif self.size==7:
                    screen.blit(X_image_win_7x7,(col*self.SQ_SIZE+self.SQ_SIZE//2-X_image_win_7x7.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-X_image_win_7x7.get_height()//2))
                elif self.size==15:
                    screen.blit(X_image_win_15x15,(col*self.SQ_SIZE+self.SQ_SIZE//2-X_image_win_15x15.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-X_image_win_15x15.get_height()//2))
            else:
                pygame.draw.rect(screen,O_COLOR_WIN,(col*self.SQ_SIZE+1,row*self.SQ_SIZE+1,self.SQ_SIZE-2,self.SQ_SIZE-2))
                if self.size==3:
                    screen.blit(O_image_win_3x3,(col*self.SQ_SIZE+self.SQ_SIZE//2-O_image_win_3x3.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-O_image_win_3x3.get_height()//2))
                elif self.size==7:
                    screen.blit(O_image_win_7x7,(col*self.SQ_SIZE+self.SQ_SIZE//2-O_image_win_7x7.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-O_image_win_7x7.get_height()//2))
                elif self.size==15:
                    screen.blit(O_image_win_15x15,(col*self.SQ_SIZE+self.SQ_SIZE//2-O_image_win_15x15.get_width()//2,row*self.SQ_SIZE+self.SQ_SIZE//2-O_image_win_15x15.get_height()//2))
    
    def draw_player(self,screen,player,current_player_symbol,timers):
        '''
        Vẽ thông tin người chơi lên màn hình
        '''

        for i,player in enumerate(player):
            avatar_pos=(WIDTH+30,50+i*150)
            
            if player.symbol=="X":
                screen.blit(avatar_X,avatar_pos)
                avatar_X_pos=(avatar_pos[0]+avatar_X.get_width(),avatar_pos[1]+avatar_X.get_height()//2)
                group_X_pos=(avatar_pos[0]+avatar_X.get_width()-30,avatar_pos[1]+avatar_X.get_height()-30)
                screen.blit(group_X,group_X_pos)
                self.time1.position=(avatar_X_pos[0]+70,avatar_X_pos[1])
                self.time1.total_time=timers[i]
                self.time1.draw(screen)
            else:
                screen.blit(avatar_O,avatar_pos)
                avatar_O_pos=(avatar_pos[0]+avatar_O.get_width(),avatar_pos[1]+avatar_O.get_height()//2)
                group_O_pos=(avatar_pos[0]+avatar_O.get_width()-30,avatar_pos[1]+avatar_O.get_height()-30)
                screen.blit(group_O,group_O_pos)
                self.time2.position=(avatar_O_pos[0]+70,avatar_O_pos[1])
                self.time2.total_time=timers[i]
                self.time2.draw(screen)

            if player.symbol==current_player_symbol:         
                if player.symbol=="X":        
                    self.time1.state_time=True
                    self.time2.state_time=False
                    self.time2.reset()
                        

                    
                else:
                    self.time1.state_time=False
                    self.time2.state_time=True
                    self.time1.reset()
                    
                      


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
                    winning_squares=self.check_cell(row,col)
                    if winning_squares:
                        return winning_squares
                    
        return []
    
    def check_cell(self,row,col):
        '''
        Kiểm tra xem có 5 ký hiệu liên tiếp theo hàng ngang, hàng dọc,đường chéo không
        '''
        if self.size==15:
            win_count=5
        elif self.size==7:
            win_count=4
        elif self.size==3:
            win_count=3
        else:
            win_count=5
        directions=[(0,1),(1,0),(1,1),(1,-1)]
        for d in directions:
            count,winning_squares=self.count_direction(row,col,d)
            if count>=win_count:
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
