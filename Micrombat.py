import math
import pygame
import random
from pygame.locals import *

# Iniciar o Jogo
pygame.init()
pygame.mixer.init()
width, height = 1080, 720
screen = pygame.display.set_mode((width, height))

# Trilha Sonora
music = False


def shootsnd():  # efeito de tiro
    effect = pygame.mixer.Sound('shoot.wav')
    effect.set_volume(0.3)
    effect.play()


def soundtrack():
    global music
    if music == False:
        pygame.mixer.music.load('soundtrack.mp3')
        pygame.mixer.music.play(-1)
        music = True


# Listas de variaveis
keys = [False, False, False, False, False]
playerpos = [508, 328]
lifepos = [510, 425]
bgpos = [0, 0]
shoots = []
frame = 0
last_updade = pygame.time.get_ticks()
hit_delay = pygame.time.get_ticks()

# Esconder o mouse
pygame.mouse.set_visible(False)


#Carregar sons
expl_snd1 = pygame.mixer.Sound('expl_snd1.wav')
expl_snd2 = pygame.mixer.Sound('expl_snd2.wav')
dano = pygame.mixer.Sound('dano.wav')
menusnd = pygame.mixer.Sound('menu_snd.ogg')
victorysnd = pygame.mixer.Sound('victorysnd.ogg')
spraysnd = pygame.mixer.Sound('spraysnd.ogg')
swallow = pygame.mixer.Sound('swallow.ogg')
sounds = [expl_snd2, expl_snd1, dano, menusnd, spraysnd, swallow]
for snd in sounds:
    snd.set_volume(0.5)


# Carregando sprites
player = [pygame.image.load('Sprites/Player.png'), pygame.image.load('Sprites/Player_01.png'),
          pygame.image.load('Sprites/Player_02.png'), pygame.image.load('Sprites/Player_03.png'),
          pygame.image.load('Sprites/Player_04.png'), pygame.image.load('Sprites/Player_03.png'),
          pygame.image.load('Sprites/Player_02.png'), pygame.image.load('Sprites/Player_01.png'),
          pygame.image.load('Sprites/Player.png'), pygame.image.load('Sprites/Player_10.png'),
          pygame.image.load('Sprites/Player_20.png'), pygame.image.load('Sprites/Player_30.png'),
          pygame.image.load('Sprites/Player_40.png'), pygame.image.load('Sprites/Player_30.png'),
          pygame.image.load('Sprites/Player_20.png'), pygame.image.load('Sprites/Player_10.png')]
bg = pygame.image.load('Sprites/bg.png')
shoot = pygame.image.load('Sprites/Shoot.png')
life = [1, 2, 3]
life[0] = pygame.image.load('Sprites/Life1.png')
life[1] = pygame.image.load('Sprites/Life2.png')
life[2] = pygame.image.load('Sprites/Life3.png')
infecload = pygame.image.load('Sprites/infec.png').convert()
infecload.set_colorkey((255,255,255))
infec = pygame.transform.scale(infecload, (256,256))
player_mask = pygame.image.load('Sprites/player_mask.png').convert_alpha()


enemy1 = []
for x in range(5):
    img = pygame.image.load('Sprites/Verde_0{}.png'.format(x)).convert()
    if x == 0:
        img.set_colorkey((255, 255, 255))
    else:
        img.set_colorkey((0,0,0))
    enemy1.append(img)

enemy2 = []
for x in range(6):
    img = pygame.image.load('Sprites/Vermelho_0{}.png'.format(x)).convert()
    img.set_colorkey((0, 0, 0))
    enemy2.append(img)

enemy3= []
for x in range(2):
    img = pygame.image.load('Sprites/Azul_0{}.png'.format(x)).convert()
    img.set_colorkey((0,0,0))
    enemy3.append(img)

enemys = [enemy1, enemy2, enemy3]

explosion_anim = []
for x in range(4):
    img = pygame.image.load('Sprites/exp_0{}.png'.format(x)).convert()
    img.set_colorkey((0,0,0))
    explosion_anim.append(img)

stun_anim = []
for x in range(6):
    imgload = pygame.image.load('Sprites/Stun_0{}.png'.format(x)).convert()
    imgload.set_colorkey((0,0,0))
    img = pygame.transform.scale(imgload, (98,50))
    stun_anim.append(img)

smoke_anim = []
for x in range(5):
    img = pygame.image.load('Sprites/smoke_0{}.png'.format(x)).convert()
    img.set_colorkey((0, 0, 0))
    smoke_anim.append(img)

