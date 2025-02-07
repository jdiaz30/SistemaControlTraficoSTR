from datetime import datetime
import sqlite3

def calcular_tiempo_verde(vehicle_count):
    base_time = 10
    extra_time = min(vehicle_count // 5, 15)
    return base_time + extra_time

def store_data_trafico(interseccion, vehicle_count, tiempo_verde):  
    conn = sqlite3.connect("data_trafico.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO data_trafico (interseccion, vehicle_count, tiempo_verde, timestamp)
    VALUES (?, ?, ?, ?)
    """, (interseccion, vehicle_count, tiempo_verde, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
