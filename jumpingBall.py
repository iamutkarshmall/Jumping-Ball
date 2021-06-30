import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 250
y = 400
radius = 25
vel = 5

isJump = False
jumpCount = 10

run = True

while run:

    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        isJump = True

    if isJump:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    
    win.fill((255, 255, 255))
    pygame.draw.circle(win, (255,0,0), (x, y), radius)   
    pygame.display.update() 
    
pygame.quit()