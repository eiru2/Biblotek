import pygame
from sys import exit, path
path.append('../BIBLOTEK') 

import funk.Button as Bt
import funk.oppstar_slut as slutt
import config as con

import bok.lån as lån

pygame.init()

"""
Den viser info om boken 
Lar det gå vidre til o lone boker
"""


screen = pygame.display.set_mode((con.width,con.height))
def run(biblotek, index):
    buttonsize = [100,50]

    back = Bt.Button((10,10), "back", fontSize=26, buttonsize=buttonsize, buttonCooler=con.colors["Red"])
    
    lone = Bt.Button((350,700), "låne", fontSize=26, buttonsize=buttonsize, buttonCooler=con.colors["Red"])
    
    bok = biblotek.boker[index]
    print(bok.titel)
    font32 = pygame.font.SysFont("Arial", 64)
    font16 = pygame.font.SysFont("Arial", 32)
    
    titel = font32.render(bok.titel, True, con.colors["White"])
    boktype = font16.render("boktype: "+bok.boktype, True, con.colors["White"])
    sjanger = font16.render("Sjanger: "+bok.fag_sjanger, True, con.colors["White"])
    forfater = font16.render("Forfater: "+bok.forfater, True, con.colors["White"])
    isbn = font16.render("isb: "+str(bok.isbn), True, con.colors["White"])
    utlont = font16.render("Utlånt: "+str(bok.utlont), True, con.colors["White"])
    
    textlist = [boktype,sjanger,forfater,isbn,utlont]
    Run = True

    clicked = False
    
    offset = [0,0] 

    while Run == True:
        

        screen.fill(con.colors["Black"])
        screen.blit(titel,(20,60))
        y = 150
        for text in textlist:
            screen.blit(text,(20,y))
            y+=60
        


        
        back.draw(screen)
        lone.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
                slutt.avslutt(biblotek)
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                if event.button == 1:
                    clicked = True
                
            elif event.type == pygame.MOUSEBUTTONUP and clicked == True:
                if event.button == 1:
                    clicked = False
                    mouse_pos = list(pygame.mouse.get_pos())
                    
                    if back.click(mouse_pos):
                        return 0
                    if lone.click(mouse_pos):
                        lån.run(biblotek, index)
                       
                    mouse_pos[0] -= offset[0]
                    mouse_pos[1] -= offset[1]

            
            elif event.type == pygame.MOUSEWHEEL:
                clicked = False
                # offset[0] += event.x * con.scrollspeed[0]
                offset[1] += event.y * con.scrollspeed[1]





        # print(offset)   
        pygame.display.update()

#  testing
import funk.boker as bok
biblo = bok.Biblotek("Jens biblotek", "skien")

# a = bok.literatur("Harry poter", "jk rowling" , 1 , "fantasy" )
# b = bok.literatur("Katt med støvler", "OLav" , 3 , "fantasy" )
# c = bok.Fagbok("Bio 2", "Jens" , 2 , "Biologi" )

# biblo.leggTilBok(a)
# biblo.leggTilBok(b)
# biblo.leggTilBok(c)
# for i in range(50):
#     c = bok.Fagbok(("Bio "+str(i)), "Jens" , 2 , "Biologi" )
#     biblo.leggTilBok(c)


# state = 1
# while state == 1:
#     state = run(biblo, 0)
#     print(state)