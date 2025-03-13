import asyncio
import subprocess
import sys
from simulacion_sensor import generar_data_trafico
from logica_trafico import calcular_tiempo_verde, store_data_trafico  

async def iniciar_semaforo():
    """
    Inicia la simulación del semáforo ejecutándolo como un proceso independiente.

    - Usa `asyncio.create_subprocess_exec()` para ejecutar `semaforo.py` en paralelo.
    - La función `await process.wait()` permite que el proceso corra sin bloquear el resto del programa.
    - Maneja excepciones para evitar fallos si el proceso no se puede iniciar.
    """
    try:
        process = await asyncio.create_subprocess_exec(sys.executable, "semaforo.py")
        await process.wait()  # Espera a que el proceso termine (no bloquea el hilo principal)
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo `semaforo.py`. Verifica que el script existe.")
    except Exception as e:
        print(f"❌ Error inesperado al iniciar el semáforo: {e}")

async def control_semaforo():
    """
    Gestiona la simulación del tráfico en múltiples intersecciones.

    - Recopila datos de tráfico en paralelo desde varios sensores.
    - Calcula el tiempo de luz verde en función del número de vehículos detectados.
    - Almacena los datos en la base de datos de manera asíncrona.
    - Maneja errores en la obtención y procesamiento de los datos.
    """
    try:
        while True:
            sensor_ids = [1, 2, 3, 4]  # Lista de sensores simulados (uno por intersección)
            tareas_sensores = [generar_data_trafico(sensor_id) for sensor_id in sensor_ids]
            
            # Ejecuta todas las tareas de sensores en paralelo y espera los resultados
            try:
                datos_trafico = await asyncio.gather(*tareas_sensores)
            except Exception as e:
                print(f"❌ Error en la obtención de datos de sensores: {e}")
                continue  # Si hay un error, continúa con la siguiente iteración

            # Procesa los datos de cada sensor de forma independiente
            for data_trafico in datos_trafico:
                try:
                    tiempo_verde = await calcular_tiempo_verde(data_trafico["vehicle_count"])  
                    await store_data_trafico(data_trafico["interseccion"], data_trafico["vehicle_count"], tiempo_verde)
                    print(f"✅ Intersección: {data_trafico['interseccion']} | Vehículos: {data_trafico['vehicle_count']} | Verde por: {tiempo_verde} segundos")
                except Exception as e:
                    print(f"❌ Error procesando datos de tráfico para {data_trafico['interseccion']}: {e}")

            await asyncio.sleep(5)  # Pausa antes de la siguiente iteración de lectura de sensores

    except Exception as e:
        print(f"❌ Error inesperado en la simulación del tráfico: {e}")

async def main():
    """
    Coordina la ejecución del sistema de control de tráfico.

    - Ejecuta el semáforo en paralelo al procesamiento de datos de tráfico.
    - Usa `asyncio.create_task()` para manejar ambas tareas sin bloqueo.
    - `asyncio.gather()` asegura que ambas tareas corran simultáneamente.
    - Maneja errores en la ejecución de las tareas principales.
    """
    try:
        tarea_semaforo = asyncio.create_task(iniciar_semaforo())  # Ejecuta el semáforo en paralelo
        tarea_control_trafico = asyncio.create_task(control_semaforo())  # Ejecuta la simulación de sensores

        await asyncio.gather(tarea_semaforo, tarea_control_trafico)  # Espera a que ambas tareas terminen
    except Exception as e:
        print(f"❌ Error crítico en la ejecución del sistema: {e}")

if __name__ == "__main__":
    # Ejecuta el programa principal si el script se ejecuta directamente.
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Simulación detenida manualmente.")
    except Exception as e:
        print(f"❌ Error inesperado al ejecutar el programa: {e}")
