import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
FPS = 30

car = pygame.image.load('car.png')

car_surf = car.convert_alpha()  # конвертируем нашу переменную car в которой записано изображение в поверхность, пользователь не видит разницы, но программа поменялась

car_surf = pygame.transform.smoothscale(car_surf, (120,60))  # pygame.transform.smoothscale - дает возмодность редактирвоать картинкуб в парметры передаем переменную в которой записана трансформированный рисунок в поверхность, а вторым параметром передаем нужные значения в скобках
car_surf_flip = pygame.transform.flip(car_surf, True, True)
car_rotate = pygame.transform.rotate(car_surf,90)
car_rotate_2 = pygame.transform.rotate(car_surf,270)

running = True
while running:
    clock.tick(FPS)
    screen.fill([80, 80, 80])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(car_surf, (100, 270))
    screen.blit(car_surf_flip, (380, 270))
    screen.blit(car_rotate, (270, 120))
    screen.blit(car_rotate_2, (270, 360))
    pygame.display.flip()
pygame.quit()
