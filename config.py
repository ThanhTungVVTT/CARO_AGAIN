import pygame

# Định nghĩa các màu ( cho dễ nhìn và sử dụng )
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
HIGHTLIGHT_COLOR=(255,234,167)
X_COLOR_WIN=(52,87,154)
O_COLOR_WIN=(187,33,41)

# Định nghĩa các thông số cần thiết cho bảng chơi
WIDTH=525
HEIGHT=525
OFFSET=200


# tải hình ảnh cho X,O
X_image=pygame.image.load('assets/images/X.png')
O_image=pygame.image.load('assets/images/O.png')
X_image_win=pygame.image.load('assets/images/X_win.png')
O_image_win=pygame.image.load('assets/images/O_win.png')