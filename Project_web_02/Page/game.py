import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_size - 10
player_speed = 2

# Bullet settings
bullet_width = 5
bullet_height = 10
bullet_speed = 25
bullets = []
bullet_fired = False  # Control single bullet firing

# Target settings
target_size = 50
target_speed = 3
targets = []

# Create a clock object to control the game's framerate
clock = pygame.time.Clock()

# Define font for score and timer display
font = pygame.font.SysFont(None, 36)

# Timer
start_time = time.time()

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_size, player_size))

# Function to fire bullets
def fire_bullet(x, y):
    global bullet_fired
    if not bullet_fired:  # Fire only if no bullet is on screen
        bullets.append([x + player_size // 2 - bullet_width // 2, y])
        bullet_fired = True

# Function to draw bullets
def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], bullet_width, bullet_height))

# Function to move bullets
def move_bullets():
    global bullet_fired
    for bullet in bullets:
        bullet[1] -= bullet_speed
    # Remove bullets that go off-screen
    bullets[:] = [bullet for bullet in bullets if bullet[1] > 0]
    if not bullets:  # If no bullets are on screen, allow firing again
        bullet_fired = False

# Function to create new targets
def create_target():
    x = random.randint(0, SCREEN_WIDTH - target_size)
    y = -target_size
    targets.append([x, y])

# Function to draw targets
def draw_targets():
    for target in targets:
        pygame.draw.rect(screen, RED, (target[0], target[1], target_size, target_size))

# Function to move targets
def move_targets():
    for target in targets:
        target[1] += target_speed
    # Remove targets that go off-screen
    targets[:] = [target for target in targets if target[1] < SCREEN_HEIGHT]

# Function to check for bullet-target collisions
def check_collisions():
    global score
    for bullet in bullets[:]:
        for target in targets[:]:
            if (target[0] < bullet[0] < target[0] + target_size) and (target[1] < bullet[1] < target[1] + target_size):
                bullets.remove(bullet)
                targets.remove(target)
                score += 1

# Function to check if player is hit by a target
def check_player_hit():
    for target in targets:
        if (target[0] < player_x + player_size and target[0] + target_size > player_x) and \
           (target[1] < player_y + player_size and target[1] + target_size > player_y):
            return True
    return False

# Main game loop
running = True
game_over = False
score = 0

while running:
    screen.fill(BLACK)

    # Draw player
    draw_player(player_x, player_y)

    # Move bullets
    move_bullets()
    draw_bullets()

    # Move and draw targets
    move_targets()
    draw_targets()

    # Check for bullet-target collisions
    check_collisions()

    # Check if player is hit
    if check_player_hit():
        game_over = True

    # Display score and timer
    elapsed_time = round(time.time() - start_time, 2)
    score_text = font.render(f"Score: {score}", True, WHITE)
    time_text = font.render(f"Time: {elapsed_time}s", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))

    # Create new target occasionally
    if random.randint(1, 100) < 2:
        create_target()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed

    # Fire bullets
    if keys[pygame.K_SPACE]:
        fire_bullet(player_x, player_y)

    # If game is over, display Game Over message and stop
    if game_over:
        game_over_text = font.render("Game Over!", True, RED)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(1000)
        running = False

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(140)

# quit the game
pygame.quit() 