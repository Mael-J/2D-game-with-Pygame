import pygame
from game import Game
import math
pygame.init()

#definir une clock
clock = pygame.time.Clock()
FPS = 60

#générer la fenetre du jeu
#titre de la fenetre
pygame.display.set_caption("Beast Game")
#taille de la fenetre
w, h = 1080, 720
screen = pygame.display.set_mode((w,h))
#image d'arriere plan
background = pygame.image.load('assets/bg.jpg')


#importer la banniere
banner = pygame.image.load('assets/banner.png')
#redimmensionner l'image
banner = pygame.transform.scale(banner,(500,500))
#rectangle de la banniere
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

#charger le bouton de lancement
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)




#charger le jeu
game = Game(w,h)

#variable pour garder la fenetre ouverte ou non
running = True

while running:

    #appliquer l'arriere plan en ajustant position
    screen.blit(background, (0,-200))


    #si le jeu a commencé
    if game.is_playing:
        #instructions de la partie
        game.update(screen)
    #si le jeu n'a pas commencé
    else:
        #ajouter l'écran de bienvenue
        screen.blit(play_button, (play_button_rect.x,play_button_rect.y))
        screen.blit(banner, (banner_rect.x,0))


    #mettre à jour l'écran
    pygame.display.flip()
    #récupère les évenements du jeu
    for event in pygame.event.get():
        #si le joueur ferme la fenetre
        if event.type == pygame.QUIT:
            #variable = fermer la fenetre
            running = False
            pygame.quit()
            print("fermeture fenetre")
        #si une touche est utilisée
        elif event.type == pygame.KEYDOWN:
            #ajoute dans le dict que la touche est active
            game.pressed[event.key] = True
            #si espace est utilisé
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    #lance le jeu
                    game.start()
                    #son du click
                    game.sound_manager.play('click')

        #si une touche n'est plus utilisée
        elif event.type == pygame.KEYUP:
            #ajoute faux au dict
            game.pressed[event.key] = False
        #si on click avec la souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #si on clique sur le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #lance le jeu
                game.start()
                #son du click
                game.sound_manager.play('click')
    #fixer le nombre de FPS sur ma clock
    clock.tick(FPS)


    
