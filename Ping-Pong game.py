from pygame import *
font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speedx, player_speedy):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speedx
        self.speedy = player_speedy
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 460:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 460:
            self.rect.y += self.speed

win_width = 800
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
window.fill((200, 255, 255))

game = True
clock = time.Clock()
FPS = 60

speed_x = 4
speed_y = 4

platform1 = Player1('platform1.png', 10, 232, 30, 135, 7, 0)
platform2 = Player2('platform2.png', 765, 232, 30, 135, 7, 0)
ball = GameSprite('ball.png', 370, 10, 60, 60, speed_x, speed_y)

font = font.Font(None, 70)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

while game != False:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((200, 255, 255))

    ball.reset()
    ball.rect.x += speed_x
    ball.rect.y += speed_y    
    
    if ball.rect.x <= 0:
        window.blit(lose1, (220, 260))
        game = False    
    if ball.rect.x >= 800:
        window.blit(lose2, (220, 260))
        game = False      

    platform1.reset()
    platform1.update()

    platform2.reset()
    platform2.update()

    if ball.colliderect(platform1):
        speed_x *= -1
    if ball.colliderect(platform2):
        speed_x *= -1
    
    if ball.rect.y >= 540:
        speed_y *= -1
    if ball.rect.y <= 0:
        speed_y *= -1

    display.update()
    clock.tick(FPS)

while game != True:
    for e in event.get():
        if e.type == QUIT:
            game = True
    
    display.update()
    clock.tick(FPS)