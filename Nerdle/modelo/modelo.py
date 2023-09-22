from dataclasses import dataclass

@dataclass
class Jugador:
    nombre_jugador: str = ""
    correo_jugador: str = ""


class Nerdle:
    def __init__(self):
        self.nombre_jugador: str = ""
        self.correo_jugador: str = ""

    def registrar_nombre_jugador(self, nombre_jugador: str) -> str:
        self.nombre_jugador = nombre_jugador
        return self.nombre_jugador

    def registrar_correo_jugador(self, correo_jugador: str) -> str:
        self.correo_jugador = correo_jugador
        return self.correo_jugador

    def iniciar_juego(self):
        filas: int = 6
        columnas: int = 8
        tablero = [[" " for _ in range(columnas)] for _ in range(filas)]
        for fila in tablero:
            print(" | ".join(fila))
            print("-" * 31)
        return tablero
