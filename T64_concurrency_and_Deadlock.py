import tkinter as tk
import pygame

parent = tk.Tk()
parent.geometry("700x700")
parent.configure(bg='#32A3A0')
parent.title("T-64 CONCURRENCY AND DEADLOCK")


def lock_variable():
    pygame.init()
    win = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("LOCK_VARIABLE")
    font = pygame.font.SysFont('arial', 20)
    font_b = pygame.font.SysFont('arial', 26, bold=1)
    font_c = pygame.font.SysFont('arial', 16)
    font_m = pygame.font.SysFont('arial', 20, bold=1)

    im_0 = pygame.transform.scale(pygame.image.load('P0.png'), (100, 100))
    im_1 = pygame.transform.scale(pygame.image.load('P1.png'), (100, 100))
    lock_img = pygame.transform.scale(pygame.image.load('lock.png'), (100, 100))
    unlock_img = pygame.transform.scale(pygame.image.load('unlock.png'), (100, 100))
    cs = pygame.transform.scale(pygame.image.load('cs.png'), (250, 250))
    tru = pygame.transform.scale(pygame.image.load('true.png'), (40, 27))
    clo = pygame.transform.scale(pygame.image.load('clo.png'), (40, 27))
    com = pygame.transform.scale(pygame.image.load('com.png'), (50, 50))

    (x0, y0) = (50, 130)
    (x1, y1) = (50, 400)
    lock = 0

    def redraw():

        # global x0, x1, y0, y1
        win.fill((255, 255, 255))

        pygame.draw.rect(win, (240, 250, 245), (0, 0, 1000, 800))
        # border of area
        pygame.draw.aaline(win, (0, 0, 0), (400, 0), (400, 600), 6)
        pygame.draw.aaline(win, (0, 0, 0), (400 + 300, 0), (400 + 300, 600), 6)
        pygame.draw.aaline(win, (0, 0, 0), (400 - 100, 0), (400 - 100, 600), 6)
        pygame.draw.aaline(win, (0, 0, 0), (400 - 200, 0), (400 - 200, 600), 6)
        pygame.draw.aaline(win, (0, 0, 0), (400 + 400, 0), (400 + 400, 600), 6)
        pygame.draw.aaline(win, (0, 0, 0), (0, 530), (1000, 530), 6)
        pygame.draw.aaline(win, (0, 0, 0), (0, 100), (1000, 100), 6)

        pygame.draw.rect(win, (200, 250, 255), (0, 250 + 15, 200, 330 - 250 + 20))

        i1 = font_c.render("HOW TO USE GUI", True, (50, 0, 200))
        i2 = font_c.render("key   Result", True, (255, 0, 0))
        i3 = font_c.render("0       move 0 to the right", True, (255, 0, 0))
        i4 = font_c.render("1       move 1 to the right", True, (255, 0, 0))
        i5 = font_c.render("R       reset screen", True, (255, 0, 0))
        win.blit(i1, (5, 260 + 15))
        win.blit(i2, (5, 270 + 5 + 15))
        win.blit(i3, (5, 280 + 10 + 15))
        win.blit(i4, (5, 290 + 15 + 15))
        win.blit(i5, (5, 300 + 20 + 15))

        sec1 = font_b.render("BEGIN", True, (0, 0, 0))
        sec2 = font_b.render("1", True, (0, 0, 0))
        sec3 = font_b.render("2", True, (0, 0, 0))
        sec4 = font_b.render("3", True, (0, 0, 0))
        sec5 = font_b.render("4", True, (0, 0, 0))
        sec6 = font_b.render("END", True, (0, 0, 0))
        win.blit(sec1, (72, 550))
        win.blit(sec2, (50 + 200, 550))
        win.blit(sec3, (45 + 300, 550))
        win.blit(sec4, (45 + 500, 550))
        win.blit(sec5, (45 + 700, 550))
        win.blit(sec6, (70 + 800, 550))

        sec_1 = font_c.render("1 - while(lock != 0);", True, (50, 0, 200))
        sec_2 = font_c.render("2 - lock = 1", True, (50, 0, 200))
        sec_3 = font_c.render("3 - { CS }", True, (50, 0, 200))
        sec_4 = font_c.render("4 - lock = 0", True, (50, 0, 200))
        pygame.draw.rect(win, (230, 230, 255), (0, 20, 200, 80))
        win.blit(sec_1, (20, 10 + 20))
        win.blit(sec_2, (20, 25 + 20))
        win.blit(sec_3, (20, 40 + 20))
        win.blit(sec_4, (20, 55 + 20))

        if (lock == 1):
            for i in range(86):
                pygame.draw.aaline(win, (255, 0, 0), (200, 101 + 5 * i), (300, 101 + 5 * i), 4)
            win.blit(lock_img, (200, 250))
            pygame.draw.rect(win, (255, 200, 200), (402, 20, 298, 80))
        else:
            win.blit(unlock_img, (200, 250))
            pygame.draw.rect(win, (200, 255, 200), (402, 20, 298, 80))

        cs_text = font_b.render("CRITICAL SECTION", True, (0, 0, 0))
        win.blit(cs_text, (450, 30))

        locktext = font.render("STATUS : LOCK = " + str(lock), True, (0, 0, 0))
        win.blit(locktext, (450, 55))

        pygame.draw.rect(win, (253, 225, 130), (802, 20, 198, 80), 0)
        pygame.draw.rect(win, (0, 0, 0), (800, 20, 160, 27), 1)
        pygame.draw.rect(win, (0, 0, 0), (800, 47, 160, 27), 1)
        pygame.draw.rect(win, (0, 0, 0), (800, 74, 160, 27), 1)
        pygame.draw.rect(win, (0, 0, 0), (960, 20, 40, 27), 1)
        pygame.draw.rect(win, (0, 0, 0), (960, 47, 40, 27), 1)
        pygame.draw.rect(win, (0, 0, 0), (960, 74, 40, 27), 1)

        pygame.draw.rect(win, (0, 0, 0), (400, 20, 300, 80), 1)
        pygame.draw.rect(win, (0, 0, 0), (0, 20, 200, 80), 1)

        if (x0 > 200):
            win.blit(com, (225, 130 + 25))
        if (x0 > 300):
            win.blit(com, (325, 130 + 25))
        if (x0 > 400):
            win.blit(com, (525, 130 + 25))
        if (x0 > 700):
            win.blit(com, (725, 130 + 25))
        if (x1 > 200):
            win.blit(com, (225, 400 + 25))
        if (x1 > 300):
            win.blit(com, (325, 400 + 25))
        if (x1 > 400):
            win.blit(com, (525, 400 + 25))
        if (x1 > 700):
            win.blit(com, (725, 400 + 25))

        mutex = font_m.render("Mut-ex", True, (0, 0, 0))
        progress = font_m.render("Progress", True, (0, 0, 0))
        bound = font_m.render("Bounded wait", True, (0, 0, 0))
        win.blit(mutex, (820, 20 + 1))
        win.blit(progress, (820, 20 + 1 + 27))
        win.blit(bound, (820, 20 + 1 + 27 * 2))

        win.blit(tru, (960, 47))
        win.blit(tru, (960, 74))

        if (x0 > 300 and x0 < 800 and x1 > 300 and x1 < 800):
            win.blit(clo, (960, 20))
        else:
            win.blit(tru, (960, 20))

        win.blit(cs, (425, 175))

        win.blit(im_0, (x0, y0))
        win.blit(im_1, (x1, y1))

    run = True
    while run:

        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_0] and x0 < 850):

            if (lock == 0 or x0 > 200):
                x0 += 2
            if (x0 > 300 and x0 <= 400):
                lock = 1
            if (x0 > 800):
                lock = 0

        if (keys[pygame.K_1] and x1 < 850):

            if (lock == 0 or x1 > 200):
                x1 += 2
            if (x1 > 300 and x1 <= 400):
                lock = 1
            if (x1 > 800):
                lock = 0

        if (keys[pygame.K_r]):
            x0 = x1 = 50
            lock = 0

        redraw()
        pygame.display.update()

    pygame.quit()


