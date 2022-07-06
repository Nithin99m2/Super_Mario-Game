import random
import math
from pygame import mixer
import pygame


pygame.init()
mixer.music.load("bgmusic.mp3")
mixer.music.play(-1)
zombie=[pygame.image.load("z1.png"),pygame.image.load("z2.png"),pygame.image.load("z3.png"),pygame.image.load("z4.png"),pygame.image.load("z5.png"),pygame.image.load("z6.png"),pygame.image.load("z7.png"),pygame.image.load("z8.png"),pygame.image.load("z9.png"),pygame.image.load("z10.png"),pygame.image.load("z11.png"),pygame.image.load("z12.png"),pygame.image.load("z13.png"),pygame.image.load("z14.png"),pygame.image.load("z15.png"),pygame.image.load("z16.png")]
zox=7100
zoy=350
zox1=7300
zoy1=350
zoy1_change=0
zoy_change=0

fortism=pygame.image.load("fd.png")
fex=10000
fey=370
fex_change=0
fey_change=0


over_font=pygame.font.Font("freesansbold.ttf",90)


def game_over():
    over_text = font.render("LEVEL-1" + "  cleared", True, (255,69,0))
    screen.blit(over_text, (290,250))
arrow=pygame.image.load("great.png")
ax1=10000
ay1=100
ax_change=0
ay_change=0
hand="hi"


helicopter=[pygame.image.load("he1.png"),pygame.image.load("res2.png"),pygame.image.load("he1.png"),pygame.image.load("res4.png"),]
hex=600
hey=100
clock = pygame.time.Clock()
x = 50
y = 455
screen = pygame.display.set_mode((800, 600))
bgpic = pygame.image.load("kom.png")
bx = 0
walkleft = [pygame.image.load("l3.png"), pygame.image.load("l3.png"), pygame.image.load("l4.png"),
            pygame.image.load("l5.png"), pygame.image.load("l6.png"), pygame.image.load("l7.png"),
            pygame.image.load("l8.png"), pygame.image.load("l9.png"), pygame.image.load("l10.png"), ]
walkright = [pygame.image.load("r2.png"), pygame.image.load("r3.png"), pygame.image.load("r4.png"),
             pygame.image.load("r5.png"), pygame.image.load("r6.png"), pygame.image.load("r7.png"),
             pygame.image.load("r8.png"), pygame.image.load("r9.png"), pygame.image.load("r10.png"), ]
coinsmov = [pygame.image.load("c1.png"), pygame.image.load("c2.png"), pygame.image.load("c3.png"),
            pygame.image.load("c4.png"),pygame.image.load("c5.png"), pygame.image.load("c6.png")]
thormov=[ pygame.image.load("t2.png"), pygame.image.load("t3.png"),pygame.image.load("t4.png"),pygame.image.load("t5.png"), pygame.image.load("t6.png"),pygame.image.load("t7.png"),pygame.image.load("t8.png"),pygame.image.load("t9.png")]
thorcos=pygame.image.load("t1.png")
flmov = [pygame.image.load("h1.png"),pygame.image.load("fl1.png"),pygame.image.load("fl2.png"),pygame.image.load("fl3.png"),pygame.image.load("fl4.png"),pygame.image.load("fl5.png"),pygame.image.load("fl6.png"),pygame.image.load("fl7.png"),pygame.image.load("fl8.png")]
fax = 2800
fay = 412
fax1=3900
fay1=412
fmovement = 0

cox = 220
coy = 222

stand = pygame.image.load("l1.png")

birdmov = [pygame.image.load("b1.png"), pygame.image.load("b10.png"), pygame.image.load("b2.png"),
           pygame.image.load("b3.png"), pygame.image.load("b4.png"), pygame.image.load("b5.png"),
           pygame.image.load("b6.png"), pygame.image.load("b7.png"), pygame.image.load("b8.png"),
           pygame.image.load("b9.png"), ]
mx = 800
my = 100

mx1 = 900
my1 = 200

