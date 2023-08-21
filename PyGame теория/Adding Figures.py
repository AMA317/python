#pygame.draw.circle(поверхность, цвет, координаты центра, радиус, толщина рамки)
#pygame.draw.rect(поверхность, цвет, координаты, толщина рамки)
import pygame
import time

pygame.init()

width = 800
height = 800
white = [255,255,255]
red = [255,0,0]

screen = pygame.display.set_mode([400,500])
screen.fill(white)

pygame.draw.circle(screen,red, [width/2, height/2], 50)

pygame.display.flip()
time.sleep(5)

pygame.quit()