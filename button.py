import pygame
pygame.init()


class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if not self.image:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image:
			self.highlight_image(pygame.mouse.get_pos(), screen)
		screen.blit(self.text, self.text_rect)

	def zoom_in_text(self,position,screen):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			text_1=self.text.copy()
			text_surf = pygame.transform.scale_by(text_1, 1.4)
			text_1=pygame.Surface((text_surf.get_width() + 8, text_surf.get_height() + 8),pygame.SRCALPHA,)
			text_1.fill((71,43,58,128))
			text_1.blit(text_surf,((text_1.get_width() - text_surf.get_width()) / 2,(text_1.get_height() - text_surf.get_height()) / 2),)
			screen.blit(text_1, text_surf.get_rect(center=(self.x_pos, self.y_pos)))
		else:
			screen.blit(self.text, self.text_rect)

	def highlight_image(self,position,screen):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			highlight_image=pygame.Surface((self.rect.width+15,self.rect.height+15),pygame.SRCALPHA)
			highlight_image.fill((240,228,212,128))
			highlight_image_rect=highlight_image.get_rect(center=(self.x_pos,self.y_pos))
			screen.blit(highlight_image,highlight_image_rect)
			screen.blit(self.image, self.rect)
		else:
			screen.blit(self.image, self.rect)
			
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
