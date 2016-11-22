#===============================================================================
# Robert Mitchell
#
# Computer Science - CSUF
#===============================================================================
import pygame
import time
import random

# initialize pygame.
pygame.init()

# environment colors
blackColor = (0,0,0)
whiteColor = (255,255,255)

# seed random for pipe position generation.
random.seed(time.time())

# define and create the game surface.
world_height = 350 # height of background.png
world_width = 640 # width of background.png
koopas_world = pygame.display.set_mode((world_width, world_height))



# set title of window.
pygame.display.set_caption('Koopa\'s Hunt for Flappy Bird')

# define pipe obstacle. Consists of bottom and top pipe
class Pipe:
    # - 284 pixels of vertical height between the sky and the ground.
    # - 284/2 = 142 pixels for top and bottom pipe.
    # - Each pipe should be separated by 127.5 pixels as calculated by the actual ratio between
    #   pipe width and separation form the actual game. Lets use choose a value of 125 pixels for separation.
    # - Each pipe points to a different image,we use five different pipe heights.
    # - A random number pointsf the the pipe object to the pipe image.
    break_position = None
    position = None
    width = None
    top_end_y = None
    bottom_end_y = None
    sprite = None

    def randomize(self):
        # randomly set the height position of the pipe. There are 6 height positions a pipe may be located.
        self.break_position = random.randint(0,5)

        # set proper pipe image and passage area based on position. Passages are hard coded to correspond to the images.
        # if the koopa passes between pipe.top_end_y and pipe.bottom_end_y while
        # being between pipe.position and pipe.position+pipe.width, koopa is free.
        if self.break_position == 0:
            self.sprite = pygame.image.load('sprites/pipe_0.png')
            self.top_end_y = 40
            self.bottom_end_y = self.top_end_y + 80
        elif self.break_position == 1:
            self.sprite = pygame.image.load('sprites/pipe_1.png')
            self.top_end_y = 50
            self.bottom_end_y = self.top_end_y + 80
        elif self.break_position == 2:
            self.sprite = pygame.image.load('sprites/pipe_2.png')
            self.top_end_y = 80
            self.bottom_end_y = self.top_end_y + 80
        elif self.break_position == 3:
            self.sprite = pygame.image.load('sprites/pipe_3.png')
            self.top_end_y = 110
            self.bottom_end_y = self.top_end_y + 80
        elif self.break_position == 4:
            self.sprite = pygame.image.load('sprites/pipe_4.png')
            self.top_end_y = 140
            self.bottom_end_y = self.top_end_y + 80
        elif self.break_position == 5:
            self.sprite = pygame.image.load('sprites/pipe_5.png')
            self.top_end_y = 170
            self.bottom_end_y = self.top_end_y + 80

    def __init__(self, position):

        # specify x,y coordinates of pipe. Pipe is always drawn from the top y=0, but the x coordinate varies as it scrolls or is initialized.
        self.position = (position, 0)

        # all pipes are the same with, 60px.
        self.width = 60

        # set proper pipe image based on position.
        self.randomize()


