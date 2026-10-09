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
font = pygame.font.Font(None, 36)

# creating the basket (made once, before the loop)
basket = pygame.Rect(0, 0, 100, 20)  # left, top, width, height
basket.midbottom = (screen.get_width() / 2, screen.get_height() - 20)
basket_x = float(basket.x)  # exact position, because a Rect only stores whole numbers
basket_speed = 400  # pixels per second


# creating the balls
ball_size = 30
balls = []                    # every ball currently on screen
spawn_delay = 1.25            # seconds between new balls
spawn_timer = spawn_delay     # starts full, so the first ball appears straight away

def make_ball():
    rect = pygame.Rect(0, 0, ball_size, ball_size)
    rect.x = random.randint(5, screen.get_width() - ball_size - 5)
    rect.y = 5
    return {"rect": rect, "y": float(rect.y), "colour": random.choice(["red", "blue", "green", "yellow"])}
ball_speed = 200                             # pixels per second


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

    # spawn a new ball every spawn_delay seconds
    spawn_timer += dt
    if spawn_timer >= spawn_delay:
        balls.append(make_ball())
        spawn_timer = 0

    # move every ball, then check for catches and misses
    for ball in balls[:]:         # [:] loops over a copy, so removing balls is safe
        ball["y"] += ball_speed * dt
        ball["rect"].y = round(ball["y"])

        if basket.colliderect(ball["rect"]):
            score += 1
            balls.remove(ball)
        elif ball["rect"].top > screen.get_height():
            lives -= 1
            balls.remove(ball)
        
    if score % 5 == 0 and score != 0:  # every 5 points, increase speed
        ball_speed += 20
        ball_speed = min(ball_speed, 500)  # limit the maximum speed
        basket_speed += 20
        basket_speed = min(basket_speed, 500)  # limit the maximum speed
        score += 1  # to avoid increasing speed again on the next frame
        lives += 1  # give the player an extra life for every 5 points
    if lives == 0:
       running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Gray")

    # display the score and lives on the screen
    score_text = font.render(f"Score: {score}", True, "black")
    lives_text = font.render(f"Lives: {lives}", True, "black")
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    #drawing the basket
    pygame.draw.rect(screen, "chocolate3", basket)

    for ball in balls:
        pygame.draw.circle(screen, ball["colour"], ball["rect"].center, ball_size // 2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

print("Final score:", score)
pygame.quit()