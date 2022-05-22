
from pygame import *


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('Background.jpg'), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

game = True
while game:
	for i in event.get():
		if i.type == QUIT:
			game = False

	window.blit(background, (0, 0))
	display.update()