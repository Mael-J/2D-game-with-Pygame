import pygame

#classe du projectile

class Projectile(pygame.sprite.Sprite):
    #instancie la classe avec l'argument du joueur
    def __init__(self,player):
        super().__init__()
        #joueur
        self.player = player
        #vitesse 
        self.velocity = 5
        #image du projectil
        self.image = pygame.image.load('assets/projectile.png')
        #self.image = pygame.image.load('assets/apple.png')
        #self.image = pygame.image.load('assets/projectile2.png')
        #redimensionne l'image
        self.image = pygame.transform.scale(self.image,(50,50))
        #carré entourant l'image
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        #image d'origine
        self.origin_image = self.image
        #angle de rotation
        self.angle = 0
    def rotate(self):
        """tourne le projectile"""
        self.angle -= 12
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect = self.image.get_rect(center =self.rect.center)
    def remove(self):
        """methode pour detruire le projectile"""
        self.player.all_projectiles.remove(self)
    def move(self, screen_width):
        """methode pour deplace le projectile"""
        #fait avancer le projectile
        self.rect.x += self.velocity
        #tourne le projectile
        self.rotate()

        # si le projectile rentre en collision avec le monstre
        for monster in self.player.game.check_collision(self,self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()
            #inflige les degats
            monster.damage(self.player.attack)

        #detruit projectile hors ecran
        if self.rect.x > screen_width:
            self.remove()
            print('projectile supprimé')
