import pygame
import funk.inputbox as inp
import config as con

from sys import exit, path
import os

pygame.init()


screen = pygame.display.set_mode((con.width,con.height))
def run():
    a =inp.Inputbox((100,100),(200,100),con.colors["White"],"Titel")

    Run = True

    clicked = False

    while Run == True:
                
        screen.fill(con.colors["Black"])
        a.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                if a.rect().collidepoint(mouse_pos):
                    a.active = True
                else:
                    a.active = False
                    
                    
            if event.type == pygame.KEYDOWN:
                    if a.active:
                        # Enter 
                        if event.key == pygame.K_RETURN:
                            print(a.inputText)
                            a.inputText = ''
                            a.active = False
                        # fjerner
                        elif event.key == pygame.K_BACKSPACE:
                            a.inputText = a.inputText[:-1]
                        # legger til karakter
                        else:
                            a.inputText += event.unicode

                
        pygame.display.update()
