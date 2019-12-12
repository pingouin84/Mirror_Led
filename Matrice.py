# Florian DUCORD
# florian.developpement@gmail.com
# https://github.com/pingouin84/Mirror_Led.git

import config
import pygame as pg
import time
#from pygame.locals import *
from math import pi

if not config.DEBUG:
    import board
    import neopixel as neo


class Matrice:
    if not config.DEBUG:
        # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
        # NeoPixels must be connected to D10, D12, D18 or D21 to work.
        PIXEL_PIN = board.D21

        # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
        # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
        ORDER = neo.GRB

    # The number of NeoPixels
    FIELD_WIDTH = 12
    FIELD_HEIGHT = 20
    NUM_PIXELS = 240
    SIZE = [FIELD_WIDTH, FIELD_HEIGHT]
    FONT_MANE = "data/fonts/Picopixel.ttf"

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

    BTN_KILL = 256
    BTN_START = 11
    BTN_SELECT = 12
    BTN_A = 0
    BTN_B = 1
    BTN_X = 3
    BTN_Y = 4
    BTN_R3 = 14
    BTN_R2 = 9
    BTN_R1 = 7
    BTN_L3 = 13
    BTN_L2 = 8
    BTN_L1 = 6
    BTN_HOME = 3

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
        pg.init()
        if not config.DEBUG:
            self.screen = pg.display.set_mode(self.SIZE)  # ,pg.SCALED)
        else:
            self.screen = pg.display.set_mode(self.SIZE, pg.SCALED)

        pg.display.set_caption("Example code for the draw module")

        self.clock = pg.time.Clock()
        # self.screen.fill((255,0,0))

        if not config.DEBUG:
            self.pixels = self.neo.NeoPixel(
                self.PIXEL_PIN, self.NUM_PIXELS, brightness=0.2, auto_write=False, pixel_order=self.ORDER
            )
        #self.pixels.fill((255, 0, 0))

    def initControl(self):
        # On compte les joysticks
        nb_joysticks = pg.joystick.get_count()

        # Et on en crée un s'il y a en au moins un
        if nb_joysticks > 0:
            mon_joystick = pg.joystick.Joystick(0)
            mon_joystick.init()  # Initialisation

            return True

        return False

    def control(self):
        self.clock.tick(10)
        for event in pg.event.get():  # User did something
            if event.type == pg.QUIT:  # If user clicked close
                return self.BTN_KILL
            elif event.type == pg.JOYHATMOTION:
                return event.value
            elif event.type == pg.JOYBUTTONDOWN:
                print(event.button)
                return event.button
            # utilisation clavier
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    return self.BTN_START
                elif event.key == pg.K_ESCAPE:
                    return self.BTN_KILL
                elif event.key == pg.K_LEFT:
                    return self.BTN_LEFT
                elif event.key == pg.K_RIGHT:
                    return self.BTN_RIGHT
                else:
                    print(event.key)

    def showPixels(self):
        pg.display.flip()

        if not config.DEBUG:
            self.pixels.show()

    def setTablePixel(self, x, y, color):
        pg.draw.rect(self.screen, color, [x, y, 1, 1])
        #FIELD_WIDTH = 12
        #FIELD_HEIGHT = 20
        #value = (12-x)*20 + (20-y)

        if x % 2 == 0:
            # print("pair")
            value = ((self.FIELD_WIDTH-x)*self.FIELD_HEIGHT-1) - \
                ((self.FIELD_HEIGHT-1)-y)
        else:
            # print("impair")
            value = ((self.FIELD_WIDTH-x)*self.FIELD_HEIGHT-1) - y

        #value = (self.FIELD_WIDTH-x)*self.FIELD_HEIGHT + (self.FIELD_HEIGHT-y)
        #print("{} : {}".format(value,color))

        if not config.DEBUG:
            self.pixels[value] = tuple(color)  # (0,255,0)

    def afficher_heure(self):
        self.screen.fill(self.BLACK)
        #font = pg.font.SysFont ( "free" ,  6 )
        # font_name = "Pixeled.ttf" #5
        # font_name = "Picopixel.ttf" #7
        #font = pg.font.SysFont ( font_name ,  5 )
        font = pg.font.Font(self.FONT_MANE, 7)

        #val_time = time.localtime()
        val_heure = time.strftime("%H")
        val_minute = time.strftime("%M")
        val_seconde = time.strftime("%S")

        text = font.render(val_heure, True, self.GREEN)
        self.screen.blit(text, [3, 0])
        text = font.render(val_minute, True, self.GREEN)
        self.screen.blit(text, [3, 7])
        text = font.render(val_seconde, True, self.GREEN)
        self.screen.blit(text, [3, 14])
        pg.display.flip()
        self.actualiser_led()

    def afficher_image(self,path):
        image = pg.image.load(path)
        self.screen.blit(image, (0,0))
        pg.display.flip()

    def actualiser_led(self):
        surface = pg.Surface(self.SIZE)
        pixels = pg.surfarray.array2d(self.screen)

        for x in range(11):
            for y in range(19):
                if x % 2 == 0:
                    # print("pair")
                    value = ((self.FIELD_WIDTH-x)*self.FIELD_HEIGHT -
                             1) - ((self.FIELD_HEIGHT-1)-y)
                else:
                    # print("impair")
                    value = ((self.FIELD_WIDTH-x)*self.FIELD_HEIGHT-1) - y

                if pixels[x, y] > 0:
                    value = value

                if not config.DEBUG:
                    self.pixels[value] = pixels[x, y]  # (0,255,0)
                    self.pixels.show()
