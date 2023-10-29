import pygame
import math
import constants

class Character():

    def __init__(self, x, y, char_animation, char_type):
        self.animation_list = char_animation[char_type]
        self.char_type = char_type
        self.flip = False
        self.frame_index = 0
        self.action = 1 #0:default, 1:right, 2:left, 3:up, 4:down
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect(0, 0, 64, 64)  #cria um retangulo para o personagem
        self.rect.center = (x,y) #define onde o centro do retângulo vai ficar
        self.image = self.animation_list[self.action][self.frame_index]

        self.dir = True

    def move(self, dx, dy):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

        if dx < 0:
            #self.flip = False #setado como false pq n é necessário aqui
            self.left = True

        if dx > 0:
            #self.flip = False #setado como false pq n é necessário aqui
            self.right = True

        if dy < 0:
            self.up = True

        if dy > 0:
            self.down = True

        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2)/2)

        self.rect.x += dx
        self.rect.y += dy

    def update(self):


        #check what action the player is performing
        if self.right == True:
            self.update_action(1)
            self.dir = False

        elif self.left == True:
            self.update_action(2)
            self.dir = False

        elif self.up == True:
            self.update_action(3)
            self.dir = False

        elif self.down == True:
            self.update_action(4)
            self.dir = False

        else:
            self.dir = True


        #handle animation
        #update image
        self.image =self.animation_list[self.action][self.frame_index]

        if self.dir == True and self.frame_index>1:
            self.frame_index = 0

        #check if enought time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > constants.running_animation_cooldown and self.dir == False:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.update_time > constants.animation_cooldown and self.dir == True and self.char_type!=0:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()

        if self.frame_index >= len(self.animation_list[self.action]) and self.dir == False:
            self.frame_index = 1

    def update_action(self, new_action):
        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 1
            self.update_time = pygame.time.get_ticks()
    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipped_image, self.rect)
        pygame.draw.rect(surface , constants.RED, self.rect, 1)

