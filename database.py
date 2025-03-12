import aiosqlite
import asyncio

async def setup_database():
    """
    Configura la base de datos SQLite de manera asíncrona.

    - Crea la base de datos `data_trafico.db` si no existe.
    - Define la tabla `data_trafico` para almacenar información sobre el tráfico vehicular.
    - La tabla contiene los siguientes campos:
        - `id`: Identificador único (clave primaria, autoincremental).
        - `interseccion`: Nombre de la intersección donde se capturaron los datos.
        - `vehicle_count`: Número de vehículos detectados en la intersección.
        - `tiempo_verde`: Tiempo en segundos que el semáforo estuvo en verde.
        - `timestamp`: Marca de tiempo de cuándo se almacenaron los datos.

    La función usa `aiosqlite` para permitir acceso asíncrono a la base de datos,
    evitando bloqueos en otras operaciones concurrentes del sistema.
    """
    async with aiosqlite.connect("data_trafico.db") as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS data_trafico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                interseccion TEXT,
                vehicle_count INTEGER,
                tiempo_verde INTEGER,
                timestamp TEXT
            )
        """)
        await conn.commit()  # Guarda los cambios en la base de datos
        print("Base de datos inicializada correctamente.")  # Mensaje de confirmación

if __name__ == "__main__":
    # Ejecuta la configuración de la base de datos si el script se ejecuta directamente
    asyncio.run(setup_database())
