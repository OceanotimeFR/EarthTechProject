import pygame, threading, time, random, sys, functions
from colors import * ; from testing.roymain import * ; from villeclass import * ; import json
pygame.mixer.init()

# Initialisation
width, height = 1366, 720
pygame.font.init()
police = "textfonts/CARBON-DROID.ttf"

nomville = "Your City"

random_text = ["Carbone + Dioxygène = CO2",
               "Le saviez-vous ? Greencity a été créé par 5 personnes !",
               "Astuce : Ne faites pas 'Alt+F4'",
               "Il était une fois une ville verte...",
               "Ecologie ? Ca veut dire quoi ?",
               "C'est une Early Access !"]

badluck_txt = ["L'isolation a mal été réalisée. Vous devez payer.",
               "Des intempéries ont abîmé le batîment, et vous devez le réparer.",
               "Vous avez été surpris en pleine fraude fiscale !"]

luck_txt = ["L'infrastructure s'est montrée fructueuse pour la ville !",
            "Le bâtiment a bien été isolé."]

random_event = ["Visite d'une autorité locale'", "Visite du Ministre de l'Ecologie","Manifestation contre l'environnement",""]

class RunGame(object):
    def __init__(self) :
        # Initialiser Pygame
        pygame.init()

        # Définir la taille de la fenêtre
        width, height = 1366, 720
        self.screen = pygame.display.set_mode((width, height))
        self.menuimage = pygame.transform.scale(pygame.image.load("images/titlefont2.png"),(width, height))
        self.tour = 0
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

        # UI Fonts Cityscapes
        self.font1 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font1.png"),(width, height/2+40))
        self.font2 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font2.png"),(width, height/2+40))
        self.font3 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font3.png"),(width, height/2+40))
        self.font4 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font4.png"),(width, height/2+40))
        self.font5 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font5.png"),(width, height/2+40))
        self.font6 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font6.png"),(width, height/2+40))

        # Initialisation Icones

        self.admin_icon_tr = self.imageloadnsize("images/icones/icones_stats/administration.png",(50,40))
        self.money_icon_tr = self.imageloadnsize("images/icones/icones_stats/money.png",(50,45))
        self.pollution_icon_tr = self.imageloadnsize("images/icones/icones_stats/pollution.png",(50,50))
        self.population_icon_tr = self.imageloadnsize("images/icones/icones_stats/population.png",(50,40))
        self.time_icon_tr = self.imageloadnsize("images/icones/icones_stats/time.png",(70,53))
        self.upgrade_icon_tr = self.imageloadnsize("images/icones/icones_stats/upgrade.png",(50,40))

        # Menu Buttons
        self.Menu_NewGame = pygame.Rect((width // 2 - 100, height // 2 - 50), (200, 25))
        self.ResumeGame = pygame.Rect((width // 2 - 100, height // 2),(200,25))
        self.Menu_LeaveGame = pygame.Rect((width // 2 - 100, height // 2 + 50), (200, 25))
        self.RetourMenu = pygame.Rect((width-100,15),(200,25))
        self.saveButton = pygame.Rect((15,15),(200,25))

    def imageloadnsize(self, image, size):
        img = pygame.image.load(image)
        img = pygame.transform.scale(img,size)
        return img
    
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

    def gamesave(self,cityname,year,money,pop,tauxpollution) :
        # Passage en .JSON file
        data = {
            "City":cityname,
            "Annee":year,
            "Argent":money,
            "Population":pop,
            "TauxPollution":tauxpollution
        }
        with open('userdata.json', 'w') as outfile:
            json.dump(data, outfile,indent=2)

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
        versiontext = pygame.font.Font(police,15).render("Early Access - Build Version 0.1.2",True, WHITE) ; screen.blit(versiontext, (width-versiontext.get_size()[0]-3,height-versiontext.get_size()[1]-2))
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
        pygame.draw.rect(self.screen, BLACK,[0,0,width,1/8*height]) ; pygame.display.flip()
        self.drawtext(screen,"Chargement, merci de patienter...",25,WHITE,-320)
        for i in range(3) :
            pygame.draw.rect(self.screen, BLACK,[0,5/6*height,width,1/6*height]) ; pygame.display.flip()
            self.drawtext(screen,random_text[random.randint(0,len(random_text)-1)],25,WHITE,+5/12*height-15)
            pygame.display.flip()
            time.sleep(5)
        pygame.draw.rect(self.screen, BLACK,[0,5/6*height,width,1/6*height]) ; pygame.display.flip()
        pygame.draw.rect(self.screen, BLACK,[0,0,width,1/8*height]) ; pygame.display.flip()
        self.drawtext(screen,"Prêt à jouer !",25,WHITE,+5/12*height-15)
        pygame.display.flip()
        time.sleep(3)


    def game_ui(self, cityname, year, money, popu, pollu) :

            global nom_th2, annee_th2, argent_th2, population_th2, tco2_th2

            self.Menu_NewGame = pygame.Rect((width // 2 - 100, height // 2 - 50), (0, 0))
            self.ResumeGame = pygame.Rect((width // 2 - 100, height // 2),(0,0))
            self.Menu_LeaveGame = pygame.Rect((width // 2 - 100, height // 2 + 50), (0, 0))
            self.RetourMenu = pygame.Rect((width-100,15),(200,25))
            self.saveButton = pygame.Rect((15,15),(200,25))

            #Cityscape Font
            self.cityscape(popu)
            # Bande Top Screen
            pygame.draw.rect(self.screen,GREY,[0,0,width,60])
            pygame.draw.rect(self.screen,GREY,[width/3,40,width/3,60],0,0,0,0,5,5)
            pygame.draw.rect(self.screen,BLACK,[width/3+10,62,width/3-20,30],0,5)

            # Bouton Retour Menu
            backmenu_txtBG = pygame.font.Font(police,25).render("MENU",True, BLACK) ; screen.blit(backmenu_txtBG, (width-100,18))
            backmenu_txt = pygame.font.Font(police,25).render("MENU",True, WHITE) ; screen.blit(backmenu_txt, (width-100,15))
            save_txtBG = pygame.font.Font(police,25).render("Sauvegarder",True, BLACK) ; screen.blit(save_txtBG, (15,18))
            save_txt = pygame.font.Font(police,25).render("Sauvegarder",True, WHITE) ; screen.blit(save_txt, (15,15))

            # UI
            pos_y = height-height/2+40 ; epaisseur = width/3 ; hauteur = height/2-50
            pygame.draw.rect(self.screen, GREY, [0, pos_y-10, 3*epaisseur, height], 0,10)
            pygame.draw.rect(self.screen, BLACK, [5, pos_y, epaisseur, hauteur],5)
            pygame.draw.rect(self.screen, BLACK, [width/3, pos_y, epaisseur, hauteur],5)
            pygame.draw.rect(self.screen, BLACK, [2*width/3-5, pos_y, epaisseur, hauteur],5)

            # STATISTIQUES & VARIABLES

            stats_text = pygame.font.Font(police,30).render("Statistiques",True, BLACK) ; screen.blit(stats_text, (epaisseur/2-1/2*stats_text.get_size()[0],pos_y+10))

            self.drawtext(screen,cityname,30,BLACK,-340)
            self.drawtext(screen,cityname,30,GREEN,-343)
            nom_th2 = cityname

            pygame.draw.rect(self.screen,BLACK,[30,pos_y+55,55,55],0,100)
            pygame.draw.rect(self.screen,WHITE,[30,pos_y+55,55,55],1,100)
            screen.blit(self.time_icon_tr,(22,pos_y+55))
            year_txt = pygame.font.Font(police,30).render("Année : ",True, BLACK) ; screen.blit(year_txt, (100,pos_y+68))
            
            pygame.draw.rect(self.screen,GREY,[100+year_txt.get_size()[0]+10,height-height/2+110,100,25])
            thread_year = threading.Thread(target=self.display,args=(f"{year}", BLACK,(100+year_txt.get_size()[0]+10,height-height/2+110))) ; thread_year.start() ; thread_year.join()
            annee_th2 = year

            pygame.draw.rect(self.screen,BLACK,[30,pos_y+115,55,55],0,100)
            pygame.draw.rect(self.screen,WHITE,[30,pos_y+115,55,55],1,100)
            screen.blit(self.money_icon_tr,(32,pos_y+120))
            money_txt = pygame.font.Font(police,30).render("Argent : ",True, BLACK) ; screen.blit(money_txt, (100,pos_y+130))

            pygame.draw.rect(self.screen,GREY,[100+money_txt.get_size()[0]+10,pos_y+130,100,25])
            thread_money = threading.Thread(target=self.display,args=(f"{round(money,0)} C", BLACK,(100+money_txt.get_size()[0]+10,pos_y+130))) ; thread_money.start() ; thread_money.join()  
            argent_th2 = money

            pygame.draw.rect(self.screen,BLACK,[30,pos_y+175,55,55],0,100)
            pygame.draw.rect(self.screen,WHITE,[30,pos_y+175,55,55],1,100)
            screen.blit(self.population_icon_tr,(32,pos_y+182))
            pop_txt = pygame.font.Font(police,30).render("Population : ",True, BLACK) ; screen.blit(pop_txt, (100,pos_y+190))
            
            pygame.draw.rect(self.screen,GREY,[100+pop_txt.get_size()[0],pos_y+190,100,25])
            thread_pop = threading.Thread(target=self.display,args=(f"{round(popu,0)}", BLACK,(100+pop_txt.get_size()[0],pos_y+190))) ; thread_pop.start() ; thread_pop.join()
            population_th2 = popu

            pygame.draw.rect(self.screen,BLACK,[30,pos_y+235,55,55],0,100)
            pygame.draw.rect(self.screen,WHITE,[30,pos_y+235,55,55],1,100)
            screen.blit(self.pollution_icon_tr,(32,pos_y+237))
            co2_txt = pygame.font.Font(police,30).render("Pollution : ",True, BLACK) ; screen.blit(co2_txt, (100,pos_y+250))

            pygame.draw.rect(self.screen,GREY,[100+pop_txt.get_size()[0],pos_y+250,100,25])
            thread_pollution = threading.Thread(target=self.display,args=(f"{round(pollu,0)} T", BLACK,(100+pop_txt.get_size()[0],pos_y+250))) ; thread_pollution.start() ; thread_pollution.join()
            tco2_th2 = pollu

            dialog_text = pygame.font.Font(police,30).render("Dialogue",True, BLACK) ; screen.blit(dialog_text, (3*epaisseur/2-1/2*dialog_text.get_size()[0],pos_y+10))

            actions_text = pygame.font.Font(police,30).render("Actions",True, BLACK) ; screen.blit(actions_text, (5*epaisseur/2-1/2*actions_text.get_size()[0],pos_y+10))

            self.display("[J] Dev. Produits Locaux", BLACK,(5*epaisseur/2-1/2*actions_text.get_size()[0]-150,pos_y+71))
            self.display("[J] Dev. Produits Locaux", WHITE,(5*epaisseur/2-1/2*actions_text.get_size()[0]-150,pos_y+68))
            self.display("[K] Dev. Transports", BLACK,(5*epaisseur/2-1/2*actions_text.get_size()[0]-150,pos_y+68*2+3))
            self.display("[K] Dev. Transports", WHITE,(5*epaisseur/2-1/2*actions_text.get_size()[0]-150,pos_y+68*2))
            self.display("[L] Dev. Infrastructures", BLACK,(5*epaisseur/2-1/2*actions_text.get_size()[0]-150,pos_y+68*3+3))
            self.display("[L] Dev. Infrastructures", WHITE,(5*epaisseur/2-1/2*actions_text.get_size()[0]-150,pos_y+68*3))

            self.gamesave(cityname, year, money, popu, pollu)

    def display(self, txt,color, pos):
        text = pygame.font.Font(police,25).render(txt, True, color)
        self.screen.blit(text, pos)

    def cityscape(self, pop):
        if pop <= 1000 :
            self.display("Petite Ville",(255,0,0),(0,0))
            screen.blit(self.font1,(0, 0, width, height/2))
            pygame.display.flip()
        elif 1000 < pop <= 25000 :
            screen.blit(self.font2,(0, 0,width,height/2))
        elif 25000 < pop <= 250000 :
            screen.blit(self.font3,(0, 0,width,height/2))
        elif 250000 < pop <= 1000000 :
            screen.blit(self.font4,(0, 0,width,height/2))
        elif 1000000 < pop <= 5000000 :
            screen.blit(self.font5,(0, 0,width,height/2))
        elif 5000000 < pop : # 5M+ pop
            screen.blit(self.font6,(0, 0,width,height/2))
        pygame.display.flip()

# Display Text
    def display(self, txt, color, pos):
        text = pygame.font.Font(police,25).render(txt, True, color)
        self.screen.blit(text, pos)

# Musique Fond & Sons
    def play_sound(self, sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    def background_sound(self, path):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(path) 
        sound.set_volume(0.1) 
        sound.play(-1)

# Fonctions Jeu
    def developperProduitLocaux(self, pollution, argent):
        pollution *= 1.05
        argent *= 0.95
        return round(pollution,1), round(argent, 1)

    def developperTransports(self, pollution, population, argent):
        # Transports Combustion / Electrique
        pollution *= 1.05
        chance = random.randint(0,2)
        if chance == 0 : population *= 0.95
        elif chance == 1 : population *= 1.05
        elif chance == 2 : population *= 1.25
        argent *= 0.85
        return round(pollution,1), round(population,1), round(argent, 1)

    def developperInfrastructures(self, pollution, population, argent) :
        pollution *= 1.02
        chance = random.randint(0,2)
        if chance == 0 : population *= 0.95 ; argent *= 0.98 ; pollution *= 1.25 #^; self.display(random.randint(0,len(badluck_txt)),WHITE,)
        elif chance == 1 : population *= 1.05 ; argent *= 1.01 ; pollution *= 1.05
        elif chance == 2 : population *= 1.25 ; argent *= 1.05 ; pollution *= 0.95
        argent *= 0.9
        return round(pollution,1), round(population,1), round(argent, 1)

    def increasepop():
        global population
        population+= random.randint(0, 20)
        return(round(population,0))
    def decreasepop():
        global population
        population -= random.randint(0, 20)
        return(round(population,0))
    def increasemoney():
        global Money
        Money+= random.randint(0, 20)
        return(round(Money,1))
    def decreasemoney():
        global Money
        Money -= random.randint(0, 20)
        return(round(Money,1))

# Main Game
    def run_game(self):
        intro = True
        menu = True
        thread_music = threading.Thread(target=self.background_sound, args=("soundtrack/music/MainTheme.mp3",))
        play_song = False

        while True:
            if self.tour == 3:
                self.tour = 0
                annee+=1
                pollution += round(population*0.1, 1)
                pop += round(((1/2)*pop*0.8), 0)
                argent += round(argent*0.1, 1)
            if intro : 
                x1 = width/2-(331/2) ; y1 = height/2 - (123/2)
                # Affichage Logo EFREI
                self.fondu(self.image_intro1,x1,y1,1)
                pygame.draw.rect(self.screen, BLACK,[0,0,width,height], 0)
                pygame.display.flip()
                time.sleep(1)
                intro = False
                menu = True
                play_song = True
            
            if play_song :
                thread_music.start()
                play_song = False

            for event in pygame.event.get():
                if menu : 
                    RunGame.menu(self)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #elif self.is_button_clicked(event, self.button) :
                    return

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:
                        self.tour += 1
                        pollution, argent = self.developperProduitLocaux(pollution, argent)
                        RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                        pygame.display.flip()
                    elif event.key == pygame.K_k:
                        chance = random.randint(0,1)
                        pollution, pop, argent = self.developperTransports(pollution, pop, argent)
                        self.tour += 1
                        RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                        pygame.display.flip()
                    elif event.key == pygame.K_l:
                        pollution, pop, argent = self.developperInfrastructures(pollution, pop, argent)
                        self.tour += 1
                        RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                        pygame.display.flip()
                    elif event.key == pygame.K_b:
                        # Skip Year
                        self.tour += 1
                        RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                        pygame.display.flip()

                elif self.is_button_clicked(event, self.Menu_NewGame): 
                    menu = False
                    annee = 2024
                    argent = random.randint(1, 38)
                    pop = random.randint(5, 20)
                    pollution = random.randrange(50,85)
                    nomville = "GreenCity"

                    self.gamesave(nomville, annee, argent, pop, pollution)

                    RunGame.loading_screen(self) ; time.sleep(1)

                    pygame.draw.rect(self.screen, BLACK, [0, 0, width, height], 0)
                    RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                    pygame.display.flip()

                elif self.is_button_clicked(event, self.saveButton) :
                    self.gamesave(nom_th2,annee_th2,argent_th2,population_th2,tco2_th2)

                elif self.is_button_clicked(event, self.ResumeGame) :
                    menu = False
                    RunGame.loading_screen(self) ; time.sleep(1)
                    pygame.draw.rect(self.screen, BLACK, [0, 0, width, height], 0)
                    with open ("userdata.json","r") as f:
                        data = json.load(f)
                    RunGame.game_ui(self,data["City"],data["Annee"],data["Argent"],data["Population"],data["TauxPollution"])
                    pygame.display.flip()

                elif self.is_button_clicked(event, self.Menu_LeaveGame) : 
                    pygame.draw.rect(self.screen, BLACK, [0, 0, width, height], 0) ; pygame.display.flip()
                    menu = False
                    pygame.quit()
                    sys.exit()

                elif self.is_button_clicked(event, self.RetourMenu) : 
                    pygame.draw.rect(self.screen, BLACK, [0, 0, width, height], 0) ; pygame.display.flip()
                    self.gamesave(nom_th2,annee_th2,argent_th2,population_th2,tco2_th2)
                    menu = True


if __name__ == "__main__":
    game = RunGame()
    game.run_game()