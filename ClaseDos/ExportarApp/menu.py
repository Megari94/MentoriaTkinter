import tkinter as tk
from PIL import Image, ImageTk
import os, sys

from AgregarTarea import agregar_tarea_ventana
from VerTarea import ver_tarea_ventana
from EliminarTarea import eliminar_tarea_ventana

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def menu_ventana():
    ventana = tk.Tk()
    ventana.title("Menu del Block")
    ventana.geometry("500x370")
    ventana.resizable(False, False)
    ventana.config(bg="#B3BBFF")

    fuente_boton = ("Aptos", 12, "bold")

    # Logo
    imagen = Image.open(resource_path("logo.png"))
    imagen = imagen.resize((500, 100))
    logo = ImageTk.PhotoImage(imagen)
    tk.Label(ventana, image=logo, bg="#B3BBFF").grid(row=0, column=0, sticky="we", pady=(0,10))

    # Botones
    tk.Button(ventana, text="Agregar Tarea", bg="#2F0070", fg="white",
              height=3, font=fuente_boton, command=lambda:[ventana.destroy(), agregar_tarea_ventana()]).grid(row=1, column=0, sticky="we", pady=5)

    tk.Button(ventana, text="Ver Tareas", bg="#2F0070", fg="white",
              height=3, font=fuente_boton, command=lambda:[ventana.destroy(), ver_tarea_ventana()]).grid(row=2, column=0, sticky="we", pady=5)

    tk.Button(ventana, text="Eliminar Tareas", bg="#2F0070", fg="white",
              height=3, font=fuente_boton, command=lambda:[ventana.destroy(), eliminar_tarea_ventana()]).grid(row=3, column=0, sticky="we", pady=5)

    ventana.mainloop()

# Para ejecutar directamente
if __name__ == "__main__":
    menu_ventana()
