# py game is a library available for developing games in python
import pygame

black = (0,0,0)
white = (255,255,255)

pygame.init()
# here we are creating a surface for our game given some heights and width to it
surface = pygame.display.set_mode((1000,500))
# caption is being provided to our game using display.set
pygame.display.set_caption('heli-fly')
# below code judges for how many times a frame is used in a second.
clock = pygame.time.Clock()

img = pygame.image.load('heli.jpg')
x = 150
y = 200
y_move = 5

def game_over():
    pygame.quit()
    quit()


# this function is required to place the helicopter
def helicopter(x,y,image):
    surface.blit(img, (x,y))


# there is a loop created so as to quit the game or to stay in game
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # this line of code helps us to move up or down our helicopter
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_move = 5
    y += y_move

    surface.fill(black)
    helicopter(x,y,img)

    if y > 460 or y < 0:
        game_over()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