pygame.display.set_caption("POLICE MARIO")
bullets = pygame.image.load("ec.png")
ix = 50
iy = 0
ix_change = 15
iy_change = 0
bullet_state = "Ready"

lbullet = pygame.image.load("lec.png")
lx = 50
ly = 0
lx_change = 15
ly_change = 0
l_state = "Ready"

x_change = 0
y_change = 0
walkcount = 0
sd = 0

left = False
right = False
zx_change = 0

fx_change = 0



fxleft = False
hand=False
def handism(a,b):
    global hand
    global ay_change
    if hand==False:
        ay_change=ay_change-1
    if ay_change==-7:
        hand=True
    if hand==True:
        ay_change=ay_change+1
    if ay_change==7:
        hand= False
    screen.blit(arrow, (a, b))




def animations(a, b):
    global walkcount

    if walkcount + 1 > 9:
        walkcount = 0
    if left:
        screen.blit(walkleft[walkcount], (a, b))
        walkcount = walkcount + 1

    elif right:
        screen.blit(walkright[walkcount], (a, b))
        walkcount = walkcount + 1
    else:
        screen.blit(stand, (a, b))

    pygame.display.update()

frmov=pygame.image.load("k2.png")

foxjump=False
fvelocity=1

def foxanimations(a, b):
    global fmovement
    global fax

    if fmovement + 1 > 7:
        fmovement = 0
    if fxleft==True:
        screen.blit(flmov[fmovement], (a, b))
        fmovement=fmovement+1
        fax=fax-2
    else:
        screen.blit(frmov,(a,b))


    pygame.display.update()



zpic=pygame.image.load("z10.png")
zomovement=0
zomovement1=0
zox_change=0
zox1_change=0
z_left=False
def zomanimations(a,b):
    global zox
    global zomovement
    if zomovement + 1 > 15:
        zomovement = 0
    if z_left==True:
        screen.blit(zombie[zomovement], (a, b))
        zomovement = zomovement + 1
        zox=zox-2
    else:
        screen.blit(zpic,(a,b))

    pygame.display.update()

z1_left=False
def zomanimations1(a,b):
    global zox1
    global zomovement1
    if zomovement1 + 1 > 15:
        zomovement1 = 0
    if z1_left==True:
        screen.blit(zombie[zomovement1], (a, b))
        zomovement1 = zomovement1 + 1
        zox1=zox1-2
    else:
        screen.blit(zpic,(a,b))

    pygame.display.update()






fxleft1=False
def foxanimations1(a, b):
    global fmovement
    global fax1

    if fmovement + 1 > 7:
        fmovement = 0
    if fxleft1==True:
        screen.blit(flmov[fmovement], (a, b))
        fmovement=fmovement+1
        fax1=fax1-2
    else:
        screen.blit(frmov,(a,b))


    pygame.display.update()


tmovement=0
tax=4670
tay=390
tleft=False
def tanimations(a, b):
    global tmovement
    global tax

    if tmovement + 1 > 7:
        tmovement = 0
    if tleft==True:
        screen.blit(thormov[tmovement], (a, b))
        tmovement=tmovement+1
        tax=tax-4
    else:
        screen.blit(thorcos,(a,b))


    pygame.display.update()



birdcount = 0


def birdism(a, b):
    global birdcount

    if birdcount + 1 > 9:
        birdcount = 0
    birdcount = birdcount + 1

    screen.blit(birdmov[birdcount], (a, b))


def birdism2(a, b):
    global birdcount
    if birdcount + 1 > 9:
        birdcount = 0
    birdcount = birdcount + 1

    screen.blit(birdmov[birdcount], (a, b))


coincount = 0


def coinism(a, b):
    global coincount
    if coincount + 1 > 5:
        coincount = 0
    coincount = coincount + 1
    screen.blit(coinsmov[coincount], (a, b))


jumping = False
velocity = 1
sc = 250
sy = 400


def injec(a, b):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bullets, (a + 20, b + 25))


def lef(a, b):
    global l_state
    l_state = "Fire"
    screen.blit(lbullet, (a + 20, b + 25))


