import pygame


pygame.init()
width = 900
height = 600

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
FPS = 20

bg = pygame.image.load("sky.jpeg") #выгружаем наше фото, которые предварительно переместили в проект
air = pygame.image.load("air.png")
air_left = pygame.image.load("air_left.png")

x_air = 0
y_air = 500
speed = 5
number_frames = 0
game_run = True

while game_run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
    number_frames += 1

    screen.blit(bg, (0,0))  # "заливаем" наш экарн фото, используя screen.blit(наша переменная с фото, (кординаты с которых начнет отрисовываться изображение))

    if number_frames % 2 == 0:
        screen.blit(air, (x_air, y_air))
    else:
        screen.blit(air_left,(x_air,y_air))

    #движение по диагонали
    x_air += speed
    y_air -= speed

    pygame.display.flip()

pygame.quit()