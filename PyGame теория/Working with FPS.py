import pygame
pygame.init()

#код, описвающий окно программы
watch = pygame.time.Clock() #в переменную watch пишем pygame.time.Clock()
FPS = 30 #в переменную FPS закидываем нуюно кол-во FPS

game_run = True
while game_run:
    watch.tick(FPS)  # контроль  кол-во выполениния цикла while в секунуду
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            game_run = False
    #код дейтсвия

pygame.quit()