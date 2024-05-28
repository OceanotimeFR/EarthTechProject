import pygame, threading, time, random, sys, functions
from colors import * ; from testing.roymain import * ; from villeclass import * ; import json


# Initialisation
width, height = 1366, 720
pygame.font.init()
police = "textfonts/CARBON-DROID.ttf"

random_text = ["A vous de redresser la barre !",
               "Prenez soin de vos citoyens !",
               "Astuce : Ne faites pas 'Alt+F4'",
               "Il était une fois une ville verte...",
               "Ecologie ? Ca veut dire quoi ?",
               "Carbone + Dioxygène = CO2"]

class RunGame(object):
    def __init__(self) :
        # Initialiser Pygame
        pygame.init()

        # Définir la taille de la fenêtre
        width, height = 1366, 720
        self.screen = pygame.display.set_mode((width, height))
        self.menuimage = pygame.transform.scale(pygame.image.load("images/titlefont2.png"),(width, height))

        self.whitescreen = pygame.transform.scale(pygame.image.load("images/coloredfonts/whites.png"),(width, height))
        self.blackscreen = pygame.transform.scale(pygame.image.load("images/coloredfonts/blacks.png"),(width, height))

        # Initialisation Images
        self.image_intro1 = pygame.image.load("images/efrei2.png").convert_alpha() # (331, 123)
        self.alpha = 0
        self.image_intro1.set_alpha(self.alpha)

        self.image_intro2 = pygame.image.load("images/greencity-transformed.png").convert_alpha() # (375, 375)
        self.alpha = 0
        self.image_intro2.set_alpha(self.alpha)

        self.loading1 = pygame.transform.scale(pygame.image.load("images/titlefont.png"),(width, height)).convert_alpha()
        self.alpha = 0
        self.loading1.set_alpha(self.alpha)

        # Initialisation Icones
        self.admin_icon = pygame.image.load("images/icones/administration.png")
        self.admin_icon_tr = pygame.transform.scale(self.admin_icon,(50,40))

        self.money_icon = pygame.image.load("images/icones/money.png")
        self.money_icon_tr = pygame.transform.scale(self.money_icon,(50,45))

        self.pollution_icon = pygame.image.load("images/icones/pollution.png")
        self.pollution_icon_tr = pygame.transform.scale(self.pollution_icon,(50,50))

        self.population_icon = pygame.image.load("images/icones/population.png")
        self.population_icon_tr = pygame.transform.scale(self.population_icon,(50,40))

        self.time_icon = pygame.image.load("images/icones/time.png")
        self.time_icon_tr = pygame.transform.scale(self.time_icon,(70,53))

        self.upgrade_icon = pygame.image.load("images/icones/upgrade.png")
        self.upgrade_icon_tr = pygame.transform.scale(self.upgrade_icon,(50,40))

        # Menu Buttons
        self.Menu_NewGame = pygame.Rect((width // 2 - 100, height // 2 - 50), (200, 25))
        self.ResumeGame = pygame.Rect((width // 2 - 100, height // 2),(200,25))
        self.Menu_LeaveGame = pygame.Rect((width // 2 - 100, height // 2 + 50), (200, 25))
        self.RetourMenu = pygame.Rect((width-100,15),(200,25))
        self.saveButton = pygame.Rect((15,15),(200,25))

    def fondu(self, image, x, y, temps):
        for i in range(101):
            image.set_alpha(i)
            self.screen.blit(image, (x, y))
            time.sleep(0.05)
            pygame.display.flip()
            if i == 100:
                break
            pygame.display.flip()
        time.sleep(temps)

    def gamesave(self,cityname,money,pop,tauxpollution) :
        # Passage en .JSON file
        data = {
            "City":cityname,
            "Argent":money,
            "Population":pop,
            "TauxPollution":tauxpollution
        }
        with open('userdata.json', 'w') as outfile:
            json.dump(data, outfile,indent=2)

    def loading_bar(self,color,x,y):
        #* Bordure de la barre de chargement
        pygame.draw.rect(self.screen,BLACK,[x, y, 500, 35],1)
        pygame.display.flip()

        #* Barre de chargement
        progress = 0
        for i in range (500) :
            progress+=1
            time.sleep(0.0025)
            pygame.draw.rect(self.screen,color,[x, y, progress, 35],0)
            pygame.display.flip()
            i+=1
        time.sleep(3)

    def draw_button(self, screen, color, rect, text, police_size):
        pygame.draw.rect(screen, color, rect)
        text_surf = pygame.font.Font(police,police_size).render(text, True, WHITE)
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect)

    def drawtext(self,screen,text,police_size,color,heightpos):
        texte = pygame.font.Font(police,police_size).render(text,True, color)
        xpos = width/2-1/2*texte.get_size()[0]
        ypos = height/2+heightpos
        screen.blit(texte, (xpos,ypos))

    def is_button_clicked(self, event, rect):
        souris_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic Gauche
                if rect.collidepoint(souris_pos):
                    return True
        return False

    def menu(self) :

        self.Menu_NewGame = pygame.Rect((width // 2 - 100, height // 2 - 50), (200, 25))
        self.ResumeGame = pygame.Rect((width // 2 - 100, height // 2),(200,25))
        self.Menu_LeaveGame = pygame.Rect((width // 2 - 100, height // 2 + 50), (200, 25))
        self.RetourMenu = pygame.Rect((width-100,15),(0,0))
        self.saveButton = pygame.Rect((15,15),(0,0))

        # Textes :
        screen.blit(self.menuimage, (0,0))
        self.drawtext(screen,"GREENCITY",100,BLACK,-197) ; self.drawtext(screen,"GREENCITY",100,GREEN,-200)
        subtitleBG = pygame.font.Font(police,30).render("For a new home",True, BLACK) ; screen.blit(subtitleBG, (width/2+70,253))
        subtitle = pygame.font.Font(police,30).render("For a new home",True, LIGHT_BLUE) ; screen.blit(subtitle, (width/2+70,250))
        self.drawtext(screen,"Nouvelle Partie",25,BLACK,-47) ; self.drawtext(screen,"Nouvelle Partie",25,WHITE,-50)
        self.drawtext(screen,"Reprendre Partie",25,BLACK,3) ; self.drawtext(screen,"Reprendre Partie",25,WHITE,0)
        self.drawtext(screen,"Quitter",25,BLACK,53) ; self.drawtext(screen,"Quitter",25,WHITE,50)
        versiontext = pygame.font.Font(police,15).render("Early Access - Build Version 0.1.1a",True, WHITE) ; screen.blit(versiontext, (width-versiontext.get_size()[0]-3,height-versiontext.get_size()[1]-2))
        mouse_pos = pygame.mouse.get_pos()
        if self.Menu_NewGame.collidepoint(mouse_pos):
            self.drawtext(screen,"Nouvelle Partie",25,YELLOW,-50)
        elif self.ResumeGame.collidepoint(mouse_pos):
            self.drawtext(screen,"Reprendre Partie",25,YELLOW,0)
        elif self.Menu_LeaveGame.collidepoint(mouse_pos):
            self.drawtext(screen,"Quitter",25,YELLOW,50)
        pygame.display.flip()

    def loading_screen(self):
        self.fondu(self.loading1,0,0,0.05)
        for i in range(3) :
            pygame.draw.rect(self.screen, BLACK,[0,5/6*height,width,1/6*height]) ; pygame.display.flip()
            self.drawtext(screen,random_text[random.randint(0,len(random_text)-1)],25,WHITE,+5/12*height-15)
            pygame.display.flip()
            time.sleep(5)
        pygame.draw.rect(self.screen, BLACK,[0,5/6*height,width,1/6*height]) ; pygame.display.flip()
        self.drawtext(screen,"Prêt à jouer !",25,WHITE,+5/12*height-15)
        pygame.display.flip()
        time.sleep(3)

    def game_ui(self) :
            
            self.Menu_NewGame = pygame.Rect((width // 2 - 100, height // 2 - 50), (0, 0))
            self.ResumeGame = pygame.Rect((width // 2 - 100, height // 2),(0,0))
            self.Menu_LeaveGame = pygame.Rect((width // 2 - 100, height // 2 + 50), (0, 0))
            self.RetourMenu = pygame.Rect((width-100,15),(200,25))
            self.saveButton = pygame.Rect((15,15),(200,25))

            # UI
            pos_y = height-height/2+40 ; epaisseur = width/3 ; hauteur = height/2-50
            pygame.draw.rect(self.screen, GREY, [0, pos_y-10, 3*epaisseur, height], 0,10)
            pygame.draw.rect(self.screen, BLACK, [5, pos_y, epaisseur, hauteur],5)
            pygame.draw.rect(self.screen, BLACK, [width/3, pos_y, epaisseur, hauteur],5)
            pygame.draw.rect(self.screen, BLACK, [2*width/3-5, pos_y, epaisseur, hauteur],5)

            stats_text = pygame.font.Font(police,30).render("Statistiques",True, BLACK) ; screen.blit(stats_text, (epaisseur/2-1/2*stats_text.get_size()[0],pos_y+10))
            pygame.draw.rect(self.screen,BLACK,[30,pos_y+55,55,55],0,100)
            pygame.draw.rect(self.screen,WHITE,[30,pos_y+55,55,55],1,100)
            screen.blit(self.time_icon_tr,(22,pos_y+55))
            year_txt = pygame.font.Font(police,30).render("Année : ",True, BLACK) ; screen.blit(year_txt, (100,pos_y+68))
            
            pygame.draw.rect(self.screen,BLACK,[30,pos_y+115,55,55],0,100)
            pygame.draw.rect(self.screen,WHITE,[30,pos_y+115,55,55],1,100)
            screen.blit(self.money_icon_tr,(32,pos_y+120))
            money_txt = pygame.font.Font(police,30).render("Argent : ",True, BLACK) ; screen.blit(money_txt, (100,pos_y+130))
            
            pygame.draw.rect(self.screen,BLACK,[30,pos_y+175,55,55],0,100)
            pygame.draw.rect(self.screen,WHITE,[30,pos_y+175,55,55],1,100)
            screen.blit(self.population_icon_tr,(32,pos_y+182))
            pop_txt = pygame.font.Font(police,30).render("Population : ",True, BLACK) ; screen.blit(pop_txt, (100,pos_y+190))
            
            pygame.draw.rect(self.screen,BLACK,[30,pos_y+235,55,55],0,100)
            pygame.draw.rect(self.screen,WHITE,[30,pos_y+235,55,55],1,100)
            screen.blit(self.pollution_icon_tr,(32,pos_y+237))
            co2_txt = pygame.font.Font(police,30).render("Pollution : ",True, BLACK) ; screen.blit(co2_txt, (100,pos_y+250))
            
            dialog_text = pygame.font.Font(police,30).render("Dialogue",True, BLACK) ; screen.blit(dialog_text, (3*epaisseur/2-1/2*dialog_text.get_size()[0],pos_y+10))

            actions_text = pygame.font.Font(police,30).render("Actions",True, BLACK) ; screen.blit(actions_text, (5*epaisseur/2-1/2*actions_text.get_size()[0],pos_y+10))

            # Bouton Retour Menu
            backmenu_txt = pygame.font.Font(police,25).render("MENU",True, WHITE) ; screen.blit(backmenu_txt, (width-100,15))
            save_txt = pygame.font.Font(police,25).render("Sauvegarder",True, WHITE) ; screen.blit(save_txt, (15,15))
            pygame.display.flip()
            
    def run_game(self):
        intro = False
        menu = True
        while True:
            if intro : 
                x1 = width/2-(331/2) ; y1 = height/2 - (123/2)
                x2 = width/2-(375/2) ; y2 = height/2 - (375/2+50)
                x3 = width/2-250 ; y3 = height/2 + 100
                # Affichage Logo EFREI
                self.fondu(self.image_intro1,x1,y1,1)
                pygame.draw.rect(self.screen, WHITE,[0,0,width,height], 0)
                pygame.display.flip()
                time.sleep(1)
                # Affichage Logo Jeu
                self.fondu(self.image_intro2,x2,y2,1)
                self.loading_bar(GREEN,x3,y3)
                pygame.display.flip()
                intro = False
                menu = True

            for event in pygame.event.get():
                if menu : 
                    RunGame.menu(self)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif self.is_button_clicked(event, self.Menu_NewGame): 
                    menu = False
                    #RunGame.loading_screen(self) ; time.sleep(1)
                    pygame.draw.rect(self.screen, BLACK, [0, 0, width, height], 0) ; pygame.display.flip()
                    RunGame.game_ui(self)

                elif self.is_button_clicked(event, self.saveButton) :
                    self.gamesave("Test",15,15,0.18)

                elif self.is_button_clicked(event, self.ResumeGame) :
                    menu = False
                    #RunGame.loading_screen(self) ; time.sleep(1)
                    pygame.draw.rect(self.screen, BLACK, [0, 0, width, height], 0) ; pygame.display.flip()
                    RunGame.game_ui(self)

                elif self.is_button_clicked(event, self.Menu_LeaveGame) : 
                    pygame.draw.rect(self.screen, BLACK, [0, 0, width, height], 0) ; pygame.display.flip()
                    menu = False
                    pygame.quit()
                    sys.exit()

                elif self.is_button_clicked(event, self.RetourMenu) : 
                    pygame.draw.rect(self.screen, BLACK, [0, 0, width, height], 0) ; pygame.display.flip()
                    #^ self.savegame() !!!!
                    menu = True
"""
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
        thread2 = threading.Thread(target=functions.etpvar_maj,args=(f"round(Ville.pib,2)M €",2,62,74,BLACK))
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
"""

if __name__ == "__main__":
    game = RunGame()
    game.run_game()