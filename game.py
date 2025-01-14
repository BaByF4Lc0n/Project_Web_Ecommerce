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
GREEN = (0, 255, 0)

# Player settings
PLAYER_SIZE = 50
PLAYER_SPEED = 5
BULLET_SPEED = 7
SHOOT_DELAY = 500  # milliseconds

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
        self.last_shot = pygame.time.get_ticks()

    def update(self, keys, up, down, left, right, shoot):
        if keys[up]:
            self.rect.y -= self.speed
        if keys[down]:
            self.rect.y += self.speed
        if keys[left]:
            self.rect.x -= self.speed
        if keys[right]:
            self.rect.x += self.speed
        now = pygame.time.get_ticks()
        if keys[shoot] and now - self.last_shot > SHOOT_DELAY:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.bullets.add(bullet)
            self.last_shot = now

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
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 5)
        self.color = color

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
        color = random.choice([WHITE, GREEN, RED])
        target = Target(color)
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
        for hit in hits:
            if hit.color == WHITE:
                player.score += 1
            elif hit.color == GREEN:
                player.score *= 2
            elif hit.color == RED:
                player.score -= 2

    # Display scores and timer
    font = pygame.font.Font(None, 36)
    score_text1 = font.render(f"Player 1 Score: {player1.score}", True, WHITE)
    score_text2 = font.render(f"Player 2 Score: {player2.score}", True, WHITE)
    screen.blit(score_text1, (10, 10))
    screen.blit(score_text2, (WIDTH - 200, 10))

    elapsed_time = time.time() - start_time
    timer_text = font.render(f"Time: {int(GAME_DURATION - elapsed_time)}", True, WHITE)
    screen.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, 10))

    # Check timer
    if elapsed_time >= GAME_DURATION:
        running = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Determine winner
if player1.score > player2.score:
    winner_text = "Player 1 Wins!"
elif player2.score > player1.score:
    winner_text = "Player 2 Wins!"
else:
    winner_text = "It's a Tie!"

# Display winner
screen.fill(BLACK)
winner_text_surface = font.render(winner_text, True, WHITE)
screen.blit(winner_text_surface, (WIDTH // 2 - winner_text_surface.get_width() // 2, HEIGHT // 2 - winner_text_surface.get_height() // 2))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
