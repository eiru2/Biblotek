import pygame
from sys import exit, path
path.append('../BIBLOTEK') 

import funk.Button as Bt
import funk.inputbox as Ib
import funk.personer as Pr
import funk.oppstar_slut as slutt
import config as con

"""
for o lone boker po et navn
"""

pygame.init()




screen = pygame.display.set_mode((con.width,con.height))
def run(biblotek, index):
    buttonsize = [100,50]

    back = Bt.Button((10,10), "back", fontSize=26, buttonsize=buttonsize, buttonCooler=con.colors["Red"])
    InNavn = Ib.Inputbox((100,100),(200,100),con.colors["White"],"Navn")
    lone = Bt.Button((350,700), "låne", fontSize=26, buttonsize=buttonsize, buttonCooler=con.colors["Red"])
    
    bok = biblotek.boker[index]
    print(bok.titel)

    

    

    Run = True

    clicked = False
    
    offset = [0,0] 

    def lon_bok(navn:str):
        """_summary_
        lånner ut boken

        Args:
            navn (str): navn po persone som skall lone boken
        """
        inlist = False
        if biblotek.boker[index].utlont:
            print("lånt ut ", biblotek.boker[index].titel , index)
        else:
            # kjeker om person allerde eksister
            for person in biblotek.personer:
                if navn == person.navn:
                    person.leggTilBok(index)
                    biblotek.boker[index].utlont = True
                    inlist = True
                        
            if inlist == False:
                biblotek.leggTilpersoner((Pr.person(str(navn))))
                # biblotek.personer.append()
                biblotek.personer[-1].leggTilBok(index)
                biblotek.boker[index].utlont = True
    
            
    while Run == True:
        

        screen.fill(con.colors["Black"])



        
        back.draw(screen)
        lone.draw(screen)
        InNavn.draw(screen)
        
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
                        navn = str(InNavn.inputText)
                        lon_bok(navn)
                        return 0
                        
                    if InNavn.rect().collidepoint(mouse_pos):
                        InNavn.active = True
                    else:
                        InNavn.active = False
                    mouse_pos[0] -= offset[0]
                    mouse_pos[1] -= offset[1]

            
            elif event.type == pygame.MOUSEWHEEL:
                clicked = False
                # offset[0] += event.x * con.scrollspeed[0]
                offset[1] += event.y * con.scrollspeed[1]
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # test key for print ut verdier om personer
                    # print(personListe)
                    for person in biblotek.personer:
                        print("Navn: " + person.navn)
                        for id in person.boker:
                            print(id)
                if InNavn.active:
                    # Enter 
                    if event.key == pygame.K_RETURN:
                        navn = str(InNavn.inputText)
                        lon_bok(navn)
                        
                        
                        
                        InNavn.inputText = ''
                        InNavn.active = False
                    # fjerner
                    elif event.key == pygame.K_BACKSPACE:
                        InNavn.inputText = InNavn.inputText[:-1]
                    # legger til karakter
                    else:
                        InNavn.inputText += event.unicode
        





        # print(offset)   
        pygame.display.update()

#  testing
import funk.boker as bok
biblo = bok.Biblotek("Jens biblotek", "skien")



# a = bok.literatur("Harry poter", "jk rowling" , 1 , "fantasy" )
# b = bok.literatur("Katt med støvler", "OLav" , 3 , "fantasy" )
b = bok.Bok("Bio 1", "Jens" , 2 ,"fagbok", "Biologi" )
c = bok.Bok("Bio 2", "Jens" , 2 ,"fagbok", "Biologi" )

# biblo.leggTilBok(a)
biblo.leggTilBok(b)
biblo.leggTilBok(c)
# for i in range(50):
#     c = bok.Fagbok(("Bio "+str(i)), "Jens" , 2 , "Biologi" )
    # biblo.leggTilBok(c)


# state = 1
# while state == 1:
#     state = run(biblo, 0)
#     print(state)