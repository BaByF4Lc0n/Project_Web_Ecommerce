import pygame
print(pygame.ver)

from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Local Multiplayer Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player settings
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 60
PLAYER_SPEED = 5
SKILL_COOLDOWN = 500

# Fireball settings
FIREBALL_SPEED = 7


class Fireball:
    def __init__(self, x, y, color, direction):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.color = color
        self.direction = direction

    def move(self):
        self.rect.y += FIREBALL_SPEED * self.direction

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)


class Player:
    def __init__(self, x, y, color, controls):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = color
        self.controls = controls
        self.vel_x = 0
        self.vel_y = 0
        self.skills = []
        self.shield = False
        self.last_skill_time = 0

    def move(self):
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        self.vel_y = 0

        if keys[self.controls['left']]:
            self.vel_x = -PLAYER_SPEED
        if keys[self.controls['right']]:
            self.vel_x = PLAYER_SPEED
        if keys[self.controls['up']]:
            self.vel_y = -PLAYER_SPEED
        if keys[self.controls['down']]:
            self.vel_y = PLAYER_SPEED

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Keep player in bounds
        self.rect.x = max(0, min(WIDTH - PLAYER_WIDTH, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - PLAYER_HEIGHT, self.rect.y))

    def use_skill(self, skill_type):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_skill_time > SKILL_COOLDOWN:
            self.last_skill_time = current_time
            if skill_type == "fireball":
                direction = -1 if self.vel_y < 0 else 1
                fireball = Fireball(self.rect.centerx, self.rect.top, self.color, direction)
                self.skills.append(fireball)
            elif skill_type == "shield":
                self.shield = True
                pygame.time.set_timer(pygame.USEREVENT + 1, 2000)  # Shield lasts 2 seconds

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.shield:
            pygame.draw.ellipse(screen, BLUE, self.rect.inflate(20, 20), 2)


# Main Game Loop
player1 = Player(100, 100, RED, {
    'left': K_a, 'right': K_d, 'up': K_w, 'down': K_s
})
players = [player1]

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.USEREVENT + 1:
            player1.shield = False  # Disable shield after 2 seconds

    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        player1.use_skill("fireball")

    for player in players:
        player.move()
        player.draw(screen)
        for skill in player.skills[:]:
            if isinstance(skill, Fireball):
                skill.move()
                skill.draw(screen)
                if skill.rect.bottom < 0 or skill.rect.top > HEIGHT:
                    player.skills.remove(skill)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
