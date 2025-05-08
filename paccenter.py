#!/usr/bin/python3

import pyfiglet
from shell import shell
import interfaz
import sys

def printlet(texto):
    print(pyfiglet.figlet_format(texto, "slant"))

def upclean():
    print("Corriendo pacman...")
    shell("sudo pacman -Syu --noconfirm")
    print("Eliminando paquetes residuales...")
    shell("sudo pacman -Scc --noconfirm")
    print("Sistema actualizado correctamente.")

def reparacion():
    printlet("MODO REPARACION")
    print("Eliminando archivo db.lck")
    shell("sudo rm /var/lib/pacman/db.lck")
    print("Sincronizando bases de datos...")
    shell("sudo pacman -Syy")
    print("Bases de datos reparadas...")
    print("Intentando actualizar...")
    upclean()

arg = sys.argv[1]

if arg == "up-clean":
    printlet("ACTUALIZADOR COMUN")
    upclean()
elif arg == "reparacion":
    reparacion()
elif arg == "grafico":
    interfaz.interfaz()
else:
    print("""Comando incorrecto, use el comando con el argumento up-clean para hacer una actualización normal y eliminar residuos de instaladores,
con el argumento reparacion para recuperar las bases de datos bloqueadas
y con el argumento grafico para usar el ayudante con GUI.""")