def strict_alternation():
    # initialize pygame
    pygame.init()
    (width, height) = (1020, 700)
    background_colour = (255, 255, 255)
    # create the screen
    screen = pygame.display.set_mode((width, height))
    screen.fill(background_colour)
    # caption to window
    pygame.display.set_caption('Strict alteration')
    icon = pygame.image.load('python3.8.png')
    pygame.display.set_icon(icon)

    right = pygame.image.load('correct.png')
    right = pygame.transform.scale(right, (30, 30))

    wrogn = pygame.image.load('wrogn.png')
    wrogn = pygame.transform.scale(wrogn, (20, 20))

    font = pygame.font.SysFont("arial", 22)
    font1 = pygame.font.SysFont("TIMES", 20, bold=True)
    Strict = font.render("Strict Alteration ", True, (0, 100, 240))

    text = pygame.image.load('text.png')
    text = pygame.transform.scale(text, (350, 350))
    # game loop
    turn = 0
    turn2 = 0
    count = 0
    count1 = 0
    px = []
    py = []
    py_change = []
    px_change = []
    px_mychange = []
    py_mychange = []
    pimg = []
    p = 0

    for i in range(2):
        st = "P" + str(i) + ".png"
        img = pygame.image.load(st)
        pimg.append(pygame.transform.scale(img, (100, 100)))
        if i == 0:
            px.append(100)
        else:
            px.append(px[i - 1] + 200)
        py.append(280)
        py_change.append(0.4)
        px_change.append(0.4)
        px_mychange.append(0.8)
        py_mychange.append(0.8)
    pro0 = font1.render("Process 0", True, (0, 0, 0))
    pro1 = font1.render("PROCESS 1", True, (0, 0, 0))

    def Mutual_exclusion():
        Mutual_e = font1.render("Mutual exclusion", True, (0, 100, 240))
        screen.blit(Mutual_e, (735, 70))

    def progress():
        progress = font1.render("Progress", True, (0, 100, 240))
        screen.blit(progress, (735, 100))

    def bounded_wait():
        bounded = font1.render("Bounded wait", True, (0, 100, 240))
        screen.blit(bounded, (735, 130))

    def Turn_variable():
        # pygame.draw.ellipse(screen, (0,0,0), ((410, 50), (170, 70)), 4)
        turn = font.render("TURN  ", True, (0, 100, 240))
        screen.blit(turn, (350, 70))

    def Critical_section():
        critical = font.render("CRITICAL SECTION ", True, (0, 100, 240))
        screen.blit(critical, (330, 620))

    def nonCritical_section():
        noncritical = font.render("NON CRITICAL SECTION ", True, (0, 100, 240))
        screen.blit(noncritical, (150, 240))

    def whileloop():
        whileloop = font.render("WHILE LOOP  ", True, (255, 0, 0))
        screen.blit(whileloop, (500, 240))

    running = True
    while running:
        screen.fill(background_colour)
        Turn_variable()
        Critical_section()
        nonCritical_section()
        Mutual_exclusion()
        whileloop()
        progress()
        bounded_wait()
        screen.blit(right, (900, 65))
        screen.blit(right, (900, 125))

        screen.blit(text, (730, 220))
        pygame.draw.rect(screen, (0, 0, 0), [730, 60, 220, 100], 2)
        pygame.draw.rect(screen, (0, 0, 0), [730, 200, 250, 400], 2)
        pygame.draw.line(screen, (0, 0, 0), (890, 60), (890, 160), 2)  # mutual exclusion,progress
        pygame.draw.line(screen, (0, 0, 0), (730, 390), (980, 390), 2)  # process code
        pygame.draw.line(screen, (0, 0, 0), (410, 270), (700, 270), 2)  # while loop
        pygame.draw.line(screen, (0, 0, 0), (100, 270), (400, 270), 2)  # noncs
        pygame.draw.line(screen, (0, 0, 0), (100, 615), (700, 615), 2)  # cs
        # screen.blit(wrogn, (880, 90))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # screen.blit(Strict,(195, 70))
        # lowest
        pygame.draw.rect(screen, (0, 0, 0), [100, 450, 600, 200], 3)
        # top most
        pygame.draw.rect(screen, (0, 0, 0), [100, 20, 600, 200], 3)
        # middle
        pygame.draw.rect(screen, (0, 0, 0), [100, 230, 300, 200], 3)
        # middle right
        pygame.draw.rect(screen, (0, 0, 0), [410, 230, 290, 200], 3)

        # screen.blit(pro0, (350, 90))

        if turn == 0 and p == 0:
            pro0 = font1.render("PROCESS 0", True, (0, 0, 0))
            screen.blit(pro0, (330, 110))
            py[0] = py[0] + py_change[0]
            if py[0] > 500:
                py[0] = 500
                pygame.time.wait(2000)
                py_change[0] = - py_change[0]
            if py[1] == 280:
                px[1] = px[1] + py_change[1]
                if px[1] > 430:
                    px[1] = 430

                # pygame.time.wait(2000)
            if py[0] < 280:
                py[0] = 280
                # pro0 = font.render("process 0", True, (255, 255, 255))
                turn = 1
        if turn == 1:
            # pro0 = font.render("process 0", True, (255, 255, 255))
            screen.blit(pro1, (330, 110))
            if turn == 1:
                py[1] = py[1] + py_change[1]

            if py[0] == 280:
                px[0] = px[0] + px_mychange[0]
                if px[0] > 550:
                    px[0] = 550
            if py[1] > 500:
                screen.blit(wrogn, (900, 100))
                py[1] = 500

            if turn2 == 0:
                # px[1] = px[1] - px_change[0]
                if px[1] < 300:
                    px[1] = 300
                    # py_change[1] = - py_change[1]
                if px[1] == 300:
                    if py[1] == 500:
                        pygame.time.wait(1000)
                    # if py[1] == 500:
                    #   py_change[1] = - py_change[1]

                    if py[1] < 280:
                        py[1] = 280

        # if turn == 2:
        # py[0] = py[0] - py_mychange[0]

        for i in range(2):
            screen.blit(pimg[i], (px[i], py[i]))
        pygame.display.update()
    pygame.quit()


