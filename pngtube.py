import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple PNG VTuber")

# Load character images from a specific directory (change the path as needed)
image_path = "images/"  # Adjust this to match your directory structure
idle_image = pygame.image.load(image_path + "idle.png")  # Default expression
happy_image = pygame.image.load(image_path + "happy.png")  # Happy expression
sad_image = pygame.image.load(image_path + "sad.png")  # Sad expression

# Resize images if needed
idle_image = pygame.transform.scale(idle_image, (200, 200))
happy_image = pygame.transform.scale(happy_image, (200, 200))
sad_image = pygame.transform.scale(sad_image, (200, 200))

# Character settings
x, y = WIDTH // 2, HEIGHT // 2  # Start position
speed = 5
current_image = idle_image  # Default image

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    # Change expressions
    if keys[pygame.K_1]:
        current_image = idle_image
    if keys[pygame.K_2]:
        current_image = happy_image
    if keys[pygame.K_3]:
        current_image = sad_image
    
    # Draw character
    screen.blit(current_image, (x, y))
    
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
