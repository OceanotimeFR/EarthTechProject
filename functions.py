import pygame, time
from colors import *

# Initialisation
pygame.init()

width, height = 1366, 720

efrei = pygame.image.load("images\efrei2.png").convert_alpha()
screen = pygame.display.set_mode((width, height))

police2 = pygame.font.SysFont("Bahnschrift",50)
police = pygame.font.SysFont("Bahnschrift",25)

fond = pygame.image.load("images\montagne.jpg").convert_alpha()
efrei = pygame.image.load("images\efrei2.png").convert_alpha()
gamelogo = pygame.image.load("images\greencity-transformed.png").convert_alpha()


def loading_screen(image,ecran,image2,width,height):
    #? Loading Logo EFREI
    for i in range (101) :
        image.set_alpha(i)
        ecran.blit(image,(500,300))
        time.sleep(0.05)
        pygame.display.flip()
        if i==100 : break
        pygame.display.flip()
    time.sleep(1)

    #? Reset Ecran
    pygame.draw.rect(ecran,WHITE,[0, 0, width, height],0)
    pygame.display.flip()


    #* Loading Logo GreenCity
    for i in range (101) :
        image2.set_alpha(i)
        ecran.blit(image2,(500,150))
        time.sleep(0.025)
        pygame.display.flip()
        if i==100 : break
        pygame.display.flip()
    time.sleep(1)


    #* Bordure de la barre de chargement
    pygame.draw.rect(ecran,BLACK,[width/2-250, 500, 500, 35],1)
    pygame.display.flip()


    #* Barre de chargement
    progress = 0
    for i in range (500) :
        progress+=1
        time.sleep(0.0025)
        pygame.draw.rect(ecran,GREEN,[width/2-250, 500, progress, 35],0)
        pygame.display.flip()
    time.sleep(3)

def printspeed(word, speed = 50, sound = "", volume = 1):
    word = str(word)
    string = ""
    for i in range(len(str(word))):
        string += word[i]
        print(f"\r{string}", end=" ")
        time.sleep(0.01)

def draw_image(image,x,y):
    screen.blit(image,(x,y))

def draw_text(text,font,text_col,x,y):
    txt = police.render(text,True,text_col)
    screen.blit(txt,(x,y))

def etpgame_ui(pos_y,image,scale_x,scale_y,pos_x,pos2_y) :
    import pygame

    pygame.draw.rect(screen,BLACK,[63,pos_y, 195, 50],1,10) # Contours
    pygame.draw.rect(screen,BLACK,[12, pos_y, 50, 50],0,10) # Fond
    pygame.display.flip()
    img = pygame.image.load(image).convert_alpha()
    img = pygame.transform.scale(img, (scale_x, scale_y))
    screen.blit(img,(pos_x,pos2_y))


def game_ui() :
    # Ombre
    pygame.draw.rect(screen,DARK_GREEN,[7, 15, 250, 154],0,10)
    pygame.display.flip()
    # Fond
    pygame.draw.rect(screen,GREEN,[10, 10, 250, 154],0,10)
    pygame.display.flip()

    etpgame_ui(12,"images\clock.png",74,75,0,2)
    etpgame_ui(62,"images\coin.png",70,70,2,53)
    etpgame_ui(112,"images\city.png",50,50,12,112)

    pygame.display.flip()

def etpvar_maj(txt,val,nbtour,rectpos_y,txtpos_y,txtcol) :
    import pygame, time
    i = 0
    for i in range (nbtour) :
        draw_text(f"{txt} : {val}","",txtcol,73,txtpos_y)
        pygame.draw.rect(screen,BLACK,[63, rectpos_y, 195, 50],1,10)
        pygame.display.flip()
        pygame.draw.rect(screen,BISTRE,[63, rectpos_y, 195, 50],0,10)
        pygame.display.flip()
    draw_text(f"{txt} : {val}","",txtcol,73,txtpos_y)
    pygame.draw.rect(screen,BLACK,[63, rectpos_y, 195, 50],1,10)
    pygame.display.flip()

# Fond
def mainrects(t):
    global rect_x, rect_y
    rect_x = t
    rect_y = 355
    # Rectangle Gauche
    pygame.draw.rect(screen,WOOD,[t, 355, 1346/3, 355],0,10)
    pygame.display.flip()
    # Rectangle Middle
    pygame.draw.rect(screen,BISTRE,[t, 355, 1346/3, 355],10,15)
    pygame.display.flip()
    # Rectangle Droite
    pygame.draw.rect(screen,WHITE,[t, 355, 1346/3, 355],2,10)
    pygame.display.flip()

mainrects(10) ; mainrects(455) ; mainrects(900)
