#Florian DUCORD
#florian.developpement@gmail.com
#https://github.com/pingouin84/Mirror_Led.git

import sys
import config
if len(sys.argv) > 1:
        config.DEBUG = sys.argv[1]=="debug"

import Menu
import Tetris
import Matrice
import time


def main():
        menu = Menu.Menu()
        menu.afficher_menu()

        #tetris =  Tetris.Tetris()
        #tetris.tetrisInit()
        #tetris.runTetris()


def test_matrice():
        matrice = Matrice.Matrice()
        matrice.initMatrice()
        for x in range(12):
                for y in range(20):
                        matrice.setTablePixel(x, y, matrice.GREEN)

    #matrice.setTablePixel(0, 0, matrice.GREEN)
    #matrice.setTablePixel(0, 0, matrice.GREEN)
    #matrice.setTablePixel(0, 0, matrice.GREEN)
    #matrice.setTablePixel(0, 0, matrice.GREEN)

    #matrice.setTablePixel(0, 19, matrice.GREEN)
    #matrice.setTablePixel(11, 19, matrice.GREEN)
    #matrice.setTablePixel(11, 0, matrice.GREEN)
        matrice.showPixels()
        time.sleep(3)

        while True:
                matrice.setTablePixel(5, 9, matrice.BLUE)
                matrice.setTablePixel(5, 10, matrice.BLUE)
                matrice.setTablePixel(6, 10, matrice.BLUE)
                matrice.setTablePixel(6, 9, matrice.BLUE)
                matrice.showPixels()
                time.sleep(1)
                matrice.setTablePixel(5, 9, matrice.GREEN)
                matrice.setTablePixel(5, 10, matrice.GREEN)
                matrice.setTablePixel(6, 10, matrice.GREEN)
                matrice.setTablePixel(6, 9, matrice.GREEN)
                matrice.showPixels()
                time.sleep(1)

main()
#test_matrice()