# level 1.
class PipeLevel:
    position = None
    length = None
    pipes = None
    finish_location = None
    mario_position = None # update this with scrolling
    mario_sprite = None
    mario_walking = None
    mario_standing = None
    mario_peace = None
    flappy_bird_position = None # update this with scrolling
    flappy_bird_sprite = None
    level_complete = None

    # initialize all obstacles.
    def __init__(self):
        self.position = 0
        self.length = 640*6 # level is 7040px long.
        self.finish_location = int((640*1.2) + (10*150)) # the finish is 1/5 a level's length past the last pipe.
        self.pipes = []
        self.mario_position = 2350
        self.mario_walking = pygame.image.load('sprites/mario_walking.png')
        self.mario_standing = pygame.image.load('sprites/mario_standing.png')
        self.mario_peace = pygame.image.load('sprites/mario_peace.png')
        self.mario_sprite = self.mario_standing
        self.flappy_bird_sprite = pygame.image.load('sprites/flappy_bird_in_cage.png')
        self.flappy_bird_position = self.mario_position + 50 # 50 pixels behind mario.
        self.level_complete = False

        # how many pipes?
        for x in range(0, 10):
            # Creat pipes whose position starts at the edge of the screen, and are separated by 90 pixels each.
            self.pipes.append(Pipe(640 + x*150)) # level must be at least 5040px long. self.finish_location must lie beyond 5040px.
        print 'level initialized'

    # if the level is complete, flip boolean.
    def is_compelete(self):
        return self.level_complete

    # given the dimensions of a sprite, and its position, determine if it has collided with a pipe.
    def detect_collision(self, sprite_width, sprite_height, sprite_position):
        # uncomment this vvvvv to pass through all the pipes.
        #return False

        # get sprite position
        (sprite_x, sprite_y) = sprite_position

        # compare the position of the pipes to the object's position. Return true or false if there is a collision.
        for pipe in self.pipes:
            # get pipe position
            (pipe_x, pipe_y) = pipe.position

            # if sprite is between a pipe's x coordinates, make sure that it is also between the gap in the pipe, its y coordinates.
            if (pipe_x <= (sprite_x+sprite_width)) and ((pipe_x+pipe.width) >= sprite_x):
                if (pipe.top_end_y <= sprite_y) and (pipe.bottom_end_y >= (sprite_y+sprite_height-10)): # -10 to make it a bit easier.
                    # Return true because the sprite is betwen the gap in the pipe.
                    return False
                else:
                    # Return true because the sprite is not between the gap, there has been a collision.
                    return True

        # this is here for testing without pipes.
        return False

    # restart the level from the beginning.
    def restart(self):
        self.position = 0
        self.length = 640*6 # level is 7040px long.
        self.finish_location = int((640*1.2) + (10*150)) # the finish is 1/5 a level's length past the last pipe.
        self.pipes = []
        self.mario_position = 2350
        self.mario_walking = pygame.image.load('sprites/mario_walking.png')
        self.mario_standing = pygame.image.load('sprites/mario_standing.png')
        self.mario_peace = pygame.image.load('sprites/mario_peace.png')
        self.mario_sprite = self.mario_standing
        self.flappy_bird_sprite = pygame.image.load('sprites/flappy_bird_in_cage.png')
        self.flappy_bird_position = self.mario_position + 50 # 50 pixels behind mario.
        self.level_complete = False

        # how many pipes?
        for x in range(0, 10):
            # Creat pipes whose position starts at the edge of the screen, and are separated by 90 pixels each.
            self.pipes.append(Pipe(640 + x*150)) # level must be at least 5040px long. self.finish_location must lie beyond 5040px.
        print 'level initialized'

    # draw all pipes without moving them.
    def draw(self):
        # any pipe whose x coordinate is on the screen will be drawn.
        for pipe in self.pipes:
            # get pipe position.
            (x,y) = pipe.position

            # draw all the pipes that are in the screen space.
            if (x <= 640) and (x >= 0):
                koopas_world.blit(pipe.sprite, pipe.position)

    # scroll obstacles right to left based on their position.
    def scroll(self):

        # draw the pipes if we haven't passed the finish location.
        #if self.position <= self.finish_location:

        # update mario and flappy bird's positions.
        if self.mario_position > (int((world_width/3)+60)):
            # update the level position as long as mario hasn't moved upto a point.
            self.position += 1
            # move mario to the left only upto a point.
            self.mario_position -= 1
            # move flappy bird to the left only upto a point.
            self.flappy_bird_position -= 1

        # any pipe whose x coordinate is on the screen, should be drawn and updated, else just update the coordinates.
        for pipe in self.pipes:
            # get pipe position.
            (x,y) = pipe.position

            # draw all the pipes that are on the screen and update their position.
            if (x <= 640) and (x >= 0):
                koopas_world.blit(pipe.sprite, pipe.position)
                pipe.position = (x-1,y)
            else:
                pipe.position = (x-1,y)
    #else:
        #draw mario when he is on screen.
        if self.mario_position < 640:
            # if mario has stopped walking
            if self.mario_position == (int((world_width/3)+60)):
                self.mario_sprite = self.mario_peace
                koopas_world.blit(self.mario_sprite, (self.mario_position, world_height-(66+45)))
                self.level_complete = True
            else: # if mario is walking, animate his walking.
                if (int((640%(self.mario_position/10))/10) % 2 == 0): # <----- Whew* wipes sweat off forehead.
                    self.mario_sprite = self.mario_walking
                    koopas_world.blit(self.mario_sprite, (self.mario_position, world_height-(66+45)))
                else:
                    self.mario_sprite = self.mario_standing
                    koopas_world.blit(self.mario_sprite, (self.mario_position, world_height-(66+45)))

        # draw caged flappy bird when on screen.
        if self.flappy_bird_position < 640:
            koopas_world.blit(self.flappy_bird_sprite, (self.flappy_bird_position, world_height-(66+106)))

# protagonist
class Koopa_paratroopa:
    lives = None
    sprite = None
    height = None
    width = None
    resting_koopa = None
    flapping_koopa = None
    dead_koopa = None
    position = None
    speed = None

    def jump(self):
        (x,y) = self.position
        self.speed = -8
        self.position = (x, y+self.speed)

    def reset(self):
        self.position = (world_width/3, 0)
        self.sprite = self.resting_koopa
        self.speed = 0

    def __init__(self):
        self.lives = 3
        self.resting_koopa = pygame.image.load('sprites/koopa_paratroopa.png')
        self.flapping_koopa = pygame.image.load('sprites/koopa_paratroopa_flapping.png')
        self.dead_koopa = pygame.image.load('sprites/koopa_paratroopa_dead.png')
        self.sprite = self.resting_koopa
        # the sprite images are 30x45px
        self.height = 45
        self.width = 30
        self.position = (world_width/3, 0)
        self.speed = 0

