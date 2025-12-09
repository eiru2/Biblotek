import pygame
from sys import exit, path
path.append('../BIBLOTEK') 

import funk.Button as Bt
import funk.inputbox as Ib
import funk.personer as Pr
import funk.oppstar_slut as slutt
import funk.boker as Bok
import config as con
"""
Side for å legg till en bok
"""


pygame.init()




screen = pygame.display.set_mode((con.width,con.height))

def run(biblotek):
    buttonsize = [100,50]

    back = Bt.Button((10,10), "back", fontSize=26, buttonsize=buttonsize, buttonCooler=con.colors["Red"])
    leggtill = Bt.Button((350,700), "legg till bok", fontSize=26, buttonsize=(150,75), buttonCooler=con.colors["Red"])
    
    Intitel = Ib.Inputbox((100,100),(250,100),con.colors["White"],"titel")
    InForfater = Ib.Inputbox((400,100),(250,100),con.colors["White"],"Forfater")
    InIsbn = Ib.Inputbox((100,300),(250,100),con.colors["White"],"Isbn")   
    InBoktype = Ib.Inputbox((400,300),(250,100),con.colors["White"],"Fagbok eller literatur")
    InFag_Sjanger = Ib.Inputbox((100,500),(250,100),con.colors["White"],"sjanger/fag")
    
    inputlist = [Intitel,InForfater,InIsbn,InBoktype,InFag_Sjanger]
    
    

    Run = True

    clicked = False
    
    offset = [0,0] 

            
    while Run == True:
        

        screen.fill(con.colors["Black"])

        for inp in inputlist:
            inp.draw(screen)
            

        
        back.draw(screen)
        leggtill.draw(screen)


        
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

                    for inp in inputlist:   
                        if inp.rect().collidepoint(mouse_pos):
                            inp.active = True
                        else:
                            inp.active = False
                            
                    if leggtill.click(mouse_pos):
                        # kjekker om det er gyldig verdier for leggtil en bok
                        fylltut = True
                        for inp in inputlist:
                            if inp.inputText.strip() == "":
                                fylltut = False
                            
                                
                        if fylltut == False:  
                            print("Ikke utfyltt")  
                            break    

                        eksisteren_isbn = False
                        for bok in biblotek.boker:
                            if bok.isbn == InIsbn.inputText:
                                eksisteren_isbn = True
                        if eksisteren_isbn:
                            print("Alle redd ekistern isbn")
                            break
                        
                        try:
                            int(InIsbn.inputText.strip())
                        except:
                            print("isbn er ikke et hell nummer")
                            break
                        
                                
             
                        # kan fjernest
                        if InBoktype.inputText.strip() == "fagbok":
                            if InFag_Sjanger.inputText.strip() not in con.fag:
                                print("aksepter ikke fag")
                                break
                            biblotek.boker.append(Bok.Bok(Intitel.inputText.strip(), InForfater.inputText.strip(), InIsbn.inputText.strip(), "fagbok", InFag_Sjanger.inputText.strip()))
                            return 0
                        elif InBoktype.inputText.strip() == "literatur":
                            if InFag_Sjanger.inputText.strip() not in con.sjangre:
                                print("aksepter ikke sjanger")
                                break
                            biblotek.boker.append(Bok.Bok(Intitel.inputText.strip(), InForfater.inputText.strip(), InIsbn.inputText.strip(), "literatur", InFag_Sjanger.inputText.strip()))
                            return 0
                        else:
                            print("ugyldig bok")
                            
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
                        print("Navn: " + bok.titel, "type: " + bok.boktype)
                       
                            
                for inp in inputlist:          
                    if inp.active:
                        # Enter 
                        if event.key == pygame.K_RETURN:
                            # navn = str(inp.inputText)
                            # inp.inputText = ''
                            inp.active = False
                        # fjerner
                        elif event.key == pygame.K_BACKSPACE:
                            inp.inputText = inp.inputText[:-1]
                        # legger til karakter
                        else:
                            inp.inputText += event.unicode
        





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
#     state = run(biblo)
#     print(state)