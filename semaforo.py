import asyncio
import redis

# Conexión a Redis
REDIS_HOST = "localhost"  # Cambia esto si Redis está en otro servidor
REDIS_CHANNEL = "Semaforo"

# Inicializar Redis
redis_client = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

# Estados del semáforo
semaforo = {"Verde": True, "Amarillo": False, "Rojo": False}

async def control_semaforo():
    while True:
        print("\n---- SEMÁFORO ----")

        # Fase Verde
        if semaforo["Verde"]:
            print("🚦 Semáforo en VERDE (Paso permitido)")
            redis_client.publish(REDIS_CHANNEL, "Verde")  
            semaforo["Verde"], semaforo["Amarillo"], semaforo["Rojo"] = False, True, False
            await asyncio.sleep(4)  
        
        # Fase Amarilla
        elif semaforo["Amarillo"]:
            print("⚠️ Semáforo en AMARILLO (Precaución)")
            redis_client.publish(REDIS_CHANNEL, "Amarillo")  
            semaforo["Verde"], semaforo["Amarillo"], semaforo["Rojo"] = False, False, True
            await asyncio.sleep(2)  

        # Fase Roja
        elif semaforo["Rojo"]:
            print("🛑 Semáforo en ROJO (Alto)")
            redis_client.publish(REDIS_CHANNEL, "Rojo") 
            semaforo["Verde"], semaforo["Amarillo"], semaforo["Rojo"] = True, False, False
            await asyncio.sleep(4)  

if __name__ == "__main__":
    asyncio.run(control_semaforo())
