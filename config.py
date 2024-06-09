import pygame
pygame.init()
# Định nghĩa các màu ( cho dễ nhìn và sử dụng )
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
BG_BOARD=(0,120,255)
HIGHTLIGHT_COLOR=(255,234,167)
X_COLOR_WIN=(52,87,154)
O_COLOR_WIN=(187,33,41)

# Định nghĩa các thông số cần thiết cho bảng chơi
WIDTH=700
HEIGHT=700
OFFSET=200


# tải hình ảnh cho X,O
#15x15
X_image_15x15=pygame.image.load('assets/images/X_15x15.png')
O_image_15x15=pygame.image.load('assets/images/O_15x15.png')
X_image_win_15x15=pygame.image.load('assets/images/X_WIN_15X15.png')
O_image_win_15x15=pygame.image.load('assets/images/O_WIN_15X15.png')
#7x7
X_image_7x7=pygame.image.load('assets/images/X_7x7.png')
O_image_7x7=pygame.image.load('assets/images/O_7x7.png')
X_image_win_7x7=pygame.image.load('assets/images/X_WIN_7X7.png')
O_image_win_7x7=pygame.image.load('assets/images/O_WIN_7X7.png')
#3x3
X_image_3x3=pygame.image.load('assets/images/X_3x3.png')
O_image_3x3=pygame.image.load('assets/images/O_3x3.png')
X_image_win_3x3=pygame.image.load('assets/images/X_WIN_3X3.png')
O_image_win_3x3=pygame.image.load('assets/images/O_WIN_3X3.png')

# tải hình ảnh cho background, play, options, quit
back_ground_image=pygame.image.load('assets/images/Background.png')
font=pygame.font.Font('assets/fonts/font.ttf',50)
image_play=pygame.image.load('assets/images/Play Rect.png')
image_options=pygame.image.load('assets/images/Options Rect.png')
image_quit=pygame.image.load('assets/images/Quit Rect.png')

volume_image_on=pygame.image.load('assets/images/volume_on.png')
volume_image_on=pygame.transform.scale(volume_image_on,(50,50))
volume_image_off=pygame.image.load('assets/images/volume_off.png')

sound_click_X_O=pygame.mixer.Sound('assets/sounds/click_X_O_sound.wav')
sound_win=pygame.mixer.Sound('assets/sounds/sound_win.mp3')
sound_click=pygame.mixer.Sound('assets/sounds/mouse_click.wav')
sound_menu=pygame.mixer.Sound('assets/sounds/music_loop_6.mp3')

avatar_O=pygame.image.load('assets/images/avatar_O.png')
avatar_O=pygame.transform.scale(avatar_O,(120,120))
avatar_X=pygame.image.load('assets/images/avatar_X.png')
avatar_X=pygame.transform.scale(avatar_X,(120,120))

group_X=pygame.image.load('assets/images/Group 330.png')

group_O=pygame.image.load('assets/images/Group O.png')
board_3x3=pygame.image.load('assets/images/3x3_board.png')
board_7x7=pygame.image.load('assets/images/7x7_board.png')
board_15x15=pygame.image.load('assets/images/15x15_board.png')
def get_font(size):
    return pygame.font.Font("assets/fonts/font.ttf", size)