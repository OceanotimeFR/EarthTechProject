import pygame, time
from pygame.locals import * ; from earthtechproject_colors import *

pygame.init()

width, height = 1366, 720


# Taille fenêtre
screen = pygame.display.set_mode((width, height))

# Police écriture
police = pygame.font.SysFont("Bahnschrift",50)

# Def Images
fond = pygame.image.load("images\montagne.jpg").convert_alpha()
efrei = pygame.image.load("images\efrei2.png").convert_alpha()
gamelogo = pygame.image.load("images\greencity-transformed.png").convert_alpha()

# Fonctions Introduction Texte & Image
def draw_image(image,x,y):
    screen.blit(image,(x,y))

def draw_text(text,font,text_col,x,y):
    txt = police.render(text,True,text_col)
    screen.blit(txt,(x,y))

# Paramètres fenêtre jeu (Nom & Logo)
pygame.display.set_caption("GreenCity")
pygame.display.set_icon(gamelogo)


# Définir la taille de la fenêtre
efrei = pygame.image.load("images\efrei2.png").convert_alpha()


# Loading Logo EFREI
for i in range (101) :
    efrei.set_alpha(i)
    screen.blit(efrei,(500,300))
    time.sleep(0.025)
    pygame.display.flip()
    if i==100 : break
    pygame.display.flip()
time.sleep(1)


# Reset Ecran
pygame.draw.rect(screen,WHITE,[0, 0, width, height],0)
pygame.display.flip()


# Loading Logo GreenCity
for i in range (101) :
    gamelogo.set_alpha(i)
    screen.blit(gamelogo,(500,150))
    time.sleep(0.025)
    pygame.display.flip()
    if i==100 : break
    pygame.display.flip()
time.sleep(1)


# Bordure de la barre de chargement
pygame.draw.rect(screen,BLACK,[width/2-250, 500, 500, 35],1)
pygame.display.flip()


# Barre de chargement
progress = 0
for i in range (500) :
    progress+=1
    time.sleep(0.0025)
    pygame.draw.rect(screen,GREEN,[width/2-250, 500, progress, 35],0)
    pygame.display.flip()
time.sleep(3)


# Main Game
running = True
while running :   
    draw_text("MENU",police,TEXT_COL,550,300)
    draw_image(fond,0,0)
    pygame.display.flip()

    # Détection évènements (appuyer touche, cliquer, bouger souris...)
    for event in pygame.event.get():

        # Quand appuyer sur croix rouge, quitter le jeu
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.K_SPACE :
            pass