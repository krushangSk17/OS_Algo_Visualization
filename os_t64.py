import pygame
pygame.init()

win = pygame.display.set_mode((1000,600))
pygame.display.set_caption("LOCK_VARIABLE")
font = pygame.font.SysFont('arial', 20)
font_b = pygame.font.SysFont('arial', 26,bold=1)
font_c = pygame.font.SysFont('arial', 16)
font_m = pygame.font.SysFont('arial',20,bold=1)

im_0 = pygame.transform.scale(pygame.image.load('0.png'), (100, 100))
im_1 = pygame.transform.scale(pygame.image.load('1.png'), (100, 100))
lock_img = pygame.transform.scale(pygame.image.load('lock.png'), (100, 100))
unlock_img = pygame.transform.scale(pygame.image.load('unlock.png'), (100, 100))
cs = pygame.transform.scale(pygame.image.load('cs.png'), (250, 250))
tru = pygame.transform.scale(pygame.image.load('true.png'), (40, 27))
clo = pygame.transform.scale(pygame.image.load('clo.png'), (40, 27))
com = pygame.transform.scale(pygame.image.load('com.png'), (50,50))


(x0,y0) = (50,130)
(x1,y1) = (50,400)
lock = 0

def redraw():

    global x0,x1,y0,y1
    win.fill((255, 255, 255))

    pygame.draw.rect(win,(240,250,245),(0,0,1000,800))
    #border of area
    pygame.draw.aaline(win,(0,0,0),(400,0),(400,600),6)
    pygame.draw.aaline(win,(0,0,0),(400+300,0),(400+300,600),6)
    pygame.draw.aaline(win,(0,0,0),(400-100,0),(400-100,600),6)
    pygame.draw.aaline(win,(0,0,0),(400-200,0),(400-200,600),6)
    pygame.draw.aaline(win,(0,0,0),(400+400,0),(400+400,600),6)
    pygame.draw.aaline(win, (0, 0, 0), (0,530), (1000,530), 6)
    pygame.draw.aaline(win, (0, 0, 0), (0,100), (1000,100), 6)

    pygame.draw.rect(win,(200,250,255),(0,250+15,200,330-250+20))

    i1 = font_c.render("HOW TO USE GUI", True, (50, 0, 200))
    i2 = font_c.render("key   Result", True, (255, 0, 0))
    i3 = font_c.render("0       move 0 to the right", True, (255, 0, 0))
    i4 = font_c.render("1       move 1 to the right", True, (255, 0, 0))
    i5 = font_c.render("R       reset screen", True, (255, 0, 0))
    win.blit(i1, (5, 260+15))
    win.blit(i2, (5, 270 + 5+15))
    win.blit(i3, (5, 280 + 10+15))
    win.blit(i4, (5, 290 + 15+15))
    win.blit(i5, (5, 300 + 20+15))

    sec1 = font_b.render("BEGIN",True,(0,0,0))
    sec2 = font_b.render("1",True,(0,0,0))
    sec3 = font_b.render("2",True,(0,0,0))
    sec4 = font_b.render("3",True,(0,0,0))
    sec5 = font_b.render("4", True, (0,0,0))
    sec6 = font_b.render("END", True, (0,0,0))
    win.blit(sec1,(72,550))
    win.blit(sec2,(50+200,550))
    win.blit(sec3,(45+300,550))
    win.blit(sec4,(45+500,550))
    win.blit(sec5,(45+700,550))
    win.blit(sec6,(70+800,550))

    sec_1 = font_c.render("1 - while(lock != 0);",True,(50,0,200))
    sec_2 = font_c.render("2 - lock = 1",True,(50,0,200))
    sec_3 = font_c.render("3 - { CS }",True,(50,0,200))
    sec_4 = font_c.render("4 - lock = 0",True,(50,0,200))
    pygame.draw.rect(win,(230,230,255),(0,20,200,80))
    win.blit(sec_1,(20,10+20))
    win.blit(sec_2,(20,25+20))
    win.blit(sec_3,(20,40+20))
    win.blit(sec_4,(20,55+20))

    if (lock == 1):
        for i in range(86):
            pygame.draw.aaline(win, (255, 0, 0), (200,101+5*i), (300,101+5*i), 4)
        win.blit(lock_img,(200,250))
        pygame.draw.rect(win, (255,200,200), (402, 20, 298, 80))
    else:
        win.blit(unlock_img, (200, 250))
        pygame.draw.rect(win, (200, 255, 200), (402, 20, 298, 80))

    cs_text = font_b.render("CRITICAL SECTION", True, (0, 0, 0))
    win.blit(cs_text, (450, 30))

    locktext = font.render("STATUS : LOCK = " + str(lock), True, (0,0,0))
    win.blit(locktext, (450,55))

    pygame.draw.rect(win, (253, 225, 130), (802, 20, 198, 80),0)
    pygame.draw.rect(win, (0, 0, 0), (800,20,160,27), 1)
    pygame.draw.rect(win, (0, 0, 0), (800,47,160,27), 1)
    pygame.draw.rect(win, (0, 0, 0), (800,74,160,27), 1)
    pygame.draw.rect(win, (0, 0, 0), (960,20,40,27), 1)
    pygame.draw.rect(win, (0, 0, 0), (960,47,40,27), 1)
    pygame.draw.rect(win, (0, 0, 0), (960,74,40,27), 1)

    pygame.draw.rect(win, (0, 0, 0), (400, 20, 300, 80), 1)
    pygame.draw.rect(win, (0, 0, 0), (0,20,200,80), 1)

    if(x0>200):
        win.blit(com,(225,130+25))
    if(x0>300):
        win.blit(com,(325,130+25))
    if(x0>400):
        win.blit(com,(525,130+25))
    if(x0>700):
        win.blit(com,(725,130+25))
    if(x1>200):
        win.blit(com,(225,400+25))
    if(x1>300):
        win.blit(com,(325,400+25))
    if(x1>400):
        win.blit(com,(525,400+25))
    if(x1>700):
        win.blit(com,(725,400+25))


    mutex = font_m.render("Mut-ex",True,(0,0,0))
    progress = font_m.render("Progress", True, (0, 0, 0))
    bound = font_m.render("Bounded wait", True, (0, 0, 0))
    win.blit(mutex, (820,20+1))
    win.blit(progress, (820, 20+1+27 ))
    win.blit(bound, (820, 20+1+27*2 ))

    win.blit(tru, (960, 47))
    win.blit(tru, (960, 74))

    if(x0 > 300 and x0 < 800 and x1 > 300 and x1 < 800):
        win.blit(clo, (960, 20))
    else:
        win.blit(tru, (960, 20))

    win.blit(cs, (425,175))

    win.blit(im_0, (x0, y0))
    win.blit(im_1, (x1, y1))

run =True
while run:

    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()


    if(keys[pygame.K_0] and x0 < 850):

        if (lock == 0 or x0 > 200):
            x0 += 2
        if(x0 > 300 and x0 <= 400):
            lock = 1
        if(x0 > 800):
            lock = 0

    if(keys[pygame.K_1] and x1 < 850):

        if(lock == 0 or x1 > 200):
            x1 += 2
        if(x1 > 300 and x1 <= 400):
            lock = 1
        if(x1 > 800):
            lock = 0

    if(keys[pygame.K_r]):
        x0 = x1 = 50
        lock = 0

    redraw()
    pygame.display.update()

pygame.quit()