from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_latest_data():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''SELECT temperature, humidity, pressure, altitude, wind_direction, 
                        wind_speed, precipitation, soil_humidity, timestamp
                 FROM weather ORDER BY id DESC LIMIT 1''')
    data = c.fetchone()
    conn.close()
    return data

def get_last_10_data(variable):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute(f'''SELECT {variable}, timestamp FROM weather ORDER BY id DESC LIMIT 10''')
    data = c.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/latest', methods=['GET'])
def latest():
    data = get_latest_data()
    if data:
        (temperature, humidity, pressure, altitude, wind_direction, 
         wind_speed, precipitation, soil_humidity, timestamp) = data
    else:
        temperature = humidity = pressure = altitude = wind_direction = "N/A"
        wind_speed = precipitation = soil_humidity = timestamp = "N/A"
    return jsonify({
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure,
        "altitude": altitude,
        "wind_direction": wind_direction,
        "wind_speed": wind_speed,
        "precipitation": precipitation,
        "soil_humidity": soil_humidity,
        "timestamp": timestamp
    })

@app.route('/last10/<variable>', methods=['GET'])
def last_10(variable):
    data = get_last_10_data(variable)
    return jsonify(data)

@app.route('/receive', methods=['POST'])
def receive():
    data = request.form['data']
    (temperature, humidity, pressure, altitude, wind_direction, 
     wind_speed, precipitation, soil_humidity) = data.split(';')
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO weather 
                 (temperature, humidity, pressure, altitude, wind_direction, 
                  wind_speed, precipitation, soil_humidity)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
              (float(temperature), float(humidity), float(pressure), float(altitude), 
               float(wind_direction), float(wind_speed), float(precipitation), float(soil_humidity)))
    conn.commit()
    conn.close()
    return 'Data received and stored'

if __name__ == "__main__":
    app.run(debug=True)
