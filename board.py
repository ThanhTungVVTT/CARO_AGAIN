import pygame
from config import *



class Board:
    '''
    Lớp Board đại diện cho bảng chơi cờ caro ( vẽ bảng, thông tin người chơi, kiểm tra thắng thua)
    '''
    def __init__(self,size=15):
        '''
        Khởi tạo bảng chơi với kích thước cho trước
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
        '''
        Vẽ lại bảng chơi khi có người chơi thắng
        '''
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

    def draw_info_player(self,screen,player,current_player_symbol,timers):
        '''
        Vẽ thông tin người chơi lên màn hình
        '''
        for i,player in enumerate(player):
            avatar_pos=(WIDTH+150,80+i*250)
            elapsed_time=timers[i]
        
            time_text=get_font(20,"Designer","otf").render(f"Time left: {elapsed_time}",True,BLACK)
            score_text=get_font(20,"Designer","otf").render(f"Score: {player.score}",True,BLACK)

            if player.symbol=="X":
                avatar_X_pos=avatar_X.get_rect(center=avatar_pos)
                screen.blit(avatar_X,avatar_X_pos)
                
                group_X_pos=(avatar_X_pos.right-group_X.get_width(),avatar_X_pos.bottom-group_X.get_height())
                screen.blit(group_X,group_X_pos)
                
                time_text_center=(avatar_X_pos.centerx,avatar_X_pos.bottom+15)
                time_text_rect=time_text.get_rect(midtop=time_text_center)
                screen.blit(time_text,time_text_rect)
                
                score_text_center=(avatar_X_pos.centerx,avatar_X_pos.bottom+45)
                score_text_rect=score_text.get_rect(midtop=score_text_center)
                screen.blit(score_text,score_text_rect)

            else:
                avatar_O_pos=avatar_O.get_rect(center=avatar_pos)
                screen.blit(avatar_O,avatar_O_pos)
                
                group_O_pos=(avatar_O_pos.right-group_O.get_width(),avatar_O_pos.bottom-group_O.get_height())
                screen.blit(group_O,group_O_pos)
                
                time_text_center=(avatar_O_pos.centerx,avatar_O_pos.bottom+15)
                time_text_rect=time_text.get_rect(midtop=time_text_center)
                screen.blit(time_text,time_text_rect)

                score_text_center=(avatar_O_pos.centerx,avatar_O_pos.bottom+45)
                score_text_rect=score_text.get_rect(midtop=score_text_center)
                screen.blit(score_text,score_text_rect)

            if player.symbol == current_player_symbol:
                ARROW_SIZE=35
                if player.symbol == "X":
                    arrow_pos = (avatar_X_pos.left - ARROW_SIZE, avatar_X_pos.centery)
                else:
                    arrow_pos = (avatar_O_pos.left - ARROW_SIZE, avatar_O_pos.centery)
                
                arrow_shape = [
                    (arrow_pos[0], arrow_pos[1]),
                    (arrow_pos[0] -25, arrow_pos[1] - 20),
                    (arrow_pos[0] -25, arrow_pos[1] + 20)
                ]

                pygame.draw.polygon(screen, WHITE, arrow_shape)
                  
    def is_full(self):
        '''
        Kiểm tra xem bảng đã đầy chưa
        '''
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col]=='':
                    return False
        return True

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
        Kiểm tra xem số lượng ký hiệu liên tiếp theo một hướng nhất định có đủ để thắng chưa
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
