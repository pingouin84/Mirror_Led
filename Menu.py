from Matrice import Matrice
import Tetris

class Menu:

    def __init__(self):
        self.matrice = Matrice()

    def afficher_menu(self):
        self.matrice.initMatrice()
        self.matrice.initControl()
        self.stop = True

        while self.stop:
            self.matrice.afficher_heure()
            curControl = self.matrice.control()
            if curControl == 256:
                self.stop = False

            if curControl == Matrice.BTN_START:
                tetris =  Tetris.Tetris()
                tetris.tetrisInit()
                tetris.runTetris()


