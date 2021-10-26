import pygame
import random

#classe pour gérer la comete

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #image de la comete
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,3)
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        self.comet_event.game.sound_manager.play('meteorite')

        #s'il n'y a plus de comètes
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            #faire apparaitre les monstres
            self.comet_event.game.start()


    def fall(self):

        self.rect.y += self.velocity
        #si tombe sur le sol
        if self.rect.y >= 500:
            print("sol")
            #retirer la comete
            self.remove()
            #s'il n'y a plus de comete
            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        #si la comete touche le jour
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            #retirer la boule de feu
            self.remove()
            #dégats du joueur
            self.comet_event.game.player.damage(20)