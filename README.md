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

Luego crear la base de datos

~~~
python create_database.py
~~~

Y por ultimo activa la web
~~~
python app.py
~~~