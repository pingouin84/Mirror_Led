import Tetris
import Matrice
import time

def main():
        tetris =  Tetris.Tetris()
        tetris.tetrisInit()
        tetris.runTetris()


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