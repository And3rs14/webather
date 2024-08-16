## Clona el repositorio
~~~
git clone https://github.com/And3rs14/webather.git
~~~

## Crear tu ambiente
Primero crea tu ambiente de anaconda

~~~
conda create -n webather python=3.8
~~~

~~~
conda activate webather
~~~

Y una vez dentro de tu ambiente instala los paquetes necesarios

~~~~
pip install -r requirements.txt
~~~~

## Levantar la web
Luego crear la base de datos

~~~
python create_database.py
~~~

Y por ultimo activa la web
~~~
python app.py
~~~

## Enviar datos
Para enviar los datos por ip, cambiar la ip local por la pública
    
    temperature; humidity; pressure; altitude; wind_direction; wind_speed; precipitation; soil_humidity
    22;55;101325;150;180;15;3.5;250

~~~
curl -X POST -d "data=22;55;101325;150;180;15;3.5;250" http://127.0.0.1:5000/receive
~~~