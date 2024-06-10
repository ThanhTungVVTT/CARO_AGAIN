import pygame
import pygame.freetype  # Import the freetype module for font rendering

pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Luật Chơi CARO")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_COLOR = WHITE

# Khởi tạo font
pygame.font.init()
font = pygame.freetype.Font(None, 24)  # Font mặc định, kích thước 24

# Văn bản dài cần hiển thị
instructions = """
Place the number of pieces (depending on the grid type) 
   in a column, a row, or diagonally to win the game.

                Grid 3x3: 3 pieces
                Grid 7x7: 4 pieces
                Grid 15x15: 5 pieces
"""

# Chia văn bản thành các đoạn nhỏ
def split_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''
    
    for word in words:
        test_line = current_line + word + ' '
        if font.get_rect(test_line).width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '
    
    lines.append(current_line)  # Thêm dòng cuối cùng
    return lines

def draw_text(screen, text, pos, font, color=WHITE, max_width=WIDTH-40):
    lines = split_text(text, font, max_width)
    x, y = pos
    for line in lines:
        font.render_to(screen, (x, y), line, color)
        y += font.get_sized_height() + 5  # Thêm khoảng cách giữa các dòng

running = True
while running:
    screen.fill(BLACK)
    
    # Vẽ văn bản hướng dẫn
    draw_text(screen, instructions, (20, 20), font, FONT_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
