import sqlite3

class Persistencia:

    def __init__(self):
        self.db = "juego.db"

    def crear_tablas(self):
        conexion = sqlite3.connect(self.db)
        cursor = conexion.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS partidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_jugador TEXT,
            nivel_actual INTEGER,
            vida INTEGER,
            vida_maxima INTEGER,
            fuerza INTEGER,
            ataque INTEGER
        )
        """)

        conexion.commit()
        conexion.close()

    def guardar_partida(self, nombre, nivel, vida, vida_maxima, fuerza, ataque):
        conexion = sqlite3.connect(self.db)
        cursor = conexion.cursor()

        cursor.execute("""
        INSERT INTO partidas
        (nombre_jugador, nivel_actual, vida, vida_maxima, fuerza, ataque)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, nivel, vida, vida_maxima, fuerza, ataque))

        conexion.commit()
        id_partida = cursor.lastrowid
        conexion.close()
        return id_partida

    def actualizar_partida(self, id_partida, nivel, vida, vida_maxima, fuerza, ataque):
        conexion = sqlite3.connect(self.db)
        cursor = conexion.cursor()

        cursor.execute("""
        UPDATE partidas
        SET nivel_actual=?, vida=?, vida_maxima=?, fuerza=?, ataque=?
        WHERE id=?
        """, (nivel, vida, vida_maxima, fuerza, ataque, id_partida))

        conexion.commit()
        conexion.close()

    def cargar_ultima_partida(self):
        conexion = sqlite3.connect(self.db)
        cursor = conexion.cursor()

        cursor.execute("""
        SELECT * FROM partidas
        ORDER BY id DESC
        LIMIT 1
        """)

        fila = cursor.fetchone()
        conexion.close()
        return fila