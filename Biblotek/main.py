import pygame
import config as con
import funk.boker as bok
import funk.personer as per
import funk.oppstar_slut as  star_slutt

from sys import exit, path


import _test.test as test
import FrontSide
import bok.listSide as listSide
import bok.leverbok as leverbok

"""
Den som kjore helle koden
"""


pygame.init()


screen = pygame.display.set_mode((con.width,con.height))

biblo = bok.Biblotek("Jens biblotek", "skien")

star_slutt.oppstart(biblo)


STATE = 0    # 1.x er for bøker     3.x er for forfater      4.x er leve in

Run = True


while Run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            star_slutt.avslutt(biblo)
            Run = False
            pygame.quit()
            exit()
    screen.fill(con.colors["Black"])
    if STATE == -1:
        test.run()
    if STATE == 0:
        STATE = FrontSide.run(biblo)
    if STATE == 1:
        STATE = listSide.run(biblo)
    if STATE == 4:
        STATE = leverbok.run(biblo)


             
    pygame.display.update()
