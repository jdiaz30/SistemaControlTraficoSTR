import asyncio
import redis.asyncio as redis  # Se usa la versión moderna de Redis compatible con asyncio

# Configuración de Redis
REDIS_HOST = "localhost"  # Cambia si Redis está en otro servidor
REDIS_CHANNEL = "Semaforo"  # Canal de comunicación para publicar los estados del semáforo

async def control_semaforo():
    """
    Maneja el ciclo de un semáforo simulando el cambio de luces (verde, amarillo, rojo)
    y publicando estos cambios en Redis de forma concurrente.

    Utiliza un diccionario `semaforo` para rastrear el estado actual de la luz
    y cambia su estado en un bucle infinito con los siguientes tiempos:
    - Verde: 4 segundos (permitido el paso).
    - Amarillo: 2 segundos (precaución).
    - Rojo: 4 segundos (alto).
    
    La información se publica en Redis para que otros procesos puedan suscribirse a los cambios.
    """
    redis_client = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

    # Estado inicial del semáforo
    semaforo = {"Verde": True, "Amarillo": False, "Rojo": False}

    while True:
        print("\n---- SEMÁFORO ----")

        # Fase Verde: Permite el paso
        if semaforo["Verde"]:
            print("🚦 Semáforo en VERDE (Paso permitido)")
            await redis_client.publish(REDIS_CHANNEL, "Verde")  # Publica en Redis el estado del semáforo
            semaforo = {"Verde": False, "Amarillo": True, "Rojo": False}  # Cambia al siguiente estado
            await asyncio.sleep(4)  # Tiempo de luz verde

        # Fase Amarilla: Precaución
        elif semaforo["Amarillo"]:
            print("⚠️ Semáforo en AMARILLO (Precaución)")
            await redis_client.publish(REDIS_CHANNEL, "Amarillo")
            semaforo = {"Verde": False, "Amarillo": False, "Rojo": True}
            await asyncio.sleep(2)  # Tiempo de luz amarilla

        # Fase Roja: Alto
        elif semaforo["Rojo"]:
            print("🛑 Semáforo en ROJO (Alto)")
            await redis_client.publish(REDIS_CHANNEL, "Rojo")
            semaforo = {"Verde": True, "Amarillo": False, "Rojo": False}
            await asyncio.sleep(4)  # Tiempo de luz roja

async def main():
    """
    Función principal que inicia la simulación del semáforo de manera asíncrona.
    """
    await control_semaforo()

if __name__ == "__main__":
    # Ejecuta la función principal si el script se ejecuta directamente.
    asyncio.run(main())
