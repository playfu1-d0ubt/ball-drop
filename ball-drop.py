import pygame
import random

# pygame setup
pygame.init()
# opens a window
screen = pygame.display.set_mode(size=(680,680), flags=pygame.SCALED, )
clock = pygame.time.Clock()
running = True
dt = 0

score=0
lives=3

# creating the basket (made once, before the loop)
basket = pygame.Rect(0, 0, 100, 20)  # left, top, width, height
basket.midbottom = (screen.get_width() / 2, screen.get_height() - 20)
basket_x = float(basket.x)  # exact position, because a Rect only stores whole numbers
basket_speed = 400  # pixels per secondplayer_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()*0.80)

# creating the ball (made once, before the loop)
ball = pygame.Rect(0, 0, 30, 30)             # left, top, width, height
ball.midtop = (screen.get_width() / 2, 5)    # centred horizontally, touching the top edge
ball_colour = "red"                          # TO DO: multiple colours
ball_speed = 200                             # pixels per second
#random x pos for ball
ball.x = random.randint(5, screen.get_width()-5)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move the basket left or right - WASD and arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        basket_x -= basket_speed * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        basket_x += basket_speed * dt

    # limiting movement of the basket 
    basket_x = max(5, min(basket_x, screen.get_width() - basket.width - 5))
    basket.x = round(basket_x)

    # making the ball fall
    stop = screen.get_height() - 40
    ball.y += ball_speed * dt
    if ball.y > stop:
        ball.y = stop
        #detecting ball 
        if basket.colliderect(ball) == True:
            score += 1
            ball.y = 5
            ball.x = random.randint(5, screen.get_width()-5)
        else:
            lives -= 1
            ball.y = 5
            ball.x = random.randint(5, screen.get_width()-5)

    if lives == 0:
       running = False
    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Gray")

    #drawing the basket
    pygame.draw.rect(screen, "chocolate3", basket)

    # drawing the ball
    pygame.draw.circle(screen, ball_colour, ball.center, ball.width//2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()