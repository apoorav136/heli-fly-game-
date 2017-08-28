# py game is a library available for developing games in python
import pygame

pygame.init()
# here we are creating a surface for our game given some heights and width to it
surface = pygame.display.set_mode((800,400))
# caption is being provided to our game using display.set
pygame.display.set_caption('heli-fly')
# below code judges for how many times a frame is used in a second.
clock = pygame.time.Clock()
# there is a loop created so as to quit the game or to stay in game
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()