def peterson_algo():
    pygame.init()
    background_colour = (245, 255, 255)
    peterson = pygame.display.set_mode((1200, 700))
    peterson.fill(background_colour)
    pygame.display.set_caption('Peterson')
    font = pygame.font.SysFont('arial', 24)
    interested = [True, True]
    turn = 0

    def conditions():
        pygame.draw.rect(peterson, (0, 0, 0,), (800, 50, 300, 120), 4)
        ME = font.render("Mutual Exclusion :", True, (153, 0, 76))
        Progress = font.render("Progress :", True, (153, 0, 76))
        BW = font.render("Bounded Waiting :", True, (153, 0, 76))
        HF = font.render("Hardware feasible: ", True, (153, 0, 76))
        peterson.blit(ME, (810, 65))
        peterson.blit(Progress, (810, 87))
        peterson.blit(BW, (810, 110))
        peterson.blit(HF, (810, 130))

    def turn_text():
        pygame.draw.rect(peterson, (0, 0, 0), (40, 260, 180, 90), 4)
        turn_text = font.render("Turn:" + str(turn), True, (0, 128, 128))
        peterson.blit(turn_text, (55, 270))

    def interestedP1():
        interestedP1 = font.render("Interested 1: " + str(interested[0]), True, (0, 128, 128))
        peterson.blit(interestedP1, (55, 290))

    def interestedP2():
        interestedP2 = font.render("Interested 2: " + str(interested[1]), True, (0, 128, 128))
        peterson.blit(interestedP2, (55, 310))

    PImg = []
    imagex = []
    imagey = []
    imagey_change = []

    count = 0
    count1 = 0
    flag = False
    flag1 = False
    P1 = "P1.png"
    P1 = pygame.image.load(P1)
    PImg.append(pygame.transform.scale(P1, (100, 100)))

    P2 = "P2.png"
    P2 = pygame.image.load(P2)
    PImg.append(pygame.transform.scale(P2, (100, 100)))

    right = pygame.image.load("right.png")
    right1 = pygame.transform.scale(right, (30, 30))

    process1 = pygame.image.load("untitled.png")
    process1 = pygame.transform.scale(process1, (350, 200))

    process2 = pygame.image.load("process2.png")
    process2 = pygame.transform.scale(process2, (350, 200))

    for i in range(2):
        if i == 0:
            imagex.append(250)
        else:
            imagex.append(450)
        imagey.append(250)
        imagey_change.append(0.3)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        peterson.fill(background_colour)
        pygame.draw.rect(peterson, (0, 0, 0), [55, 500, 700, 140], 4)
        pygame.draw.rect(peterson, (0, 0, 0), [55, 470, 150, 30], 4)
        cs = font.render("Critical Section ", True, (0, 100, 240))
        peterson.blit(cs, (64, 470))
        pygame.draw.rect(peterson, (0, 0, 0), [150, 55, 500, 100], 4)
        pygame.draw.rect(peterson, (0, 0, 0), [150, 25, 130, 30], 4)
        cs = font.render("While_loop() ", True, (0, 100, 240))
        peterson.blit(cs, (155, 25))
        Reset = font.render("After one round is over, Press R to Reset the conditions", True, (153, 0, 76))
        p_1 = font.render("Press 1 to make TURN = 1", True, (50, 150, 50))
        p_2 = font.render("Press 2 to make TURN = 2", True, (50, 150, 50))
        peterson.blit(Reset, (100, 650))
        peterson.blit(p_1, (5, 205))
        peterson.blit(p_2, (5, 230))
        green = (139, 69, 19)
        blue = (65, 105, 225)
        text = font.render('PETERSON ALGORITHM', True, green, blue)
        peterson.blit(text, (815, 5))
        peterson.blit(process1, (800, 200))
        peterson.blit(process2, (800, 420))
        turn_text()
        interestedP1()
        interestedP2()
        conditions()
        if interested[0] and turn == 1:
            imagey[0] += imagey_change[0]
            imagey[1] += imagey_change[1]
            if imagey[0] >= 550:
                imagey[0] = 550
            if imagey[1] > 400:
                imagey_change[1] = -0.3
            if imagey[1] <= 60:
                imagey[1] = 60
                pygame.time.wait(1000)
                interested[0] = False

        elif interested[1] and turn == 2:
            imagey[1] += imagey_change[1]
            imagey[0] += imagey_change[0]
            if imagey[1] >= 550:
                imagey[1] = 550
            if imagey[0] > 400:
                imagey_change[0] = -0.3
            if imagey[0] <= 60:
                imagey[0] = 60
                pygame.time.wait(1000)
                interested[1] = False

        if not interested[0]:
            if imagey[0] <= 550.3:
                imagey[0] -= 0.3
                if imagey[0] < 250:
                    imagey[0] = 250
            if imagey[0] == 250 and count == 0:
                if imagey[1] > 550:
                    imagey[1] = 550
                imagey[1] += 0.3
            if imagey[0] == 250 and imagey[1] == 550.3:
                pygame.time.wait(1000)
                interested[1] = False
                count = 1

        if not interested[1]:
            if imagey[1] <= 550.3:
                imagey[1] -= 0.3
                if imagey[1] < 250:
                    imagey[1] = 250
            if imagey[1] == 250 and count1 == 0:
                if imagey[0] > 550:
                    imagey[0] = 550
                imagey[0] += 0.3
            if imagey[1] == 250 and imagey[0] == 550.3:
                pygame.time.wait(1000)
                interested[0] = False
                count1 = 1

        if (imagey[0] > 500 and imagey[1] < 480) or (imagey[0] < 500 and imagey[1] > 250):
            peterson.blit(right1, (1000, 65))
            flag1 = True

        if (imagey[0] == 250 and imagey[1] >= 550) or (imagey[1] == 250 and imagey[0] >= 550):
            peterson.blit(right1, (940, 83))  # progress
            flag = True

        if imagey[0] < 480 and imagey[1] < 480:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                turn = 1
            if keys[pygame.K_2]:
                turn = 2

        if not interested[0] and not interested[1] and (
                (imagey[0] == 250 and imagey[1] == 250.0) or (imagey[0] == 250.3 and imagey[1] == 250)):
            imagey[0] = 250
            imagey[1] = 250
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                interested = [True, True]
                turn = 0
                count = 0
                count1 = 0
                flag = False
                flag1 = False
                imagey_change[0] = imagey_change[1] = 0.3

        for i in range(2):
            peterson.blit(PImg[i], (imagex[i], imagey[i]))
        if flag == True:
            peterson.blit(right1, (940, 83))  # progress
            peterson.blit(right1, (1000, 105))  # bounded waiting
        if flag1 == True:
            peterson.blit(right1, (1000, 65))  # mutual exclusion

        peterson.blit(right1, (1010, 129))  # hardware
        pygame.display.update()

    pygame.quit()


