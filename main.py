import pygame, time, sys, threading, random, testing.test2 as test2
from pygame.locals import * ; from colors import * ; from testing.roymain import * ; from functions import *

pygame.init()

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