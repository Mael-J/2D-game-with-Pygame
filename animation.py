import pygame

#classe d'animation

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size = (200,200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True
    #animer le sprite
    def animate(self,loop=False):
        #si animation est active
        if self.animation:
            #passer à l'image suivante
            self.current_image += 1
            #vérifier si ona atteint la fin de l'animation
            if self.current_image >= len(self.images):
                self.current_image = 0
                #si l'naimation n'est pas une boucle
                if loop == False:
                    #désactive l'animation
                    self.animation = False
            #modifier l'image de l'animation
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


#charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger les 24 images de ce sprite dan sle dossier
    images = []
    #chemin du dossier
    path = f'assets/{sprite_name}/{sprite_name}'
    #boucle sur les image du dossier
    for num in range(1,24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images

#dictionnaire des iamges chargées de chaque sprite
animations = {
    'mummy' : load_animation_images('mummy'),
    'player' : load_animation_images('player'),
    'alien' : load_animation_images('alien'),
    }