score_gained = 0
font = pygame.font.Font("freesansbold.ttf", 34)
scX = 10
scY = 10

over_font = pygame.font.Font("freesansbold.ttf", 64)


def points(a, b):
    score = font.render("SCORE:" + str(score_gained), True, (0, 100, 0))
    screen.blit(score, (a, b))

dplay=False
def dogism():
    global dplay
    if dplay==True:
        dog_sound = mixer.Sound('deepbark.wav')
        dog_sound.play()

fy1_change=0
f1velocity=1
foxjump1=False


zx = 670
zx1 = 930
zx2 = 1300
zx3 = 1360
zx4 = 1420
zx5 = 1480
zx6 = 1540
zx7 = 1970
zx8 = 1920
zx9 = 2020
zx10 = 1970
zx11 = 2940
zx12 = 2900
zx13 = 2870
zx14 = 2990
zx15 = 3020
zx16 = 4256
zx17 = 4510
zx18 = 3300
zx19 = 6000
zx20 = 5950
zx21 = 6050
zx22 = 6000
zx23 = 6500
zx24 = 6450
zx25 = 6400
zx26 = 6550
zx27 = 6600
zx28 = 7840
zx30 = 7900
tx_change=0
fy_change=0


tay_change=0
tvelocity=1
villainjump=False

