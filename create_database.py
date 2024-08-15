import sqlite3

def init_db():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temperature REAL,
                    wind_speed INTEGER,
                    wind_direction TEXT,
                    humidity REAL,
                    precipitation REAL
                )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
