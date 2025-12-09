import pygame
from sys import exit, path
path.append('../BIBLOTEK') 



import config as con






pygame.init()


screen = pygame.display.set_mode((con.width,con.height))



Run = True


while Run == True:
    screen.fill((0,0,0))
    for x in range(0,con.width ,20):
        for y in range(0,con.height, 20):
            pygame.draw.rect(screen,(255-(x/10) ,255-(x/10),255-(y/10)),(x,y,20,20))
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
            pygame.quit()
            exit()

      
    

             
    pygame.display.update()
