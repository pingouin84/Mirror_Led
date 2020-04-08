# Import a library of functions called 'pygame'
import pygame
from pygame.locals import *
from math import pi

import Matrice

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

h = {
	(0,0):  'c',
	(1,0):  'DROITE', (1,1):   'NE', (0,1):  'HAUT', (-1,1): 'NW',
	(-1,0): 'GAUCHE', (-1,-1): 'SW', (0,-1): 'BAS', (1,-1): 'SE'
}

# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

#mon_joystick = pygame.joystick.Joystick
nb_joysticks = pygame.joystick.get_count()
if nb_joysticks > 0:
        #if mon_joystick == pygame.joystick.Joystick:
        mon_joystick = pygame.joystick.Joystick(0)
        mon_joystick.init() #Initialisation
        print("Axes :", mon_joystick.get_numaxes())
        print("Boutons :", mon_joystick.get_numbuttons())
        print("Trackballs :", mon_joystick.get_numballs())
        print("Hats :", mon_joystick.get_numhats())

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    #On compte les joysticks
    nb_joysticks = pygame.joystick.get_count()

    #Et on en crée un s'il y a en au moins un
    if nb_joysticks > 0:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == JOYBUTTONDOWN:
                print(event.button)
            if event.type == KEYDOWN:
                print(event.key)
            if event.type == MOUSEBUTTONDOWN:
                print(event.button)
            if event.type == JOYAXISMOTION:
                if event.axis == 0 and event.value > 0:
                    print("droite %d",event.value)
                if event.axis == 0 and event.value < 0:
                    print("gauche %d",event.value)
            if event.type == JOYHATMOTION:
                print(event.hat,h[event.value])
                #if event.Hats == 0 and event.value > 0:
                    #print("droite %d",event.value)
                #if event.axis == 0 and event.value < 0:
                    #print("gauche %d",event.value)
            #if event.type != 7:
                #print(event.type)



    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    pygame.draw.rect(screen, Matrice.Matrice.BLUE, [1*10, 1*10, 10, 10])

    # Draw on the screen a GREEN line from (0,0) to (50.75)
    # 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [50, 30], 5)

    # Draw on the screen a GREEN line from (0,0) to (50.75)
    # 5 pixels wide.
    pygame.draw.lines(
        screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5
    )

    # Draw on the screen a GREEN line from (0,0) to (50.75)
    # 5 pixels wide.
    pygame.draw.aaline(screen, GREEN, [0, 50], [50, 80], True)

    # Draw a rectangle outline
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)

    # Draw a solid rectangle
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

    # Draw an ellipse outline, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)

    # Draw an solid ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    pygame.draw.arc(screen, BLACK, [210, 75, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen, GREEN, [210, 75, 150, 125], pi / 2, pi, 2)
    pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi, 3 * pi / 2, 2)
    pygame.draw.arc(screen, RED, [210, 75, 150, 125], 3 * pi / 2, 2 * pi, 2)

    # Draw a circle
    pygame.draw.circle(screen, BLUE, [60, 250], 40)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
