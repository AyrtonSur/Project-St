import pygame
import constants
from character import Character

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Rofnein")

#create clock for maintaining frame rate
clock = pygame.time.Clock()

#define player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

#load character images
char_animation = []
main_chars = ["player", "player1"]

animation_type = ["default", "right", "left", "up", "down"]
for char in main_chars:
    #load images
    animation_list = []
    for animation in animation_type:
        temp_list = []
        for i in range(4):
            image = pygame.image.load(f"assets/images/characters/{char}/{animation}/{i}.png").convert_alpha()
            if char == "player1":
                image = scale_img(image, constants.Player1_scale)
            elif char == "player":
                image = scale_img(image, constants.Player_scale)
            temp_list.append(image)
        animation_list.append(temp_list)
    char_animation.append(animation_list)

#inicializando imagem de possíveis inimigos
mob_animations = []
mob_types = ["elf", "imp", "skeleton", "goblin", "muddy", "tiny_zombie", "big_demon"]

animation_types = ["idle", "run"]
for mob in mob_types:
  #load images
  animation_list = []
  for animation in animation_types:
    #reset temporary list of images
    temp_list = []
    for i in range(4):
      img = pygame.image.load(f"assets/images/characters/{mob}/{animation}/{i}.png").convert_alpha()
      img = scale_img(img, constants.SCALE)
      temp_list.append(img)
    animation_list.append(temp_list)
  mob_animations.append(animation_list)

#create player
player = Character(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, char_animation, 0)

#main game loop
run = True
while run:

    #control frame rate
    clock.tick(constants.FPS)

    screen.fill(constants.BG)

    #calculate player movement
    dx = 0
    dy = 0

    #checks if the keys are being pressed at the same time or not
    if moving_right == True and moving_left == True:
        dx = 0
    elif moving_left == True:
        dx = (-1)*(constants.player_speed)
    elif moving_right == True:
        dx = constants.player_speed
    else:
        dx = 0

    #checks if the keys are being pressed at the same time or not
    if moving_up == True and moving_down == True:
        dy = 0
    elif moving_up == True:
        dy = (-1)*constants.player_speed
    elif moving_down == True:
        dy = constants.player_speed
    else:
        dy = 0

    #move player
    player.move(dx, dy)

    #update player
    player.update()

    #drawing
    player.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #take keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False


    pygame.display.update()

pygame.quit()
