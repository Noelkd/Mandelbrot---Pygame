from __future__ import division

import pygame
import sys

def pixel(surface, color, pos):
    pygame.draw.line(surface, color, pos, pos)

def exit_game():
	sys.exit()

def run_game():
	BG_COLOR = 0, 0, 0
	PX_COLOR = 225, 200, 200
	
	clock = pygame.time.Clock()
	WINDOW_HEIGHT = 480
	WINDOW_WIDTH = 640
	MAX_ITERTIONS = 30
	pygame.init()
	screen = pygame.display.set_mode(
							(WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

	MinRe = -2.0
	MaxRe = 1.0
	MinIm = -1.2
	MaxIm = MinIm + (MaxRe-MinRe) * WINDOW_HEIGHT / WINDOW_WIDTH

	Re_factor = (MaxRe - MinRe) / (WINDOW_WIDTH - 1)
	Im_factor = (MaxIm - MinIm) / (WINDOW_HEIGHT - 1)

	c_re_func = lambda x: MinRe + x * Re_factor
	c_im_func = lambda y: MaxIm - y * Im_factor

	for y in range(1, WINDOW_HEIGHT+1):
		c_im = c_im_func(y)
		#print "c_im:" + str(c_im)
		for x in range(1, WINDOW_WIDTH+1):
			c_re = c_re_func(x)
			#print "c_re:" + str(c_re) 
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

				pixel(screen,PX_COLOR,(x, y))
				pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game()
		pygame.display.flip()


if __name__ == "__main__":
	run_game()