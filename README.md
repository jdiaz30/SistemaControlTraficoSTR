Sistema de Control de Semáforos Inteligentes

Descripción

Este proyecto simula un Sistema de Control de Semáforos Inteligentes utilizando programación concurrente en Python. Los semáforos ajustan su duración en función del tráfico detectado en tiempo real, optimizando el flujo vehicular en intersecciones concurridas.

El sistema se basa en la recopilación de datos de sensores de tráfico, el cálculo dinámico del tiempo de luz verde y el almacenamiento de información en una base de datos para análisis futuro.

Características principales

Simulación en tiempo real del flujo vehicular en diferentes intersecciones.

Ajuste dinámico del tiempo de luz verde en función del tráfico detectado.

Uso de programación concurrente con asyncio para manejar múltiples sensores y semáforos simultáneamente.

Almacenamiento de datos en SQLite para registrar estadísticas del tráfico.

Comunicación con Redis para sincronizar estados de los semáforos en tiempo real.

Tecnologías utilizadas

Python 3.10+

asyncio (para programación concurrente)

aiosqlite (para acceso asíncrono a SQLite)

redis.asyncio (para comunicación en tiempo real entre procesos)

Instalación y ejecución

1. Clonar el repositorio
 git clone https://github.com/jdiaz30/SistemaControlTraficoSTR.git
 cd SistemaControlTraficoSTR

 2. Crear un entorno virtual e instalar dependencias
 python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate  # En Windows
pip install -r requirements.txt

3. Iniciar la base de datos
python database.py

4. Ejecutar el sistema
python main.py


Explicación de los archivos
main.py: Coordina la ejecución del semáforo y la simulación del tráfico.
semaforo.py: Controla el cambio de luces del semáforo y publica el estado en Redis.
simulacion_sensor.py: Simula la detección de vehículos en diferentes intersecciones.
logica_trafico.py: Calcula el tiempo de luz verde en función del tráfico y almacena los datos en SQLite.
database.py: Configura la base de datos SQLite.

Funcionamiento

Se ejecutan múltiples sensores en paralelo para simular el tráfico en distintas intersecciones.

La información se procesa en tiempo real, ajustando el tiempo del semáforo según el tráfico detectado.

Los estados del semáforo se publican en Redis, permitiendo la sincronización con otros módulos del sistema.

Se almacenan los datos del tráfico en SQLite para análisis y optimización futura.


Proyecto desarrollado por Jelsy Manuel Díaz Jiménez como parte de la asignatura Ingeniería de Software en Tiempo Real en UNIBE.