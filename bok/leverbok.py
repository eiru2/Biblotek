import pygame
from sys import exit, path
path.append('../BIBLOTEK') 

import funk.Button as Bt
import funk.inputbox as Ib
import funk.personer as Pr
import funk.boker as Bok
import funk.oppstar_slut as slutt
import config as con

"""
for o lever in bok ved bruk av isbn
"""

pygame.init()




screen = pygame.display.set_mode((con.width,con.height))

def run(biblotek):
    buttonsize = [100,50]

    back = Bt.Button((10,10), "back", fontSize=26, buttonsize=buttonsize, buttonCooler=con.colors["Red"])
    leverbok = Bt.Button((350,700), "lever bok", fontSize=26, buttonsize=(150,75), buttonCooler=con.colors["Red"])
    

    InIsbn = Ib.Inputbox((100,300),(250,100),con.colors["White"],"Isbn")   

    

    
    

    Run = True

    clicked = False
    
    offset = [0,0] 

            
    while Run == True:
        

        screen.fill(con.colors["Black"])

        InIsbn.draw(screen)

        
        back.draw(screen)
        leverbok.draw(screen)


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                slutt.avslutt(biblotek)
                Run = False
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

                    if InIsbn.rect().collidepoint(mouse_pos):
                        InIsbn.active = True 
                    else:
                        InIsbn.active = False
                        
                    if leverbok.click(mouse_pos):
                        # kjeker om den finner isbn i en orliste
                        biblotek.get_bokDict()
                        try:
                            print(biblotek.bokDict[InIsbn.inputText])
                            index = biblotek.bokDict[InIsbn.inputText]["id"]
                            print(index)
                            if biblotek.boker[index].utlont == False:
                                print("er levert in")
                            else:
                                for person in biblotek.personer:
                                    for i in range(len(person.boker)):
                                        if person.boker[i] == index:
                                            person.boker.remove(index)
                                        else:
                                            print("fant ingen person som har lånt")
                                
                                biblotek.boker[index].utlont = False
                                    
                                
                        
                        except:
                            print("fant ikke insb i dataen")
                        
                            
                    mouse_pos[0] -= offset[0]
                    mouse_pos[1] -= offset[1]

            
            elif event.type == pygame.MOUSEWHEEL:
                clicked = False
                # offset[0] += event.x * con.scrollspeed[0]
                offset[1] += event.y * con.scrollspeed[1]
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # print(personListe)
                    for bok in biblotek.boker:
                        print("Navn: " + bok.titel, "type: " + bok.boktype, )
                       
                            
                         
                if InIsbn.active:
                    # Enter 
                    if event.key == pygame.K_RETURN:
                        # navn = str(inp.inputText)
                        # inp.inputText = ''
                        InIsbn.active = False
                    # fjerner
                    elif event.key == pygame.K_BACKSPACE:
                        InIsbn.inputText = InIsbn.inputText[:-1]
                    # legger til karakter
                    else:
                        InIsbn.inputText += event.unicode
        





        # print(offset)   
        pygame.display.update()

#  testing
import funk.boker as bok
biblo = bok.Biblotek("Jens biblotek", "skien")



a = bok.Bok("Harry poter", "jk rowling" , 1 , "literatur","fantasy" )
b = bok.Bok("Katt med støvler", "OLav" , 3 , "literatur", "fantasy" )
c = bok.Bok("Bio 2", "Jens" , 2 , "fagbok","Biologi" )

biblo.leggTilBok(a)
biblo.leggTilBok(b)
biblo.leggTilBok(c)
for i in range(500):
    c = bok.Bok(("Bio "+str(i)), "Jens" , (i+4) , "fagbok", "Biologi" )
    biblo.leggTilBok(c)


# state = 1
# while state == 1:
#     state = run(biblo)
#     print(state)