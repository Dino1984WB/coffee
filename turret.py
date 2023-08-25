# Dino

from missile import Missile

class Turret:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.broken = False

    def draw(self, window, color):
        import pygame
        if not self.broken:
            pygame.draw.circle(window, color, (self.x, self.y), 10)

    def shoot(self, target_x, target_y):
        return Missile(self.x, self.y, target_x, target_y)
