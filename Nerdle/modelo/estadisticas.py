import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class Estadisticas:

    def __init__(self):
        self.datos = ["partidas_perdidas", "partidas_ganadas",
                      "ganadas en un intento",
                      "ganadas en 2 intentos",
                      "ganadas en 3 intentos",
                      "ganadas en 4 intentos",
                      "ganadas en mas de 5 intentos"]

        self.numeros = [0, 0, 0, 0, 0, 0, 0]

    def mostrar_grafica(self):
        """
        Funcion tomada de
        https://stackoverflow.com/questions/73745245/error-using-matplotlib-in-pycharm-has-no-attribute-figurecanvas
        """
        fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
        ax.bar(self.datos, self.numeros)
        plt.show()

