################################
# Whole Code For Youtube Video #
################################

import time
import pygame
import sys
pygame.init()

grid = [
       ['', '', ''],
       ['', '', ''],
       ['', '', '']
        ]

a = 0
white = (255, 255, 255)
black = (0, 0, 0)
ximage = pygame.image.load('x.png')
oimage = pygame.image.load('o.png')
cellcord1 = (0 + 25,0 + 25)
cellcord2 = (0 + 25,200 + 25)
cellcord3 = (0 + 25,400 + 25)
cellcord4 = (200 + 25,0 + 25)
cellcord5 = (200 + 25,200 + 25)
cellcord6 = (200 + 25,400 + 25)
cellcord7 = (400 + 25,0 + 25)
cellcord8 = (400 + 25,200 + 25)
cellcord9 = (400 + 25,400 + 25)

win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic Tac Toe")
win.fill((255, 255, 255))

font2 = pygame.font.SysFont('freesansbold', 75, True)

def cross(grid):
    if grid[0][0] == grid[0][1] == grid[0][2] == 'x':
        write(130, 300, 'PLAYER 1 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[0][0] == grid[0][1] == grid[0][2] == 'o':
        write(130, 300, 'PLAYER 2 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[1][0] == grid[1][1] == grid[1][2] == 'x':
        write(130, 300, 'PLAYER 1 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[1][0] == grid[1][1] == grid[1][2] == 'o':
        write(130, 300, 'PLAYER 2 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[2][0] == grid[2][1] == grid[2][2] == 'x':
        write(130, 300, 'PLAYER 1 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[2][0] == grid[2][1] == grid[2][2] == 'o':
        write(130, 300, 'PLAYER 2 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[0][0] == grid[1][0] == grid[2][0] == 'x':
        write(130, 300, 'PLAYER 1 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[0][0] == grid[1][0] == grid[2][0] == 'o':
        write(130, 300, 'PLAYER 2 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[0][1] == grid[1][1] == grid[2][1] == 'x':
        write(130, 300, 'PLAYER 1 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[0][1] == grid[1][1] == grid[2][1] == 'o':
        write(130, 300, 'PLAYER 2 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[0][2] == grid[1][2] == grid[2][2] == 'x':
        write(130, 300, 'PLAYER 1 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[0][2] == grid[1][2] == grid[2][2] == 'o':
        write(130, 300, 'PLAYER 2 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[0][0] == grid[1][1] == grid[2][2] == 'x':
        write(130, 300, 'PLAYER 1 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[0][0] == grid[1][1] == grid[2][2] == 'o':
        write(130, 300, 'PLAYER 2 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[0][2] == grid[1][1] == grid[2][0] == 'x':
        write(130, 300, 'PLAYER 1 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

    if grid[0][2] == grid[1][1] == grid[2][0] == 'o':
        write(130, 300, 'PLAYER 2 WON', (0, 0, 255))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pygame.quit()
        sys.exit()

def write(x, y, val,color):
    num = font2.render(val, True, color)
    win.blit(num, (x, y))

def pygame_MouseButtonClick(a):


    #check Mouse click co-ordinate
    (x, y) = pygame.mouse.get_pos()
    font = pygame.font.SysFont('Showcard Gothic', 60)
    # Block 1 logic
    if x >= 0 and x <= 200 and y >= 0 and y <= 200:
        cell1 = True
        if a == 0:
            win.blit(ximage, cellcord1)
            pygame.draw.rect(win, white, (75, 600, 0, 610))
            write(0, 610, 'PLAYER 1', (0,0,0))
            grid[0][0] = 'x'
            pygame.display.update()
            a = 1

        else:
            win.blit(oimage, cellcord1)
            pygame.draw.rect(win, white, (75, 600, 0, 610))
            write(0, 610, 'PLAYER 2', (0,0,0))
            grid[0][0] = 'o'
            pygame.display.update()
            a = 0
    # Block 4 logic
    if x >= 200 and x <= 400 and y >= 0 and y <= 200:
        cell4 = True
        if a == 0:
            win.blit(ximage, cellcord4)
            pygame.draw.rect(win, white, (75, 600, 0, 610))
            write(0, 610, 'PLAYER 1', (0, 0, 0))
            grid[1][0] = 'x'
            pygame.display.update()
            a = 1
        else:
            win.blit(oimage, cellcord4)
            pygame.draw.rect(win, white, (75, 600, 0, 610))
            write(0, 610, 'PLAYER 2', (0,0,0))
            grid[1][0] = 'o'
            pygame.display.update()
            a = 0
    # Block 7 logic
    if x >= 400 and x <= 600 and y >= 0 and y <= 200:
        cell7 = True
        if a == 0:
            win.blit(ximage, cellcord7)

            write(0, 610, 'PLAYER 1', (0,0,0))
            grid[2][0] = 'x'
            pygame.display.update()
            a = 1
        else:
            win.blit(oimage, cellcord7)
            pygame.draw.rect(win, white, (75, 600, 0, 610))
            write(0, 610, 'PLAYER 2', (0,0,0))
            grid[2][0] = 'o'
            pygame.display.update()
            a = 0
    # Block 2 logic
    if x >= 0 and x <= 200 and y >= 200 and y <= 400:
        cell2 = True
        if a == 0:
            win.blit(ximage, cellcord2)

            write(0, 610, 'PLAYER 1', (0,0,0))
            grid[0][1] = 'x'
            pygame.display.update()
            a = 1
        else:
            win.blit(oimage, cellcord2)
            grid[0][1] = 'o'
            write(0, 610, 'PLAYER 2', (0,0,0))
            pygame.display.update()
            a = 0
    # Block 5 logic
    if x >= 200 and x <= 400 and y >= 200 and y <= 400:
        cell5 = True
        if a == 0:
            win.blit(ximage, cellcord5)
            write(0, 610, 'PLAYER 1', (0,0,0))
            grid[1][1] = 'x'
            pygame.display.update()
            a = 1
        else:
            win.blit(oimage, cellcord5)
            grid[1][1] = 'o'
            write(0, 610, 'PLAYER 2', (0,0,0))
            pygame.display.update()
            a = 0
    # Block 8 logic
    if x >= 400 and x <= 600 and y >= 200 and y <= 400:
        cell8 = True
        if a == 0:
            win.blit(ximage, cellcord8)
            write(0, 610, 'PLAYER 1', (0,0,0))
            grid[2][1] = 'x'
            pygame.display.update()
            a = 1
        else:
            win.blit(oimage, cellcord8)
            grid[2][1] = 'o'
            write(0, 610, 'PLAYER 2', (0,0,0))
            pygame.display.update()
            a = 0
    # Block 3 logic
    if x >= 0 and x <= 200 and y >= 400 and y <= 600:
        cell3 = True
        if a == 0:
            win.blit(ximage, cellcord3)

            write(0, 610, 'PLAYER 1', (0,0,0))
            grid[0][2] = 'x'
            pygame.display.update()
            a = 1
        else:
            win.blit(oimage, cellcord3)
            write(0, 610, 'PLAYER 2', (0,0,0))
            grid[0][2] = 'o'
            pygame.display.update()
            a = 0
    # Block 6 logic
    if x >= 200 and x <= 400 and y >= 400 and y <= 600:
        cell6 = True
        if a == 0:
            win.blit(ximage, cellcord6)
            write(0, 610, 'PLAYER 1', (0,0,0))
            grid[1][2] = 'x'
            pygame.display.update()
            a = 1
        else:
            win.blit(oimage, cellcord6)
            grid[1][2] = 'o'
            write(0, 610, 'PLAYER 2', (0,0,0))
            pygame.display.update()
            a = 0
    # Block 9 logic
    if x >= 400 and x <= 600 and y >= 400 and y <= 600:
        cell9 = True
        if a == 0:
            win.blit(ximage, cellcord9)

            write(0, 610, 'PLAYER 1', (0,0,0))
            grid[2][2] = 'x'
            pygame.display.update()
            a = 1
        else:
            win.blit(oimage, cellcord9)

            write(0, 610, 'PLAYER 2', (0,0,0))
            grid[2][2] = 'o'
            pygame.display.update()
            a = 0
    return a
run = True
while run:
    # Display 3*3 Table
    pygame.draw.line(win, (0,0,0), (0,200), (600,200))
    pygame.draw.line(win, (0,0,0), (0,400), (600,400))
    pygame.draw.line(win, (0,0,0), (200,0), (200,600))
    pygame.draw.line(win, (0,0,0), (400,0), (400,600))
    pygame.draw.line(win, (0, 0, 0), (0,600), (600, 600))
    # End of Display 3*3 Table

    #for a in range(8):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            a = pygame_MouseButtonClick(a)
            cross(grid)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
