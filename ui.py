import pygame, threading, time, random, sys, functions
from colors import * ; from testing.roymain import * ; from villeclass import * ; import json
pygame.mixer.init()

global nom_th2, annee_th2, argent_th2, population_th2, tco2_th2

# Initialisation
width, height = 1366, 720
pygame.font.init()
police = "textfonts/CARBON-DROID.ttf"
volume = 0.25

music = ["KD Main - The Boston Bounce","King Major - Cruise Control", "King Major - Play For Keeps","Montana Birds - Cologne","Montana Birds - New Day","Montana Birds - Sunny Days"]
mois = ["Jan.","Fev.","Mar.","Avr.","Mai.","Jun.","Jul.","Aou.","Sep.","Oct.","Nov.","Dec."]

nomville = "Your City"

random_text = ["Carbone + Dioxygène = CO2",
               "Greencity a été créé par 5 personnes !",
               "'La nature ne fait rien en vain.' - Aristote",
               "Il était une fois une ville verte...",
               "Ecologie ? Ca veut dire quoi ?",
               "'Nous n'héritons pas de la terre de nos ancêtres, nous l'empruntons à nos enfants.' - Antoine de Saint-Exupéry"]

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
        self.alpha = 0
        self.image_intro1 = pygame.image.load("images/efrei2.png").convert_alpha() # (331, 123)
        self.image_intro1.set_alpha(self.alpha)

        self.image_intro2 = pygame.image.load("images/greencity-transformed.png").convert_alpha() # (375, 375)
        self.image_intro2.set_alpha(self.alpha)

        self.loading1 = pygame.transform.scale(pygame.image.load("images/titlefont.png"),(width, height)).convert_alpha()
        self.loading1.set_alpha(self.alpha)

        self.badending = pygame.transform.scale(pygame.image.load("images/icones/pollutionair.png"),(width/2,height/2-50))
        self.goodending = pygame.transform.scale(pygame.image.load("images/titlefont2.png"),(width/2,height/2-50))
        self.bankrupt = pygame.transform.scale(pygame.image.load("images/bankrupt.png"),(width/2,height/2-50))

        # UI Fonts Cityscapes
        self.font1 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font1.png"),(width, height/2+40))
        self.font2 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font2.png"),(width, height/2+40))
        self.font3 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font3.png"),(width, height/2+40))
        self.font4 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font4.png"),(width, height/2+40))
        self.font5 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font5.png"),(width, height/2+40))
        self.font6 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font6.png"),(width, height/2+40))
        self.font7 = pygame.transform.scale(pygame.image.load("images/ui_fonts/Font7.png"),(width, height/2+40))

        # Initialisation Icones
        self.admin_icon_tr = self.imageloadnsize("images/icones/icones_stats/administration.png",(50,40))
        self.money_icon_tr = self.imageloadnsize("images/icones/icones_stats/money.png",(50,45))
        self.pollution_icon_tr = self.imageloadnsize("images/icones/icones_stats/pollution.png",(50,50))
        self.population_icon_tr = self.imageloadnsize("images/icones/icones_stats/population.png",(50,40))
        self.time_icon_tr = self.imageloadnsize("images/icones/icones_stats/time.png",(70,53))
        self.upgrade_icon_tr = self.imageloadnsize("images/icones/icones_stats/upgrade.png",(50,40))
        self.iconPlaySound_tr = self.imageloadnsize("images/icones/menu_ui/SoundOn.png",(50,50))
        self.iconStopSound_tr = self.imageloadnsize("images/icones/menu_ui/SoundOff.png",(50,50))

        # Icones Actions
        self.hydro_icon_tr = self.imageloadnsize("images/icones/icones_choices/action_buttons/BarrageHydro.png",(72,72))
        self.coaloil_icon_tr = self.imageloadnsize("images/icones/icones_choices/action_buttons/CoalOil.png",(72,72))
        self.solar_icon_tr = self.imageloadnsize("images/icones/icones_choices/action_buttons/SolarPanel.png",(72,72))
        self.recycle_icon_tr = self.imageloadnsize("images/icones/icones_choices/action_buttons/Recycle.png",(72,72))
        self.sensibiliser_icon_tr = self.imageloadnsize("images/icones/icones_choices/action_buttons/Sensibiliser.png",(72,72))
        self.eol_icon_tr = self.imageloadnsize("images/icones/icones_choices/action_buttons/Eoliennes.png",(72,72))
        self.eleccar_icon_tr = self.imageloadnsize("images/icones/icones_choices/action_buttons/ElecCar.png",(72,72))

        # Menu Buttons
        self.Menu_NewGame = pygame.Rect((width // 2 - 100, height // 2 - 50), (200, 25))
        self.ResumeGame = pygame.Rect((width // 2 - 100, height // 2),(200,25))
        self.Menu_LeaveGame = pygame.Rect((width // 2 - 100, height // 2 + 50), (200, 25))
        self.RetourMenu = pygame.Rect((width-100,15),(200,25))
        self.saveButton = pygame.Rect((15,15),(200,25))

        # Boutons UI
        self.EolButn = pygame.Rect([0,0,0,0])
        self.SolButn = pygame.Rect([0,0,0,0])
        self.ElecCarButn = pygame.Rect([0,0,0,0])
        self.RecycleButn = pygame.Rect([0,0,0,0])
        self.HydroButn = pygame.Rect([0,0,0,0])
        self.CoalOilButn = pygame.Rect([0,0,0,0])
        self.AwareButn = pygame.Rect([0,0,0,0])

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
        self.screen.fill(BLACK)
        self.Menu_NewGame = pygame.Rect((width // 2 - 150, height // 2 - 50), (300, 25))
        self.ResumeGame = pygame.Rect((width // 2 - 150, height // 2),(300,25))
        self.Menu_LeaveGame = pygame.Rect((width // 2 - 100, height // 2 + 50), (200, 25))
        self.RetourMenu = pygame.Rect((width-100,15),(0,0))
        self.saveButton = pygame.Rect((15,15),(0,0))
        self.PlayMusic = pygame.Rect((width-125,height-80),(50,50))
        self.StopMusic = pygame.Rect((width-75,height-80),(50,50))

        # Textes :
        screen.blit(self.menuimage, (0,0))
        self.drawtext(screen,"GREENCITY",100,BLACK,-197) ; self.drawtext(screen,"GREENCITY",100,GREEN,-200)
        subtitleBG = pygame.font.Font(police,30).render("For a new home",True, BLACK) ; screen.blit(subtitleBG, (width/2+70,253))
        subtitle = pygame.font.Font(police,30).render("For a new home",True, LIGHT_BLUE) ; screen.blit(subtitle, (width/2+70,250))
        self.drawtext(screen,"Nouvelle Partie",25,BLACK,-47) ; self.drawtext(screen,"Nouvelle Partie",25,WHITE,-50)
        self.drawtext(screen,"Reprendre Partie",25,BLACK,3) ; self.drawtext(screen,"Reprendre Partie",25,WHITE,0)
        self.drawtext(screen,"Quitter",25,BLACK,53) ; self.drawtext(screen,"Quitter",25,WHITE,50)
        versiontext = pygame.font.Font(police,15).render("Accès Anticipé - Build Version 0.1.5",True, WHITE) ; screen.blit(versiontext, (width-versiontext.get_size()[0]-3,height-versiontext.get_size()[1]-2))
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
        self.drawtext(screen,"Chargement, merci de patienter...",20,WHITE,-320)
        for i in range(3) :
            pygame.draw.rect(self.screen, BLACK,[0,5/6*height,width,1/6*height]) ; pygame.display.flip()
            self.drawtext(screen,random_text[random.randint(0,len(random_text)-1)],20,WHITE,+5/12*height-15)
            pygame.display.flip()
            time.sleep(5)
        pygame.draw.rect(self.screen, BLACK,[0,5/6*height,width,1/6*height]) ; pygame.display.flip()
        pygame.draw.rect(self.screen, BLACK,[0,0,width,1/8*height]) ; pygame.display.flip()
        self.drawtext(screen,"Prêt à jouer !",20,WHITE,+5/12*height-15)
        pygame.display.flip()
        time.sleep(3)

#! Game UI
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
            pygame.draw.rect(self.screen,BLACK,[width/3,40,width/3,63],0,0,0,0,5,5)
            pygame.draw.rect(self.screen,GREY,[width/3,40,width/3,60],0,0,0,0,5,5)
            pygame.draw.rect(self.screen,BLACK,[0,0,width,60+3])
            pygame.draw.rect(self.screen,GREY,[0,0,width,60])
            pygame.draw.rect(self.screen,BLACK,[width/3+10,62,width/3-20,30],0,5)

            # Bouton Retour Menu
            backmenu_txtBG = pygame.font.Font(police,25).render("MENU",True, BLACK) ; screen.blit(backmenu_txtBG, (width-100,18))
            backmenu_txt = pygame.font.Font(police,25).render("MENU",True, WHITE) ; screen.blit(backmenu_txt, (width-100,15))
            save_txtBG = pygame.font.Font(police,25).render("Sauvegarder",True, BLACK) ; screen.blit(save_txtBG, (15,18))
            save_txt = pygame.font.Font(police,25).render("Sauvegarder",True, WHITE) ; screen.blit(save_txt, (15,15))

            # UI
            pos_y = height-height/2+40 ; epaisseur = width/3 ; hauteur = height/2-50
            pygame.draw.rect(self.screen, BLACK, [-1.5, pos_y-13, 3*epaisseur+3, height], 0,10)
            pygame.draw.rect(self.screen, GREY, [0, pos_y-10, 3*epaisseur, height], 0,10)
            pygame.draw.rect(self.screen, BLACK, [5, pos_y, epaisseur, hauteur],5)
            pygame.draw.rect(self.screen, BLACK, [width/3, pos_y, 2*epaisseur-5, hauteur/2+5],5)
            pygame.draw.rect(self.screen, BLACK, [width/3, pos_y+hauteur/2, 2*epaisseur-5, hauteur/2],5)

            # STATISTIQUES & VARIABLES

            stats_text = pygame.font.Font(police,30).render("Statistiques",True, BLACK) ; screen.blit(stats_text, (epaisseur/2-1/2*stats_text.get_size()[0],pos_y+10))

            self.drawtext(screen,cityname,30,BLACK,-340)
            self.drawtext(screen,cityname,30,GREEN,-343)
            nom_th2 = cityname
            self.drawtext(screen,ville_info,25,WHITE,-295)

            pygame.draw.rect(self.screen,BLACK,[30,pos_y+55,55,55],0,100)
            pygame.draw.rect(self.screen,WHITE,[30,pos_y+55,55,55],1,100)
            screen.blit(self.time_icon_tr,(22,pos_y+55))
            year_txt = pygame.font.Font(police,30).render("Année : ",True, BLACK) ; screen.blit(year_txt, (100,pos_y+68))
            
            pygame.draw.rect(self.screen,GREY,[100+year_txt.get_size()[0]+10,height-height/2+110,100,25])
            thread_year = threading.Thread(target=self.display,args=(f"{mois[self.tour-1]} {year}", BLACK,(100+year_txt.get_size()[0]+10,height-height/2+110))) ; thread_year.start() ; thread_year.join()
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
            co2_txt = pygame.font.Font(police,30).render("Emissions : ",True, BLACK) ; screen.blit(co2_txt, (100,pos_y+250))

            pygame.draw.rect(self.screen,GREY,[100+pop_txt.get_size()[0],pos_y+250,100,25])
            thread_pollution = threading.Thread(target=self.display,args=(f"{round(pollu,0)} T", BLACK,(100+pop_txt.get_size()[0],pos_y+250))) ; thread_pollution.start() ; thread_pollution.join()
            tco2_th2 = pollu

            actions_text = pygame.font.Font(police,30).render("Actions",True, BLACK) ; screen.blit(actions_text, (2*epaisseur-1/2*actions_text.get_size()[0],pos_y+15))
            reglesttl_text = pygame.font.Font(police,30).render("Règles",True, BLACK) ; screen.blit(reglesttl_text, (2*epaisseur-1/2*reglesttl_text.get_size()[0],pos_y+170))
            obj_text = pygame.font.Font(police,20).render("Objectif : Baisser les émissions en dessous de 5 Tonnes par an d'ici 2050",True, BLACK) ; screen.blit(obj_text, (2*epaisseur-1/2*obj_text.get_size()[0],pos_y+205))
            rule1_text = pygame.font.Font(police,20).render("Pour ce faire, vous disposez de boutons d'actions ci-dessus.",True, BLACK) ; screen.blit(rule1_text, (2*epaisseur-1/2*rule1_text.get_size()[0],pos_y+240))
            rule2_text = pygame.font.Font(police,20).render("Touches 1 à 7 : Actions | Retour : Passer une année | Entrée : Passer un mois",True, BLACK) ; screen.blit(rule2_text, (2*epaisseur-1/2*rule2_text.get_size()[0],pos_y+278))
            rule2_text = pygame.font.Font(police,20).render("Touches 1 à 7 : Actions | Retour : Passer une année | Entrée : Passer un mois",True, YELLOW) ; screen.blit(rule2_text, (2*epaisseur-1/2*rule2_text.get_size()[0],pos_y+275))

            pygame.draw.rect(self.screen,EF_BLUE,[1/3*width+60,pos_y+60,75,75],0,10)
            pygame.draw.rect(self.screen,BLACK,[1/3*width+60,pos_y+60,75,75],3,10)
            screen.blit(self.eol_icon_tr,(1/3*width+61.5,pos_y+61.5))
            self.EolButn = pygame.Rect((1/3*width+60,pos_y+60),(75,75))
            cost_eol = pygame.font.Font(police,20).render("15 C",True, BLACK) ; screen.blit(cost_eol, (1/3*width+75,pos_y+40))
            time_eol = pygame.font.Font(police,20).render("2 Mois",True, BLACK) ; screen.blit(time_eol, (1/3*width+60,pos_y+135))

            pygame.draw.rect(self.screen,EF_BLUE,[1/3*width+180,pos_y+60,75,75],0,10)
            pygame.draw.rect(self.screen,BLACK,[1/3*width+180,pos_y+60,75,75],3,10)
            screen.blit(self.solar_icon_tr,(1/3*width+181.5,pos_y+61.5))
            self.SolButn = pygame.Rect((1/3*width+180,pos_y+60),(75,75))
            cost_sol = pygame.font.Font(police,20).render("20 C",True, BLACK) ; screen.blit(cost_sol, (1/3*width+195,pos_y+40))
            time_sol = pygame.font.Font(police,20).render("2 Mois",True, BLACK) ; screen.blit(time_sol, (1/3*width+180,pos_y+135))
            
            pygame.draw.rect(self.screen,EF_BLUE,[1/3*width+300,pos_y+60,75,75],0,10)
            pygame.draw.rect(self.screen,BLACK,[1/3*width+300,pos_y+60,75,75],3,10)
            screen.blit(self.hydro_icon_tr,(1/3*width+301.5,pos_y+61.5))
            self.HydroButn = pygame.Rect((1/3*width+300,pos_y+60),(75,75))
            cost_hydro = pygame.font.Font(police,20).render("75 C",True, BLACK) ; screen.blit(cost_hydro, (1/3*width+315,pos_y+40))
            time_hydro = pygame.font.Font(police,20).render("1 An",True, BLACK) ; screen.blit(time_hydro, (1/3*width+300+1/3*time_hydro.get_size()[0],pos_y+135))

            pygame.draw.rect(self.screen,EF_BLUE,[1/3*width+420,pos_y+60,75,75],0,10) 
            pygame.draw.rect(self.screen,BLACK,[1/3*width+420,pos_y+60,75,75],3,10) 
            screen.blit(self.coaloil_icon_tr,(1/3*width+421.5,pos_y+61.5))
            self.CoalOilButn = pygame.Rect((1/3*width+420,pos_y+60),(75,75))
            cost_coaloil = pygame.font.Font(police,20).render("85 C",True, BLACK) ; screen.blit(cost_coaloil, (1/3*width+420+15,pos_y+40))
            time_coaloil = pygame.font.Font(police,20).render("2 Ans",True, BLACK) ; screen.blit(time_coaloil, (1/3*width+420+1/12*time_coaloil.get_size()[0],pos_y+135))

            pygame.draw.rect(self.screen,EF_BLUE,[1/3*width+540,pos_y+60,75,75],0,10) 
            pygame.draw.rect(self.screen,BLACK,[1/3*width+540,pos_y+60,75,75],3,10) 
            screen.blit(self.eleccar_icon_tr,(1/3*width+541.5,pos_y+61.5))
            self.ElecCarButn = pygame.Rect((1/3*width+540,pos_y+60),(75,75))
            cost_eleccar = pygame.font.Font(police,20).render("50 C",True, BLACK) ; screen.blit(cost_eleccar, (1/3*width+540+15,pos_y+40))
            time_eleccar = pygame.font.Font(police,20).render("6 Mois",True, BLACK) ; screen.blit(time_eleccar, (1/3*width+540,pos_y+135))


            pygame.draw.rect(self.screen,EF_BLUE,[1/3*width+660,pos_y+60,75,75],0,10) 
            pygame.draw.rect(self.screen,BLACK,[1/3*width+660,pos_y+60,75,75],3,10) 
            screen.blit(self.sensibiliser_icon_tr,(1/3*width+661.5,pos_y+61.5))
            self.AwareButn = pygame.Rect((1/3*width+660,pos_y+60),(75,75))
            cost_aware = pygame.font.Font(police,20).render("5 C",True, BLACK) ; screen.blit(cost_aware, (1/3*width+660+15,pos_y+40))
            time_aware = pygame.font.Font(police,20).render("1 Mois",True, BLACK) ; screen.blit(time_aware, (1/3*width+660,pos_y+135))
            
            pygame.draw.rect(self.screen,EF_BLUE,[1/3*width+780,pos_y+60,75,75],0,10)
            pygame.draw.rect(self.screen,BLACK,[1/3*width+780,pos_y+60,75,75],3,10)
            screen.blit(self.recycle_icon_tr,(1/3*width+781.5,pos_y+61.5))
            self.RecycleButn = pygame.Rect((1/3*width+780,pos_y+60),(75,75))
            cost_recycle = pygame.font.Font(police,20).render("35 C",True, BLACK) ; screen.blit(cost_recycle, (1/3*width+780+15,pos_y+40))
            time_recycle = pygame.font.Font(police,20).render("3 Mois",True, BLACK) ; screen.blit(time_recycle, (1/3*width+780,pos_y+135))

            self.gamesave(cityname, year, money, popu, pollu)

    def display(self, txt,color, pos):
        text = pygame.font.Font(police,25).render(txt, True, color)
        self.screen.blit(text, pos)

    def cityscape(self, pop):
        global ville_info
        screen.fill(WHITE)
        if pop <= 20 :
            ville_info = "Petite Cité"
            screen.blit(self.font1,(0, 0, width, height/2))
        elif 20 < pop <= 50 :
            ville_info = "Moyenne Cité"
            screen.blit(self.font2,(0, 0,width,height/2))
        elif 50 < pop <= 75 :
            ville_info = "Grande Cité"
            screen.blit(self.font3,(0, 0,width,height/2))
        elif 75 < pop <= 100 :
            ville_info = "Cité Majeure"
            screen.fill(EF_BLUE)
            screen.blit(self.font4,(0, 0,width,height/2))
        elif 100 < pop <= 125 :
            ville_info = "Grande Cité Majeure"
            screen.fill(EF_BLUE)
            screen.blit(self.font5,(0, 0,width,height/2))
        elif 125 < pop < 150 :
            ville_info = "Cité Capitale"
            screen.fill(BLACK)
            screen.blit(self.font6,(0, 0,width,height/2))
        else : 
            ville_info = "Cité Capitale Majeure"
            screen.fill(BLACK)
            screen.blit(self.font7,(0, 0,width,height/2))

# Display Text
    def display(self, txt, color, pos):
        text = pygame.font.Font(police,25).render(txt, True, color)
        self.screen.blit(text, pos)

# Musique Fond & Sons
    def play_sound(self, sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    def background_sound(self, path, vol):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(path) 
        sound.set_volume(vol) 
        sound.play(-1)

# Fonctions Jeu
# 15 C 
    def creer_eolienne(self, tour, pop, pollution, argent):
        if argent < 15 : 
            pygame.font.Font(police,30).render("Argent : ",True, RED) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
            time.sleep(0.5)
            pygame.font.Font(police,30).render("Argent : ",True, BLACK) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
        else :
            if tour+2 <= 12 : 
                argent -= 15
                pop += 1
                if pollution < 2 : pollution*=0.9
                else : pollution -= 2
                tour += 2
            else : pass
        return tour, round(pop,0), round(pollution,0), round(argent, 0)
# 20 C
    def creer_pansolaire(self, tour, pop, pollution, argent):
        if argent < 20 : 
            pygame.font.Font(police,30).render("Argent : ",True, RED) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
            time.sleep(0.5)
            pygame.font.Font(police,30).render("Argent : ",True, BLACK) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
        else : 
            if tour+3 <= 12 :
                argent -= 20
                pop += 1
                if pollution < 5 : pollution*=0.9
                else : pollution -= 5
                tour+=3
            else : pass
        return tour, round(pop,0), round(pollution,0), round(argent, 0)
# 50 C
    def creer_voitures_elec(self, tour, pop, pollution, argent):
        if argent < 50 :
            pygame.font.Font(police,30).render("Argent : ",True, RED) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
            time.sleep(0.5)
            pygame.font.Font(police,30).render("Argent : ",True, BLACK) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
        else : 
            if tour+6 <= 12 :
                argent -= 50
                if pollution < 10 : pollution*=0.95
                else : pollution -= 10
                pop += 3
                tour+=6
            else : pass
        return tour, round(pop,0), round(pollution,0), round(argent, 0)
# 35 C
    def recyclage(self, tour, pop, pollution, argent):
        if argent < 35 :
            pygame.font.Font(police,30).render("Argent : ",True, RED) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
            time.sleep(0.5)
            pygame.font.Font(police,30).render("Argent : ",True, BLACK) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
        else : 
            if tour+3 <= 12 :
                argent -= 35
                if pollution < 15 : pollution*=0.95
                else : pollution -= 15
                pop += 15
                tour+=3
            else : pass
        return tour,round(pop,0), round(pollution,0), round(argent, 0)
# 75 C
    def creer_barragehydro(self,annee, pop,pollution,argent):
        if argent < 75 :
            pygame.font.Font(police,30).render("Argent : ",True, RED) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
            time.sleep(0.5)
            pygame.font.Font(police,30).render("Argent : ",True, BLACK) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
        else : 
            if annee+1 < 2050 : 
                annee += 1
                argent -= 75
                if pollution < 20 : pollution*=0.75
                else : pollution -= 20
                pop += 10
            else : pass
        return annee, round(pop,0), round(pollution,0), round(argent, 0)
# 85 C 
    def stop_coaloil(self,annee,pop,pollution,argent):
        if argent < 85 :
            pygame.font.Font(police,30).render("Argent : ",True, RED) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
            time.sleep(0.5)
            pygame.font.Font(police,30).render("Argent : ",True, BLACK) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
        else : 
            if annee+2 < 2050 : 
                annee += 2
                argent -= 85
                pop += 15
                if pollution < 35 : pollution*=0.5
                else : pollution -= 35
            else : pass
        return annee,round(pop,0), round(pollution,0), round(argent, 0)
# 5 C
    def sensibiliser(self,tour,pop,pollution,argent):
        if argent < 5 :
            pygame.font.Font(police,30).render("Argent : ",True, RED) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
            time.sleep(0.5)
            pygame.font.Font(police,30).render("Argent : ",True, BLACK) 
            screen.blit(pygame.font.Font(police,30).render("Argent : ",True, RED) , (100,height-height/2+40+130))
            pygame.display.flip()
        else : 
            if tour+1 <= 12 :
                argent -= 5
                if pollution < 2 : pollution*=0.95
                else : pollution -= 2
                pop += 10
                tour+=1
            else : pass
        return tour,round(pop,0), round(pollution,0), round(argent, 0)

# Main Game
    def run_game(self):
        gamestop = False
        intro = False
        menu = True
        thread_music = threading.Thread(target=self.background_sound, args=(f"soundtrack/music/{music[random.randint(0,len(music)-1)]}.ogg",volume)) #vol : 0.25 (base def)
        play_song = False
        self.tour = 1

        while True :
            if self.tour >= 12:
                self.tour = self.tour-12
                pop += 2
                argent += pop*0.5
                pollution *= 1.05
                if argent == 0 or argent < 1/5*pop :
                    self.saveButton = pygame.Rect((0,0),(0,0))
                    self.EolButn = pygame.Rect((0,0),(0,0))
                    self.ElecCarButn = pygame.Rect((0,0),(0,0))
                    self.SolButn = pygame.Rect((0,0),(0,0))
                    self.HydroButn = pygame.Rect((0,0),(0,0))
                    self.RecycleButn = pygame.Rect((0,0),(0,0))
                    self.CoalOilButn = pygame.Rect((0,0),(0,0))
                    self.AwareButn = pygame.Rect((0,0),(0,0))

                    self.RetourMenu = pygame.Rect((width//2-50,height/2+150),(100,50))

                    screen.blit(self.bankrupt,[(width/2-1/2*(width/2-100)-50,height/2-100),(width/2,height/2-50)])

                    self.drawtext(self.screen,"Fin de la Partie",35,BLACK,-75)
                    self.drawtext(self.screen,"Fin de la Partie",35,WHITE,-78)
                    self.drawtext(self.screen,f"Année : 2050",25,BLACK,-35)
                    self.drawtext(self.screen,f"Année : 2050",25,WHITE,-38)
                    self.drawtext(self.screen,"MENU",25,BLACK,+163) ; self.drawtext(self.screen,"MENU",25,YELLOW,+160)

                    self.drawtext(self.screen,"Banqueroute !",35,BLACK,+35)
                    self.drawtext(self.screen,"Banqueroute !",35,LOWRED,+32)
                    self.drawtext(self.screen,"Malgré vos efforts",25,BLACK,+85)
                    self.drawtext(self.screen,"Malgré vos efforts",25,WHITE,+82)
                    self.drawtext(self.screen,"l'économie de la ville a plongé dans le rouge",25,BLACK,+120)
                    self.drawtext(self.screen,"l'économie de la ville a plongé dans le rouge",25,WHITE,+117)

                    pygame.display.flip()
                    gamestop = True

                if annee < 2050 : annee+=1
                else :
                    self.saveButton = pygame.Rect((0,0),(0,0))
                    self.EolButn = pygame.Rect((0,0),(0,0))
                    self.ElecCarButn = pygame.Rect((0,0),(0,0))
                    self.SolButn = pygame.Rect((0,0),(0,0))
                    self.HydroButn = pygame.Rect((0,0),(0,0))
                    self.RecycleButn = pygame.Rect((0,0),(0,0))
                    self.CoalOilButn = pygame.Rect((0,0),(0,0))
                    self.AwareButn = pygame.Rect((0,0),(0,0))

                    self.RetourMenu = pygame.Rect((width//2-50,height/2+150),(100,50))

                    if pollution > 5 : 
                        screen.blit(self.badending,[(width/2-1/2*(width/2-100)-50,height/2-100),(width/2,height/2-50)])
                        pygame.draw.rect(self.screen,BLACK,[(width/2-1/2*(width/2-100)-50,height/2-100),(width/2,height/2-50)],3)
                        
                        self.drawtext(self.screen,"Fin de la Partie",35,BLACK,-75)
                        self.drawtext(self.screen,"Fin de la Partie",35,WHITE,-78)
                        self.drawtext(self.screen,f"Année : 2050",25,BLACK,-35)
                        self.drawtext(self.screen,f"Année : 2050",25,WHITE,-38)
                        self.drawtext(self.screen,"MENU",25,BLACK,+163) ; self.drawtext(self.screen,"MENU",25,YELLOW,+160)

                        self.drawtext(self.screen,"Dommage !",35,BLACK,+35)
                        self.drawtext(self.screen,"Dommage !",35,LOWRED,+32)
                        self.drawtext(self.screen,"Malgré vos efforts",25,BLACK,+85)
                        self.drawtext(self.screen,"Malgré vos efforts",25,WHITE,+82)
                        self.drawtext(self.screen,"les émissions restent trop élevées",25,BLACK,+120)
                        self.drawtext(self.screen,"les émissions restent trop élevées",25,WHITE,+117)
                    else : 
                        screen.blit(self.goodending,[(width/2-1/2*(width/2-100)-50,height/2-100),(width/2,height/2-50)])
                        pygame.draw.rect(self.screen,BLACK,[(width/2-1/2*(width/2-100)-50,height/2-100),(width/2,height/2-50)],3)
                        
                        self.drawtext(self.screen,"Fin de la Partie",35,BLACK,-75)
                        self.drawtext(self.screen,"Fin de la Partie",35,WHITE,-78)
                        self.drawtext(self.screen,f"Année : 2050",25,BLACK,-35)
                        self.drawtext(self.screen,f"Année : 2050",25,WHITE,-38)
                        self.drawtext(self.screen,"MENU",25,BLACK,+163) ; self.drawtext(self.screen,"MENU",25,YELLOW,+160)

                        self.drawtext(self.screen,"Félicitations !",35,BLACK,+35)
                        self.drawtext(self.screen,"Félicitations !",35,LOWGREEN,+32)
                        self.drawtext(self.screen,"Vos efforts ont payés",25,BLACK,+85)
                        self.drawtext(self.screen,"Vos efforts ont payés",25,WHITE,+82)
                        self.drawtext(self.screen,"Les émissions sont à des niveaux raisonnables",25,BLACK,+120)
                        self.drawtext(self.screen,"Les émissions sont à des niveaux raisonnables",25,WHITE,+117)
                    pygame.display.flip()
                    gamestop = True
                    
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

                # nom_th2,annee_th2,argent_th2,population_th2,tco2_th2

                elif gamestop == False and menu == False and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 :
                        self.tour, pop, pollution, argent = self.creer_eolienne(self.tour, pop, pollution, argent)
                        RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                        pygame.display.flip()

                    elif event.key == pygame.K_2:
                        self.tour, pop, pollution, argent = self.creer_pansolaire(self.tour, pop, pollution, argent)
                        RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                        pygame.display.flip()

                    elif event.key == pygame.K_3:
                        annee, pop, pollution, argent = self.creer_barragehydro(annee, pop, pollution, argent)
                        RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                        pygame.display.flip()

                    elif event.key == pygame.K_4 : 
                        self.tour, pop, pollution, argent = self.creer_voitures_elec(self.tour, pop, pollution, argent)
                        RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                        pygame.display.flip()
                    
                    elif event.key == pygame.K_5 : 
                        self.tour, pop, pollution, argent = self.recyclage(self.tour, pop, pollution, argent)
                        RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                        pygame.display.flip()
                    
                    elif event.key == pygame.K_6 :
                        annee, pop, pollution, argent = self.stop_coaloil(annee, pop, pollution, argent)
                        RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                        pygame.display.flip()
                    
                    elif event.key == pygame.K_7 :
                        self.tour, pop, pollution, argent = self.sensibiliser(self.tour, pop, pollution, argent)
                        RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                        pygame.display.flip()

                    elif event.key == pygame.K_RETURN:
                        # Skip Mois
                        self.tour += 1
                        RunGame.game_ui(self,"GreenCity",annee,argent,pop,pollution)
                        pygame.display.flip()
                    
                    elif event.key == pygame.K_BACKSPACE : 
                        self.tour = 12
                        RunGame.game_ui(self,"GreenCity",annee,argent,pop,pollution)
                        pygame.display.flip()

                elif self.is_button_clicked(event,self.EolButn) : 
                    self.tour, pop, pollution, argent = self.creer_eolienne(self.tour, pop, pollution, argent)
                    RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                    pygame.display.flip()
                
                elif self.is_button_clicked(event,self.SolButn):
                    self.tour, pop, pollution, argent = self.creer_pansolaire(self.tour, pop, pollution, argent)
                    RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                    pygame.display.flip()

                elif self.is_button_clicked(event,self.HydroButn):
                    annee, pop, pollution, argent = self.creer_barragehydro(annee, pop, pollution, argent)
                    RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                    pygame.display.flip()

                elif self.is_button_clicked(event,self.ElecCarButn) : 
                    self.tour, pop, pollution, argent = self.creer_voitures_elec(self.tour, pop, pollution, argent)
                    RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                    pygame.display.flip()
                    
                elif self.is_button_clicked(event,self.RecycleButn) : 
                    self.tour, pop, pollution, argent = self.recyclage(self.tour, pop, pollution, argent)
                    RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                    pygame.display.flip()
                
                elif self.is_button_clicked(event,self.CoalOilButn):
                    annee, pop, pollution, argent = self.stop_coaloil(annee, pop, pollution, argent)
                    RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                    pygame.display.flip()
                    
                elif self.is_button_clicked(event,self.AwareButn) :
                    self.tour, pop, pollution, argent = self.sensibiliser(self.tour, pop, pollution, argent)
                    RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                    pygame.display.flip()

                elif self.is_button_clicked(event, self.Menu_NewGame): 
                    gamestop = False
                    menu = False
                    annee = 2024
                    argent = random.randint(1, 38)
                    pop = random.randint(5, 20)
                    pollution = random.randrange(50,85)
                    nomville = "GreenCity"

                    self.gamesave(nomville, annee, argent, pop, pollution)
                    RunGame.loading_screen(self) ; time.sleep(1)
                    self.screen.fill(BLACK)
                    RunGame.game_ui(self,nomville,annee,argent,pop,pollution)
                    pygame.display.flip()

                elif self.is_button_clicked(event, self.saveButton) :
                    self.gamesave(nom_th2,annee_th2,argent_th2,population_th2,tco2_th2)

                elif self.is_button_clicked(event, self.ResumeGame) :
                    menu = False
                    RunGame.loading_screen(self) ; time.sleep(1)
                    self.screen.fill(BLACK)
                    with open ("userdata.json","r") as f:
                        data = json.load(f)
                    RunGame.game_ui(self,data["City"],data["Annee"],data["Argent"],data["Population"],data["TauxPollution"])
                    pygame.display.flip()

                elif self.is_button_clicked(event, self.Menu_LeaveGame) : 
                    self.screen.fill(BLACK) ; pygame.display.flip()
                    menu = False
                    pygame.quit()
                    sys.exit()

                elif self.is_button_clicked(event, self.RetourMenu) : 
                    self.screen.fill(BLACK) ; pygame.display.flip()
                    self.gamesave(nom_th2,annee_th2,argent_th2,population_th2,tco2_th2)
                    menu = True