import pygame
import random
import threading

pygame.init()

screen = pygame.display.set_mode((1366, 720))

pygame.display.set_caption("Game")

run = True
font = pygame.font.FontType('freesansbold.ttf', 24)
timer = pygame.time.Clock()

class button():
    def __init__(self, x, y, height, width, txt) -> None:
        self.x, self.y, self.height, self.width, self.txt= x, y, height, width, txt
    def draw(self):
        self.btn = pygame.draw.rect(screen, 'light grey', (self.x, self.y, self.height, self.width), 0, 5)
        self.btn = pygame.draw.rect(screen, 'dark grey', (self.x, self.y, self.height, self.width), 5, 5)
        surface = font.render(self.txt, True, (0, 0, 0))
        screen.blit(surface, (self.x + 10, self.y + 10))
    def checkclick(self):
        button_rect = pygame.Rect(self.x, self.y, self.height, self.width)
        return button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]

    
snip = font.render("", True, "black")
counter = 1
speed = 3
Money = random.randint(0, 200)
def menu():
    global menu_event
    global main_gameevent
    global counter
    global ClickedChatbox
    Btn = button(1366/2, 200, 150, 50, "Start Game")
    Btn2 = button(1366/2, 350, 150, 50, "Quit")
    Btn2.draw()
    Btn.draw()
    timer.tick(60)
    if Btn.checkclick():
        menu_event = False
        main_gameevent = True
    if Btn2.checkclick():
        global run
        run = False
def dialog(txt, coords):
    global counter
    snip = font.render(txt[0:(int(counter))], True, "black")
    if counter < len(txt):
        counter += 0.3
        snip = font.render(txt[0:(int(counter))], True, "black") 
    screen.blit(snip, (coords[0], coords[1]))
def maingame():
    global menu_event, counter, main_gameevent, location, Name, ClickedChatbox
    Btn = button(650, 0, 150, 60, "Menu")
    Btn.draw()
    StatsRect = button(0, 0, 200, 400, "Statistiques:")
    StatsRect.draw()
    DialogRect = button(0, 400, 600, 200, f"")
    DialogRect.draw()
    dialog(f"Dialogue: {str(location)}", (DialogRect.x + 30, DialogRect.y + 20))
    dialog(f"Réponse: {str(locationAnswer)}", (DialogRect.x + 30, DialogRect.y + 125))
    dialog(f"Nom: {str(Name)}", (10, 100))
    dialog(f"Argent: {str(Money)}", (10, 200))
    dialog(f"Population: {str(population)}", (10, 300))
    
    if Btn.checkclick():
        menu_event = True
        main_gameevent = False
    if DialogRect.checkclick():
        ClickedChatbox = True
def increasepop():
    global population
    population+= random.randint(0, 20)
def decreasepop():
    global population
    population -= random.randint(0, 20)
def increasemoney():
    global Money
    Money+= random.randint(0, 20)
def decreasemoney():
    global Money
    Money -= random.randint(0, 20)
def cleardialog():
    global location
    location = ""
def askquestionbinary(txt, action1, action2):
    global location, population, Question1
    location = txt
    BtnYes = button(600, 400, 200, 100, f"Oui")
    BtnNo = button(600,500, 200, 100, f"Non")
    BtnYes.draw()
    BtnNo.draw()
    check = False
    if BtnYes.checkclick():
        action1()
        cleardialog()
        Question1 = False
        check = True
    if BtnNo.checkclick():
        action2()
        cleardialog()
        Question1 = False
        check = True

menu_event = True
main_gameevent = False
clock = pygame.time
population = random.randint(0, 50)
location = "Appuyez"
locationAnswer = " "
input = ""
Name = " "
NameGiven = False
ClickedChatbox = False
Question1 = False
Question2 = False
if __name__ == "__main__":
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
    pygame.quit()