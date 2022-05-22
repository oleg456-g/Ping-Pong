
from pygame import *


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('Background.jpg'), (win_width, win_height))


game = True
while game:
	for i in event.get():
		if i.type == QUIT:
			game = False

	window.blit(background, (0, 0))
	display.update()
