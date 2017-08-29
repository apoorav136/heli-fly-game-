# py game is a library available for developing games in python
import pygame, time
from random import  *
black = (0, 0, 0)
white = (255, 255, 255)
sunset  = (253,72,47)

greenyellow =(117, 20,246)
brightblue = (47,228,253)
orange = (211,255,206)
yellow =(255,236,0)
purple = (185,156,209)

colorChoices = [greenyellow,brightblue,orange,yellow,purple]


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

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("score : " + str(count), True, white)
    surface.blit(text, [0,0])


def blocks(x_block,y_block,block_width,block_height,gap, colorChoice):

    pygame.draw.rect(surface,colorChoice,[x_block,y_block,block_width,block_height])
    pygame.draw.rect(surface, colorChoice, [x_block, y_block+block_height+gap, block_width, surfaceHeight])

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
    current_score = 0
    blockColor = colorChoices[randrange(0,len(colorChoices))]

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

        blocks(x_block, y_block, block_width, block_height,gap, blockColor)

        score(current_score)
        x_block -= block_move

        if y > surfaceHeight - 40 or y < 0:
            game_Over()

        if x_block <(-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0,surfaceHeight/2)
            blockColor = colorChoices[randrange(0, len(colorChoices))]
        if x + imageWidth > x_block:
            if x < x_block + block_width:

                if y <   block_height:

                    if x -imageWidth < block_width + x_block:

                        game_Over()
        if x + imageWidth > x_block:

            if y + imageHeight > block_height+gap:

                if x < block_width +x_block:
                    game_Over()

        if x < x_block and x> x_block - block_move:
            current_score +=1

        if 3 <= current_score <5:
            block_move =5.5
            gap = imageHeight * 3.7


        pygame.display.update()
        clock.tick(80)

main()
pygame.quit()
quit()