spray = []
for x in range(5):
    img = pygame.image.load('Sprites/spray_0{}.png'.format(x)).convert()
    img.set_colorkey((0, 0, 0))
    spray.append(img)

aim = [1, 2]
aim[0] = pygame.image.load('Sprites/aim_01.png')
aim[1] = pygame.image.load('Sprites/aim_02.png')
I = aim[0]
tela2 = pygame.Surface((3000, 3000))
xtela = 0
ytela = 0

#img menu
logo = pygame.image.load('Sprites/logo.png').convert()
logo.set_colorkey((255,255,255))
play1 = pygame.image.load('Sprites/Play.png').convert()
play1.set_colorkey((255,255,255))
play2 = pygame.image.load('Sprites/Play1.png').convert()
play2.set_colorkey((255,255,255))
diff1 = pygame.image.load('Sprites/Difficulty.png').convert()
diff1.set_colorkey((255,255,255))
diff2 = pygame.image.load('Sprites/Difficulty1.png').convert()
diff2.set_colorkey((255,255,255))
easy1 = pygame.image.load('Sprites/easy.png').convert()
easy1.set_colorkey((255,255,255))
easy2 = pygame.image.load('Sprites/easy1.png').convert()
easy2.set_colorkey((255,255,255))
medium1 = pygame.image.load('Sprites/medium.png').convert()
medium1.set_colorkey((255,255,255))
medium2 = pygame.image.load('Sprites/medium1.png').convert()
medium2.set_colorkey((255,255,255))
hard1 = pygame.image.load('Sprites/hard.png').convert()
hard1.set_colorkey((255,255,255))
hard2 = pygame.image.load('Sprites/hard1.png').convert()
hard2.set_colorkey((255,255,255))
victory = pygame.image.load('Sprites/Victory.png').convert()
victory.set_colorkey((255,255,255))
howto1 = pygame.image.load('Sprites/Howtoplay.png').convert()
howto1.set_colorkey((255,255,255))
howto2 = pygame.image.load('Sprites/Howtoplay1.png').convert()
howto2.set_colorkey((255,255,255))
howtoplayimg = pygame.image.load('Sprites/screenhowtoplay.png').convert()
gameoverimg = pygame.image.load('Sprites/GameOver.png').convert()
gameoverimg.set_colorkey((255,255,255))

h2p = [howto1, howto2]
diff = [diff1, diff2]
play = [play1, play2]
easy = [easy1, easy2]
medium = [medium1, medium2]
hard = [hard1, hard2]

cursor = pygame.image.load('Sprites/cursor.png').convert()
cursor.set_colorkey((255,255,255))


minimapa = pygame.Surface((120,120))
minimapa.fill((30,30,30))
minimapa.set_alpha(220)
clock = pygame.time.Clock()


def newSmoke():
    smoke = Smoke()
    smokes.add(smoke)
    all_sprites.add(smoke)

