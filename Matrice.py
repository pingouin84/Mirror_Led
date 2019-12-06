import pygame
from pygame.locals import *
from math import pi

DEBUG = True

if not DEBUG:
    import board
    import neopixel

class Matrice:
    if not DEBUG:
        # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
        # NeoPixels must be connected to D10, D12, D18 or D21 to work.
        PIXEL_PIN = board.D21

        # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
        # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
        ORDER = neopixel.GRB

    # The number of NeoPixels
    FIELD_WIDTH = 12
    FIELD_HEIGHT = 20
    NUM_PIXELS = 240

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (247, 255, 0)

    BTN_RIGHT = (1, 0)
    BTN_LEFT = (-1, 0)
    BTN_UP = (0, 1)
    BTN_DOWN = (0, -1)

    def __init__(self):
        # self.BLACK = 0x000000
        # self.BLUE = 0x001F
        # self.RED = 0xF80000
        # self.GREEN = 0x07E000
        # self.CYAN = 0x07FF
        # self.MAGENTA = 0xF81F
        # self.YELLOW = 0xFFE0
        # self.WHITE = 0xFFFFFF

        self.colorLib = [self.YELLOW, self.BLUE, self.GREEN, self.RED]

    def initMatrice(self):
        pygame.init()
        size = [120, 200]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Example code for the draw module")
        self.clock = pygame.time.Clock()
        #self.screen.fill((255,0,0))

        if not DEBUG:
            self.pixels = neopixel.NeoPixel(
                self.PIXEL_PIN, self.NUM_PIXELS, brightness=0.2, auto_write=False, pixel_order=self.ORDER
            )   
        #self.pixels.fill((255, 0, 0))

        
    def initControl(self):
        #On compte les joysticks
        nb_joysticks = pygame.joystick.get_count()

        #Et on en crée un s'il y a en au moins un
        if nb_joysticks > 0:
            mon_joystick = pygame.joystick.Joystick(0)
            mon_joystick.init() #Initialisation

            return True
        
        return False


    def control(self):
        self.clock.tick(10)
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == JOYHATMOTION:
                return event.value

    def showPixels(self):
        pygame.display.flip()

        if not DEBUG:
            self.pixels.show()

    def setTablePixel(self, x, y, color):
        pygame.draw.rect(self.screen, color, [x * 10, y * 10, 10, 10])
        #FIELD_WIDTH = 12
        #FIELD_HEIGHT = 20
        #value = (12-x)*20 + (20-y)

        if x%2 == 0:
            #print("pair")
            value = ((self.FIELD_WIDTH-x)*self.FIELD_HEIGHT-1) - ((self.FIELD_HEIGHT-1)-y)
        else:
            #print("impair")
            value = ((self.FIELD_WIDTH-x)*self.FIELD_HEIGHT-1) - y
            

        #value = (self.FIELD_WIDTH-x)*self.FIELD_HEIGHT + (self.FIELD_HEIGHT-y)
        #print("{} : {}".format(value,color))

        if not DEBUG:
            self.pixels[value] = tuple(color) #(0,255,0)

