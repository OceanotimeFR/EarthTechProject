import pygame
import sys

pygame.init()

VERT = (0, 128, 0)  
BLANC = (255, 255, 255)
NOIR = (0, 0, 0) 

# Définition des dimensions de l'écran et de l'image
largeur_ecran, hauteur_ecran = 1280, 720
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))


# Définition de la police et de la taille
taille_police = 100  
police = pygame.font.SysFont(None, taille_police) 

# Fonction pour afficher le texte centré
def dessiner_texte_centre(texte, police, couleur, surface, y):
    objet_texte = police.render(texte, True, couleur)
    rectangle_texte = objet_texte.get_rect(center=(largeur_ecran / 2, y))
    surface.blit(objet_texte, rectangle_texte)
    return rectangle_texte 

def menu_principal(police): 
    jouer_rect = dessiner_texte_centre('Jouer', police, BLANC, ecran, hauteur_ecran * 0.4)
    option_rect = dessiner_texte_centre('Options', police, BLANC, ecran, hauteur_ecran * 0.55)
    quitter_rect = dessiner_texte_centre('Quitter', police, BLANC, ecran, hauteur_ecran * 0.7)

    while True:
        ecran.fill(VERT)
        # Position titre "Menu Principal" en haut
        dessiner_texte_centre('Menu Principal', police, BLANC, ecran, hauteur_ecran * 0.2)

        # Récupérer la position de la souris lors du clic
        position_souris = pygame.mouse.get_pos()
        clic = pygame.mouse.get_pressed()

        # Changer la couleur du texte lorsque la souris passe dessus
        if jouer_rect.collidepoint(position_souris):
            dessiner_texte_centre('Jouer', police, NOIR, ecran, hauteur_ecran * 0.4)
        else:
            dessiner_texte_centre('Jouer', police, BLANC, ecran, hauteur_ecran * 0.4)

        if option_rect.collidepoint(position_souris):
            dessiner_texte_centre('Options', police, NOIR, ecran, hauteur_ecran * 0.55)
        else:
            dessiner_texte_centre('Options', police, BLANC, ecran, hauteur_ecran * 0.55)

        if quitter_rect.collidepoint(position_souris):
            dessiner_texte_centre('Quitter', police, NOIR, ecran, hauteur_ecran * 0.7)
            if clic[0]: #Permet de quitter le jeu lors du clic gauche 
                pygame.quit()
                sys.exit()
        else:
            dessiner_texte_centre('Quitter', police, BLANC, ecran, hauteur_ecran * 0.7)

        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

menu_principal(police) 
x