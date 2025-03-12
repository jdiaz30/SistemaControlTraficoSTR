import asyncio
import aiosqlite
from datetime import datetime

async def calcular_tiempo_verde(vehicle_count):
    """
    Calcula el tiempo que un semáforo debe permanecer en verde según la cantidad de vehículos detectados.

    Args:
        vehicle_count (int): Número de vehículos detectados en la intersección.

    Returns:
        int: Tiempo de luz verde en segundos.

    La fórmula utilizada es:
    - Base de 10 segundos.
    - Se agregan segundos extra dependiendo del número de vehículos (1 segundo extra por cada 5 vehículos, hasta un máximo de 15 segundos adicionales).
    """
    base_time = 10
    extra_time = min(vehicle_count // 5, 15)  # Máximo 15 segundos adicionales
    tiempo_verde = base_time + extra_time
    print(f"Tiempo de luz verde calculado: {tiempo_verde} segundos para {vehicle_count} vehículos.")
    return tiempo_verde

async def store_data_trafico(interseccion, vehicle_count, tiempo_verde):
    """
    Almacena los datos del tráfico en la base de datos SQLite de manera asíncrona.

    Args:
        interseccion (str): Nombre de la intersección.
        vehicle_count (int): Número de vehículos detectados.
        tiempo_verde (int): Tiempo asignado para la luz verde en la intersección.

    La información se guarda en la tabla `data_trafico` de la base de datos `data_trafico.db`,
    registrando el momento exacto en que se almacenaron los datos.
    """
    async with aiosqlite.connect("data_trafico.db") as conn:
        await conn.execute("""
            INSERT INTO data_trafico (interseccion, vehicle_count, tiempo_verde, timestamp)
            VALUES (?, ?, ?, ?)
        """, (interseccion, vehicle_count, tiempo_verde, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        await conn.commit()
        print(f"Datos almacenados en la BD: {interseccion}, {vehicle_count} vehículos, {tiempo_verde} seg de luz verde.")

async def procesar_trafico(interseccion, vehicle_count):
    """
    Procesa los datos de tráfico de una intersección específica:
    - Calcula el tiempo de luz verde.
    - Guarda los datos en la base de datos.

    Args:
        interseccion (str): Nombre de la intersección.
        vehicle_count (int): Cantidad de vehículos detectados.
    """
    tiempo_verde = await calcular_tiempo_verde(vehicle_count)
    await store_data_trafico(interseccion, vehicle_count, tiempo_verde)

if __name__ == "__main__":
    # Simulación de prueba: procesamiento de tráfico en la intersección "Avenida 27 de Febrero" con 35 vehículos detectados.
    asyncio.run(procesar_trafico("Avenida 27 de Febrero", 35))
