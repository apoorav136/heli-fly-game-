# py game is a library available for developing games in python
import pygame, time
from random import  *
black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
# here we are creating a surface for our game given some heights and width to it
surfaceWidth = 1000
surfaceHeight = 500
imageHeight = 43
imageWidth = 100


surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
# caption is being provided to our game using display.set
pygame.display.set_caption('heli-fly')
# below code judges for how many times a frame is used in a second.
clock = pygame.time.Clock()

img = pygame.image.load('heli.jpg')


def blocks(x_block,y_block,block_width,block_height,gap):
    pygame.draw.rect(surface,white,[x_block,y_block,block_width,block_height])
    pygame.draw.rect(surface, white, [x_block, y_block+block_height+gap, block_width, surfaceHeight])

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None


def makeTextObjs(text, font):
    textSurafce = font.render(text, True, white)
    return textSurafce, textSurafce.get_rect()


def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)
    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('press any key to continue', smallText)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()
    main()


def game_Over():
    msgSurface('bammm!')


# this function is required to place the helicopter
def helicopter(x, y, image):
    surface.blit(img, (x, y))


# there is a loop created so as to quit the game or to stay in game
def main():
    x = 150
    y = 200
    y_move = 0

    x_block = surfaceWidth
    y_block = 0
    block_width = 75
    block_height = randint(0, (surfaceHeight/2))
    gap = imageHeight * 4.1
    block_move = 3

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
        helicopter(x, y, img)
        blocks(x_block, y_block, block_width, block_height,gap)
        x_block -= block_move

        if y > surfaceHeight - 40 or y < 0:
            game_Over()

        if x_block <(-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0,surfaceHeight/2)

        if x + imageWidth > x_block:
            if x < x_block + block_width:
                print ('possibly in boundary of x')
                if y <   block_height:
                    print ('y crossover upper')
                    if x -imageWidth < block_width + x_block:
                        print ('game over hit upper')
                        game_Over()
        if x + imageWidth > x_block:
            print ('x crossover')
            if y + imageHeight > block_height+gap:
                print ('y crossover lower')
                if x < block_width +x_block:
                    print ('game over lower')
                    game_Over()


        pygame.display.update()
        clock.tick(80)

main()
pygame.quit()
quit()
