#Florian DUCORD
#florian.developpement@gmail.com
#https://github.com/pingouin84/Mirror_Led.git

from Matrice import Matrice
import Tetris

class Menu:

    def __init__(self):
        self.matrice = Matrice()
        self.matrice.initMatrice()

    def afficher_menu_back(self):
        self.matrice.initControl()
        stop = True

        while stop:
            self.matrice.afficher_heure()
            curControl = self.matrice.control()
            if curControl == 256:
                stop = False

            if curControl == Matrice.BTN_START:
                self.lancer_tetris()

    def afficher_veille(self):
        self.matrice.initControl()

        stop = True
        while stop:
            self.matrice.afficher_heure()
            curControl = self.matrice.control()
            if curControl == Matrice.BTN_START:
                self.afficher_menu()
            elif curControl == Matrice.BTN_KILL:
                stop = False

    def afficher_menu(self):
        stop = True
        index_menu = 0

        while stop:
            if index_menu == 0:
                self.matrice.afficher_image("data/menu/tetris.gif")
            elif index_menu == 1:
                self.matrice.afficher_image("data/menu/snake.gif")
            elif index_menu == 2:
                self.matrice.afficher_image("data/menu/pong.gif")

            curControl = self.matrice.control()
            if curControl == Matrice.BTN_KILL:
                stop = False
            elif curControl == Matrice.BTN_LEFT:
                if index_menu == 0:
                    index_menu = 2
                else:
                    index_menu -=1
            elif curControl == Matrice.BTN_RIGHT:
                if index_menu == 2:
                    index_menu = 0
                else:
                    index_menu +=1
            elif curControl == Matrice.BTN_START:
                if index_menu == 0:
                    self.lancer_tetris()
          
    def lancer_tetris(self):
        tetris =  Tetris.Tetris(self.matrice)
        tetris.tetrisInit()
        tetris.runTetris()


