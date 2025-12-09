import pygame
from sys import exit, path

import funk.Button as Bt
import funk.oppstar_slut as slutt
import config as con

"""
Det er en meny som lar deg velg mellom 

"""

pygame.init()




screen = pygame.display.set_mode((con.width,con.height))
def run(biblotek):
    buttonsize = [200,100]


    x = (con.width/2) - 100

    y = [100, 250, 400]

    bok = Bt.Button((x,y[0]), "Bøker", fontSize=32, buttonsize=buttonsize)
    person = Bt.Button((x,y[1]), "person", fontSize=32, buttonsize=buttonsize)
    leverIn = Bt.Button((x,y[2]), "leverin", fontSize=32, buttonsize=buttonsize)

    Run = True

    clicked = False
    
    offset = [0,0] 

    while Run == True:
        

        screen.fill(con.colors["Black"])
        bok.draw(screen)
        person.draw(screen)
        leverIn.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                slutt.avslutt(biblotek)
                Run = False
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                mouse_pos = pygame.mouse.get_pos()
                
                if bok.click(mouse_pos):
                    return 1

                elif person.click(mouse_pos):
                    return 2

                elif leverIn.click(mouse_pos):
                    return 4
                



                
        pygame.display.update()

#  testing
# import funk.boker as bok
# biblo = bok.Biblotek("Jens biblotek", "skien")
# state = 0
# while state == 0:
#     state = run(state,biblo)
#     print(state)