#делаем так чтобы программа

import pygame
pygame.init()

screen = pygame.display.set_mode([800,500])

game_run = True #создаем индификатор работы игры, переменная = True

while game_run: #пока индикатор game_run в позиции работы игры
    for i in pygame.event.get(): #переберо всех проиозошедших событий в Pygame, и записваем их в любую переменную,в нашем случае I

        if i.type == pygame.QUIT: #цикл проверяет нажата ли кнопка закрытия окна или нет
            game_run = False #индикатор переходит в позицию "игра завершена" и цикл while заканчивается
    #код игры в цикле While
    screen.fill([255,255,255])
    pygame.display.flip()

pygame.quit()