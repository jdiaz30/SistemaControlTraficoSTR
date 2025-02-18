import asyncio
import subprocess
import sys
import semaforo
from simulacion_sensor import generar_data_trafico
from logica_trafico import calcular_tiempo_verde, store_data_trafico  

subprocess.Popen([sys.executable, "semaforo.py"])

async def control_semaforo():
    while True:
        data_trafico = generar_data_trafico()
        tiempo_verde = calcular_tiempo_verde(data_trafico["vehicle_count"])  
        store_data_trafico(data_trafico["interseccion"], data_trafico["vehicle_count"], tiempo_verde)

        print(f" Intersección: {data_trafico['interseccion']} |  Vehículos: {data_trafico['vehicle_count']} |  Verde por: {tiempo_verde} segundos")

        await asyncio.sleep(5) 

if __name__ == "__main__":
    asyncio.run(control_semaforo())  
