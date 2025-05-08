import subprocess

def shell(comando):
    subprocess.run(comando, shell=True)