from subprocess import run

def shell(comando):
    run(comando, shell=True) # Aquí sí se usa shell=True porque es para comandos que no implican entradas, solo comandos que YO defino dentro del proyecto