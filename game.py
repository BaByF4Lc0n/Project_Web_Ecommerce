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
        self.score = 0

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

# Target class
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

# Initialize players and targets
player1 = Player(RED, WIDTH // 4, HEIGHT - PLAYER_SIZE)
player2 = Player(BLUE, 3 * WIDTH // 4, HEIGHT - PLAYER_SIZE)

players = pygame.sprite.Group()
players.add(player1)
players.add(player2)

targets = pygame.sprite.Group()

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

    # Spawn targets
    if random.randint(1, 20) == 1:
        target = Target()
        targets.add(target)

    # Update targets
    targets.update()

    # Draw players and targets
    players.draw(screen)
    player1.draw(screen)
    player2.draw(screen)
    targets.draw(screen)

    # Check for collisions
    for player in players:
        hits = pygame.sprite.groupcollide(player.bullets, targets, True, True)
        player.score += len(hits)

    # Display scores
    font = pygame.font.Font(None, 36)
    score_text1 = font.render(f"Player 1 Score: {player1.score}", True, WHITE)
    score_text2 = font.render(f"Player 2 Score: {player2.score}", True, WHITE)
    screen.blit(score_text1, (10, 10))
    screen.blit(score_text2, (WIDTH - 200, 10))

    # Check timer
    elapsed_time = time.time() - start_time
    if elapsed_time >= GAME_DURATION:
        running = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
