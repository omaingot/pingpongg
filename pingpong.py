'''Импорт нужных библиотек и модулей'''
from pygame import *
from random import *

'''Все нужные классы'''

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

'''Создание окна и установка его параметров'''
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')

'''Создание всех нужных объектов'''
racket1 = Player('zel1.png', 30, 200, 4, 50, 150) 
racket2 = Player('zel2.png', 520, 200, 4, 50, 150)
ball = GameSprite('podsol.png', 200, 200, 4, 50, 50)
background = GameSprite('Без названия.jpg', 0, 0, 0, win_width, win_height)

'''Создание переменных для корректной работы игрового цикла'''
game = True
finish = False
clock = time.Clock()
FPS = 60

win_player1 = GameSprite('player1.jpg', 0, 0, 0, win_width, win_height)
win_player2 = GameSprite('pl2.jpg', 0, 0, 0, win_width, win_height)

speed_x = 3
speed_y = 3

'''Игровой цикл'''
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= randint(-13, -7) / 10
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            win_player2.reset()
            continue
        if ball.rect.x > win_width - 50:
            finish = True
            win_player1.reset()
            continue


        background.reset()
        
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)