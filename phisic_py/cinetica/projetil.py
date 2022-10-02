#---------------------------------------------
#   Author: Renan Campos
#   Github: github.com/ArandaCampos
#   Projéteis
#---------------------------------------------

import pygame
import math
import os
from base import Window, Menu

WIDTH, HEIGHT = 1200, 600
WHITE, BLACK, GRAY = (210, 210, 210), (0, 0, 0, 0.8), (108, 108, 108, .8)
ABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
IMG_PATH = os.path.join(ABS_PATH, 'sprites')

class Objeto:
	g = -9.807 		       	# Aceleração da gravidade (m/s^2)

	def __init__(self, h, velocity, angle):
		self.x = 0											# Posição Vertical (m)
		self.y = h													# Posição Horizontal (m)
		self.angle = angle
		self.v = velocity
		self.vy = velocity * math.sin(math.radians(angle))		# Velocidade Inicial eixo y
		self.vx = velocity * math.cos(math.radians(angle))		# Velocidade Inicial eixo x
		self.diameter = 20 			# Raio (m)
		self.menu = Menu(('clock.png', 'pointer.png', 'pointer.png', 'speedometer.png', 'speedometer.png', 'accelaration.png'))
		self.font = pygame.font.SysFont('Arial', 12)

		self.movements = []
		self.velocities = []
		self.position = 0
		self.interval = 0
		self.a = self.g
		self.SCALE = 0

	def draw(self, win):
		if self.position > 2:
			points = []
			for movement in self.movements[0: self.position + 1]:
				points.append(self.transform(movement))
			pygame.draw.lines(win, GRAY, False, points, 2)

		pygame.draw.circle(win, BLACK, self.transform(self.movements[self.position]), self.diameter)

		timer = self.font.render('{:.2f} s'.format(self.position * self.interval), True, BLACK)
		posx = self.font.render('{:.1f} m (x)'.format(self.movements[self.position][0]), True, BLACK)
		posy = self.font.render('{:.1f} m (y)'.format(self.movements[self.position][1]), True, BLACK)
		velx = self.font.render('{:.2f} Km/h (x)'.format(self.velocities[self.position][0]), True, BLACK)
		vely = self.font.render('{:.2f} Km/h (y)'.format(self.velocities[self.position][1]), True, BLACK)
		a = self.font.render('{:.2f} m/s² (y)'.format(self.a), True, BLACK)
		self.menu.draw(win, (timer, posx, posy, velx, vely, a))

	def transform(self, position):
		if not self.SCALE:
			xmax =  self.movements[-1][0]
			hmax = (math.pow(self.v, 2) * math.pow(math.sin(math.radians(self.angle)), 2)) / (-2 * self.g) + self.y
			if xmax / WIDTH >= hmax / HEIGHT:
				self.SCALE = (WIDTH - self.diameter - 50) / self.movements[-1][0]
			else:
				self.SCALE = (HEIGHT - self.diameter - 150) / hmax
		x, y = position
		return (x * self.SCALE + 25, HEIGHT - y * self.SCALE - self.diameter - 55)

	def vel(self, t):
		vx = self.vx * t
		vy = self.vy * t + self.g * math.pow(t, 2) / 2
		return vx, vy

	def movement(self, interval):
		x, y = self.x , self.y
		self.interval = interval
		time = 0
		while y >= 0:
			vx, vy = self.vel(time)
			x = self.x + vx
			y = self.y + vy
			time += interval
			self.movements.append((x, y))
			self.velocities.append((self.vx, self.vy + self.a * time))
		return len(self.movements)

	def update_position(self, frame):
		if frame < len(self.movements) and frame >= 0:
			self.position = frame

class Game(Window):
	def __init__(self, size, title, font):
		super().__init__(size, title)


	def run(self):
		run = True
		clock = pygame.time.Clock()
		h = velocity = angle = None

		while h == None:
			try:
				h = float(input('Qual a altura o objeto a ser lançado? (metros) '))
			except ValueError:
				print("Valor incompatível")
		while velocity == None or velocity <= 0:
			try:
				velocity = float(input('Qual a velocidade inicial (m/s): '))
			except ValueError:
				print("Valor incompatível")
		while angle == None or (angle < 0 and angle >=90):
			try:
				angle = float(input('Qual o angulo que o objeto será lançado? (graus) '))
			except ValueError:
				print("Valor incompatível")

		self.init()
		obj = Objeto(h, velocity, angle)
		self.frames = obj.movement(self.velocity)
		self.append_component(obj)

		while self.start:
			clock.tick(40)
			self.refresh_screen()
			self.get_event()
			
			if self.play:
				self.frame += self.speed
			obj.update_position(self.frame)

		self.exit()

if __name__ == "__main__":
    game = Game((WIDTH, HEIGHT), "Movimento Retilíneo Uniformemente Variado", ("comicsans", 16))
    game.run()
