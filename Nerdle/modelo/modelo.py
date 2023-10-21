from dataclasses import dataclass
from Nerdle.modelo.claseEcuacion import Ecuacion


@dataclass
class Jugador:
    nombre_jugador: str = ""
    correo_jugador: str = ""


class Nerdle(Ecuacion):
    def __init__(self):
        super().__init__()
        self.nombre_jugador: str = ""
        self.correo_jugador: str = ""

    def registrar_nombre_jugador(self, nombre_jugador: str) -> str:
        self.nombre_jugador = nombre_jugador
        return self.nombre_jugador

    def registrar_correo_jugador(self, correo_jugador: str) -> str:
        self.correo_jugador = correo_jugador
        return self.correo_jugador

    """ Se borra el metodo juego nuevo pues no necesitamos mostrar la tabla por consola"""

    """
    El metodo iniciar nuevo juego es el que debe ser llamado cuando el jugador de click en jugar, este genera y retorna
    la ecuacion, y a su vez la imprime en consola
    """

    def iniciar_nuevo_juego(self):
        print(f"{'_':_^30}")
        titulo = "COMIENZA A JUGAR: "
        print(f"\n{titulo.center(30)}")
        print(f"La ecuacion generada es: = {super().generar_ecuacion()}")


N = Nerdle()
N.iniciar_nuevo_juego()

