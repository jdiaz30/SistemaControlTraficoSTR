import sqlite3

def setup_database():
    conn = sqlite3.connect("data_trafico.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_trafico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        interseccion TEXT,
        vehicle_count INTEGER,
        tiempo_verde INTEGER,
        timestamp TEXT
    )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