# exit game. call this from anywhere to exit the game.
def exit_game():
    # uninitialize pygame.
    pygame.quit()
    # quit python.
    quit()

# create clock to control frames per second.
FRAMES_PER_SECOND = 60
clock = pygame.time.Clock()

#   initialize game level.
level = PipeLevel()

# initialize koopa.
koopa = Koopa_paratroopa()


# display intro screen and backstory.
user_ready = False
while not user_ready:
    # set background as black
    koopas_world.fill((0,0,0))

    # draw intro sprite.
    intro_sprite = pygame.image.load('sprites/intro_screen.png')
    koopas_world.blit(intro_sprite, (0,0))

    #update
    pygame.display.update()

    # get user input to continue
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            user_ready = True
        if event.type == pygame.QUIT:
            exit_game()

# set up game background.
background_image = pygame.image.load('sprites/background.png') #
koopas_world.blit(background_image, (100,100))



# main game loop.
while True:
    # get user input for gameplay.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            koopa.jump()
        if event.type == pygame.QUIT:
            exit_game()

    # render background image first, so it is behind everything.
    koopas_world.blit(background_image, (0,0))


    # if koopa has not collided with anything, keep game play going.
    if not level.detect_collision(koopa.width, koopa.height, koopa.position):

        # move enemies/obstacles right to left. when to scroll the level? Hmmmmmmmm...
        level.scroll()

        # enact gravity upon koopa.
        (x,y) = koopa.position
        if y >= world_height-(66+45):
            # if koopa has hit the the ground, stop falling.
            koopa.speed = 0
            koopa.position = (x, world_height-(66+45))
            koopas_world.blit(koopa.sprite, koopa.position)
        else:
            # else fall at an increasing rate.
            koopa.position = (x, y+int((koopa.speed/4))) # for 60 fps and level speed, 4 seems good. Very CPU intensive though. Consider lowering frame rate and moving level faster than 1 pixel per frame.
            koopa.speed += 1
            # if koopa is traveling upwards, that is if the koopa has a negative speed, spread wings, else just let koopa rest.
            if koopa.speed <= 0:
                koopa.sprite = koopa.flapping_koopa
            else:
                koopa.sprite = koopa.resting_koopa
            # draw koopa
            koopas_world.blit(koopa.sprite, koopa.position)


        # if we beat the level, show the winning koopa.
        if level.is_compelete():
            # update koopa to dead koopa. He dies of fright.
            koopa.sprite = koopa.dead_koopa
            koopas_world.blit(koopa.sprite, koopa.position)

            # show game over.
            game_over_sprite = pygame.image.load('sprites/game_over.png')
            koopas_world.blit(game_over_sprite, (int((world_width/2)-150), int((world_height/2))-150) )

            # update the new blits.
            pygame.display.update()

            # just sit here until the user quits.
            while True:
                # quit upon user pressing enter
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        exit_game()

        # render lives.
        koopa_life_text_sprite = pygame.image.load('sprites/koopa_life_text.png')
        koopas_world.blit(koopa_life_text_sprite, (0,0))
        koopa_life_sprite = pygame.image.load('sprites/koopa_life.png')
        for x in range(0,koopa.lives):
            koopas_world.blit(koopa_life_sprite, (100+(50*x),0))


        # update display.
        pygame.display.flip()

        # clock
        clock.tick(FRAMES_PER_SECOND)
    else:
        # koopa has died, remove 1 life.
        koopa.lives -= 1

        # if the koopa still has lives left, show dead koopa and restart the level when user presses enter.
        if koopa.lives > 0:
            koopa_is_alive = False
            while not koopa_is_alive:

                # draw background image
                koopas_world.blit(background_image, (0,0))

                # draw the level as it was when koopa died. i.e. do not scroll the level.
                level.draw()

                # koopa is not alive so make koopa a dead koopa.
                koopa.sprite = koopa.dead_koopa

                # draw dead koopa
                koopas_world.blit(koopa.sprite, koopa.position)

                # update display
                pygame.display.flip()

                # clock
                clock.tick(FRAMES_PER_SECOND)

                # keep showing dead koopa until user presses enter or clicks quit.
                for event in pygame.event.get():
                    # quit the game gracefully.
                    if event.type == pygame.QUIT:
                        exit_game()
                    # reset koopa and restart the level.
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        # reset koopa
                        koopa.reset()
                        # restart level
                        level.restart()
                        # exit death loop to begin game play again.
                        koopa_is_alive = True
        else: # else show game over.
            # make backgorund black.
            koopas_world.fill((0,0,0)) # fill with black.

            # set sprite image.
            game_over_sprite = pygame.image.load('sprites/game_over.png')

            # do not blit in the center of the screen, but move over 150 to accomodate the size of the image. Just hardcode it for now.
            koopas_world.blit(game_over_sprite, (int((world_width/2)-150), int((world_height/2))-150) )
            pygame.display.update()

            # just wait until the user presses enter.
            while True:
                # quit upon user pressing enter
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        exit_game()

#===============================================================================
