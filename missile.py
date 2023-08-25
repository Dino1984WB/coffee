# Dino

class Missile:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.speed = 2
        self.radius = 5

    def move(self):
        direction_x = self.target_x - self.x
        direction_y = self.target_y - self.y
        distance = (direction_x ** 2 + direction_y ** 2) ** 0.5
        if distance < 5:
            return True
        direction_x /= distance
        direction_y /= distance
        self.x += direction_x * self.speed
        self.y += direction_y * self.speed
        return False

    def draw(self, window, color):
        import pygame
        pygame.draw.circle(window, color, (int(self.x), int(self.y)), self.radius)
