import sqlite3

def init_db():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temperature REAL,              -- Grados Celsius (°C)
                    humidity REAL,                 -- Porcentaje de humedad relativa (%)
                    pressure REAL,                 -- Pascales (Pa)
                    altitude REAL,                 -- Metros
                    wind_direction INTEGER,        -- Grados (°)
                    wind_speed REAL,               -- Kilómetros por hora (kph)
                    precipitation REAL,            -- Milímetros (mm)
                    soil_humidity REAL             -- Valor analógico sin unidad específica
                )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
