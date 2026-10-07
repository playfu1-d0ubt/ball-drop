import pygame

# pygame setup
pygame.init()
# opens a window
screen = pygame.display.set_mode(size=(680,680), flags=pygame.SCALED, )
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Gray")

pygame.quit()