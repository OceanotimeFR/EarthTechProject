import pygame, time
from functions import *

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