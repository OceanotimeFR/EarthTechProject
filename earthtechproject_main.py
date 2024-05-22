import pygame, time, sys, threading, random, test2
from pygame.locals import * ; from earthtechproject_colors import * ; from roymain import *

pygame.init()

width, height = 1366, 720

def printspeed(word, speed = 50, sound = "", volume = 1):
    word = str(word)
    string = ""
    for i in range(len(str(word))):
        string += word[i]
        print(f"\r{string}", end=" ")
        time.sleep(0.01)

class Ville:
    def __init__(self, name, pib, population, AugmentationPIB = 0.03, Annee = 0):
        self.pib = pib
        self.name = name
        self.Annee = Annee
        self.tauxcarbon = 8
        self.population = population
        self.infrastructure = {"Peu Polluantes": 10, "Moyennement Polluantes": 20, "Très Polluantes": 5}
        self.emissioncarbone = self.population*self.tauxcarbon + self.infrastructure["Peu Polluantes"]*800 + self.infrastructure["Moyennement Polluantes"]*1200 + self.infrastructure["Très Polluantes"]*2000
        # Les - 20 de ans, 20 à 65 ans, + de 65ans
        self.tranchedages = ((self.population*(24/100)), (self.population*(55/100)), (self.population*(21/100)))
        self.txnatalite = (self.population/2) * (0.02 + 0.03 * self.Annee)
        self.AugPIB = AugmentationPIB

    def augmenterpib(self):
        self.pib += self.pib*self.AugPIB

    def augmenterpop(self):
        self.population += self.txnatalite

    def DeveloperTransport(self):
        Qualite = input(("Qualité?: Médiocre, Moyenne, Supérieur"))
        if Qualite == "Médiocre":
            facteurqualite = 15
        if Qualite == "Moyenne":
            facteurqualite = 30
        if Qualite == "Supérieur":
            facteurqualite = 50
        printspeed(f"Facteur de qualité: {facteurqualite}, Prix: {(facteurqualite*(self.tranchedages[1] + self.tranchedages[0]))} Millions")
        self.pib -= (facteurqualite*(self.tranchedages[1] + self.tranchedages[0]))*(10**(-3))
        self.tauxcarbon -= 0.5
        self.emissioncarbone = self.population*self.tauxcarbon + self.infrastructure["Peu Polluantes"]*800 + self.infrastructure["Moyennement Polluantes"]*1200 + self.infrastructure["Très Polluantes"]*2000
    def MiseAJourStats(self):
        self.augmenterpop()
        self.tranchedages = ((self.population * (24 / 100)), (self.population * (55 / 100)), (self.population * (21 / 100)))
        self.augmenterpib()
    def developperProduitLocaux(self):
        self.tauxcarbon -= 0.5
        self.pib -= self.pib*0.09
        printspeed("C'est bon!")


    def taketurn(self):
        try:
            action = int(input("Choissisez une action (1. Developper produits locaux, 2. Developpe transports)"))
        except:
            action = int(input("Mettez une valeur valide"))

        if action == 1:
            self.developperProduitLocaux()
        elif action == 2:
            self.DeveloperTransport()
        else:
            action = int(input("Valeur invalide"))

#? Taille fenêtre
screen = pygame.display.set_mode((width, height))

#? Police écriture
police2 = pygame.font.SysFont("Bahnschrift",50)
police = pygame.font.SysFont("Bahnschrift",25)

#? Def Images
fond = pygame.image.load("images\montagne.jpg").convert_alpha()
efrei = pygame.image.load("images\efrei2.png").convert_alpha()
gamelogo = pygame.image.load("images\greencity-transformed.png").convert_alpha()

#^ Fonctions Introduction Texte & Image
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

# MAJ Variables
def etpvar_maj(txt,val,nbtour,rectpos_y,txtpos_y,txtcol) :
    import pygame, time
    i = 0
    for i in range (nbtour) :
        draw_text(f"{txt} : {val}","",txtcol,73,txtpos_y)
        pygame.draw.rect(screen,BLACK,[63, rectpos_y, 195, 50],1,10)
        pygame.display.flip()
        pygame.draw.rect(screen,GREEN,[63, rectpos_y, 195, 50],0,10)
        pygame.display.flip()
    draw_text(f"{txt} : {val}","",txtcol,73,txtpos_y)
    pygame.draw.rect(screen,BLACK,[63, rectpos_y, 195, 50],1,10)
    pygame.display.flip()



#* Paramètres fenêtre jeu (Nom & Logo)
pygame.display.set_caption("GreenCity")
pygame.display.set_icon(gamelogo)


#* Définir la taille de la fenêtre
efrei = pygame.image.load("images\efrei2.png").convert_alpha()


#? Loading Logo EFREI
for i in range (101) :
    efrei.set_alpha(i)
    screen.blit(efrei,(500,300))
    time.sleep(0.05)
    pygame.display.flip()
    if i==100 : break
    pygame.display.flip()
time.sleep(1)

#? Reset Ecran
pygame.draw.rect(screen,WHITE,[0, 0, width, height],0)
pygame.display.flip()


#* Loading Logo GreenCity
for i in range (101) :
    gamelogo.set_alpha(i)
    screen.blit(gamelogo,(500,150))
    time.sleep(0.025)
    pygame.display.flip()
    if i==100 : break
    pygame.display.flip()
time.sleep(1)


#* Bordure de la barre de chargement
pygame.draw.rect(screen,BLACK,[width/2-250, 500, 500, 35],1)
pygame.display.flip()


#* Barre de chargement
progress = 0
for i in range (500) :
    progress+=1
    time.sleep(0.0025)
    pygame.draw.rect(screen,GREEN,[width/2-250, 500, progress, 35],0)
    pygame.display.flip()
time.sleep(3)


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



#! Main Game
running = True
while running :   
    draw_text("MENU",police,TEXT_COL,550,300)
    draw_image(fond,0,0)
    pygame.display.flip()

    # Détection évènements (appuyer touche, cliquer, bouger souris...)
    for event in pygame.event.get():

        # Quand appuyer sur croix rouge, quitter le jeu

        if event.type == pygame.KEYDOWN :
            pib = random.randint(1, 38)
            pop = random.randint(5, 100)

        while run:
            screen.fill('light blue')
            timer.tick(120)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and main_gameevent:
                    if event.key == pygame.K_RETURN:
                        ClickedChatbox = False
                        if NameGiven == False:
                            Name = locationAnswer
                            NameGiven = True
                            Question1 = True
                        locationAnswer = " "
                    elif event.key == pygame.K_BACKSPACE:
                        locationAnswer = locationAnswer[0: (len(input)-1)]
                    elif event.key == pygame.K_e and not ClickedChatbox:
                        population += 1
                    elif event.key == pygame.K_a and not ClickedChatbox:
                        Money += 1
                    elif ClickedChatbox:
                        locationAnswer += event.unicode
            if NameGiven == False:
                location = "Nommez votre ville"
            if Question1:
                askquestionbinary("Augmenter la population?", increasepop, decreasepop)
            elif Question2:
                askquestionbinary("Augmentez les revenus?", increasepop, decreasepop)
            if menu_event:
                menu()
            if main_gameevent:
                maingame()
            
            pygame.display.flip()
                
        if event.type == pygame.QUIT:
            running = False
            sys.exit()