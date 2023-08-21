#создание анимации
import pygame
pygame.init()
screen = pygame.display.set_mode([1000, 800])

game_run = True

bg = [255, 255, 255]
objects = [0, 0, 0]

FPS = 30
clock = pygame.time.Clock()

x = 465 #задаем две кординаты по которым наш квадарт (любой объект) будет двигаться
y = 365
speed = 5 #задаем скорость, которую будем прибавлять или уменьшать для перемещения
#как токового перемещения у нас нет, у нас происходит мена кадров, предыдущий кадр закрашивается и повялется новый, так и происходито анимация
while game_run:
    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game_run = False

    if y < 730: #выбираем кордианту по которой будет двигаться объект, для того чтобы если объект врезался в стенку, то он прекратил дивжение
#730 потому что ширина экрана по y = 800, ширина объекта по y = 70, значит 800 - 70 = 730, тогда объект остановится четко около стенки
        y += speed #здесь мы изменяем нашу кординату y, на скорость. Если у гас += spedd то оьъект дивжется в одном направлении, а если -= то в противоположном направлении

    screen.fill(bg) #заливаем наш фон цветом bg, который мы указывал в 8 сторчке
    pygame.draw.rect(screen, objects, [x, y, 70, 70]) #выриосвываем наш кадарт, использя обновленный кординаты
    pygame.display.flip()

pygame.quit()
