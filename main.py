import pygame
import math
import time
from config import *

class CountdownTimer:
    def __init__(self, total_time=30, position=(100, 100)):
        """
        Khởi tạo CountdownTimer với tổng thời gian và vị trí cụ thể.
        :param total_time: Tổng thời gian đếm ngược (tính bằng giây).
        :param position: Vị trí trung tâm của bộ đếm thời gian.
        """
        self.total_time = total_time
        self.start_time = time.time()
        self.position = position
        self.time_left = total_time
        self.font = get_font(15)
        self.state_time = False
        self.paused = False
        self.pause_start_time = 0
        self.accumulated_pause_time = 0
        self.pause_game=False
        
        # Thiết lập màu sắc
        self.BLUE = (0, 122, 255)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.BLACK = (0, 0, 0)

    def update(self):
        """
        Cập nhật thời gian còn lại.
        """
        if not self.paused:
            elapsed_time = time.time() - self.start_time - self.accumulated_pause_time
            self.time_left = self.total_time - elapsed_time
            if self.time_left < 0:
                self.time_left = 0

    def reset(self):
        self.start_time = time.time()
        self.time_left = self.total_time
        self.accumulated_pause_time = 0

    def pause(self):
        if not self.paused:
            self.paused = True
            self.pause_start_time = time.time()

    def resume(self):
        if self.paused:
            self.paused = False
            self.accumulated_pause_time += time.time() - self.pause_start_time

    def draw(self, screen):
        """
        Vẽ bộ đếm thời gian lên màn hình.
        :param screen: Màn hình Pygame để vẽ bộ đếm thời gian.
        """
        if self.pause_game:
            self.pause()
        else:
            self.resume()
        
        self.update()

        # Tính toán góc cho phần màu xanh lá
        if self.time_left > 0:
            angle = 360 * (self.time_left / self.total_time)
        else:
            angle = 0

        clock_radius = 40
        # Vẽ hình tròn nền trắng
        pygame.draw.circle(screen, self.WHITE, self.position, clock_radius)

        # Vẽ phần hình tròn màu xanh lá biểu thị thời gian còn lại
        if self.time_left > 0:
            rect = pygame.Rect(self.position[0] - clock_radius, self.position[1] - clock_radius, clock_radius * 2, clock_radius * 2)
            start_angle = 270  # Bắt đầu từ vị trí 12 giờ (270 độ)
            end_angle = 270 + angle  # Góc kết thúc tương ứng với thời gian còn lại
            pygame.draw.arc(screen, self.GREEN, rect, math.radians(start_angle), math.radians(end_angle), clock_radius)
        
        # Vẽ đường viền bên ngoài
        pygame.draw.circle(screen, self.GREEN, self.position, clock_radius, 2)

        # Tính toán phút và giây từ thời gian còn lại
        minutes, seconds = divmod(int(self.time_left), 60)
        time_text_str = f"{minutes:02}:{seconds:02}"
        # Hiển thị thời gian còn lại dưới dạng văn bản
        time_text = self.font.render(time_text_str, True, self.BLACK)
        text_rect = time_text.get_rect(center=(self.position[0], self.position[1] + 55))
        screen.blit(time_text, text_rect)


