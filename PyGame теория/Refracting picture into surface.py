import pygame

pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()
FPS = 30

car = pygame.image.load('car.png')

car_surf = car.convert_alpha() #конвертируем нашу переменную car в которой записано изображение в поверхность, пользователь не видит разницы, но программа поменялась
car_surf = pygame.transform.smoothscale(car_surf, (200,200)) #pygame.transform.smoothscale - дает возмодность редактирвоать картинкуб в парметры передаем переменную в которой записана трансформированный рисунок в поверхность, а вторым параметром передаем размеры картинки я в скобках
car_surf_flip = pygame.transform.flip(car_surf, True, True) #отзеркаливаем картинкус помощью pygame.transform.flip, в параметры передаем ту картинку которую хотим перевернуть, а True, True, это знаачит что: по x и y надо отзеркалить, True - надо одзеркалить, False - не надо
car_rotate = pygame.transform.rotate(car_surf, 90) #car_rotate = pygame.transform.rotate - функция поворота, car_surf - поверхность которую мы поворачиваем, 90 - угол поворота


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(car_surf, (100, 270))
    screen.blit(car_surf_flip, (0,170)) #отзеркаленной картинки передаем кординаты, если без этой строчки то будет ошибка
    pygame.display.flip()
pygame.quit()