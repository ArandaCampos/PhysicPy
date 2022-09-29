#---------------------------------------------
#   Author: Renan Campos
#   Github: github.com/ArandaCampos
#   Projéteis
#---------------------------------------------

import pygame
import math
from base import Window

WIDTH, HEIGHT = 1200, 600
WHITE, BLACK, GREY = (210, 210, 210), (0, 0, 0, .8), (128, 128, 128)

class Objeto:
	g = -9.807 		       	# Aceleração da gravidade (m/s^2)
	ESCALA = 10				# 10px == 1 metro

	def __init__(self, h, velocity, angle):
		self.x = 0											# Posição Vertical (m)
		self.y = h													# Posição Horizontal (m)
		self.vy = velocity * math.sin(math.radians(angle))		# Velocidade Inicial eixo y
		self.vx = velocity * math.cos(math.radians(angle))		# Velocidade Inicial eixo x
		self.diameter = 20 			# Raio (m)
		self.movements = []
		self.position = 0
		self.SCALE = 0

	def draw(self, win):
		if self.position > 2:
			points = []
			for movement in self.movements[0: self.position]:
				points.append(self.transform(movement))
			pygame.draw.lines(win, GREY, False, points, 2)

		pygame.draw.circle(win, BLACK, self.transform(self.movements[self.position]), self.diameter)

	def transform(self, position):
		self.SCALE = WIDTH / self.movements[-1][0]
		x, y = position
		return (x * self.SCALE - self.diameter, HEIGHT - y * self.SCALE - self.diameter)

	def velocity(self, t):
		Vx = self.vx * t
		Vy = self.vy * t + self.g * math.pow(t, 2) / 2
		return Vx, Vy

	def movement(self, interval):
		y = self.y
		x = time = 0
		time = interval
		while y >= 0:
			vx, vy = self.velocity(time)
			x += vx
			y += vy
			time += interval
			self.movements.append((x, y))
		print(self.movements)

	def update_position(self, frame):
		if frame < len(self.movements) and frame >= 0:
			self.position = frame

class Game(Window):
	def __init__(self, size, title, font):
		super().__init__(size, title)

		self.velocity = 1/20
		self.speed = 1
		self.frame = 0

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
		obj.movement(self.velocity)
		self.append_component(obj)

		while run:
			clock.tick(20)
			self.refresh_screen()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.handle_play()
					if event.key == pygame.K_LEFT:
						self.to_back()
					if event.key == pygame.K_RIGHT:
						self.forward()

			if self.play:
				self.frame += self.speed
				obj.update_position(self.frame)

		self.exit()

if __name__ == "__main__":
    game = Game((WIDTH, HEIGHT), "Movimento Retilíneo Uniformemente Variado", ("comicsans", 16))
    game.run()
