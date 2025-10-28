import tkinter as tk
from tkinter import messagebox

def agregar_tarea_ventana():
    ventana = tk.Tk()
    ventana.title("Agregar Tarea")
    ventana.geometry("500x370")
    ventana.resizable(False, False)
    ventana.config(bg="#B3BBFF")
    ventana.columnconfigure(0, weight=1)
    fuente_boton = ("Aptos", 12, "bold")

    tk.Label(
        ventana,
        text="Ingrese una nueva tarea",
        bg="#B3BBFF",
        font=("Aptos", 14)
    ).grid(row=0, column=0, pady=5)

    entry_tarea = tk.Entry(ventana, width=60)
    entry_tarea.grid(row=1, column=0, pady=10, padx=10, sticky="we", ipady=20)

    def guardar_tarea():
        tarea = entry_tarea.get().strip()
        if tarea != "":
            with open("tareas.txt", "a", encoding="utf-8") as f:
                f.write(tarea + "\n")
            entry_tarea.delete(0, tk.END)
            messagebox.showinfo("Éxito", "Tarea guardada correctamente")
        else:
            messagebox.showinfo("Atención", "No se pueden guardar tareas vacías")

    def volver_menu():
        ventana.destroy()
        from menu import menu_ventana
        menu_ventana()

    tk.Button(ventana, text="Guardar Tarea", bg="#2F0070", fg="white",
              height=3, font=fuente_boton, command=guardar_tarea).grid(row=2, column=0, pady=5, sticky="we")

    tk.Button(ventana, text="Volver al Menu", bg="#2F0070", fg="white",
              height=3, font=fuente_boton, command=volver_menu).grid(row=3, column=0, pady=5, sticky="we")

    ventana.mainloop()
