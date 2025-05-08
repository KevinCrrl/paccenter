import customtkinter as tk
from shell import shell

def interfaz():
    root = tk.CTk()
    root.title("paccenter")
    root.geometry("500x300")

    def act():
        shell("pkexec pacman -Syu --noconfirm")
        shell("pkexec pacman -Scc --noconfirm")
        texto1 = tk.CTkLabel(root, text="Actualización finalizada.")
        texto1.pack()

    def rep():
        shell("pkexec rm /var/lib/pacman/db.lck")
        shell("pkexec pacman -Syy")
        texto1 = tk.CTkLabel(root, text="Reparación finalizada.")
        texto1.pack()

    def inst():
        paquete = entrada1.get()
        shell(f"pkexec pacman -S {paquete} --noconfirm")
        texto1 = tk.CTkLabel(root, text="Paquete instalado.")
        texto1.pack()

    aclaracion = tk.CTkLabel(root, text="En las opciones actualizar y reparar se pide la contraseña dos veces.")
    aclaracion.pack(pady=10)

    texto = tk.CTkLabel(root, text="Ayudante gráfico de paccenter.")
    texto.pack

    boton1 = tk.CTkButton(root, text="Actualizar", command=act)
    boton1.pack()

    boton2 = tk.CTkButton(root, text="Reparar", command=rep)
    boton2.pack(pady=10)

    texto3 = tk.CTkLabel(root, text="Ingresa el nombre de un paquete que quieras instalar:")
    texto3.pack()

    entrada1 = tk.CTkEntry(root)
    entrada1.pack(pady=10)

    boton3 = tk.CTkButton(root, text="Instalar", command=inst)
    boton3.pack()

    root.mainloop()