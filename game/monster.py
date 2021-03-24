import pygame
import random
import animation

#classe monstre
class Monster(animation.AnimateSprite):

    #instancie la classe
    def __init__(self,game):
        #instancie la classe Sprite
        super().__init__('mummy')
        #le jeu
        self.game = game
        #vie du monstre
        self.health = 100
        #vie initiale
        self.max_health = 100
        #force de l'attaque
        self.attack = 0.3
        #self.image = pygame.image.load('assets/mummy2.png')
        self.image = pygame.transform.scale(self.image,(128,128))
        #rectangle de l'image
        self.rect = self.image.get_rect()
        #debut de l'emplacement
        self.rect.x = self.game.screen_width - 80 + random.randint(0,300)
        self.rect.y = self.game.screen_height - 180
        #vitesse du monstre
        self.velocity = random.randint(1,3)
        self.start_animation()

    def damage(self, amount):
        """degats subits par le monstre"""
        #enleve des points de vie
        self.health -= amount
        #si le monstre decede
        if self.health <=0:
            #faire reapparaitre le monstre
            self.rect.x = self.game.screen_width - 80 + random.randint(0,300)
            self.health =self.max_health
            self.velocity = random.randint(1,3)
            #si la barre dévénement est chargée au max
            if self.game.comet_event.is_full_loaded():
                #retirer le jeu
                self.game.all_monsters.remove(self)
                #essaye de décléchencher la pluie
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop = True)
    def update_health_bar(self,surface):
        """actualise la barre de vie du monstre"""
        #dessiner la jauge couleur rgb, position, (x, y , w, h)
        pygame.draw.rect(surface,(60,63,60),[self.rect.x+ 10,self.rect.y - 20,self.max_health,5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x+ 10,self.rect.y - 20,self.health,5])


    def forward(self):
        """methode pour faire avancer le monstre"""
        
        #si le monstre sort de l'écran
        if self.rect.x < 0:
            #faire reapparaitre le monstre
            self.rect.x = self.game.screen_width - 80 + random.randint(0,300)
            self.health =self.max_health
            self.velocity = random.randint(1,3)
        #si le monstre n'entre pas en collision avec le joueur
        if not self.game.check_collision(self,self.game.all_players):
            #fait avancer le monstre
            self.rect.x -= self.velocity
        #si le monstre entre en collision
        else:
            #inflige des degats au joueur
            self.game.player.damage(self.attack)

