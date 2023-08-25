# Dino

class Explosion:
    def __init__(self, x, y, max_radius=30, effective_radius=20):
        self.x = x
        self.y = y
        self.radius = 0
        self.max_radius = max_radius
        self.effective_radius = effective_radius


    def update(self):
        self.radius += 2
        if self.radius >= self.max_radius:
            return True
        return False

    def draw(self, window, color):
        import pygame
        pygame.draw.circle(window, color, (int(self.x), int(self.y)), self.radius, 1)
