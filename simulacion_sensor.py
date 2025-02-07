import random

def generar_data_trafico():
    intersecciones = ["Avenida 27 de Febrero", "Av. Charles de Gaulle", "Av. Roberto Pastoriza", "Av. Winston Churchill"]
    return {
        "interseccion": random.choice(intersecciones),
        "vehicle_count": random.randint(0, 50),
    }