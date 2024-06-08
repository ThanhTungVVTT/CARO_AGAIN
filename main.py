# import pygame
# import math
# import time

# # Khởi tạo Pygame
# pygame.init()

# # Thiết lập kích thước màn hình và các thông số
# screen = pygame.display.set_mode((200, 200))
# pygame.display.set_caption("Countdown Timer")

# # Thiết lập màu sắc
# BLUE = (0, 122, 255)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)

# # Thiết lập font
# font = pygame.font.SysFont(None, 36)

# def draw_timer(screen, time_left, total_time):
#     # Vẽ nền xanh
#     screen.fill(BLUE)

#     # Tính toán góc cho phần màu xanh lá
#     angle = 360 * (time_left / total_time)
#     end_angle = 360 - angle

#     # Vẽ hình tròn nền trắng
#     pygame.draw.circle(screen, WHITE, (100, 100), 50)

#     # Vẽ phần hình tròn màu xanh lá biểu thị thời gian còn lại
#     rect = pygame.Rect(50, 50, 100, 100)
#     pygame.draw.arc(screen, GREEN, rect, math.radians(270), math.radians(270 + angle), 50)

#     # Vẽ đường viền bên ngoài
#     pygame.draw.circle(screen, GREEN, (100, 100), 50, 2)

#     # Tính toán phút và giây từ thời gian còn lại
#     minutes, seconds = divmod(int(time_left), 60)
#     time_text_str = f"{minutes:02}:{seconds:02}"

#     # Hiển thị thời gian còn lại dưới dạng văn bản
#     time_text = font.render(time_text_str, True, WHITE)
#     text_rect = time_text.get_rect(center=(100, 160))
#     screen.blit(time_text, text_rect)

# def main():
#     running = True
#     total_time = 30  # Tổng thời gian tính bằng giây
#     start_time = time.time()  # Lưu thời điểm bắt đầu

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         # Tính toán thời gian còn lại
#         elapsed_time = time.time() - start_time
#         time_left = total_time - elapsed_time

#         if time_left <= 0:
#             time_left = 0
#             running = False  # Kết thúc vòng lặp khi thời gian hết

#         # Vẽ bộ đếm thời gian
#         draw_timer(screen, time_left, total_time)

#         # Cập nhật màn hình
#         pygame.display.flip()

#         # Giới hạn FPS
#         pygame.time.Clock().tick(60)

#     pygame.quit()

# if __name__ == "__main__":
#     main()
time={0:30,1:20}
x=time[0]