def testset():
    pygame.init()
    background_colour = (255, 252, 239)
    testandset = pygame.display.set_mode((1200, 700))
    testandset.fill(background_colour)
    pygame.display.set_caption('TestandSet')
    font = pygame.font.SysFont('arial', 24)

    l = 0
    start = 0

    algorithm = pygame.image.load("testandset.jpeg")
    algorithm = pygame.transform.scale(algorithm, (350, 200))

    def lock():
        pygame.draw.ellipse(testandset, (23, 2, 34), ((30, 180), (170, 70)), 4)
        loc = font.render("Lock " + str(l), True, (0, 100, 240))
        testandset.blit(loc, (80, 200))

    PImg = []
    imagex = []
    imagey = []
    imagey_change = []

    P1 = "P1.png"
    P1 = pygame.image.load(P1)
    PImg.append(pygame.transform.scale(P1, (80, 80)))

    P2 = "P2.png"
    P2 = pygame.image.load(P2)
    PImg.append(pygame.transform.scale(P2, (80, 80)))

    for i in range(2):
        if i == 0:
            imagex.append(350)
        else:
            imagex.append(550)
        imagey.append(0)
        imagey_change.append(0.3)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        testandset.fill(background_colour)
        pygame.draw.rect(testandset, (0, 0, 0), [250, 120, 500, 80], 4)
        cs = font.render("while(Test-and-Set(Lock)); ", True, (0, 100, 240))
        testandset.blit(cs, (380, 90))

        pygame.draw.rect(testandset, (0, 0, 0), [250, 280, 500, 80], 4)
        cs = font.render("Critical Section ", True, (0, 100, 240))
        testandset.blit(cs, (420, 250))

        pygame.draw.rect(testandset, (0, 0, 0), [250, 450, 500, 80], 4)
        cs = font.render("Lock = 0 ", True, (0, 100, 240))
        testandset.blit(cs, (450, 420))

        testandset.blit(algorithm, (820, 230))

        lock()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            start = 1

        Start = font.render("Press 's' to Start", True, (190, 14, 76))
        testandset.blit(Start, (800, 10))

        text = font.render('TEST AND SET', True, (220, 14, 76), (127, 255, 212))
        testandset.blit(text, (5, 5))

        Entry = font.render("ENTRY SECTION", True, (0, 139, 139))
        testandset.blit(Entry, (770, 140))

        Exit = font.render("EXIT SECTION", True, (0, 139, 139))
        testandset.blit(Exit, (770, 470))

        if (start == 1):
            imagey[0] += imagey_change[0]
            if (450 > imagey[0] >= 120):
                l = 1
                if (122 < imagey[0] < 122.2):
                    pygame.time.wait(500)
                if (280 < imagey[0] < 280.5):
                    pygame.time.wait(500)
            if (150 < imagey[0]):
                if (imagey[1] < 120 and l == 1):
                    imagey[1] += imagey_change[1]
            if (520 > imagey[0] >= 450):
                l = 0
                if (450 < imagey[0] < 450.5):
                    pygame.time.wait(500)
                if (imagey[0] == 451):
                    imagey[1] = 151
                if (imagey[1] >= 155):
                    l = 1
                imagey[1] += imagey_change[1]
            if (imagey[0] > 520):
                imagey[1] += imagey_change[1]
                if (280 < imagey[1] < 280.5):
                    pygame.time.wait(500)
                if (450 < imagey[1] < 450.5):
                    pygame.time.wait(500)
                    l = 0

            if (imagey[0] > 550):
                imagey[0] = 550
                if (550 > imagey[0] >= 190.5):
                    imagey[1] += imagey_change[1]
            if (imagey[1] > 550):
                imagey[1] = 550

        for i in range(2):
            testandset.blit(PImg[i], (imagex[i], imagey[i]))

        pygame.display.update()
    pygame.quit()


def counting_semaphore():
    pygame.init()
    s = 3
    p = 0
    count = 0
    flag = False
    background_colour = (253, 255, 255)
    (width, height) = (1250, 780)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Counting Semaphore')
    screen.fill(background_colour)
    font = pygame.font.SysFont('arial', 24)
    font1 = pygame.font.SysFont('arial', 18, bold=True)
    font2 = pygame.font.SysFont('Times', 18)
    shape_color = (0, 0, 0)
    pImg = []
    px = []
    py = []
    px_change = []
    py_change = []

    for i in range(5):
        st = "p" + str(i + 1) + ".png"
        standImage = pygame.image.load(st)
        pImg.append(pygame.transform.scale(standImage, (100, 100)))
        py_change.append(0.4)
        px_change.append(0)
        if i == 0:
            px.append(100)
        else:
            px.append(px[i - 1] + 150)
        py.append(300)

    def algo_text():
        x = 1030
        y = 280
        l1 = font2.render("WAIT(semaphore s){ ", True, (0, 0, 0))
        l2 = font2.render("      s = s – 1;", True, (0, 0, 0))
        l3 = font2.render("      if (s <= 0){       ", True, (0, 0, 0))
        l4 = font2.render("             //Block the process", True, (0, 0, 0))
        l5 = font2.render("             sleep() }", True, (0, 0, 0))
        l6 = font2.render("}", True, (0, 100, 0))
        l7 = font2.render("SIGNAL (semaphore s){", True, (0, 0, 0))
        l8 = font2.render("      s = s + 1;", True, (0, 0, 0))
        l9 = font2.render("      if (s <= 0){", True, (0, 0, 0))
        l10 = font2.render("            //wake up the process", True, (0, 0, 0))
        l11 = font2.render("             //from block queue}", True, (0, 0, 0))
        l12 = font2.render("             wakeup()}", True, (0, 0, 0))
        l13 = font2.render("}", True, (0, 0, 0))

        screen.blit(l1, (x, y))
        screen.blit(l2, (x, y + 20))
        screen.blit(l3, (x, y + 40))
        screen.blit(l4, (x, y + 60))
        screen.blit(l5, (x, y + 80))
        screen.blit(l6, (x, y + 100))
        screen.blit(l7, (x, y + 140))
        screen.blit(l8, (x, y + 160))
        screen.blit(l9, (x, y + 180))
        screen.blit(l10, (x, y + 200))
        screen.blit(l11, (x, y + 220))
        screen.blit(l12, (x, y + 240))
        screen.blit(l13, (x, y + 260))

    def signal_text(x, y):
        signal = font.render("SIGNAL() ", True, (0, 100, 0))
        screen.blit(signal, (x, y + 100))

    def BLOCK_text():
        blck = font.render("BLOCK QUEUE ", True, (255, 0, 0))
        screen.blit(blck, (830, 300))

    def wait_text(x, y):
        blck = font.render("WAIT() ", True, (255, 0, 0))
        screen.blit(blck, (x + 10, y + 100))

    def complete_text(x, y):
        complete = font.render("Completed ", True, (255, 0, 0))
        screen.blit(complete, (x - 10, y + 110))

    def semaphore_text():
        pygame.draw.ellipse(screen, shape_color, ((410, 50), (170, 70)), 4)
        semaphore = font.render("Semaphore " + str(s), True, (0, 100, 240))
        screen.blit(semaphore, (435, 70))

    running = True
    while running:
        screen.fill(background_colour)
        semaphore_text()
        algo_text()
        pygame.draw.rect(screen, shape_color, [55, 500, 900, 200], 4)
        pygame.draw.rect(screen, shape_color, [850, 80, 100, 220], 3)
        pygame.draw.rect(screen, shape_color, [1020, 260, 230, 310], 2)
        pygame.draw.line(screen, (0, 0, 0), (1020, 410), (1250, 410), 2)
        BLOCK_text()
        Start = font.render("Press 's' to Start", True, (190, 14, 76))
        screen.blit(Start, (1030, 150))
        bs = font1.render("COUNTING SEMAPHORE", True, (255, 255, 255), (0, 130, 120))
        cs = font.render("CRITICAL SECTION ", True, (0, 100, 240))
        screen.blit(cs, (450, 700))
        screen.blit(bs, (1030, 200))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            p = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not flag:  # before cs
            if p == 1:  # up
                py[0] = py[0] - py_change[0]
                if py[0] <= 74.8:
                    py[0] = 75
                    py_change[0] = -0.4
                    s = s - 1
                if py[0] >= 550:
                    py[0] = 550
                    p = 2
                if s == 3:
                    wait_text(px[0], py[0])

            elif p == 2:
                py[1] = py[1] - py_change[1]
                if py[1] <= 74.8:
                    py[1] = 75
                    py_change[1] = -0.4
                    s = s - 1
                if py[1] >= 550:
                    py[1] = 550
                    p = 3
                if s == 2:
                    wait_text(px[1], py[1])
            elif p == 3:
                py[2] = py[2] - py_change[2]
                if py[2] <= 110:
                    py[2] = 110
                    py_change[2] = -0.4
                    s = s - 1
                if py[2] >= 550:
                    py[2] = 550
                    p = 4
                if s == 1:
                    wait_text(px[2], py[2])
            elif p == 4:
                py[3] = py[3] - py_change[3]
                px[3] = px[3] - px_change[3]
                if py[3] < 80:
                    py[3] = 80
                    py_change[3] = 0
                    px_change[3] = -0.3
                    s = s - 1
                if px[3] >= 850:
                    px_change[3] = 0.4
                    p = 5
                if s == 0:
                    wait_text(px[3], py[3])
            elif p == 5:
                py[4] = py[4] - py_change[4]
                px[4] = px[4] - px_change[4]
                if s == -1:
                    wait_text(px[4], py[4])
                if py[4] < 100:
                    py[4] = 100
                    py_change[4] = -0.4
                    count = 1
                    s = s - 1
                if py[4] >= 200 and count == 1:
                    py_change[4] = 0
                    px_change[4] = -0.4
                if px[4] > 850:
                    px[4] = 850
                    px_change[4] = 0.4
                    py_change[4] = 0
                    p = 1

        else:
            if p == 1:
                if s == -2:
                    py[0] = py[0] + py_change[0]
                    signal_text(px[0], py[0])
                    if py[0] <= 110:
                        py[0] = 110
                        py_change[0] = 0.4
                        s = s + 1
                        complete_text(px[0], py[0])

                if s == -1:
                    complete_text(px[0], py[0])
                    px[3] = px[3] - px_change[3]
                    py[3] = py[3] - py_change[3]
                    if px[3] < 550:
                        px[3] = 550
                        py_change[3] = -0.4
                        px_change[3] = 0
                    if py[3] > 550:
                        py[3] = 550
                        p = 2

            elif p == 2:
                complete_text(px[0], py[0])
                if s == -1:
                    py[1] = py[1] + py_change[1]
                    signal_text(px[1], py[1])
                    if py[1] <= 110:
                        py[1] = 110
                        py_change[1] = 0.4
                        s = s + 1
                        complete_text(px[1], py[1])
                if s == 0:
                    complete_text(px[1], py[1])
                    px[4] = px[4] - px_change[4]
                    py[4] = py[4] - py_change[4]
                    if px[4] < 700:
                        px[4] = 700
                        py_change[4] = -0.4
                        px_change[4] = 0
                    if py[4] > 550:
                        py[4] = 550
                        p = 3
            elif p == 3:
                complete_text(px[0], py[0])
                complete_text(px[1], py[1])
                py[2] = py[2] + py_change[2]
                signal_text(px[2], py[2])
                if py[2] <= 110:
                    py[2] = 110
                    py_change[2] = 0.4
                    s = s + 1
                    complete_text(px[2], py[2])
                    p = 4
            elif p == 4:
                for i in range(3):
                    complete_text(px[i], py[i])
                py[3] = py[3] + py_change[3]
                signal_text(px[3], py[3])
                if py[3] <= 110:
                    py[3] = 110
                    py_change[3] = 0.4
                    s = s + 1
                    complete_text(px[3], py[3])
                    p = 5
            elif p == 5:
                for i in range(4):
                    complete_text(px[i], py[i])
                py[4] = py[4] + py_change[4]
                signal_text(px[4], py[4])
                if py[4] <= 110:
                    py[4] = 110
                    py_change[4] = 0.4
                    p = 6
                    s = 3
                    complete_text(px[4], py[4])
            else:
                for i in range(5):
                    complete_text(px[i], py[i])
                # running = False

        for i in range(len(px)):
            screen.blit(pImg[i], (px[i], py[i]))
        pygame.display.update()
    pygame.quit()


