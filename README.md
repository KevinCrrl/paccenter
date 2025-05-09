# PACCENTER

Ayudante para hacer actualizaciones completas y eliminando residuos de caché en el gestor de paquetes pacman (usado en sistemas basados en Arch Linux).

## Modo Reparación

Este modo elimina el bloqueo de las bases de datos (archivo /var/lib/pacman/db.lck) y sincroniza las bases de datos para luego hacer una actualización del sistema.

## MODO GRÁFICO

El modo gráfico está pensado para los que están poco acostumbrados a la terminal, está hecho en customtkinter y pide la contraseña usando también una interfaz gráfica con pkexec.

## USO Y EJECUCCIÓN

PACCENTER está pensado para ejecutarse de manera independiente por lo que debería darle permisos para que python lo ejecute sin necesidad de ser llamado:

Ejecutando el comando: chmod +x paccenter.py

Así ya se puede ejecutar usando: ./paccenter argumento

## Requerimientos

pygilet: Se usa para crear títulos en ascii para el modo terminal, se instala con "pacman -S python-pyfiglet"

customtkinter: Se usa para construir la interfaz gráfica, se instala con "yay -S customtkinter" (yay se compila clonando su repositorio), además en instalaciones de Python en Linux no suele venir la librería tkinter que es ecesaria para el funcionamiento de customtkinter, se instala con "pacman -S tk"
