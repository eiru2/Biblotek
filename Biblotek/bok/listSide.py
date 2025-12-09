import pygame
from sys import exit, path
path.append('../BIBLOTEK') 


import funk.Button as Bt
import funk.inputbox as Ib
import funk.boker as boker
import funk.oppstar_slut as slutt
import config as con

import bok.bokside as bokside
import bok.leggtil as leggtil


pygame.init()


def update_boker(biblotek, search:str = ""):
    """_summary_

    Args:
        biblotek (class): biblotek classen
        search (str, optional): Hva den skal filtrere etter i titel og forfater. Defaults to "".

    Returns:
        list: Det er en liste over knapper som har en format i knapper
    """
    bokBoxer = []
    x = 25
    y = 100
    
    size = [150,150]
    index = 0
    for bok in biblotek.boker:
        # print(bok)
        if search in bok.titel or search in bok.forfater:
            bokBox = Bt.Button((x,y),bok.titel, buttonsize=size, fontSize=20, returnValue=index)
            bokBoxer.append(bokBox)
            x += 200
            if x >= con.width-10:
                y+= 200
                x = 25
        index += 1
        
    return bokBoxer
    

screen = pygame.display.set_mode((con.width,con.height))
def run(biblotek):
    buttonsize = [100,50]
    


    back = Bt.Button((10,10), "back", fontSize=26, buttonsize=buttonsize, buttonCooler=con.colors["Red"])
    leggtilBok = Bt.Button((300,650), "legg til bok", fontSize=32, buttonsize=[200,100])
    
    search = Ib.Inputbox((200,10), buttonsize, con.colors["White"], "søke" , fontSize=26)
    bokBoxer = update_boker(biblotek)

        
        

    Run = True

    clicked = False
    
    offset = [0,0] 

    while Run == True:
        

        screen.fill(con.colors["Black"])

        for bokBox in bokBoxer:

            if bokBox.pos[1] + offset[1] > -70 and bokBox.pos[1] < con.height - offset[1] - 150:
                bokBox.draw(screen,offset)
                
        # for o lage en boks som bok listen kan hjemes bak før forsviner
        pygame.draw.rect(screen, con.colors["Black"],(0,600,con.width,200))
        pygame.draw.rect(screen, con.colors["Black"],(0,0,con.width,70))
        
        back.draw(screen)
        leggtilBok.draw(screen)
        search.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                slutt.avslutt(biblotek)
                Run = False
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print(biblotek.personer)
                    for person in biblotek.personer:
                        print("Navn: " + person.navn)
                        for id in person.boker:
                            print(id)
                            
                if event.key == pygame.K_t:
                    print(biblotek.boker)

            
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                if event.button == 1:
                    clicked = True
                
            elif event.type == pygame.MOUSEBUTTONUP and clicked == True:
                if event.button == 1:
                    clicked = False
                    mouse_pos = list(pygame.mouse.get_pos())
                    
                    click = False # for o sorge for at det er kun en av kanppen som ut fører en hedelse cis overlap
                    if back.click(mouse_pos):
                        click = False
                        return 0
                    elif search.rect().collidepoint(mouse_pos):
                        click = True
                        search.active = True  
                    elif leggtilBok.click(mouse_pos):
                        click = True
                        leggtil.run(biblotek)
                        bokBoxer = update_boker(biblotek)    
                    else:
                        search.active = False

                    mouse_pos[0] -= offset[0]
                    mouse_pos[1] -= offset[1]
                    if click == False:
                        for bokBox in bokBoxer:
                            temp = bokBox.click(mouse_pos)
                            # print(temp)
                            if type(temp) != type(False):
                                bokside.run(biblotek,temp)
                                # return str(str(state) + "," + str(temp))
            
            elif event.type == pygame.MOUSEWHEEL:
                clicked = False
                # offset[0] += event.x * con.scrollspeed[0]
                offset[1] += event.y * con.scrollspeed[1]
                
            if event.type == pygame.KEYDOWN:
                    if search.active:
                        # Enter 
                        if event.key == pygame.K_RETURN:
                            print(search.inputText)
                            bokBoxer = update_boker(biblotek, search.inputText)
                            search.inputText = ''
                            search.active = False
                        # fjerner
                        elif event.key == pygame.K_BACKSPACE:
                            search.inputText = search.inputText[:-1]
                        # legger til karakter
                        else:
                            search.inputText += event.unicode





        # print(offset)   
        pygame.display.update()

#  testing
import funk.boker as bok
biblo = bok.Biblotek("Jens biblotek", "skien")

search = bok.Bok("Harry poter", "jk rowling" , 1 , "literatur","fantasy" )
b = bok.Bok("Katt med støvler", "OLav" , 3 , "literatur", "fantasy" )
c = bok.Bok("Bio 2", "Jens" , 2 , "fagbok","Biologi" )

biblo.leggTilBok(search)
biblo.leggTilBok(b)
biblo.leggTilBok(c)
for i in range(500):
    c = bok.Bok(("Bio "+str(i)), "Jens" , (i+4) , "fagbok", "Biologi" )
    biblo.leggTilBok(c)


# state = 1
# while state == 1:
#     state = run(biblo)
#     print(state)