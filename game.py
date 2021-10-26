import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager


#classe du jeu
class Game:
    def __init__(self,screen_width ,screen_height):
        #le jeu a commencé T/F
        self.is_playing = False
        #taille de l'ecran de jeu
        self.screen_width = screen_width
        self.screen_height = screen_height
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        #générer l'evenement
        self.comet_event = CometFallEvent(self)
        #touche pressee
        self.pressed = {}
        #score à 0
        self.score = 0
        
        #afficher le score sur l'écran
        self.font = pygame.font.Font("assets/myfont.ttf",30)

        #gerer le son
        self.sound_manager = SoundManager()

    def start(self):
        """lance le jeu et les monstres"""
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

        #le joueur dans un groupe
        self.all_players =pygame.sprite.Group()
        #generer notre joueur
        self.player = Player(self)
        #ajoute le joueur au groupe
        self.all_players.add(self.player)

    def add_score(self, points =10):
        """ajout de points """
        self.score += points

    def game_over(self):
        """ arret du jeu """
        #groupe de monstre vide
        self.all_monsters = pygame.sprite.Group()
        #groupe de comètes vide
        self.comet_event.all_comets = pygame.sprite.Group()
        #vie du joueur
        self.player.health = self.player.max_health
        #jauge d'événement à 0
        self.comet_event.reset_percent()
        self.is_playing = False
        #remise à 0 du score
        self.score = 0
        #son game over
        self.sound_manager.play('game_over')

    def update(self, screen):
        """mise à jour des evevenements """ 

        
        score_text = self.font.render(f"Score : {self.score}", 1, (0,0,0))
        screen.blit(score_text, (20,20))

        #appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)
        #actualise la barre de vie du joueur
        self.player.update_health_bar(screen)

        #actualise la barre d'évènement du jeu
        self.comet_event.update_bar(screen)

        #actualiser l'animation du joeur
        self.player.update_animation()

        #boucle sur les projectiles
        for projectile in self.player.all_projectiles:
            #lance projectile
            projectile.move(screen.get_width())


        #boucle sur les monstres
        for monster in self.all_monsters:
            #fait avancer les monstres
            monster.forward()
            #affiche bar de vie
            monster.update_health_bar(screen)
            #anime le monstre
            monster.update_animation()

        #appliquer le projectile sur l'ecran
        self.player.all_projectiles.draw(screen)

        #boucle sur les cometes
        for comet in self.comet_event.all_comets:
            comet.fall()

        #appliquer les monstres
        self.all_monsters.draw(screen)

        #appliquer les comètes
        self.comet_event.all_comets.draw(screen)

        #verifie le sens de deplacement du joueur
        #print(self.pressed)
        #si touche droite activée
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width< screen.get_width():
            #déplacement à droite
            self.player.move_right()
            #si touche gauche activée
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            #déplacement à gauche
            self.player.move_left()


    def check_collision(self, sprite, group):
        """methode qui gere les collisions"""
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
    def spawn_monster(self,monster_class_name):
        """methode d'apparition du monstre"""
        #création d'une liste de monstres
        self.all_monsters.add(monster_class_name.__call__(self))

