import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")
print("woaaaao que guapooo")

player = pygame.Rect(400, 300, 50, 50)

move_up = False
move_down = False
move_left = False
move_right = False

run = True
while run:
    #calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if move_right == True:
        delta_x = 100
    if move_left == True:
        delta_x = -100
    if move_up == True:
        delta_y = -100
    if move_down == True:
        delta_y = 100

    position_screen = player.move(delta_x, delta_y)


    pygame.draw.rect(window,(255,0, 0), player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_left = True
                if event.key == pygame.K_d:
                    move_right = True
                if event.key == pygame.K_w:
                    move_up = True
                if event.key == pygame.K_s:
                    move_down = True

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_d:
                    move_right = False
                if event.key == pygame.K_w:
                    move_up = False
                if event.key == pygame.K_s:
                    move_down = False

    pygame.display.update()

pygame.quit()