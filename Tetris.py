# Import a library of functions called 'pygame'
# import pygame
import time
from Matrice import Matrice
import random
from numpy import array
from numpy import zeros

# from numpy import ndarray


class Brick:
    def __init__(self):
        self.enabled = False
        self.xpos = 0
        self.ypos = 0
        self.siz = 0
        self.color = Matrice.BLACK
        self.pix = array(
            [
                [0 for x in range(Tetris.MAX_BRICK_SIZE)]
                for x in range(Tetris.MAX_BRICK_SIZE)
            ]
        )


class AbstractBrick:
    def __init__(self):
        self.yOffset = 0
        self.siz = 0
        self.pix = array(
            [
                [0 for x in range(Tetris.MAX_BRICK_SIZE)]
                for x in range(Tetris.MAX_BRICK_SIZE)
            ]
        )


class Field:
    def __init__(self):
        self.pix = array(
            [
                [0 for x in range(Matrice.FIELD_WIDTH)]
                for x in range(Matrice.FIELD_HEIGHT + 1)
            ]
        )
        self.color = array(
            [
                [Matrice.BLACK for x in range(Matrice.FIELD_WIDTH)]
                for x in range(Matrice.FIELD_HEIGHT)
            ]
        )
        #self.color = zeros((Matrice.FIELD_HEIGHT,Matrice.FIELD_WIDTH), dtype=(int,3))


