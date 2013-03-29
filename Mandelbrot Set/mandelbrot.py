from __future__ import division

import pygame
import sys
import os

cwd = os.getcwd()

def exit_game():
	sys.exit()

def save_image(image):
	image.save(cwd+"\\tmp.BMP", "BMP")


def get_load_screen(screen_size, window_height, window_width):
	loading_screen = pygame.Surface(screen_size)
	loading_screen = loading_screen.convert()
	loading_screen.fill((0, 0, 0))

	font = pygame.font.Font(None, 36)
	text = font.render("Loading....", 1, (225, 225, 225))
	textpos = text.get_rect()
	textpos.centerx = window_width / 2
	textpos.centery = window_height / 2
	loading_screen.blit(text, textpos)
	return loading_screen


class MandelBrot(object):
	def __init__(self, window_height, window_width, max_iter, MinRe, MaxRe, MinIm):
		self.window_height = window_height
		self.window_width = window_width
		self.max_iter = max_iter
		self.MinRe = MinRe
		self.MaxRe = MaxRe
		self.MinIm = MinIm
		self.MaxIm = self.MinIm + (self.MaxRe-self.MinRe) * self.window_height / self.window_width
		self.Re_factor = (self.MaxRe - self.MinRe) / (self.window_width - 1)
		self.Im_factor = (self.MaxIm - self.MinIm) / (self.window_height - 1)
		self.get_c_re = lambda x: self.MinRe + x * self.Re_factor
		self.get_c_im = lambda y: self.MaxIm - y * self.Im_factor
		self.x_offset = 0
		self.y_offset = 0
	
	def recalc(self):
		self.MaxIm = self.MinIm + (self.MaxRe-self.MinRe) * self.window_height / self.window_width
		self.Re_factor = (self.MaxRe - self.MinRe) / (self.window_width - 1)
		self.Im_factor = (self.MaxIm - self.MinIm) / (self.window_height - 1)
		self.get_c_re = lambda x: self.MinRe + x * self.Re_factor
		self.get_c_im = lambda y: self.MaxIm - y * self.Im_factor
	
	
	def get_surface(self, surface):
		print self.Re_factor, self.Im_factor,self.MinRe,self.MaxRe
		self.recalc()
		for y in range(1+self.y_offset, self.window_height+self.y_offset):
			c_im = self.get_c_im(y)

			for x in range(1+self.x_offset, self.window_width+self.x_offset):
				c_re = self.get_c_re(x)
				Z_re = c_re
				Z_im = c_im
				isInside = True

				for n in range(1, self.max_iter):
					Z_re2 = Z_re * Z_re
					Z_im2 = Z_im * Z_im

					if (Z_re2 + Z_im2 > 4):
						isInside = False
						break

					Z_im = 2 * Z_re * Z_im + c_im
					Z_re = Z_re2 - Z_im2 + c_re

				if isInside:
					surface.fill((225,225,225),(x-self.x_offset,y-self.y_offset,x-self.x_offset,y-self.y_offset))

				else:
					surface.fill((int(225/n),1,0),(x-self.x_offset,y-self.y_offset,x-self.x_offset,y-self.y_offset))
		return surface



def run_game():

	WINDOW_HEIGHT = 480
	WINDOW_WIDTH = 640
	pygame.init()
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
	pygame.display.set_caption("MENDEL VIEWER")
	loading_screen = get_load_screen(screen.get_size(),WINDOW_HEIGHT,WINDOW_WIDTH)
	screen.blit(loading_screen,(0,0))
	pygame.display.flip()

	MAX_ITERTIONS = 30
	MinRe = -2.0
	MaxRe = 1.0
	MinIm = -1.2
	mandel_maker = MandelBrot(WINDOW_HEIGHT, WINDOW_WIDTH, MAX_ITERTIONS, MinRe, MaxRe, MinIm)
	surface = mandel_maker.get_surface(pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT)))
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game()
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
				mandel_maker.y_offset += 50
				surface = mandel_maker.get_surface(surface)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
				mandel_maker.y_offset -= 50
				surface = mandel_maker.get_surface(surface)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
				mandel_maker.x_offset -= 50
				surface = mandel_maker.get_surface(surface)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
				mandel_maker.x_offset += 50
				surface = mandel_maker.get_surface(surface)

		screen.blit(surface,(0,0))
		pygame.display.flip()
		pygame.time.wait(50)


if __name__ == "__main__":
	run_game()