import sys
import pygame

# Initialize Pygame
pygame.init()

# --- 1. SCREEN SETUP ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Physics Simulation")
clock = pygame.time.Clock()

# --- 2. PHYSICS & BALL CONSTANTS ---
BALL_RADIUS = 20
BALL_COLOR = (242, 100, 25)  # Vibrant Orange
BACKGROUND_COLOR = (30, 30, 30)  # Dark Gray

# Initial Physics States
x = WIDTH // 2  # Start in the middle horizontally
y = 100  # Start near the top
vx = 1  # Constant horizontal velocity (pixels per frame)
vy = 0  # Initial vertical velocity (starting from rest)

# Physics Coefficients
GRAVITY = 0.5  # Acceleration downward (g)
BOUNCE_LOSS = 0.75  # Coefficient of restitution (retains 75% speed on bounce)
FRICTION = 0.99  # Slight air resistance / floor friction

# --- 3. MAIN ANIMATION LOOP ---
running = True
while running:
    # Handle window closing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- 4. APPLY PHYSICS ---
    # Apply gravity to vertical velocity (vy = vy + g)
    vy += GRAVITY

    # Apply friction/air resistance
    vx *= FRICTION

    # Update positions (pos = pos + v)
    x += vx
    y += vy

    # --- 5. COLLISION DETECTION & RESOLUTION ---
    # Floor Collision
    # The floor is at 'HEIGHT'. The bottom of the ball is 'y + BALL_RADIUS'
    if y + BALL_RADIUS >= HEIGHT:
        y = HEIGHT - BALL_RADIUS  # Snap ball to floor surface to prevent clipping
        vy = -vy * BOUNCE_LOSS  # Reverse direction and apply energy loss

        # Stop minute micro-bounces when energy is virtually gone
        if abs(vy) < 1.5:
            vy = 0

    # Wall Collisions (Left and Right)
    if x - BALL_RADIUS <= 0:
        x = BALL_RADIUS
        vx = -vx * BOUNCE_LOSS
    elif x + BALL_RADIUS >= WIDTH:
        x = WIDTH - BALL_RADIUS
        vx = -vx * BOUNCE_LOSS

    # --- 6. RENDER / DRAW ---
    screen.fill(BACKGROUND_COLOR)  # Clear screen

    # Draw the ball (Surface, Color, (X, Y), Radius)
    pygame.draw.circle(screen, BALL_COLOR, (int(x), int(y)), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS (dt is roughly constant)
    clock.tick(60)

pygame.quit()
sys.exit()

