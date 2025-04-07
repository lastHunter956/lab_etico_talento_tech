

# maquinas
![Texto alternativo]("./imagenes/Pasted-image-20241019070352.png")

envio de archivo malicioso:

![Texto alternativo 2]("./imagenes/Pasted-image-20241019073716.png")

se uso un envio por ssh para asumir un ataque de phishing

![Texto alternativo 2]("./imagenes/Pasted-image-20241019074909.png")
se ejecuta el script y efectivamente si se puede conectar y colocar comandos

# segundo paso

sabiendo que funciona ahora vamos a subirle el nivel, para lo anterior vamos a ofuscar el codigo, lo convertimos en un . exe y en ves de conectar una red local conectamos a un servidor propio!!
tenemos el codigo (code_no_ofuscacion.py) primero lo ofuscamos lo mas posible quedando, para que irreconocible por el antivirus (code_ofuscacion.py)

después lo convertimos en un .exe

```bach
cd ruta\a\tu\carpeta
pyinstaller --onefile code_ofuscacion.py

```

después con setoolkit metemos ese .exe en el pdf

# que se puede hacer
## Explorar datos confidenciales
- para esto nos conectamos al servidor, escuchamos en el puerto donde 444 donde esta la conexión entre estas dos maquinas

![Texto alternativo 4]("/imagenes/Pasted-image-20241019090710.png")

navegamos y localizamos 

![Texto alternativo 5]("/imagenes/Pasted-image-20241019091026.png")

vemos su contenido con el comando cat

![Texto alternativo 6]("/imagenes/Pasted-image-20241019091117.png")

## conectarse a la base de datos

![Texto alternativo 7]("/imagenes/Pasted-image-20241019092246.png")

con el acceso a la base de datos podemos obtener todo tipo de información como como los nombres y las tablas también de borrar las mismas y insertar datos.

## finalizar servicios
muy util si deseamos finalizar procesos tumbar bases de datos o elementos que se ejecuten el servidor, ejemplo:

![Texto alternativo 7]("/imagenes/Pasted-image-20241019092916.png")

nos conectamos nuevamente y finalizamos el servicio

