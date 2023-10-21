from dataclasses import dataclass
from Nerdle.modelo.claseEcuacion import Ecuacion
from Nerdle.modelo.retroalimentacion import Retroalimentacion

@dataclass
class Jugador:
    nombre_jugador: str = ""
    correo_jugador: str = ""


class Nerdle(Ecuacion):
    def __init__(self):
        super().__init__()
        self.retroalimentacion = None
        self.nombre_jugador: str = ""
        self.correo_jugador: str = ""
        self.intentos: int = 6

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
        ecuacion: list = super().generar_ecuacion()
        self.retroalimentacion: Retroalimentacion = Retroalimentacion(ecuacion)
        print(f"{'_':_^30}")
        titulo = "COMIENZA A JUGAR: "
        print(f"\n{titulo.center(30)}")
        print(f"La ecuacion generada es: = {ecuacion}")

    """El metodo retroalimentar retorna una lista con los colores en hexadecimal segun lo que puso el usuario
    asi solo se tiene que tomar el color y cambiar cada casilla segun la posicion de la lista.
    Este metodo debe llamarse cada que se de click en ingresar y se le debe pasar como argumento una lista que contenga
    los datos que el usuario ingreso."""

    def retroalimentar(self, ingreso: list):
        lista_de_colores = self.retroalimentacion.verificar_posiciones(ingreso)
        return lista_de_colores



N = Nerdle()
N.iniciar_nuevo_juego()

