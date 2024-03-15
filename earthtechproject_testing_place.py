import pygame, threading, time, random
from earthtechproject_colors import *


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


# Fonctions Introduction Texte & Image
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


# Initialiser Pygame
pygame.init()

# Définir la taille de la fenêtre
width, height = 1366, 720
screen = pygame.display.set_mode((width, height))
police = pygame.font.SysFont("Bahnschrift",25)


# Ombre
pygame.draw.rect(screen,DARK_GREEN,[7, 15, 250, 154],0,10)
pygame.display.flip()
# Fond
pygame.draw.rect(screen,GREEN,[10, 10, 250, 154],0,10)
pygame.display.flip()


# Ombre
pygame.draw.rect(screen,DARK_GREEN,[7, 180, 250, 500],0,10)
pygame.display.flip()
# Fond
pygame.draw.rect(screen,GREEN,[10, 175, 250, 500],0,10)
pygame.display.flip()


etpgame_ui(12,"images\clock.png",74,75,0,2)
etpgame_ui(62,"images\coin.png",70,70,2,53)
etpgame_ui(112,"images\city.png",50,50,12,112)

pygame.display.flip()

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
        
            pib = random.randint(1, 38)
            pop = random.randint(5, 100)

            Annee = 2024
            Ville1 = Ville("City",pib ,pop)
            if __name__ == "__main__":
                for i in range(100):

                    thread1 = threading.Thread(target=etpvar_maj,args=("Année",Annee,2,12,24,BLACK))
                    thread2 = threading.Thread(target=etpvar_maj,args=("Argent",round(Ville1.pib,2),2,62,74,BLACK))
                    thread3 = threading.Thread(target=etpvar_maj,args=("Pop.",round(Ville1.population,2),2,112,124,BLACK))

                    thread1.start() ; thread2.start() ; thread3.start()
                    time.sleep(1)
                    thread1.join() ; thread2.join() ; thread3.join()




                    Ville1.MiseAJourStats()

                    Annee += 1