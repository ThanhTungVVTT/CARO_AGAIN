import pygame
pygame.init()

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
BG_BOARD=(0,120,255)
GRAY=(159,161,165)
BACKGROUND_MENU_BUTTON=(71,43,58)
TITLE_COLOR=(181,143,63)
BUTTON_COLOR="#d7fcd4"
HIGHTLIGHT_COLOR=(255,234,167)
X_COLOR_WIN=(52,87,154)
O_COLOR_WIN=(187,33,41)


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


back_ground_image=pygame.image.load('assets/images/Background.png')

volume_image_on=pygame.image.load('assets/images/volume_on.png')
volume_image_menu_on=pygame.image.load('assets/images/volume_on_menu.png')
volume_image_off=pygame.image.load('assets/images/volume_off.png')
volume_image_menu_off=pygame.image.load('assets/images/volume_off_menu.png')

home_image=pygame.image.load('assets/images/home.png')

sound_click_X_O=pygame.mixer.Sound('assets/sounds/click_X_O_sound.wav')
sound_win=pygame.mixer.Sound('assets/sounds/sound_win.mp3')
sound_click=pygame.mixer.Sound('assets/sounds/mouse_click.wav')
sound_menu=pygame.mixer.Sound('assets/sounds/music_loop_6.mp3')

avatar_O=pygame.image.load('assets/images/avatar_O.png')
avatar_O=pygame.transform.scale(avatar_O,(120,120))
avatar_X=pygame.image.load('assets/images/avatar_X.png')
avatar_X=pygame.transform.scale(avatar_X,(120,120))

group_X=pygame.image.load('assets/images/Group X.png')
group_O=pygame.image.load('assets/images/Group O.png')

board_3x3=pygame.image.load('assets/images/3x3_board.png')
board_7x7=pygame.image.load('assets/images/7x7_board.png')
board_15x15=pygame.image.load('assets/images/15x15_board.png')

help_image=pygame.image.load('assets/images/help.png')
help_image=pygame.transform.scale(help_image,(350,350))


def get_font(size,font_name,font_type):
    return pygame.font.Font(f"assets/fonts/{font_name}.{font_type}", size)


instructions=["Place the number of pieces (depending on the grid type)",
              "in a column, a row, or diagonally to win the game.",
              "Grid 3x3: 3 pieces",
              "Grid 7x7: 4 pieces",
              "Grid 15x15: 5 pieces"]