def Binary_semaphore():
    pygame.init()
    background_colour = (245, 255, 245)
    (width, height) = (1010, 700)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Binary Semaphore')
    screen.fill(background_colour)
    font = pygame.font.SysFont('arial', 24)
    font1 = pygame.font.SysFont('arial ', 20, bold=True)
    font2 = pygame.font.SysFont('Times ', 18)
    shape_color = (0, 0, 0)
    s = 1
    p = 0
    flag = False
    count = 0

    pImg = []
    px = []
    py = []
    py_change = []
    px_change = 0.2
    for i in range(2):
        st = "p" + str(i + 1) + ".png"
        pImage = pygame.image.load(st)
        pImg.append(pygame.transform.scale(pImage, (100, 100)))
        py_change.append(0.2)
        if i == 0:
            px.append(150)
        else:
            px.append(px[i - 1] + 280)
        py.append(300)

    def signal_text(x, y):
        signal = font.render("SIGNAL() ", True, (0, 100, 0))
        screen.blit(signal, (x, y + 100))

    def algo_text():
        x = 770
        y = 180
        l1 = font2.render("WAIT(semaphore s){ ", True, (0, 0, 0))
        l2 = font2.render("   if (s.value == 1) { ", True, (0, 0, 0))
        l3 = font2.render("        s.value = 0;", True, (0, 0, 0))
        l4 = font2.render("    }", True, (0, 0, 0))
        l5 = font2.render("   else {", True, (0, 0, 0))
        l6 = font2.render("        //Block the process", True, (0, 100, 0))
        l7 = font2.render("         Sleep();} ", True, (0, 0, 0))
        l8 = font2.render("} ", True, (0, 0, 0))
        l9 = font2.render("SIGNAL(Semaphore s){ ", True, (0, 0, 0))
        l10 = font2.render("   s = 1; }", True, (0, 0, 0))

        screen.blit(l1, (x, y))
        screen.blit(l2, (x, y + 20))
        screen.blit(l3, (x, y + 40))
        screen.blit(l4, (x, y + 60))
        screen.blit(l5, (x, y + 80))
        screen.blit(l6, (x, y + 100))
        screen.blit(l7, (x, y + 120))
        screen.blit(l8, (x, y + 140))
        screen.blit(l9, (x, y + 180))
        screen.blit(l10, (x, y + 200))

    def stand_person(x, y, j):
        screen.blit(pImg[j], (x, y))

    def BLOCK_text():
        blck = font1.render("BLOCK QUEUE ", True, (255, 0, 0))
        screen.blit(blck, (560, 390))

    def wait_text(x, y):
        wai = font.render("WAIT() ", True, (255, 0, 0))
        screen.blit(wai, (x + 10, y + 110))

    def complete_text(x, y):
        complete = font.render("Completed ", True, (255, 0, 0))
        screen.blit(complete, (x - 10, y + 110))

    def semaphore_text():
        pygame.draw.ellipse(screen, shape_color, ((260, 50), (170, 70)), 4)
        semaphore = font.render("Semaphore " + str(s), True, (0, 100, 240))
        screen.blit(semaphore, (285, 70))

    running = True
    while running:
        screen.fill(background_colour)
        semaphore_text()
        algo_text()
        pygame.draw.rect(screen, shape_color, [50, 500, 615, 150], 4)
        bs = font1.render("BINARY SEMAPHORE", True, (255, 255, 255), (0, 130, 120))
        cs = font.render("Critical Section ", True, (0, 130, 120))
        screen.blit(cs, (300, 650))
        screen.blit(bs, (780, 100))
        pygame.draw.rect(screen, shape_color, [570, 150, 100, 220], 3)
        pygame.draw.rect(screen, shape_color, [760, 170, 250, 330], 2)  # code
        BLOCK_text()
        pygame.draw.line(screen, (0, 0, 0), (760, 350), (1010, 350), 2)
        screen.blit(cs, (290, 790))
        Start = font.render("Press 's' to Start", True, (190, 14, 76))
        screen.blit(Start, (790, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            p = 1
        if not flag:  # before cs
            if p == 1:
                py[0] = py[0] - py_change[0]
                if py[0] < 100:
                    py[0] = 100
                    py_change[0] = -0.2
                    s = 0
                if py[0] >= 520:
                    py[0] = 520
                    py_change[1] = 0.2
                    p = 2
                if s == 1:
                    wait_text(px[0], py[0])

            elif p == 2:
                py[1] = py[1] - py_change[1]
                if count == 0:
                    wait_text(px[1], py[1])
                if py[1] < 100:
                    py[1] = 100
                    py_change[1] = -0.2
                    count = 1
                if py[1] > 200 and count == 1:
                    py[1] = 200
                    py_change[1] = 0
                if count == 1 and py[1] == 200:
                    px[1] = px[1] + px_change
                    if px[1] >= 570:
                        px[1] = 570
                        py_change[1] = 0.2
                        count = 0
                        p = 1
                        flag = True

        else:  # after cs
            if p == 1:
                py[0] = py[0] + py_change[0]
                signal_text(px[0], py[0])
                if py[0] < 100:
                    py[0] = 100
                    py_change[0] = 0
                    complete_text(px[0], py[0])
                    s = 1
                    p = 2

            elif p == 2:
                complete_text(px[0], py[0])
                if count == 0:
                    px[1] = px[1] - px_change
                    if px[1] <= 450:
                        px[1] = 450
                        count = 1
                        s = 0
                else:
                    py[1] = py[1] + py_change[1]
                if py[1] < 100 and count > 1:
                    py[1] = 100
                    py_change[1] = -0.2
                    count += 1
                if count == 2:
                    signal_text(px[1], py[1])
                if count == 1 and py[1] < 400:
                    wait_text(px[1], py[1])
                if py[1] > 520:
                    count = 2
                    py[1] = 520
                    pygame.time.delay(2000)
                    py_change[1] = -0.2
                if count == 3:
                    complete_text(px[1], py[1])
                    s = 1
                    p = 3

            elif p == 3:
                complete_text(px[0], py[0])
                complete_text(px[1], py[1])

        for i in range(len(px)):
            stand_person(px[i], py[i], i)
        pygame.display.update()

    pygame.quit()


def producer_consumer():
    pygame.init()
    (width, height) = (800, 700)
    background_colour = (255, 255, 255)
    screen = pygame.display.set_mode((width, height))
    screen.fill(background_colour)

    pygame.display.set_caption('Producer cosumer')
    icon = pygame.image.load('python3.8.png')
    pygame.display.set_icon(icon)

    font = pygame.font.SysFont("arial", 40, bold=True)

    def buffer():
        pygame.draw.rect(screen, (0, 0, 0), [250, 200, 300, 330], 4)

    def partition():
        pygame.draw.line(screen, (0, 0, 0), (400, 1), (400, 200), 4)
        pygame.draw.line(screen, (0, 0, 0), (400, 530), (400, 600), 4)
        pygame.draw.line(screen, (0, 0, 0), (0, 600), (800, 600), 4)

    def buffertext():
        buffer = font.render("Buffer", True, (0, 70, 240))
        screen.blit(buffer, (353, 209))

    def protext():
        pro = font.render("Producer is producing product", True, (0, 70, 240))
        screen.blit(pro, (150, 609))

    def context():
        con = font.render("Consumer is consuming product", True, (0, 70, 240))
        screen.blit(con, (140, 609))

    def context1():
        con1 = font.render("Buffer is empty, consumer can't consume", True, (0, 70, 240))
        screen.blit(con1, (80, 609))

    def producer():
        producer = font.render("Producer", True, (0, 70, 240))
        screen.blit(producer, (130, 19))

    def consumer():
        consumer = font.render("Consumer", True, (0, 70, 240))
        screen.blit(consumer, (530, 19))

    px = [100, 600]
    py = [250, 250]
    px_change = [0, 0]
    pimg = []
    p0 = 0
    p1 = 0
    p = 0
    p1flag = False
    p0flag = False
    consumed = False
    produced = False
    n = 0

    for i in range(2):
        st = "p" + str(i) + ".png"
        img = pygame.image.load(st)
        pimg.append(pygame.transform.scale(img, (100, 100)))

    running = True
    while running:
        screen.fill(background_colour)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        buffer()
        buffertext()
        partition()
        producer()
        consumer()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0] and keys[pygame.K_RIGHT]:
            if produced == True and consumed == False and px[0] == 100:
                p0flag = True
                px_change[0] = 0
            else:
                px_change[0] = 0.4
                p1flag = False

        if keys[pygame.K_0] and keys[pygame.K_LEFT]:
            px_change[0] = -0.4
            if p0 == 1:
                n = n + 1
                p0 = 0
        if keys[pygame.K_1] and keys[pygame.K_RIGHT]:
            px_change[1] = 0.4
            p1 = 0
            p = 0
        if keys[pygame.K_1] and keys[pygame.K_LEFT]:
            if p == 1:
                px_change[1] = -0.4
                p1flag = False
                p0flag = False
            elif p == 0 and px[1] == 600:
                p1flag = True

        if 100 <= px[0] <= 350:
            px[0] = px_change[0] + px[0]
            if px[0] > 350:
                px[0] = 350
                px_change[0] = 0
                p0 = 1
                p = 1
                produced = True
                consumed = False
            elif px[0] < 100:
                px[0] = 100
            if p0 == 1:
                protext()
                product = font.render(str(n + 1), True, (0, 0, 0))
                screen.blit(product, (390, 400))

        if 350 <= px[1] <= 600:
            px[1] = px_change[1] + px[1]
            if p1flag:
                context1()
            if px[1] > 600:
                px[1] = 600
                px_change[1] = 0

            elif px[1] < 350:
                px[1] = 350
                px_change[1] = 0
                p1 = 1
                p = 0
                consumed = True
                produced = False
            if p1 == 1:
                context()

        if p == 1 and p0 == 0:
            product = font.render(str(n), True, (0, 0, 0))
            screen.blit(product, (390, 400))

        if p0flag:
            stopproducer = font.render("Buffer is full producer can not produce.", True, (0, 70, 240))
            screen.blit(stopproducer, (150, 609))

        for i in range(2):
            screen.blit(pimg[i], (px[i], py[i]))
        pygame.display.update()
    pygame.quit()


def Dinning_philosopher():
    pygame.init()
    background_colour = (245, 255, 245)
    (width, height) = (1300, 720)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Dining philosopher')
    screen.fill(background_colour)
    font = pygame.font.SysFont('arial', 24)
    font1 = pygame.font.SysFont('arial ', 30, bold=True)
    font2 = pygame.font.SysFont('Times ', 24)
    shape_color = (0, 0, 0)

    s = [1, 1, 1, 1, 1]
    f = []
    fx = [730, 770, 490, 280, 410]
    fy = [150, 450, 590, 360, 100]
    px = [540, 770, 640, 300, 260]
    py = [30, 250, 540, 490, 170]
    pImg = []
    occupied_by = [5, 5, 5, 5, 5]
    eating_process = [0, 0, 0, 0, 0]
    block_process = [0, 0, 0, 0, 0]
    want_stick_number = [5, 5, 5, 5, 5]
    f.append(font1.render("F0", True, (0, 0, 0)))
    f.append(font1.render("F1", True, (0, 0, 0)))
    f.append(font1.render("F2", True, (0, 0, 0)))
    f.append(font1.render("F3", True, (0, 0, 0)))
    f.append(font1.render("F4", True, (0, 0, 0)))

    block = font.render("BLOCK", True, (255, 0, 0))
    think = font.render("THINKING", True, (255, 0, 0))
    svalue = font2.render("SEMAPHORES", True, (0, 0, 0))
    eating = font.render("EATING", True, (0, 158, 0))
    algo = font1.render("ALGORITHM", True, (0, 158, 158))
    avoid = font.render("For last process :-", True, (0, 158, 158))

    instruction = pygame.image.load("DP.png")
    instruction = pygame.transform.scale(instruction, (250, 450))

    table = pygame.image.load("table.png")
    table = pygame.transform.scale(table, (650, 650))

    for i in range(5):
        st = "p" + str(i) + ".png"
        Image = pygame.image.load(st)
        pImg.append(pygame.transform.scale(Image, (100, 100)))

    y = 30
    n = 0

    def semaphore_text(i, s, sx, sy):
        semaphore = font2.render("S" + str(i) + " = " + str(s), True, (0, 0, 0))
        screen.blit(semaphore, (sx, sy))

    def algorithm_text():
        image1 = pygame.image.load("DP1.jpeg")
        image1 = pygame.transform.scale(image1, (250, 300))
        image2 = pygame.image.load("DP2.jpeg")
        image2 = pygame.transform.scale(image2, (250, 300))
        screen.blit(image1, (1050, 50))
        screen.blit(image2, (1050, 400))

    running = True
    while running:
        screen.fill(background_colour)
        pygame.draw.circle(screen, (0, 0, 0), (550, 350), 220, 3)
        pygame.draw.rect(screen, shape_color, [900, 150, 100, 220], 3)  # block
        screen.blit(think, (905, 110))
        screen.blit(table, (225, 25))
        screen.blit(instruction, (5, 250))
        screen.blit(svalue, (5, 30))
        screen.blit(algo, (1100, 10))
        screen.blit(avoid, (1050, 365))
        algorithm_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0] and keys[pygame.K_LEFT]:
            if s[0] == 1 and occupied_by[0] == 5:
                fx[0] = 640
                fy[0] = 90
                s[0] = 0
                occupied_by[0] = 0
                n = n + 1
            if s[0] == 0 and fx[0] != 640:
                block_process[0] = 1
                want_stick_number[0] = 0

        if keys[pygame.K_1] and keys[pygame.K_LEFT]:
            if s[1] == 1 and occupied_by[1] == 5:
                fx[1] = 790
                fy[1] = 350
                s[1] = 0
                occupied_by[1] = 1
                n = n + 1
            if s[1] == 0 and fx[1] != 790:
                block_process[1] = 1
                want_stick_number[1] = 1

        if keys[pygame.K_2] and keys[pygame.K_LEFT]:
            if s[2] == 1 and occupied_by[2] == 5:
                fx[2] = 610
                fy[2] = 580
                s[2] = 0
                occupied_by[2] = 2
                n = n + 1
            if s[2] == 0 and fx[2] != 610:
                block_process[2] = 1
                want_stick_number[2] = 2

        if keys[pygame.K_3] and keys[pygame.K_LEFT]:
            if s[3] == 1 and occupied_by[3] == 5:
                fx[3] = 310
                fy[3] = 460
                s[3] = 0
                occupied_by[3] = 3
                n = n + 1
            if s[3] == 0 and fx[3] != 310:
                block_process[3] = 1
                want_stick_number[3] = 3

        if keys[pygame.K_4] and keys[pygame.K_LEFT]:
            if s[4] == 1 and occupied_by[4] == 5:
                fx[4] = 345
                fy[4] = 155
                s[4] = 0
                occupied_by[4] = 4
                n = n + 1
            if s[4] == 0 and fx[4] != 345:
                block_process[4] = 1
                want_stick_number[4] = 4

        if keys[pygame.K_0] and keys[pygame.K_RIGHT]:
            if s[4] == 1 and occupied_by[4] == 5 and s[0] == 0:
                if n != 4 and occupied_by[0] == 0:
                    fx[4] = 500
                    fy[4] = 80
                    s[4] = 0
                    occupied_by[4] = 0
                    eating_process[0] = 1

            if (s[4] == 0 and fx[4] != 500 and occupied_by[0] == 0) or n == 4:
                block_process[0] = 1
                want_stick_number[0] = 4

        if keys[pygame.K_1] and keys[pygame.K_RIGHT]:
            if s[0] == 1 and occupied_by[0] == 5 and s[1] == 0:
                if n != 4 and occupied_by[1] == 1:
                    fx[0] = 780
                    fy[0] = 220
                    s[0] = 0
                    occupied_by[0] = 1
                    eating_process[1] = 1
            if (s[0] == 0 and fx[0] != 780 and occupied_by[1] == 1) or n == 4:
                block_process[1] = 1
                want_stick_number[1] = 0

        if keys[pygame.K_2] and keys[pygame.K_RIGHT]:
            if s[1] == 1 and occupied_by[1] == 5 and s[2] == 0:
                if n != 4 and occupied_by[2] == 2:
                    fx[1] = 710
                    fy[1] = 520
                    s[1] = 0
                    occupied_by[1] = 2
                    eating_process[2] = 1
            if (s[1] == 0 and fx[1] != 710 and occupied_by[2] == 0) or n == 4:
                block_process[2] = 1
                want_stick_number[2] = 1

        if keys[pygame.K_3] and keys[pygame.K_RIGHT]:
            if s[2] == 1 and occupied_by[2] == 5 and s[3] == 0:
                if n != 4 and occupied_by[3] == 0:
                    fx[2] = 400
                    fy[2] = 555
                    s[2] = 0
                    occupied_by[2] = 3
                    eating_process[3] = 1
            if (s[2] == 0 and fx[2] != 400 and occupied_by[3] == 0) or n == 4:
                block_process[3] = 1
                want_stick_number[3] = 2

        if keys[pygame.K_4] and keys[pygame.K_RIGHT]:
            if s[3] == 1 and occupied_by[3] == 5 and s[4] == 0:
                if n != 4 and occupied_by[4] == 0:
                    fx[3] = 290
                    fy[3] = 270
                    s[3] = 0
                    occupied_by[3] = 4
                    eating_process[4] = 1
            if (s[3] == 0 and fx[3] != 500 and occupied_by[4] == 0) or n == 4:
                block_process[4] = 1
                want_stick_number[4] = 3

        if block_process[0] == 1:  # p0 block
            screen.blit(block, (560, 10))
            p0 = font.render("P0", True, (0, 0, 0))
            screen.blit(p0, (940, 200))

        if block_process[1] == 1:  # p1 block
            screen.blit(block, (790, 230))
            p1 = font.render("P1", True, (0, 0, 0))
            screen.blit(p1, (940, 230))

        if block_process[2] == 1:  # p2 block
            screen.blit(block, (655, 630))
            p2 = font.render("P2", True, (0, 0, 0))
            screen.blit(p2, (940, 260))

        if block_process[3] == 1:  # p3 block
            screen.blit(block, (315, 580))
            p3 = font.render("P3", True, (0, 0, 0))
            screen.blit(p3, (940, 290))

        if block_process[4] == 1:  # p4 block
            screen.blit(block, (270, 150))
            p4 = font.render("P4", True, (0, 0, 0))
            screen.blit(p4, (940, 320))

        if eating_process[0] == 1:
            screen.blit(eating, (px[0] + 10, py[0] - 20))
        if eating_process[1] == 1:
            screen.blit(eating, (px[1] + 10, py[1] - 20))
        if eating_process[2] == 1:
            screen.blit(eating, (px[2] + 15, py[2] + 100))
        if eating_process[3] == 1:
            screen.blit(eating, (px[3] + 10, py[3] + 100))
        if eating_process[4] == 1:
            screen.blit(eating, (px[4] + 10, py[4] - 20))

        if keys[pygame.K_0] and keys[pygame.K_r]:
            eating_process[0] = 0
            block_process[0] = 0
            for i in range(5):
                if occupied_by[i] == 0:
                    if i == 0:
                        fx[0] = 730
                        fy[0] = 150
                        s[0] = 1
                        occupied_by[0] = 5
                        if want_stick_number[1] == 0:
                            block_process[1] = 0
                    if i == 4:
                        fx[4] = 410
                        fy[4] = 100
                        s[4] = 1
                        occupied_by[4] = 5
                        if want_stick_number[4] == 4:
                            block_process[4] = 0
            n = n - 1

        if keys[pygame.K_1] and keys[pygame.K_r]:
            eating_process[1] = 0
            block_process[1] = 0
            for i in range(5):
                if occupied_by[i] == 1:
                    if i == 0:
                        fx[0] = 730
                        fy[0] = 150
                        s[0] = 1
                        occupied_by[0] = 5
                        if want_stick_number[0] == 0:
                            block_process[0] = 0
                    if i == 1:
                        fx[1] = 770
                        fy[1] = 450
                        s[1] = 1
                        occupied_by[1] = 5
                        if want_stick_number[2] == 1:
                            block_process[2] = 0
            n = n - 1

        if keys[pygame.K_2] and keys[pygame.K_r]:
            eating_process[2] = 0
            block_process[2] = 0
            for i in range(5):
                if occupied_by[i] == 2:
                    if i == 2:
                        fx[2] = 490
                        fy[2] = 590
                        s[2] = 1
                        occupied_by[2] = 5
                        if want_stick_number[1] == 2:
                            block_process[1] = 0
                    if i == 1:
                        fx[1] = 770
                        fy[1] = 450
                        s[1] = 1
                        occupied_by[1] = 5
                        if want_stick_number[1] == 1:
                            block_process[1] = 0
            n = n - 1

        if keys[pygame.K_3] and keys[pygame.K_r]:
            eating_process[3] = 0
            block_process[3] = 0
            for i in range(5):
                if occupied_by[i] == 3:
                    if i == 2:
                        fx[2] = 490
                        fy[2] = 590
                        s[2] = 1
                        occupied_by[2] = 5
                        if want_stick_number[2] == 2:
                            block_process[2] = 0
                    if i == 3:
                        fx[3] = 280
                        fy[3] = 360
                        s[3] = 1
                        occupied_by[3] = 5
                        if want_stick_number[4] == 3:
                            block_process[4] = 0
            n = n - 1

        if keys[pygame.K_4] and keys[pygame.K_r]:
            eating_process[4] = 0
            block_process[4] = 0
            for i in range(5):
                if occupied_by[i] == 4:
                    if i == 4:
                        fx[4] = 410
                        fy[4] = 100
                        s[4] = 1
                        occupied_by[4] = 5
                        if want_stick_number[0] == 4:
                            block_process[0] = 0
                    if i == 3:
                        fx[3] = 280
                        fy[3] = 360
                        s[3] = 1
                        occupied_by[3] = 5
                        if want_stick_number[3] == 3:
                            block_process[3] = 0
            n = n - 1

        for i in range(5):
            y = y + 30
            screen.blit(pImg[i], (px[i], py[i]))
            screen.blit(f[i], (fx[i], fy[i]))
            semaphore_text(i, s[i], 10, y)
        y = 30
        pygame.display.update()
    pygame.quit()


