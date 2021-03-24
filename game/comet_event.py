import pygame
from comet import Comet
#créer une classe pour l'événement

class CometFallEvent:

    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 5
        #groupe de sprite de comète
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed/100
        
    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #faire tomber 10 comètes
        for i in range(1,10):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Pluie de comètes")
            self.meteor_fall()
            
            self.fall_mode = True #activer les comètes

    def update_bar(self, surface):

        #ajouter pourcentage bar
        self.add_percent()



        #barre noire arrière plan
        pygame.draw.rect(surface, (0,0,0), [
            0, # axe des x
            surface.get_height() - 20, # axe des y
           surface.get_width(),
           10 #epaisseur
           ])
        #bar rouge
        pygame.draw.rect(surface, (187,11,11), [
            0, # axe des x
            surface.get_height() - 20, # axe des y
           (surface.get_width() / 100) * self.percent,
           10 #epaisseur
           ])