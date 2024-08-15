from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_latest_data():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''SELECT temperature, wind_speed, wind_direction, humidity, precipitation 
                 FROM weather ORDER BY id DESC LIMIT 1''')
    data = c.fetchone()
    conn.close()
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/latest', methods=['GET'])
def latest():
    data = get_latest_data()
    if data:
        temperature, wind_speed, wind_direction, humidity, precipitation = data
    else:
        temperature = wind_speed = wind_direction = humidity = precipitation = "N/A"
    return jsonify({
        "temperature": temperature,
        "wind_speed": wind_speed,
        "wind_direction": wind_direction,
        "humidity": humidity,
        "precipitation": precipitation
    })

@app.route('/receive', methods=['POST'])
def receive():
    data = request.form['data']
    temperature, wind_speed, wind_direction, humidity, precipitation = data.split(';')
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO weather (temperature, wind_speed, wind_direction, humidity, precipitation)
                 VALUES (?, ?, ?, ?, ?)''', (float(temperature), int(wind_speed), wind_direction, float(humidity), float(precipitation)))
    conn.commit()
    conn.close()
    return 'Data received and stored'

if __name__ == "__main__":
    app.run(debug=True)
