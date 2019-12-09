from Matrice import Matrice
import Tetris

class Menu:

    def __init__(self):
        self.matrice = Matrice()

    def afficher_menu_back(self):
        self.matrice.initMatrice()
        self.matrice.initControl()
        stop = True

        while stop:
            self.matrice.afficher_heure()
            curControl = self.matrice.control()
            if curControl == 256:
                stop = False

            if curControl == Matrice.BTN_START:
                self.afficher_tetris()

    def afficher_menu(self):
        self.matrice.initMatrice()
        self.matrice.initControl()
        stop = True

        while stop:
            self.matrice.afficher_heure()
            curControl = self.matrice.control()
            if curControl == 256:
                stop = False

            if curControl == Matrice.BTN_START:
                self.afficher_tetris()


    def afficher_tetris(self):
        tetris =  Tetris.Tetris()
        tetris.tetrisInit()
        tetris.runTetris()


