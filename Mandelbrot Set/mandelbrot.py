from __future__ import division

import pygame
import sys
import Image
import os

cwd = os.getcwd()

def exit_game():
	sys.exit()

def save_image(image):
	image.save(cwd+"\\tmp.BMP", "BMP")

def run_game():

	WINDOW_HEIGHT = 480
	WINDOW_WIDTH = 640
	pygame.init()
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
	pygame.display.set_caption("MENDEL VIEWER")
	loading_screen = pygame.Surface(screen.get_size())
	loading_screen = loading_screen.convert()
	loading_screen.fill((0, 0, 0))

	font = pygame.font.Font(None, 36)
	text = font.render("Loading....", 1, (225, 225, 225))
	textpos = text.get_rect()
	textpos.centerx = WINDOW_WIDTH / 2
	textpos.centery = WINDOW_HEIGHT / 2
	
	loading_screen.blit(text, textpos)
	screen.blit(loading_screen,(0,0))
	pygame.display.flip()
	
	MAX_ITERTIONS = 30
	MinRe = -2.0
	MaxRe = 1.0
	MinIm = -1.2
	MaxIm = MinIm + (MaxRe-MinRe) * WINDOW_HEIGHT / WINDOW_WIDTH

	Re_factor = (MaxRe - MinRe) / (WINDOW_WIDTH - 1)
	Im_factor = (MaxIm - MinIm) / (WINDOW_HEIGHT - 1)

	get_c_re = lambda x: MinRe + x * Re_factor
	get_c_im = lambda y: MaxIm - y * Im_factor

	image = Image.new("RGB",(WINDOW_WIDTH, WINDOW_HEIGHT), "black")

	for y in range(1, WINDOW_HEIGHT):
		c_im = get_c_im(y)

		for x in range(1, WINDOW_WIDTH):
			c_re = get_c_re(x)
			Z_re = c_re
			Z_im = c_im
			isInside = True

			for n in range(1, MAX_ITERTIONS):
				Z_re2 = Z_re * Z_re
				Z_im2 = Z_im * Z_im

				if (Z_re2 + Z_im2 > 4):
					isInside = False
					break

				Z_im = 2 * Z_re * Z_im + c_im
				Z_re = Z_re2 - Z_im2 + c_re

			if isInside:
				image.putpixel((x, y), (int(255/n),255,255))
			else:
				image.putpixel((x, y), (int(225/n),0,0))

	
	image_surf = pygame.image.frombuffer(image.tostring(), image.size, image.mode)

	while True:

		screen.blit(image_surf,(0,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game()
		pygame.display.flip()


if __name__ == "__main__":
	run_game()