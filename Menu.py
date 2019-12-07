from Matrice import Matrice

class Menu:

    def __init__(self):
        self.matrice = Matrice()

    def afficher_menu(self):
        self.matrice.initMatrice()
        self.matrice.initControl()
        self.tetrisRunning = True
        
        while self.tetrisRunning:
            self.matrice.afficher_heure()
            curControl = self.matrice.control()
            if curControl == 256:
                self.tetrisRunning = False


