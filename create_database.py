import sqlite3

def init_db():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    # Añadir la columna timestamp a la tabla weather
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temperature REAL,
                    humidity REAL,
                    pressure REAL,
                    altitude REAL,
                    wind_direction REAL,
                    wind_speed REAL,
                    precipitation REAL,
                    soil_humidity REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
