import random
import pygame
import time


def printspeed(word, speed = 0, sound = 0, volume = 1):
    word = str(word)
    string = ""
    for i in range(len(str(word))):
        string += word[i]
        print(f"\r{string}", end=" ")
        time.sleep(0.01)

class Ville:
    def __init__(self, name, pib, population, AugmentationPIB = 0.001, Annee = 0):
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
        Qualite = int(input(("Qualité?: 1. Médiocre, 2. Moyenne, 3. Supérieur: ")))
        if Qualite == 1:
            facteurqualite = 15
        if Qualite == 2:
            facteurqualite = 30
        if Qualite == 3:
            facteurqualite = 50
        play_sound(r"C:\Users\royta\OneDrive\Bureau\Code\TMARK_Jingle sncf 2 (ID 0564)_LS.mp3")
        printspeed(f"Facteur de qualité: {facteurqualite}, Prix: {(facteurqualite*(self.tranchedages[1] + self.tranchedages[0]))} Millions")
        self.pib -= (facteurqualite*(self.tranchedages[1] + self.tranchedages[0]))*(10**(-1))
        self.tauxcarbon -= (0.5 + facteurqualite*(1/9)) 
        self.emissioncarbone = self.population*self.tauxcarbon + self.infrastructure["Peu Polluantes"]*800 + self.infrastructure["Moyennement Polluantes"]*1200 + self.infrastructure["Très Polluantes"]*2000
    def MiseAJourStats(self):
        self.augmenterpop()
        self.tranchedages = ((self.population * (24 / 100)), (self.population * (55 / 100)), (self.population * (21 / 100)))
        self.augmenterpib()
    def developperProduitLocaux(self):
        try:
            Choix = int(input("0. Beaucoup 1. Moyennement 2. Peu ?: "))
        except:
            Choix = int(input("Réponse valide svp 0. Beaucoup 1. Moyennement 2. Peu ?: ")) + 1
        TupleEfficacité = (80, 50, 30)
        if random.randint(0, 100) < TupleEfficacité[Choix]:
            a = (0.5 + (1/100*TupleEfficacité[Choix]))
            self.tauxcarbon -= a
            printspeed(f"La politique a eu des effets! la tx carbon /an moyen a baisser de {a} tonne")
        else:
            printspeed("La population n'a pas trop apprécié, rien n'a changé")
        TuplePrix = (20, 10, 5)
        self.pib -= TuplePrix[Choix]
        self.emissioncarbone = self.population*self.tauxcarbon + self.infrastructure["Peu Polluantes"]*800 + self.infrastructure["Moyennement Polluantes"]*1200 + self.infrastructure["Très Polluantes"]*2000


    def taketurn(self):
        for i in range(3):
            print(f"Choisissez votre action numéro {i+1}:")
            try:
                action = int(input("Choisissez une action (1. Developper produits locaux, 2. Developper transports): "))
            except:
                action = int(input("Mettez une valeur valide: "))

            if action == 1:
                self.developperProduitLocaux()
            elif action == 2:
                self.DeveloperTransport()
            else:
                action = int(input("Valeur invalide: "))

    def Stats(self):
        return  f"Population: {self.population} Millions", f"PIB:{self.pib} Md", f"Tx Carbone: {self.emissioncarbone} Mt", f"Gain PIB: +{self.AugPIB}%"

Annee = 2024
Ville1 = Ville("Bezons", random.randint(5, 100), random.randint(1, 38))
if __name__ == "__main__":
    printspeed(f"Voici votre ville: {Ville1.Stats()}")
    for i in range(2):
        Ville1.taketurn()
        Ville1.MiseAJourStats()
        Annee += 1
        print((Annee), ":")
        printspeed(Ville1.Stats())
