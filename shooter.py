import pygame
import os
from random import randint


pygame.init()

window = pygame.display.set_mode((700, 500))
FPS = 50
clock = pygame.time.Clock()
path1 = os.path.join(os.getcwd(),"media")

path_background = os.path.join(path1, "galaxy.jpg")
background = pygame.image.load(path_background)
background = pygame.transform.scale(background, (700, 500))

print(path_background)

class Gamesprite():
    def __init__(self, x, y, w, h, image, speed):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.transform.scale(image, (w, h))
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Enemy(Gamesprite):
    def move(self):
            self.rect.y+=self.speed
            if self.rect.y>=500:
                self.rect.y = -50
                self.rect.x = randint(0, 625)

class Rocket(Gamesprite):
    def r_move(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP] and self.rect.y>-1:
            self.rect.y-=self.speed
        if key_pressed[pygame.K_DOWN] and self.rect.y<500-self.rect.height:
            self.rect.y+= self.speed
        if key_pressed[pygame.K_LEFT] and self.rect.x>-1:
            self.rect.x-= self.speed
        if key_pressed[pygame.K_RIGHT] and self.rect.x<700-self.rect.width:
            self.rect.x+= self.speed

class Bullet(Enemy):
    def move(self):
        self.rect.y-=self.speed
        if self.rect.y<-30:
            bullets.remove(self)

bullets = []
Enemys = []
rocket_lost = 0


path_ufo = os.path.join(path1, 'ufo.png')
path_rocket = os.path.join(path1, 'rocket.png')
path_bullet = os.path.join(path1, 'bullet.png')
rocket_img = pygame.image.load(path_rocket)
ufo_img = pygame.image.load(path_ufo)
bullet_img = pygame.image.load(path_bullet)
rocket = Rocket(300, 350, 50, 100, rocket_img, 10)
for i in range(5):
    ufo = Enemy(randint(0, 625), -50, 150, 80, ufo_img, randint(5, 10))
    Enemys.append(ufo)

lose = pygame.font.SysFont('Arial', 70).render('Lose', True, (255,0,0))
win = pygame.font.SysFont('Arial', 70).render('Win', True, (0,255,0))

font2 = pygame.font.SysFont('Arial', 30)
lost_lab = font2.render('Gone:' + str(rocket_lost, True,(255, 255, 255)))
score_lab = font2.render('Вбито:' + str(rocket_lost, True,(255, 255, 255)))

game = True
finish = False
while game:
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(rocket.rect.centerx, rocket.rect.y, 10, 10, bullet_img, 20)
                bullets.append(bullet)
                lose.draw()


    if not finish:
        window.blit(background, (0,0))
        window.blit(lost_lab, (5, 5)))
        window.blit(score_lab (25, 5))
        rocket.draw()
        rocket.r_move()
        for i in Enemys:
            i.draw()
            i.move()
        for i in bullets:
            i.draw()
            i.move()
            for enemy in Enemys:
                if i.rect.colliderect(enemy.rect):
                        bullets.remove(i)
                        enemy.rect.y = -50
                        enemy.rect.x = randint(0, 625)
                        #rocket_lost+=1

    if game == False:
        lose.draw()