bx = 0
cx = 00
running = True
while running:
    clock.tick(24)
    rel_x = bx % bgpic.get_rect().width

    screen.blit(bgpic, (rel_x - bgpic.get_rect().width, 0))
    if rel_x < 800:
        screen.blit(bgpic, (rel_x, 0))
    bx = bx + cx

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = x_change - 0.5
                left = True
                right = False
                cx = cx + 7
                zx_change = zx_change - 7
                fx_change= fx_change - 7
                tx_change = tx_change - 7
                zox_change=zox_change -7
                zox1_change = zox1_change - 7
                ax_change=ax_change - 7
                fex_change=fex_change-7





            if event.key == pygame.K_RIGHT:
                x_change = x_change + 0.5
                right = True
                left = False
                cx = cx - 7
                zx_change = zx_change + 7
                fx_change=fx_change + 7
                tx_change=tx_change+7
                zox_change=zox_change + 7
                zox1_change = zox1_change + 7
                ax_change=ax_change + 7
                fex_change=fex_change+7




            if event.key == pygame.K_UP:
                bullet_sound = mixer.Sound("jumps2.wav")
                bullet_sound.play()

                if jumping == False:
                    jumping = True

                    y_change = -25

            if event.key == pygame.K_d:
                hamesh_sound = mixer.Sound("fasd.wav")
                hamesh_sound.play()
                if bullet_state == "Ready":

                    iy = y
                    injec(ix, iy)
            if event.key == pygame.K_a:
                if l_state == "Ready":
                    ly = y
                    lef(lx, ly)
            if event.key == pygame.K_d:
                if bullet_state == "Ready":
                    iy = y
                    ix = x
                    injec(ix, iy)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
                left = False
                right = False
                cx = 0
                zx_change = 0
                fx_change=0
                tx_change=0
                zox_change=0
                zox1_change=0
                ax_change=0
                fex_change=0



            elif event.key == pygame.K_RIGHT:
                x_change = 0
                right = False
                left = False
                cx = 0
                zx_change = 0
                fx_change=0
                tx_change=0
                zox_change=0
                zox1_change=0
                ax_change=0
                fex_change=0


    keys = pygame.key.get_pressed()

    x = x + x_change
    ax1=ax1-ax_change
    fex=fex-fex_change

    y = y + y_change
    mx = mx - 10
    if (x>=382 and x<=452 and mx<0) or (x>569 and x<680 and mx<0):
        mx=random.randint(800,810)
        my=random.randint(90,100)

        birdism(mx,my)
    if (x>=359 and x<=452 and mx1<0) or (x>569 and x<680 and mx1<0):
        mx1=random.randint(900,910)
        my1=random.randint(190,200)

        birdism2(mx1,my1)


    print(x)


    mx1 = mx1 - 8
    fax=fax-fx_change
    fax1=fax1-fx_change
    tax=tax-tx_change
    zox=zox-zox_change
    zox1=zox1-zox1_change


    keys = pygame.key.get_pressed()
    px1 = 400
    py1 = 350

    if jumping == True:
        y_change += velocity

    s1x = 208
    s2x = 177
    s3x = 155
    s4x = 126
    s5x = 108
    s6x = 266
    s7x = 91
    s8x = 242
    s9x = 330
    s10x = 347
    s11x = 365.3
    s12x = 393
    s13x = 416
    s14x = 447
    s15x = 481
    s16x = 505
    s17x = 568.5
    s18x = 586
    s19x = 604
    s20x = 633
    s21x = 655
    s22x = 686
    es1 = 108
    es2 = 277
    es3 = 347
    es4 = 515
    es5 = 586

    d1 = math.sqrt((math.pow(x - s1x, 2)))
    d2 = math.sqrt((math.pow(x - s2x, 2)))
    d3 = math.sqrt((math.pow(x - s3x, 2)))
    d4 = math.sqrt((math.pow(x - s4x, 2)))
    d5 = math.sqrt((math.pow(x - s5x, 2)))
    d6 = math.sqrt((math.pow(x - s6x, 2)))
    d7 = math.sqrt((math.pow(x - s7x, 2)))
    d8 = math.sqrt((math.pow(x - s8x, 2)))
    d9 = math.sqrt((math.pow(x - s9x, 2)))
    d10 = math.sqrt((math.pow(x - s10x, 2)))
    d11 = math.sqrt((math.pow(x - s11x, 2)))
    d12 = math.sqrt((math.pow(x - s12x, 2)))
    d13 = math.sqrt((math.pow(x - s13x, 2)))
    d14 = math.sqrt((math.pow(x - s14x, 2)))
    d15 = math.sqrt((math.pow(x - s15x, 2)))
    d16 = math.sqrt((math.pow(x - s16x, 2)))
    d17 = math.sqrt((math.pow(x - s17x, 2)))
    d18 = math.sqrt((math.pow(x - s18x, 2)))
    d19 = math.sqrt((math.pow(x - s19x, 2)))
    d20 = math.sqrt((math.pow(x - s20x, 2)))
    d21 = math.sqrt((math.pow(x - s21x, 2)))
    d22 = math.sqrt((math.pow(x - s22x, 2)))

    d23 = math.sqrt((math.pow(x - es1, 2)))
    d24 = math.sqrt((math.pow(x - es2, 2)))
    d25 = math.sqrt((math.pow(x - es3, 2)))
    d26 = math.sqrt((math.pow(x - es4, 2)))
    d27 = math.sqrt((math.pow(x - es5, 2)))

    if d1 < 3 and y > 300 and y < 310:
        y_change = 0
        print("true")
        if (keys[pygame.K_UP]):
            y_change = -25

    elif d2 < 4 and y > 300 and y < 310:
        y_change = 0
        print("g")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d3 < 4 and y > 330 and y < 340:
        y_change = 0
        print("l")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d4 < 4 and y > 370 and y < 390:
        y_change = 0
        print("k")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d5 < 7 and y > 300 and y < 310:
        y_change = 0
        print("n")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d6 < 5 and y > 300 and y < 310:
        y_change = 0
        print("q")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d7 < 2 and y > 300 and y < 310:
        y_change = 0
        print("i")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d8 < 3 and y > 455:
        y_change = 3
    elif d9 < 3 and y > 300 and y < 310:
        y_change = 0
        print('h')
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d10 < 8 and y > 300 and y < 310:
        y_change = 0
        print('u')
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d11 < 4 and y > 370 and y < 390:
        y_change = 0
        print('u')
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d12 < 4 and y > 330 and y < 340:
        y_change = 0
        print("l")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d13 < 4 and y > 300 and y < 310:
        y_change = 0
        print("g")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d14 < 3 and y > 300 and y < 310:
        y_change = 0
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d15 < 3 and y > 455:
        y_change = 3
    elif d16 < 5 and y > 300 and y < 310:
        y_change = 0
        print("q")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d17 < 2 and y > 300 and y < 310:
        y_change = 0
        print("i")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d18 < 8 and y > 300 and y < 310:
        y_change = 0
        print("n")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d19 < 4 and y > 370 and y < 390:
        y_change = 0
        print("k")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d20 < 4 and y > 330 and y < 340:
        y_change = 0
        print("l")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d21 < 4 and y > 300 and y < 310:
        y_change = 0
        print("l")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d22 < 3 and y > 300 and y < 310:
        y_change = 0
        print("true")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d23 < 3 and y > 120 and y < 140:
        y_change = 0
        print("true")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d24 < 7 and y > 130 and y < 140:
        y_change = 0
        print("q")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d25 < 2 and y > 120 and y < 140:
        y_change = 0
        print("q")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d26 < 7 and y > 130 and y < 140:
        y_change = 0
        print("q")
        if (keys[pygame.K_UP]):
            y_change = -25
    elif d27 < 2 and y > 120 and y < 140:
        y_change = 0
        print("q")
        if (keys[pygame.K_UP]):
            y_change = -25




    else:
        y_change += velocity

    if x >= 124 and x <= 130 and y > 390:
        print("true")
        x_change = 0
        cx = 0
    elif x == 152 and y > 340:
        x_change = 0
        cx = 0

    if y > 450 and x != 240 and x != 241 and x != 242 and x != 243 and x != 244 and x != 481 and x != 482 and x != 483 and x != 480 and x != 479 and x!=710:
        y = 455
        jumping = False

    if ix > 900:
        ix = x
        bullet_state = "Ready"
    if lx < 0:
        lx = x
        l_state = "Ready"
    if bullet_state == "Fire":
        injec(ix, iy)
        ix += ix_change
    if l_state == "Fire":
        lef(lx, ly)
        lx -= lx_change


    zx = zx - zx_change
    zx1 = zx1 - zx_change
    zx2 = zx2 - zx_change
    zx3 = zx3 - zx_change
    zx4 = zx4 - zx_change
    zx5 = zx5 - zx_change
    zx6 = zx6 - zx_change
    zx7 = zx7 - zx_change
    zx8 = zx8 - zx_change
    zx9 = zx9 - zx_change
    zx10 = zx10 - zx_change
    zx11 = zx11 - zx_change
    zx12 = zx12 - zx_change
    zx13 = zx13 - zx_change
    zx14 = zx14 - zx_change
    zx15 = zx15 - zx_change
    zx16 = zx16 - zx_change
    zx17 = zx17 - zx_change
    zx18 = zx18 - zx_change
    zx19 = zx19 - zx_change
    zx20 = zx20 - zx_change
    zx21 = zx21 - zx_change
    zx22 = zx22 - zx_change
    zx23 = zx23 - zx_change
    zx24 = zx24 - zx_change
    zx25 = zx25 - zx_change
    zx26 = zx26 - zx_change
    zx27 = zx27 - zx_change
    zx28 = zx28 - zx_change
    zx30 = zx30 - zx_change
    zy = 300
    zy1 = 150
    zy2 = 455
    zy3 = 455
    zy4 = 455
    zy5 = 455
    zy6 = 455
    zy7 = 140
    zy8 = 200
    zy9 = 200
    zy10 = 250
    zy11 = 340
    zy12 = 380
    zy13 = 420

    zy14 = 380
    zy15 = 420
    zy16 = 300
    zy17 = 150
    zy18 = 310
    zy19 = 170
    zy20 = 230
    zy21 = 230
    zy22 = 280
    zy23 = 340
    zy24 = 380
    zy25 = 420
    zy26 = 380
    zy27 = 420
    zy28 = 300

    animations(x, y)
    birdism(mx, my)
    birdism(mx1, my1)
    coinism(zx, zy)
    coinism(zx1, zy1)
    coinism(zx2, zy2)
    coinism(zx3, zy3)
    coinism(zx4, zy3)
    coinism(zx5, zy5)
    coinism(zx6, zy6)
    coinism(zx7, zy7)
    coinism(zx8, zy8)
    coinism(zx9, zy9)
    coinism(zx10, zy10)
    coinism(zx11, zy11)
    coinism(zx12, zy12)
    coinism(zx13, zy13)
    coinism(zx14, zy14)
    coinism(zx15, zy15)
    coinism(zx16, zy16)
    coinism(zx17, zy17)
    coinism(zx18, zy18)
    coinism(zx19, zy19)
    coinism(zx20, zy20)
    coinism(zx21, zy21)
    coinism(zx22, zy22)
    coinism(zx23, zy23)
    coinism(zx24, zy24)
    coinism(zx25, zy25)
    coinism(zx26, zy26)
    coinism(zx27, zy27)
    coinism(zx28, zy28)



    r1 = math.sqrt(((x - zx) ** 2) + ((y - zy) ** 2))
    r2 = math.sqrt(((x - zx1) ** 2) + ((y - zy1) ** 2))
    r3 = math.sqrt(((x - zx2) ** 2) + ((y - zy2) ** 2))
    r4 = math.sqrt(((x - zx3) ** 2) + ((y - zy3) ** 2))
    r5 = math.sqrt(((x - zx4) ** 2) + ((y - zy4) ** 2))
    r6 = math.sqrt(((x - zx5) ** 2) + ((y - zy5) ** 2))
    r7 = math.sqrt(((x - zx6) ** 2) + ((y - zy6) ** 2))
    r8 = math.sqrt(((x - zx7) ** 2) + ((y - zy7) ** 2))
    r9 = math.sqrt(((x - zx8) ** 2) + ((y - zy8) ** 2))
    r10 = math.sqrt(((x - zx9) ** 2) + ((y - zy9) ** 2))
    r11 = math.sqrt(((x - zx10) ** 2) + ((y - zy10) ** 2))
    r12 = math.sqrt(((x - zx11) ** 2) + ((y - zy11) ** 2))
    r13 = math.sqrt(((x - zx12) ** 2) + ((y - zy12) ** 2))
    r14 = math.sqrt(((x - zx13) ** 2) + ((y - zy13) ** 2))
    r15 = math.sqrt(((x - zx14) ** 2) + ((y - zy14) ** 2))
    r16 = math.sqrt(((x - zx15) ** 2) + ((y - zy15) ** 2))
    r17 = math.sqrt(((x - zx16) ** 2) + ((y - zy16) ** 2))
    r18 = math.sqrt(((x - zx17) ** 2) + ((y - zy17) ** 2))
    r19 = math.sqrt(((x - zx18) ** 2) + ((y - zy18) ** 2))
    r20 = math.sqrt(((x - zx19) ** 2) + ((y - zy19) ** 2))
    r21 = math.sqrt(((x - zx20) ** 2) + ((y - zy20) ** 2))
    r22 = math.sqrt(((x - zx21) ** 2) + ((y - zy21) ** 2))
    r23 = math.sqrt(((x - zx22) ** 2) + ((y - zy22) ** 2))
    r24 = math.sqrt(((x - zx23) ** 2) + ((y - zy23) ** 2))
    r25 = math.sqrt(((x - zx24) ** 2) + ((y - zy24) ** 2))
    r26 = math.sqrt(((x - zx25) ** 2) + ((y - zy25) ** 2))
    r27 = math.sqrt(((x - zx26) ** 2) + ((y - zy26) ** 2))
    r28 = math.sqrt(((x - zx27) ** 2) + ((y - zy27) ** 2))
    r29 = math.sqrt(((x - zx28) ** 2) + ((y - zy28) ** 2))

    if r1 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()

        zx = random.randint(10000000, 20000000)
        zy = random.randint(3000, 3010)
        coinism(zx, zy)
        score_gained = score_gained + 1
    elif r2 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx1 = random.randint(10000000, 20000000)
        zy1 = random.randint(3000, 3010)
        coinism(zx1, zy1)
        score_gained = score_gained + 1
    elif r3 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx2 = random.randint(10000000, 20000000)
        zy2 = random.randint(3000, 3010)
        coinism(zx2, zy2)
        score_gained = score_gained + 1
    elif r4 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx3 = random.randint(10000000, 20000000)
        zy3 = random.randint(3000, 3010)
        coinism(zx3, zy3)
        score_gained = score_gained + 1
    elif r5 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx4 = random.randint(10000000, 20000000)
        zy4 = random.randint(3000, 3010)
        coinism(zx4, zy4)
        score_gained = score_gained + 1
    elif r6 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx5 = random.randint(10000000, 20000000)
        zy5 = random.randint(3000, 3010)
        coinism(zx5, zy5)
        score_gained = score_gained + 1
    elif r7 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx6 = random.randint(10000000, 20000000)
        zy6 = random.randint(3000, 3010)
        coinism(zx6, zy6)
        score_gained = score_gained + 1
    elif r8 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx7 = random.randint(10000000, 20000000)
        zy7 = random.randint(3000, 3010)
        coinism(zx7, zy7)
        score_gained = score_gained + 1
    elif r9 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx8 = random.randint(10000000, 20000000)
        zy8 = random.randint(3000, 3010)
        coinism(zx8, zy8)
        score_gained = score_gained + 1
    elif r10 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx9 = random.randint(10000000, 20000000)
        zy9 = random.randint(3000, 3010)
        coinism(zx9, zy9)
        score_gained = score_gained + 1
    elif r11 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx10 = random.randint(10000000, 20000000)
        zy10 = random.randint(3000, 3010)
        coinism(zx10, zy10)
        score_gained = score_gained + 1
    elif r12 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx11 = random.randint(10000000, 20000000)
        zy11 = random.randint(3000, 3010)
        coinism(zx11, zy11)
        score_gained = score_gained + 1
    elif r13 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx12 = random.randint(10000000, 20000000)
        zy12 = random.randint(3000, 3010)
        coinism(zx12, zy12)
        score_gained = score_gained + 1
    elif r14 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx13 = random.randint(10000000, 20000000)
        zy13 = random.randint(3000, 3010)
        coinism(zx13, zy13)
        score_gained = score_gained + 1
    elif r15 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx14 = random.randint(10000000, 20000000)
        zy14 = random.randint(3000, 3010)
        coinism(zx14, zy14)
        score_gained = score_gained + 1
    elif r16 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx15 = random.randint(10000000, 20000000)
        zy15 = random.randint(3000, 3010)
        coinism(zx15, zy15)
        score_gained = score_gained + 1
    elif r17 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx16 = random.randint(10000000, 20000000)
        zy16 = random.randint(3000, 3010)
        coinism(zx16, zy16)
        score_gained = score_gained + 1
    elif r18 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx17 = random.randint(10000000, 20000000)
        zy17 = random.randint(3000, 3010)
        coinism(zx17, zy17)
        score_gained = score_gained + 1
    elif r19 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx18 = random.randint(10000000, 20000000)
        zy18 = random.randint(3000, 3010)
        coinism(zx18, zy18)
        score_gained = score_gained + 1
    elif r20 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx19 = random.randint(100000, 200000)
        zy19 = random.randint(3000, 3010)
        coinism(zx19, zy19)
        score_gained = score_gained + 1
    elif r21 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx20 = random.randint(100000, 200000)
        zy20 = random.randint(3000, 3010)
        coinism(zx20, zy20)
        score_gained = score_gained + 1
    elif r22 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx21 = random.randint(100000, 200000)
        zy21 = random.randint(3000, 3010)
        coinism(zx21, zy21)
        score_gained = score_gained + 1
    elif r23 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx22 = random.randint(100000, 200000)
        zy22 = random.randint(3000, 3010)
        coinism(zx22, zy22)
        score_gained = score_gained + 1
    elif r24 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx23 = random.randint(100000, 200000)
        zy23 = random.randint(3000, 3010)
        coinism(zx23, zy23)
        score_gained = score_gained + 1
    elif r25 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx24 = random.randint(100000, 200000)
        zy24 = random.randint(3000, 3010)
        coinism(zx24, zy24)
        score_gained = score_gained + 1
    elif r26 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx25 = random.randint(100000, 200000)
        zy25 = random.randint(3000, 3010)
        coinism(zx25, zy25)
        score_gained = score_gained + 1
    elif r27 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx26 = random.randint(100000, 200000)
        zy26 = random.randint(3000, 3010)
        coinism(zx26, zy26)
        score_gained = score_gained + 1
    elif r28 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx27 = random.randint(100000, 200000)
        zy27 = random.randint(3000, 3010)
        coinism(zx27, zy27)
        score_gained = score_gained + 1
    elif r29 < 27:
        coin_sound = mixer.Sound("coinwav.wav")
        coin_sound.play()
        zx28 = random.randint(100000, 200000)
        zy28 = random.randint(3000, 3010)
        coinism(zx28, zy28)
        score_gained = score_gained + 1



    exd=math.sqrt(((x - fax) ** 2) + ((y - fay) ** 2))
    exd1=math.sqrt(((x - fax1) ** 2) + ((y - fay1) ** 2))
    txd=math.sqrt((math.pow(x-tax,2)))
    exd2=math.sqrt(((x - zox) ** 2) + ((y - zoy) ** 2))
    exd3 = math.sqrt(((x - zox1) ** 2) + ((y - zoy1) ** 2))






    injd1=math.sqrt(((ix - fax) ** 2) + ((iy - fay) ** 2))
    if exd<300:
        dplay=True
        fxleft=True



    else:
        dplay=False
        fxleft=False
    if exd1<300:
        dplay=True



        fxleft1=True
    else:

        fxleft1=False

    if txd < 300:
        tleft=True
    else:
        tleft=False

    if exd2<200:
        zom_sound1 = mixer.Sound("zombiewav.wav")
        zom_sound1.play()
        print("xxx")
        z_left=True
    if (x>=465 and x<=477) and zox<=487:
        z_left=False
        zoy_change=zoy_change+1

    if exd3<400:
        zom_sound = mixer.Sound("zombiewav.wav")
        zom_sound.play()
        print("1xxx")
        z1_left=True
    if (x>=465 and x<=477) and zox1<=487:
        z1_left=False
        zoy1_change=zoy1_change+1

    print(bx)



    zoy = zoy + zoy_change
    zoy1=zoy1+zoy1_change






    injd2=math.sqrt(((ix - fax1) ** 2) + ((iy - fay1) ** 2))
    injd3=math.sqrt(((ix - tax) ** 2) + ((iy - tay) ** 2))



    fay=fay+fy_change
    if injd1 < 50:
        fxleft=False


        print("tr")
        iy = y
        bullet_state = "Ready"
        if foxjump == False:
            foxjump = True
            fy_change = -15











    if foxjump == True:
        fy_change += fvelocity


    if injd2 < 50:
        dplay = False
        dogism()
        fxleft1=False

        print("tr")
        iy = y
        bullet_state = "Ready"
        if foxjump1 == False:
            foxjump1 = True
            fy1_change = -15

    if injd3 < 50:
        tleft=False


        print("tr")
        iy = y
        bullet_state = "Ready"
        if villainjump == False:
            villainjump = True
            tay_change = -15

    if villainjump == True:
        tay_change += tvelocity




    if foxjump1 == True:
        fy1_change += f1velocity
        


    fay1=fay1+fy1_change
    tay=tay+tay_change

    if x>=660:
        handism(ax1,ay1)



    ay1=ay1+ay_change


    if x>=715:
        game_over()
        hand!=False
        hand!=True
    points(scX, scY)
    animations(x, y)
    foxanimations(fax, fay)
    foxanimations1(fax1,fay1)
    tanimations(tax,tay)
    dogism()
    zomanimations(zox,zoy)
    screen.blit(fortism,(fex,fey))

    zomanimations1(zox1, zoy1 )
    pygame.display.update()
