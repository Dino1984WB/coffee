
# Dino

import pygame
import random
import math
from missile import Missile
from turret import Turret
from explosion import Explosion

pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Missile Command")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
NEON_GREEN = (57, 255, 20)

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
            explosions.append(Explosion(missile.x, missile.y))
            missiles.remove(missile)
            missiles.append(Missile(random.randint(0, width), 0, random.randint(0, width), height))
        missile.draw(window, NEON_GREEN)

    # Update counter-missiles
    for missile in counter_missiles[:]:
        if missile.move():
            explosions.append(Explosion(missile.x, missile.y))
            counter_missiles.remove(missile)
        missile.draw(window, RED)

    # Draw turrets
    for turret in turrets:
        turret.draw(window, RED)

    # Update and draw explosions
    for explosion in explosions[:]:
        if explosion.update():
            explosions.remove(explosion)
        explosion.draw(window, NEON_GREEN)

    pygame.display.flip()
    pygame.time.delay(16)

pygame.quit()
