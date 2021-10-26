import pygame
from projectile import Projectile
import animation

#classe du joueur
class Player(animation.AnimateSprite):
    def __init__(self,game):
        #initialise la superclasse
        super().__init__('player')
        #classe du jeu
        self.game = game
        #santé
        self.health = 100
        #santé max
        self.max_health = 100
        #force d'attaque
        self.attack = 10
        #vitesse de déplacement
        self.velocity = 5
        #groupe de projectile
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.transform.scale(self.image,(200,200))
        #rectangle de l'image joueur
        self.rect = self.image.get_rect()
        #coordonnées du joueur
        #self.rect.x = 400
        #self.rect.y = 550
        self.rect.x = 400
        self.rect.y = 500
    def damage(self, amount):
        """degats subits par le joueur"""
        if self.health > 0:
            self.health -= amount
        #si le joueur n'a pas lus de vie
        else:
            #arrete le jeu
            self.game.game_over()

    def update_animation(self):
        #anime le joueur
        self.animate()

    def update_health_bar(self,surface):
        """actualise la barre de vie du monstre"""
        #dessiner la jauge couleur rgb, position, (x, y , w, h)
        pygame.draw.rect(surface,(60,63,60),[self.rect.x+ 50,self.rect.y + 20,self.max_health,7])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x+ 50,self.rect.y + 20,self.health,7])

    def launch_projectile(self):
        """methode pour lancer un projectile"""
        #ajoute le projectile dans un groupe
        self.all_projectiles.add(Projectile(self))
        self.start_animation()
        self.game.sound_manager.play('tir')
    def move_right(self):
        """methode pour déplacer le joueur vers la droite"""
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self,self.game.all_monsters):
            self.rect.x += self.velocity
    def move_left(self):
        """methode pour déplacer le joueur vers la gauche"""

        self.rect.x -= self.velocity