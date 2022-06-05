import imp
from pdb import Restart
import pip
import pygame
from sys import exit
import random
pygame.init()

score = 0
start = True
test_font = pygame.font.Font('Minecraft.ttf',70)
test_font1 = pygame.font.Font('Minecraft.ttf',35)
win = pygame.display.set_mode(size= (400,650))
pygame.display.set_caption('Flappy Bird')
start_surf = pygame.image.load("flappy_background.png")                                      
sky_surf = pygame.image.load("flappy sky.png")
bird_surf = pygame.image.load("bird sprite.png") #315 223
pipe_bottom_surf = pygame.image.load("full pipe bottom.png")
pipe_top_surf = pygame.image.load("full pipe top.png")


sky_rect = sky_surf.get_rect(topleft = (0,0))
bird_rect = bird_surf.get_rect(midbottom = (70,300))
pipe_bottom_rect = pipe_bottom_surf.get_rect(midbottom = (350,1100))
pipe_top_rect = pipe_top_surf.get_rect(midbottom = (350,130))
clock = pygame.time.Clock()
gravity = 0
on = True
game_on = True
colide_top = False


while True:
    temp = pipe_bottom_rect.y
    r = random.randint(900,1250)
    text_surf = test_font.render(f'{score}',False,(0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity = -10
        
        if game_on == False:
            if event.type == pygame.KEYDOWN:

                    pipe_bottom_rect = pipe_bottom_surf.get_rect(midbottom = (350,1100))
                    pipe_top_rect = pipe_top_surf.get_rect(midbottom = (350,130))
                    game_on = True
                    on = True
                    score = 0

    
    
    if game_on == False:
        text_surf = test_font1.render('Press space to restart' , False ,(255,255,255))
        win.blit(text_surf,(0,275))
        pygame.display.update()

    if game_on:
        bird_rect.y += gravity

        if on:
            gravity += 0.5

        if on:
            pipe_bottom_rect.left -= 3
            pipe_top_rect.left -= 3

        if pipe_bottom_rect.right < 0:
            pipe_bottom_rect = pipe_bottom_surf.get_rect(midbottom = (410,r))

        if pipe_top_rect.right < 0:
            score += 1
            pipe_top_rect.left = 410
            h = r-970
            pipe_top_rect = pipe_top_surf.get_rect(midbottom = (410,h))


        
        ######collison######

        if pygame.Rect.colliderect(bird_rect,pipe_bottom_rect):
            on = False
            gravity = 6
        
        if pygame.Rect.colliderect(bird_rect,pipe_top_rect):
            on = False
            colide_top = True
            gravity = 6

        if colide_top:
            if pygame.Rect.colliderect(bird_rect,pipe_bottom_rect):
                    gravity = 0
                    game_on = False
        

        if bird_rect.y > 570:
            on = False
            gravity = 0
            bird_rect.y = 535 
            game_on = False
        
        if (bird_rect.y + 35) == pipe_bottom_rect.y and bird_rect.x > pipe_bottom_rect.x and bird_rect.x < 104+pipe_bottom_rect.x:
            on = False
            gravity = 0
            bird_rect.y = pipe_bottom_rect.y
            game_on = False
        
        ######Display######

        win.blit(sky_surf, sky_rect)
        win.blit(bird_surf,bird_rect)
        win.blit(pipe_top_surf,pipe_top_rect)
        win.blit(pipe_bottom_surf,pipe_bottom_rect)
        win.blit(text_surf,(190,40))
        clock.tick(60)

        pygame.display.update()
    