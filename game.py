import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Local Multiplayer Shooting Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
PLAYER_SIZE = 50
PLAYER_SPEED = 5
BULLET_SPEED = 7

# Timer settings
GAME_DURATION = 60  # 1 minute

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = PLAYER_SPEED
        self.bullets = pygame.sprite.Group()

    def update(self, keys, up, down, left, right, shoot):
        if keys[up]:
            self.rect.y -= self.speed
        if keys[down]:
            self.rect.y += self.speed
        if keys[left]:
            self.rect.x -= self.speed
        if keys[right]:
            self.rect.x += self.speed
        if keys[shoot]:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.bullets.add(bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullets.draw(screen)
        self.bullets.update()

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Initialize players
player1 = Player(RED, WIDTH // 4, HEIGHT - PLAYER_SIZE)
player2 = Player(BLUE, 3 * WIDTH // 4, HEIGHT - PLAYER_SIZE)

players = pygame.sprite.Group()
players.add(player1)
players.add(player2)

# Game loop
running = True
start_time = time.time()

while running:
    screen.fill(BLACK)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update players
    player1.update(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE)
    player2.update(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RETURN)

    # Draw players
    players.draw(screen)
    player1.draw(screen)
    player2.draw(screen)

    # Check for collisions
    if pygame.sprite.spritecollide(player1, player2.bullets, True):
        print("Player 2 hit Player 1!")
    if pygame.sprite.spritecollide(player2, player1.bullets, True):
        print("Player 1 hit Player 2!")

    # Check timer
    elapsed_time = time.time() - start_time
    if elapsed_time >= GAME_DURATION:
        running = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
