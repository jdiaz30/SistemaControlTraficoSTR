import asyncio
import random

# Lista de intersecciones en las que se simulará el tráfico
intersecciones = ["Av. 27 de Febrero", "Av. Charles de Gaulle", "Av. Winston Churchill", "Av. Roberto Pastoriza"]

async def generar_data_trafico(id_sensor):
    """
    Simula la generación de datos de tráfico para una intersección específica.

    Args:
        id_sensor (int): Identificador único del sensor de tráfico.

    La función ejecuta un bucle infinito que genera datos aleatorios de tráfico,
    incluyendo la intersección y la cantidad de vehículos detectados. Luego, 
    espera un tiempo aleatorio antes de la siguiente medición.
    """
    while True:
        try:
            data = {
                "interseccion": random.choice(intersecciones),  # Selecciona una intersección aleatoria
                "vehicle_count": random.randint(0, 50),  # Número aleatorio de vehículos detectados
            }
            print(f"✅ Sensor {id_sensor}: {data}")  # Imprime la información generada
        except Exception as e:
            print(f"❌ Error en el sensor {id_sensor}: {e}")

        await asyncio.sleep(random.randint(3, 7))  # Espera entre 3 y 7 segundos antes de la próxima medición

async def main():
    """
    Crea y ejecuta múltiples sensores concurrentemente.
    
    Cada sensor simula la captura de datos de tráfico en una intersección distinta.
    """
    try:
        numero_sensores = len(intersecciones)  # Determina la cantidad de sensores según la lista de intersecciones
        tareas = [generar_data_trafico(i+1) for i in range(numero_sensores)]  # Crea tareas asíncronas para cada sensor
        await asyncio.gather(*tareas)  # Ejecuta todas las tareas en paralelo

    except Exception as e:
        print(f"❌ Error en la ejecución de los sensores: {e}")

if __name__ == "__main__":
    # Ejecuta la simulación de tráfico si el script se ejecuta directamente
    asyncio.run(main())
