#Создай собственный Шутер! 
from pygame import * 
 
 
#фоновая музыка 
mixer.init() 
mixer.music.load('musicping.ogg') 
mixer.music.play() 
 
 
 
#нам нужны такие картинки: 
img_back = "fonping.png" #фон игры 
img_hero = "stenkaping.png" #герой 
img_ball = 'ballpingo.png' #враг народа 
 
#класс-родитель для других спрайтов 
class GameSprite(sprite.Sprite): 
 #конструктор класса 
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed): 
       #Вызываем конструктор класса (Sprite): 
      sprite.Sprite.__init__(self) 
 
 
      #каждый спрайт должен хранить свойство image - изображение 
      self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
      self.speed = player_speed 
 
 
       
 
 
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан 
      self.rect = self.image.get_rect() 
      self.rect.x = player_x 
      self.rect.y = player_y 
 #метод, отрисовывающий героя на окне 
   def reset(self): 
      window.blit(self.image, (self.rect.x, self.rect.y)) 
 
 
#класс главного игрока 
class Player(GameSprite): 
   #метод для управления спрайтом стрелками клавиатуры 
   def update_r(self): 
      keys = key.get_pressed() 
      if keys[K_UP] and self.rect.y > 5: 
         self.rect.y -= self.speed 
      if keys[K_DOWN] and self.rect.y < win_width - 80: 
         self.rect.y += self.speed 
   def update_l(self): 
      keys = key.get_pressed() 
      if keys[K_w] and self.rect.y > 5: 
         self.rect.y -= self.speed 
      if keys[K_s] and self.rect.y < win_width - 80: 
         self.rect.y += self.speed 
 
 
#Создаем окошкo 
win_width = 700 
win_height = 700 
display.set_caption("Ping Pong") 
window = display.set_mode((win_width, win_height)) 
background = transform.scale(image.load(img_back), (win_width, win_height)) 
 
 
run = True  
finish = False 
clock = time.Clock() 
FPS = 50
 
 
#создаем спрайты  
racket1 = Player(img_hero, 30, 200, 110, 160, 50) 
racket2 = Player(img_hero, 520, 200, 110, 160, 50) 
ball = GameSprite(img_ball, 200, 200, 60, 40, 50) 
 
 
font.init() 
font = font.Font(None, 35) 
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0)) 
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0)) 
 
 
speed_x = 3 
speed_y = 3 
 
#основной цикл игры 
while run: 
   #событие нажатия на кнопку Закрыть 
   for e in event.get(): 
      if e.type == QUIT: 
         run = False 
 
 
 
   if finish != True: 
       #обновляем фон 
 
      racket1.update_l() 
      racket2.update_r() 
      ball.rect.x += speed_x 
      ball.rect.y += speed_y 
      window.blit(background,(0,0)) 
 
      if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball): 
         speed_x *= -1 
         speed_y *= 1 
      if ball.rect.y > win_height-50 or ball.rect.y < 0: 
         speed_y *= -1 
      if ball.rect.x < 0: 
         finish = True 
         window.blit(lose1, (200, 200)) 
         game_over = True 
       
      if ball.rect.x > win_width: 
         finish = True 
         window.blit(lose2, (200, 200)) 
         game_over = True 
 
 
      racket1.reset() 
      racket2.reset() 
      ball.reset() 
   display.update() 
   clock.tick(FPS)