class Tetris:

    MAX_BRICK_SIZE = 4

    def __init__(self):
        self.BRICKOFFSET = -1  # Y offset for new bricks
        self.INIT_SPEED = 250  # Initial delay in ms between brick drops
        self.SPEED_STEP = 100  # Factor for speed increase between levels, default 10
        self.LEVELUP = 5  # Number of rows before levelup, default 5
        self.matrice = Matrice()
        # controll
        self.DIR_UP = 1
        self.DIR_DOWN = 2
        self.DIR_LEFT = 3
        self.DIR_RIGHT = 4

        self.field = Field()
        self.activeBrick = Brick()

        self.brickLib = [
            AbstractBrick(),
            AbstractBrick(),
            AbstractBrick(),
            AbstractBrick(),
            AbstractBrick(),
            AbstractBrick(),
            AbstractBrick(),
        ]

        self.brickLib[0].yOffset = 1
        self.brickLib[0].siz = 4
        self.brickLib[0].pix = array(
            [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        )

        self.brickLib[1].yOffset = 0
        self.brickLib[1].siz = 4
        self.brickLib[1].pix = array(
            [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
        )

        self.brickLib[2].yOffset = 1
        self.brickLib[2].siz = 3
        self.brickLib[2].pix = array(
            [[0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        )

        self.brickLib[3].yOffset = 1
        self.brickLib[3].siz = 3
        self.brickLib[3].pix = array(
            [[0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        )

        self.brickLib[4].yOffset = 1
        self.brickLib[4].siz = 3
        self.brickLib[4].pix = array(
            [[0, 0, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
        )

        self.brickLib[5].yOffset = 1
        self.brickLib[5].siz = 3
        self.brickLib[5].pix = array(
            [[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        )

        self.brickLib[6].yOffset = 1
        self.brickLib[6].siz = 3
        self.brickLib[6].pix = array(
            [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        )

    def millis(self):
        return int(round(time.time() * 1000))

    def tetrisInit(self):
        self.matrice.initMatrice()
        self.matrice.initControl()
        self.matrice.showPixels()

        self.clearField()
        self.brickSpeed = self.INIT_SPEED
        self.nbRowsThisLevel = 0
        self.nbRowsTotal = 0
        self.tetrisGameOver = False
        self.newActiveBrick()

        self.tetrisRunning = True
        self.curTime = self.millis()
        self.prevUpdateTime = self.curTime

    def runTetris(self):
        #print("runTetris")
        # tetrisInit()

        while self.tetrisRunning:
            while (self.curTime - self.prevUpdateTime) < self.brickSpeed:
                # readInput()
                curControl = self.matrice.control()
                if curControl == self.matrice.BTN_KILL:
                    self.tetrisGameOver = True
                elif curControl == self.matrice.BTN_LEFT:
                    self.shiftActiveBrick(self.DIR_LEFT)
                elif curControl == self.matrice.BTN_RIGHT:
                    self.shiftActiveBrick(self.DIR_RIGHT)
                elif curControl == self.matrice.BTN_DOWN:
                    self.shiftActiveBrick(self.DIR_DOWN)
                elif curControl == self.matrice.BTN_UP:
                    self.rotateActiveBrick()
                # if (reseau.curControl != BTN_NONE):
                # .playerControlActiveBrick()
                self.printField()

                if self.tetrisGameOver:
                    break

                self.curTime = self.millis()

            self.prevUpdateTime = self.curTime

            if self.tetrisGameOver:
                self.matrice.afficher_score(self.nbRowsTotal)
                # matrice.fadeOut()
                # char buf[4]
                # int len = sprintf(buf, "%i", nbRowsTotal)

                # scrollTextBlocked(buf,len,WHITE)

                # Disable loop and exit to main menu of led table
                self.tetrisRunning = False
                break

            # If brick is still "on the loose", then move it down by one
            if self.activeBrick.enabled:
                self.shiftActiveBrick(self.DIR_DOWN)
            else:
                # Active brick has "crashed", check for full lines
                # and create new brick at top of field
                self.checkFullLines()
                self.newActiveBrick()
                self.prevUpdateTime = self.millis()
                # Reset update time to avoid brick dropping two spaces

            self.printField()

        # self.matrice.fadeOut()

    def clearField(self):
        #print("clearField")

        for y in range(self.matrice.FIELD_HEIGHT):
            for x in range(self.matrice.FIELD_WIDTH):
                self.field.pix[y, x] = 0
                self.field.color[y, x] = Matrice.BLACK

        # This last row is invisible to the player and only used for the collision detection routine
        self.field.pix[self.matrice.FIELD_HEIGHT] = 1

    def newActiveBrick(self):
        #print("newActiveBrick")
        # uint8_t selectedBrick = 3
        selectedBrick = random.randrange(6)
        selectedColor = random.randrange(3)
        #print("newActiveBrick ===============" + repr(selectedBrick))

        # Set properties of brick
        self.activeBrick.siz = self.brickLib[selectedBrick].siz
        self.activeBrick.yOffset = self.brickLib[selectedBrick].yOffset
        self.activeBrick.xpos = round(
            self.matrice.FIELD_WIDTH / 2 - self.activeBrick.siz / 2
        )
        self.activeBrick.ypos = self.BRICKOFFSET - self.activeBrick.yOffset
        self.activeBrick.enabled = True

        # Set color of brick
        self.activeBrick.color = self.matrice.colorLib[selectedColor]
        # self.activeBrick.color = colorLib[1]

        # Copy pix array of selected Brick
        # for y in range(self.MAX_BRICK_SIZE):
        # for x in range(self.MAX_BRICK_SIZE):
        # self.activeBrick.pix[y, x] = self.brickLib[selectedBrick].pix[y, x]
        self.activeBrick.pix = self.brickLib[selectedBrick].pix

        # Check collision, if already, then game is over
        if self.checkFieldCollision(self.activeBrick):
            self.tetrisGameOver = True
            #print("Game Over")

        #print("newActiveBrick_end")

    def checkFieldCollision(self, brick):
        #print("checkFieldCollision")
        for by in range(self.MAX_BRICK_SIZE):
            for bx in range(self.MAX_BRICK_SIZE):
                fx = brick.xpos + bx
                # fx = (*brick).xpos + bx
                fy = brick.ypos + by
                # fy = (*brick).ypos + by

                if (
                    (brick.pix[by, bx] == 1)
                    and (self.field.pix[fy, fx] == 1)
                    and fy >= 0
                ):
                    return True

        #print("checkFieldCollision_end")
        return False

    def shiftActiveBrick(self, dir):
        # Change position of active brick (no copy to temporary needed)
        if dir == self.DIR_LEFT:
            self.activeBrick.xpos -= 1
        elif dir == self.DIR_RIGHT:
            self.activeBrick.xpos += 1
        elif dir == self.DIR_DOWN:
            self.activeBrick.ypos += 1

        # Check position of active brick
        # Two possibilities when collision is detected:
        #    -Direction was LEFT/RIGHT, just revert position back
        #    -Direction was DOWN, revert position and fix block to field on collision
        # When no collision, keep self.activeBrick coordinates
        if self.checkSidesCollision(self.activeBrick) or self.checkFieldCollision(
            self.activeBrick
        ):
            # Serial.println("coll")
            if dir == self.DIR_LEFT:
                self.activeBrick.xpos += 1
            elif dir == self.DIR_RIGHT:
                self.activeBrick.xpos -= 1
            elif dir == self.DIR_DOWN:
                self.activeBrick.ypos -= 1  # Go back up one
                self.addActiveBrickToField()
                # Disable brick, it is no longer moving
                self.activeBrick.enabled = False

    # Check collision between specified brick and all sides of the playing field
    def checkSidesCollision(self, brick):
        #print("checkSidesCollision")
        # Check vertical collision with sides of field
        for by in range(self.MAX_BRICK_SIZE ):
            for bx in range(self.MAX_BRICK_SIZE ):
                if brick.pix[by, bx] == 1:
                    # Determine actual position in the field of the current pix of the brick
                    fx = brick.xpos + bx
                    fy = brick.ypos + by
                    if fx < 0 or fx >= self.matrice.FIELD_WIDTH:
                        return True

        #print("checkSidesCollision_end")
        return False

    # Copy active pixels to field, including color
    def addActiveBrickToField(self):
        for by in range(self.MAX_BRICK_SIZE ):
            for bx in range(self.MAX_BRICK_SIZE ):
                fx = self.activeBrick.xpos + bx
                fy = self.activeBrick.ypos + by

                if (
                    fx >= 0
                    and fy >= 0
                    and fx < self.matrice.FIELD_WIDTH
                    and fy < self.matrice.FIELD_HEIGHT
                    and self.activeBrick.pix[by, bx]
                ):
                    # Check if inside playing field
                    # field.pix[fy,fx] = field.pix[fy,fx] || self.activeBrick.pix[by,bx]
                    self.field.pix[fy, fx] = self.activeBrick.pix[by, bx]
                    self.field.color[fy, fx] = self.activeBrick.color

    def checkFullLines(self):
        #print("checkFullLines")
        minY = 0
        for y in range(self.matrice.FIELD_HEIGHT - 1, minY, -1):
            rowSum = 0
            for x in range(self.matrice.FIELD_WIDTH):
                rowSum += self.field.pix[y, x]

            if rowSum >= self.matrice.FIELD_WIDTH:
                # Found full row, animate its removal
                for x in range(self.matrice.FIELD_WIDTH):
                    self.field.pix[y, x] = 0
                    self.printField()
                    time.sleep(0.1)
                    # delay(100)

                # Move all upper rows down by one
                self.moveFieldDownOne(y)
                y += 1
                minY += 1
                self.printField()
                time.sleep(0.1)

                self.nbRowsThisLevel += 1
                self.nbRowsTotal += 1

                if self.nbRowsThisLevel >= self.LEVELUP:
                    self.nbRowsThisLevel = 0
                    self.brickSpeed -= self.SPEED_STEP
                    if self.brickSpeed < 200:
                        self.brickSpeed = 200

        #print("checkFullLines_end")

    def printField(self):
        #print("printField")
        for x in range(self.matrice.FIELD_WIDTH):
            for y in range(self.matrice.FIELD_HEIGHT):
                self.activeBrickPix = 0
                if self.activeBrick.enabled:
                    # Only draw brick if it is enabled
                    # Now check if brick is "in view"
                    if (
                        (x >= self.activeBrick.xpos)
                        and (x < (self.activeBrick.xpos + (self.activeBrick.siz)))
                        and (y >= self.activeBrick.ypos)
                        and (y < (self.activeBrick.ypos + (self.activeBrick.siz)))
                    ):
                        self.activeBrickPix = (self.activeBrick.pix)[
                            y - self.activeBrick.ypos, x - self.activeBrick.xpos
                        ]

                if self.field.pix[y, x] == 1:
                    self.matrice.setTablePixel(x, y, self.field.color[y, x])

                elif self.activeBrickPix == 1:
                    self.matrice.setTablePixel(x, y, self.activeBrick.color)

                else:
                    self.matrice.setTablePixel(x, y, self.matrice.BLACK)

        self.matrice.showPixels()
        #print("printField_end")

    def moveFieldDownOne(self, startRow):
        #print("moveFieldDownOne")
        if startRow == 0:
            # Topmost row has nothing on top to move...
            #print("moveFieldDownOne_end")
            return

        for y in range(startRow - 1, 0, -1):
            # for (y = startRow - 1 y > 0 y--)
            for x in range(self.matrice.FIELD_WIDTH):
                self.field.pix[y + 1, x] = self.field.pix[y, x]
                self.field.color[y + 1, x] = self.field.color[y, x]

        #print("moveFieldDownOne_end")


    def rotateActiveBrick(self):
        tmpBrick = Brick()
        #Copy active brick pix array to temporary pix array
        for y in range(self.MAX_BRICK_SIZE):
            for x in range(self.MAX_BRICK_SIZE):
                tmpBrick.pix[x][y] = self.activeBrick.pix[x][y]

        tmpBrick.xpos = self.activeBrick.xpos
        tmpBrick.ypos = self.activeBrick.ypos
        tmpBrick.siz = self.activeBrick.siz
        
        #Depending on size of the active brick, we will rotate differently
        if self.activeBrick.siz == 3:
            #Perform rotation around center pix
            tmpBrick.pix[0][0] = self.activeBrick.pix[0][2]
            tmpBrick.pix[0][1] = self.activeBrick.pix[1][2]
            tmpBrick.pix[0][2] = self.activeBrick.pix[2][2]
            tmpBrick.pix[1][0] = self.activeBrick.pix[0][1]
            tmpBrick.pix[1][1] = self.activeBrick.pix[1][1]
            tmpBrick.pix[1][2] = self.activeBrick.pix[2][1]
            tmpBrick.pix[2][0] = self.activeBrick.pix[0][0]
            tmpBrick.pix[2][1] = self.activeBrick.pix[1][0]
            tmpBrick.pix[2][2] = self.activeBrick.pix[2][0]
            #Keep other parts of temporary block clear
            tmpBrick.pix[0][3] = 0
            tmpBrick.pix[1][3] = 0
            tmpBrick.pix[2][3] = 0
            tmpBrick.pix[3][3] = 0
            tmpBrick.pix[3][2] = 0
            tmpBrick.pix[3][1] = 0
            tmpBrick.pix[3][0] = 0
            
        elif self.activeBrick.siz == 4:
            #Perform rotation around center "cross"
            tmpBrick.pix[0][0] = self.activeBrick.pix[0][3]
            tmpBrick.pix[0][1] = self.activeBrick.pix[1][3]
            tmpBrick.pix[0][2] = self.activeBrick.pix[2][3]
            tmpBrick.pix[0][3] = self.activeBrick.pix[3][3]
            tmpBrick.pix[1][0] = self.activeBrick.pix[0][2]
            tmpBrick.pix[1][1] = self.activeBrick.pix[1][2]
            tmpBrick.pix[1][2] = self.activeBrick.pix[2][2]
            tmpBrick.pix[1][3] = self.activeBrick.pix[3][2]
            tmpBrick.pix[2][0] = self.activeBrick.pix[0][1]
            tmpBrick.pix[2][1] = self.activeBrick.pix[1][1]
            tmpBrick.pix[2][2] = self.activeBrick.pix[2][1]
            tmpBrick.pix[2][3] = self.activeBrick.pix[3][1]
            tmpBrick.pix[3][0] = self.activeBrick.pix[0][0]
            tmpBrick.pix[3][1] = self.activeBrick.pix[1][0]
            tmpBrick.pix[3][2] = self.activeBrick.pix[2][0]
            tmpBrick.pix[3][3] = self.activeBrick.pix[3][0]
        else:
            print("Brick size error")
        
        
        #Now validate by checking collision.
        #Collision possibilities:
        #      -Brick now sticks outside field
        #      -Brick now sticks inside fixed bricks of field
        #In case of collision, we just discard the rotated temporary brick
        if not self.checkSidesCollision(tmpBrick) and not self.checkFieldCollision(tmpBrick):
            #Copy temporary brick pix array to active pix array
            for y in range(self.MAX_BRICK_SIZE):
                for x in range(self.MAX_BRICK_SIZE):
                    self.activeBrick.pix[x][y] = tmpBrick.pix[x][y]