title = tk.Label(parent,
                 text="CONCURRENCY AND DEADLOCK", bg="#FCFADA", font=("TIMES Bold", 18)).place(x=150,
                                                                                               y=5)
syn = tk.Label(parent,
               text="1. CONCURRENCY MECHANISM", bg="#FCFADA", font=("Arial Bold", 12)).place(x=90,
                                                                                             y=100)
ddlk = tk.Label(parent,
                text="2. DEADLOCK MECHANISM", bg="#FCFADA", font=("Arial Bold", 12)).place(x=90,
                                                                                           y=500)
b1 = tk.Button(parent, text="Lock Variable", command=lock_variable, activeforeground="black",
               activebackground="#E6E2E2",
               height="1", width="20", bg="#FCFADA",
               pady=10).place(x="270", y="150")
b2 = tk.Button(parent, text="Strict Alternation", command=strict_alternation, activeforeground="black",
               activebackground="#E6E2E2", height="1",
               width="20", bg="#FCFADA",
               pady=10).place(x="270", y="200")
b3 = tk.Button(parent, text="peterson solution", command=peterson_algo, activeforeground="black",
               activebackground="#E6E2E2", height="1",
               width="20", bg="#FCFADA",
               pady=10).place(x="270", y="250")
b4 = tk.Button(parent, text="TSL(Test Set Lock)", command=testset, activeforeground="black", activebackground="#E6E2E2",
               height="1",
               width="20", bg="#FCFADA",
               pady=10).place(x="270", y="300")
b5 = tk.Button(parent, text="counting Semaphore", command=counting_semaphore, activeforeground="black",
               activebackground="#E6E2E2",
               height="1", width="20", bg="#FCFADA",
               pady=10).place(x="270", y="350")
b6 = tk.Button(parent, text="Binary Semaphore", command=Binary_semaphore, activeforeground="black",
               activebackground="#E6E2E2",
               height="1", width="20", bg="#FCFADA",
               pady=10).place(x="270", y="400")
b7 = tk.Button(parent, text="Producer Consumer", command=producer_consumer, activeforeground="black",
               activebackground="#E6E2E2", height="1",
               width="20", bg="#FCFADA",
               pady=10).place(x="270", y="550")
b8 = tk.Button(parent, text="Dinning Philosopher", command=Dinning_philosopher, activeforeground="black",
               activebackground="#E6E2E2", height="1",
               width="20", bg="#FCFADA",
               pady=10).place(x="270", y="600")

parent.mainloop()
