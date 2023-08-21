import pygame #вызов библиотеки Pygame
import time #вызовк бибилиотеки time

pygame.init() #показвает, что дальше будет идити код библиотеки Pygame (это обязательно)

screen = pygame.display.set_mode([400,500]) # Вызвваем экран, задав ([ширина,высота], Чтобы ратснятуь на весь экран
# [(ширина, высота], pygameFULLSCREEN).
#Так же можно делать это через ПЕРЕМЕННЫЕ: pygame.display.set_mode([width, height])  Зажав command, наведя и нажав
#'set mode', можно посмотреть все возоможные задаваемые параметы display

screen.fill([255, 0, 4]) #залить экран ([RGB цвета])
pygame.display.flip()
time.sleep(3) #мы вызвывали библиотеку time, чтобы вспылвающий экран задеражался на 3 секунды

screen.fill([100, 60, 40])
pygame.display.flip()
time.sleep(3)