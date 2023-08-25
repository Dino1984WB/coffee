# Dino

import pygame
import random
import math

pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Missile Command")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
NEON_GREEN = (57, 255, 20)

# Define Explosion class
class Explosion:
    def __init__(self, x, y, max_radius=30):
        self.x = x
        self.y = y
        self.radius = 0
        self.max_radius = max_radius

    def update(self):
        self.radius += 2
        if self.radius >= self.max_radius:
            return True
        return False

    def draw(self, window):
        pygame.draw.circle(window, NEON_GREEN, (int(self.x), int(self.y)), self.radius, 1)

# Define Missile class
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

    def draw(self, window):
        pygame.draw.circle(window, NEON_GREEN, (int(self.x), int(self.y)), self.radius)

# Define Turret class
class Turret:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window):
        pygame.draw.circle(window, RED, (self.x, self.y), 10)

    def shoot(self, target_x, target_y):
        return Missile(self.x, self.y, target_x, target_y)

# Initialize missiles and turrets
missiles = [Missile(random.randint(0, width), 0, random.randint(0, width), height) for _ in range(3)]
turrets = [Turret(width//4, height-10), Turret(width//2, height-10), Turret(3*width//4, height-10)]
counter_missiles = []
explosions = []

# Main game loop
running = True
while running:
    window.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            turret = turrets[len(counter_missiles) % len(turrets)] # Select a turret
            counter_missiles.append(turret.shoot(x, y))

    # Update missiles
    for missile in missiles[:]:
        if missile.move():
            missiles.remove(missile)
            missiles.append(Missile(random.randint(0, width), 0, random.randint(0, width), height))
        missile.draw(window)

    # Update counter-missiles
    for cm in counter_missiles[:]:
        if cm.move():
            counter_missiles.remove(cm)
            continue
        # Check collisions with missiles
        for missile in missiles[:]:
            if math.hypot(cm.x - missile.x, cm.y - missile.y) < cm.radius + missile.radius:
                missiles.remove(missile)
                counter_missiles.remove(cm)
                explosions.append(Explosion(cm.x, cm.y))
                break
        cm.draw(window)

    # Draw turrets
    for turret in turrets:
        turret.draw(window)

    # Update and draw explosions
    for explosion in explosions[:]:
        if explosion.update():
            explosions.remove(explosion)
        explosion.draw(window)

    pygame.display.flip()
    pygame.time.delay(16)

pygame.quit()
