import pygame, threading, time, random, sys, functions
from colors import * ; from testing.roymain import * ; from villeclass import *


functions.etpgame_ui(12,"images\clock.png",74,75,0,2)
functions.etpgame_ui(62,"images\coin.png",70,70,2,53)
functions.etpgame_ui(112,"images\city.png",50,50,12,112)

pygame.display.flip()

class RunGame(object):
    def __init__(self) :
        # Initialiser Pygame
        pygame.init()

        # Définir la taille de la fenêtre
        width, height = 1366, 720
        self.screen = pygame.display.set_mode((width, height))
        self.police = pygame.font.SysFont("Bahnschrift",25)

        # Ombre
        pygame.draw.rect(screen,BISTRE,[7, 15, 250, 154],0,10)
        pygame.display.flip()
        # Fond
        pygame.draw.rect(screen,WOOD,[10, 10, 250, 154],0,10)
        pygame.display.flip()

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    pass

if __name__ == "__main__":

    Annee = 2024
    pib = random.randint(1, 38)
    pop = random.randint(5, 100)
    Ville("City",pib ,pop)
    turn_check = 0

    thread4 = threading.Thread(target=dialog,args=(f"Dialogue: {str(location)}", (475, 375)))
    thread5 = threading.Thread(target=dialog,args=(f"Réponse: {str(locationAnswer)}", (475, 415)))
    thread6 = threading.Thread(target=dialog,args=(f"Ville: {str(Name)}", (25, 375)))

    thread4.start() ; thread5.start() ; thread6.start()
    thread4.join() ; thread5.join() ; thread6.join

    for i in range(2):

        thread1 = threading.Thread(target=functions.etpvar_maj,args=("Année",Annee,2,12,24,BLACK))
        thread2 = threading.Thread(target=functions.etpvar_maj,args=("Argent",round(Ville.pib,2),2,62,74,BLACK))
        thread3 = threading.Thread(target=functions.etpvar_maj,args=("Pop.",round(Ville.population,2),2,112,124,BLACK))

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

                thread1.start() ; thread2.start() ; thread3.start()
                time.sleep(turn_check)
                thread1.join() ; thread2.join() ; thread3.join()

                Ville.MiseAJourStats()

                Annee += 1