def menu():
    menu = True
    indplay = 0
    inddiff = 0
    indhow = 0
    while menu:
        clock.tick(60)

        playbtn = pygame.draw.rect(screen, (255, 255, 255), ((440, 245), (200, 72)))
        diffbtn = pygame.draw.rect(screen, (255, 255, 255), ((320, 385), (448, 72)))
        howbtn =  pygame.draw.rect(screen, (255, 255, 255), ((285, 520), (509, 72)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbtn.collidepoint(event.pos):
                    menusnd.play()
                    menu = False
                if diffbtn.collidepoint(event.pos) :
                    menusnd.play()
                    difficulty()
                if howbtn.collidepoint(event.pos):
                    menusnd.play()
                    Howtoplay()


        if pygame.mouse.get_pos()[0] in range(440,640) and pygame.mouse.get_pos()[1] in range(245, 317):
            indplay = 1
        else:
            indplay = 0
        if pygame.mouse.get_pos()[0] in range(320, 768) and pygame.mouse.get_pos()[1] in range(385, 457):
            inddiff = 1
        else:
            inddiff = 0
        if pygame.mouse.get_pos()[0] in range(285, 794) and pygame.mouse.get_pos()[1] in range(520, 592):
            indhow = 1
        else:
            indhow = 0


        screen.fill((10, 10, 10))
        screen.blit(logo, (280,40))
        screen.blit(play[indplay], (440,245))
        screen.blit(diff[inddiff], (320, 385))
        screen.blit(h2p[indhow], (285,520))
        screen.blit(cursor, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))

        pygame.display.flip()


def difficulty():
    difficulty = True
    indeasy = 0
    indmedium = 0
    indhard = 0
    global level
    while difficulty:
        clock.tick(60)


        easybtn = pygame.draw.rect(screen, (255, 255, 255), ((444, 241), (200, 70)))
        mediumbtn = pygame.draw.rect(screen, (255, 255, 255), ((414, 389), (264, 61)))
        hardbtn = pygame.draw.rect(screen, (255, 255, 255), ((446, 529), (200, 66)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easybtn.collidepoint(event.pos):
                    level = 2
                    menusnd.play()
                    difficulty = False
                if mediumbtn.collidepoint(event.pos) :
                    level = 3
                    menusnd.play()
                    difficulty = False
                if hardbtn.collidepoint(event.pos) :
                    level = 5
                    menusnd.play()
                    difficulty = False

        if pygame.mouse.get_pos()[0] in range(444,644) and pygame.mouse.get_pos()[1] in range(241, 311):
            indeasy = 1
        else:
            indeasy = 0
        if pygame.mouse.get_pos()[0] in range(414, 678) and pygame.mouse.get_pos()[1] in range(389, 450):
            indmedium = 1
        else:
            indmedium = 0
        if pygame.mouse.get_pos()[0] in range(446, 646) and pygame.mouse.get_pos()[1] in range(529, 595):
            indhard = 1
        else:
            indhard = 0

        screen.fill((10, 10, 10))
        screen.blit(logo, (280, 40))
        screen.blit(easy[indeasy], (444,241))
        screen.blit(medium[indmedium], (414,389))
        screen.blit(hard[indhard], (446,529))

        screen.blit(cursor, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))

        pygame.display.flip()

def victoryscreen():
    venceu = True
    victorysnd.play()
    while venceu:
        clock.tick(60)

        back = pygame.draw.rect(screen, (255,255,255), ((0,0), (1080,720)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint(event.pos):
                    menusnd.play()
                    venceu = False


        screen.fill((10,10,10))
        screen.blit(logo, (280, 40))
        screen.blit(victory, (290,310))


        screen.blit(cursor, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        pygame.display.flip()

def gameoverscreen():
    perdeu = True
    while perdeu:
        clock.tick(60)

        back = pygame.draw.rect(screen, (255,255,255), ((0,0), (1080,720)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint(event.pos):
                    menusnd.play()
                    perdeu = False


        screen.fill((10,10,10))
        screen.blit(logo, (280, 40))
        screen.blit(gameoverimg, (285,320))


        screen.blit(cursor, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        pygame.display.flip()


def Howtoplay():
    howtoplay = True
    while howtoplay:
        clock.tick(60)

        back = pygame.draw.rect(screen, (255, 255, 255), ((0, 0), (1080, 720)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint(event.pos):
                    menusnd.play()
                    howtoplay = False


        screen.blit(howtoplayimg, (0,0))
        screen.blit(logo, (280, 40))

        screen.blit(cursor, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        pygame.display.flip()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.maxLife = 3
        self.life = self.maxLife
        self.indice = 0
        self.image = player[self.indice].convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 508
        self.rect.centery = 328
        self.lastupdate = pygame.time.get_ticks()
        self.rot = 0
        self.incx = 0
        self.incy = 0
        self.radius = int((self.rect.height/2) * 0.6)
        self.spawac = pygame.time.get_ticks()
        self.maskload = player_mask
        self.mask = pygame.mask.from_surface(self.maskload)

    def update(self):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_w] or keystate[pygame.K_a] or keystate[pygame.K_s] or keystate[pygame.K_d] :
            if pygame.time.get_ticks() - self.lastupdate > 50:
                self.lastupdate = pygame.time.get_ticks()
                self.indice += 1

        if keystate[pygame.K_SPACE]:
            self.Spray()

        if keystate[pygame.K_e]:
            self.Absorb()

        if self.indice >= len(player):
            self.indice = 0

        self.image = player[self.indice].convert()
        self.image.set_colorkey((0,0,0))


        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_rect().width / 2 - self.incx
        self.rect.centery = screen.get_rect().height / 2 - self.incy
        self.rot = math.atan2(mira.rect.centery - (height/2), mira.rect.centerx - (width/2))
        newimage = pygame.transform.rotate(self.image, 360 - self.rot *57.29)
        self.oldcenter = self.rect.center
        self.image = newimage
        self.maskrot = pygame.transform.rotate(self.maskload, 360 - self.rot *57.29)
        self.mask = pygame.mask.from_surface(self.maskrot)
        self.rect = self.image.get_rect()
        self.rect.center = self.oldcenter
        self.radius = int((self.rect.height / 2) * 0.6)
        if pygame.time.get_ticks() - self.spawac > 750:
            self.spawac = pygame.time.get_ticks()
            self.Anticorpos(self.rect.centerx, self.rect.centery)

        if self.life > self.maxLife:
            self.life = self.maxLife

    def Atirar(self):
        tiro = Tiro(self.rect.centerx + 64 * math.cos(self.rot) , self.rect.centery + 64 * math.sin(self.rot))
        tiros.add(tiro)
        all_sprites.add(tiro)
        shootsnd()

    def Anticorpos(self,x,y):
        anticorpo = AntiCorpos(x,y)
        anticorpos.add(anticorpo)
        all_sprites.add(anticorpo)

    def Spray(self):
        spray = Spray(self.rect.centerx + 64 * math.cos(self.rot) , self.rect.centery + 64 * math.sin(self.rot))
        sprays.add(spray)
        all_sprites.add(spray)
        spraysnd.play()

    def Absorb(self):
        hits = pygame.sprite.spritecollide(self, mobs, False)
        for hit in hits:
            if hit.stuned == True:
                hit.kill()
                hit.mystun.kill()
                self.life += 1
                swallow.play()



class Mira(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.indice = 0
        self.image = aim[self.indice]
        self.rect = self.image.get_rect()
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]
        self.mposx =  pygame.mouse.get_pos()[0]
        self.mposy =  pygame.mouse.get_pos()[1]

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]
        #self.indice = 1
        self.mposx = pygame.mouse.get_pos()[0]
        self.mposy = pygame.mouse.get_pos()[1]
        self.image = aim[self.indice]
        self.indice = 0


class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.orgimage = shoot
        self.angle = math.atan2(mira.rect.centery - ytela - (y),mira.rect.centerx - xtela - (x))
        self.image = pygame.transform.rotate(self.orgimage, 360 - self.angle * 57.29)
        self.rect = self.image.get_rect()
        self.rect.centery=  y
        self.rect.centerx = x 
        self.speedy = math.sin(self.angle) * 20
        self.speedx = math.cos(self.angle) * 20
                        

    def update(self):
        self.rect.bottom += self.speedy
        self.rect.centerx += self.speedx
        if self.rect.centerx > width - xtela or self.rect.centerx < 0:
            self.kill()
        if self.rect.bottom > height - ytela or self.rect.bottom <0:
            self.kill()

class Spray(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.ind = 0
        self.orgimage = spray[self.ind]
        self.angle = math.atan2(mira.rect.centery - ytela - (y),mira.rect.centerx - xtela - (x))
        self.image = pygame.transform.rotate(self.orgimage, 360 - self.angle * 57.29)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.last_update = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.last_update > 50:
            self.last_update = pygame.time.get_ticks()
            self.ind += 1
            if self.ind >= 4:
                self.kill()
            self.orgimage = spray[self.ind]
            self.image = pygame.transform.rotate(self.orgimage, 360 - self.angle * 57.29)



class Mob(pygame.sprite.Sprite):
    def __init__(self, spawnrange = random.randint(1, 4), x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.tamX = 64
        self.tamY = 64
        self.ind = 0
        self.ale = random.choice([0,1,2])
        self.image_orig = enemys[self.ale][self.ind]
        self.image = self.image_orig
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.spawnRange = spawnrange
        if self.spawnRange == 1:
            self.rect.centerx = random.randint(-70, width - self.tamX + 70)
            self.rect.centery = -70
        elif self.spawnRange == 2:
            self.rect.centerx = -70
            self.rect.centery = random.randint(-70, height + 70)
        elif self.spawnRange == 3:
            self.rect.centerx = random.randint(-70, width +70)
            self.rect.centery = height + 70
        elif self.spawnRange == 4:
            self.rect.centerx = width + 70
            self.rect.centery = random.randint(-70, height - self.tamY + 70)
        elif self.spawnRange == 5:
            self.rect.centerx = x
            self.rect.centery = y

        self.velX = 0
        self.velY = 0
        self.last_update = pygame.time.get_ticks()
        self.soma = 1
        self.speed = 4
        self.debuff = 0
        self.debufftimer = pygame.time.get_ticks()
        self.life = 3
        self.stuned = False
        self.recover = pygame.time.get_ticks()
        self.mystun = ''

    def update(self):
        self.rect.centerx += self.velX
        self.rect.centery += self.velY
        if playerone.rect.centerx > self.rect.centerx + 10:
            self.velX = self.speed
        elif playerone.rect.centerx < self.rect.centerx - 10:
            self.velX = -self.speed
        if playerone.rect.centery > self.rect.centery + 10:
            self.velY = self.speed
        elif playerone.rect.centery < self.rect.centery - 10:
            self.velY = -self.speed
        if pygame.time.get_ticks() - self.last_update > 50:
            self.last_update = pygame.time.get_ticks()
            self.ind += self.soma
            if self.ind >= len(enemys[self.ale]) -1:
                self.soma = -self.soma
            if self.ind <= 0:
                self.soma = -self.soma
        self.image_orig = enemys[self.ale][self.ind]

        if self.debuff > 0:
            if pygame.time.get_ticks() - self.debufftimer > 2000:
                self.debufftimer = pygame.time.get_ticks()
                self.debuff -= 1
                self.speed += 1

        if not self.stuned:
            if self.life == 1:
                self.speed = 0
                self.stuned = True
                self.recover = pygame.time.get_ticks()
                self.mystun = Stun(hit.rect.centerx, hit.rect.centery)
                all_sprites.add(self.mystun)

        if self.speed < 0:
            self.speed = 0

        if self.stuned:
            if pygame.time.get_ticks() - self.recover > 2500:
                self.recover = pygame.time.get_ticks()
                self.life += 1
                self.speed = 4
                self.stuned = False

        if self.life < 1:
            self.kill()
            self.mystun.kill()


        self.rot = (360 - (math.atan2(playerone.rect.centery - self.rect.centery , (playerone.rect.centerx) - self.rect.centerx )*57.29 ))
        new_image = pygame.transform.rotate(self.image_orig, self.rot)
        old_center = self.rect.center
        self.image = new_image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = old_center



class SpawnController(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.spawnTime = 3000
        self.startTime = pygame.time.get_ticks()
        self.rect.x = -10
        self.rect.y = -10


    def update(self):
        if pygame.time.get_ticks() - self.startTime >= self.spawnTime:
            self.startTime = pygame.time.get_ticks()
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)


class AntiCorpos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16,16))
        self.image.set_colorkey((0,0,0))
        self.circle = pygame.draw.circle(self.image, (255,255,255), (8,8), 8)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.lifetime = 10000
        self.last_update = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.last_update > self.lifetime:
            self.kill()


class Infection(pygame.sprite.Sprite):
    def __init__(self, create=False,x=random.randint(256, 2744),y =random.randint(256, 2744)):
        pygame.sprite.Sprite.__init__(self)
        self.image = infec
        self.rect = self.image.get_rect()
        if create:
            self.rect.centerx = x
            self.rect.centery = y
        else:
            self.rect.centerx = random.randint(256, 2744)
            self.rect.centery = random.randint(256, 2744)
        self.spawntime = pygame.time.get_ticks()
        self.life = 50

    def update(self):
        if pygame.time.get_ticks() - self.spawntime > 5000:
            self.spawntime = pygame.time.get_ticks()
            mob = Mob(5,self.rect.centerx, self.rect.centery)
            mobs.add(mob)
            all_sprites.add(mob)
        if self.life <= 0:
            self.kill()



class Smoke(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.indice = 0
        self.image = smoke_anim[self.indice]
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(256, 2744)
        self.rect.centery = random.randint(256, 2744)
        self.lifetime = 20000
        self.last_update = pygame.time.get_ticks()
        self.animate = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.last_update > self.lifetime:
            inf = Infection(True, self.rect.centerx, self.rect.centery)
            infections.add(inf)
            all_sprites.add(inf)
            self.kill()

        if pygame.time.get_ticks() - self.animate > 150:
            self.animate = pygame.time.get_ticks()
            self.indice += 1
            if self.indice >= len(smoke_anim):
                self.indice = 0

        self.image = smoke_anim[self.indice]



class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 80

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Stun(pygame.sprite.Sprite):
    def __init__(self, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = stun_anim[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery - 10
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 80
        self.animtime = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(stun_anim):
                self.frame = 0
            if pygame.time.get_ticks() - self.animtime > 2500:
                self.kill()

            else:
                centerx = self.rect.centerx
                centery = self.rect.centery
                self.image = stun_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.centerx = centerx
                self.rect.centery = centery


# Jogo
aberto = True
ismenu = True
gameover = True
isvictory = False
isgo = False
level = 3
while aberto:
    if isvictory:
        victoryscreen()
        isvictory = False
    if isgo:
        gameoverscreen()
        isgo = False
    if ismenu:
        menu()
        ismenu = False
    if gameover:
        mobs = pygame.sprite.Group()
        spawnController = SpawnController()
        all_sprites = pygame.sprite.Group()
        infections = pygame.sprite.Group()
        smokes = pygame.sprite.Group()
        all_sprites.add(spawnController)
        tiros = pygame.sprite.Group()
        sprays = pygame.sprite.Group()
        playerone = Player()
        players = pygame.sprite.Group()
        all_sprites.add(playerone)
        mira = Mira()
        players.add(mira)
        anticorpos = pygame.sprite.Group()
        xtela = 0
        ytela = 0
        pygame.mixer.music.set_volume(0.7)

        for x in range(level):
            inf = Infection()
            infections.add(inf)
            all_sprites.add(inf)
        gameover = False

    soundtrack()
    lifeind = 3 - playerone.life
    if lifeind > 2:
        lifeind = 2


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            aberto = False

        # Movimentação
        if event.type == pygame.MOUSEBUTTONDOWN:
            playerone.Atirar()
            mira.indice = 1
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_w]:
        ytela += 5
        playerone.incy += 5
    if keystate[pygame.K_s]:
        ytela -= 5
        playerone.incy -= 5
    if keystate[pygame.K_d]:
        xtela -= 5
        playerone.incx -= 5
    if keystate[pygame.K_a]:
        xtela += 5
        playerone.incx +=5

    # Tela
    tela2.fill((32, 0, 0))
    screen.fill((32,0,0))
    tela2.blit(bg,(0,0))
    all_sprites.update()
    all_sprites.draw(tela2)
    pygame.draw.rect(tela2, (255,255,255), ((0,0), (3000, 3000)),2)
    screen.blit(tela2, (xtela,ytela))


    #Plote dos ícones no minimapa
    minimapa.fill((0,0,0))
    for mob in mobs:
        pygame.draw.circle(minimapa, (210,60,60), (mob.rect.centerx // 25, mob.rect.centery // 25), 2)
    for inf in infections:
        pygame.draw.circle(minimapa, (155, 70, 240), (inf.rect.centerx // 25, inf.rect.centery // 25), 5)
    for smk in smokes:
        pygame.draw.circle(minimapa, (255,255,0), (smk.rect.centerx // 25, smk.rect.centery // 25), 5)
    pygame.draw.circle(minimapa, (255, 255, 255), (playerone.rect.centerx // 25, playerone.rect.centery // 25), 3)

    players.update()
    players.draw(screen)
    screen.blit(life[lifeind], (lifepos))
    screen.blit(minimapa, (932, 20))


    # Tiros
    hits = pygame.sprite.groupcollide(mobs,tiros, False, True)
    for hit in hits:
        hit.life -= 1
        if hit.life <= 0:
            expl = Explosion(hit.rect.center)
            all_sprites.add(expl)
            expl_snd2.play()

    if len(infections) == 0:
        spawnController.kill()
        if len(mobs) == 0:
            pygame.mixer.music.pause()
            music = False
            isvictory = True
            ismenu = True
            gameover = True

    if playerone.life == 0:
        pygame.mixer.music.pause()
        music = False
        isgo = True
        ismenu = True
        gameover = True


    hits = pygame.sprite.spritecollide(playerone, mobs, False, pygame.sprite.collide_mask)
    for hit in hits:
        if not hit.stuned:
            if pygame.time.get_ticks() - hit_delay > 2000:
                hit_delay = pygame.time.get_ticks()
                playerone.life -= 1
                dano.play()

    hits = pygame.sprite.groupcollide(mobs, anticorpos, False, True)
    for hit in hits:
        hit.speed -= 1

    hits = pygame.sprite.groupcollide(infections, tiros, False, True)
    for hit in hits:
        hit.life -= 1
        if hit.life <=0:
            expl_snd2.play()

    hits = pygame.sprite.groupcollide(sprays, smokes, False, True)

    if random.random() > 0.9995:
        newSmoke()


    # Rotação do personagema
    clock.tick(60)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
