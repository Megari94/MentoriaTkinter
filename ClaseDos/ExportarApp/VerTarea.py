import tkinter as tk

def ver_tarea_ventana():
    ventana = tk.Tk()
    ventana.title("Ver Tarea")
    ventana.geometry("500x370")
    ventana.resizable(False, False)
    ventana.config(bg="#B3BBFF")
    ventana.columnconfigure(0, weight=1)
    fuente_boton = ("Aptos", 12, "bold")

    tk.Label(ventana, text="Tareas existentes", bg="#B3BBFF", font=("Aptos", 14)).grid(row=0, column=0, pady=5)

    text_tareas = tk.Text(ventana, height=10, font=("Arial", 12))
    text_tareas.grid(row=1, column=0, padx=10, pady=5, sticky="we")
    ventana.rowconfigure(1, weight=1)

    def cargar_tareas():
        text_tareas.delete(1.0, tk.END)
        try:
            with open("tareas.txt", "r", encoding="utf-8") as f:
                tareas = f.readlines()
            if tareas:
                for idx, tarea in enumerate(tareas, start=1):
                    text_tareas.insert(tk.END, f"{idx}. {tarea}")
            else:
                text_tareas.insert(tk.END, "No hay tareas guardadas")
        except FileNotFoundError:
            text_tareas.insert(tk.END, "No hay tareas guardadas")

    cargar_tareas()

    def volver_menu():
        ventana.destroy()
        from menu import menu_ventana
        menu_ventana()

    tk.Button(ventana, text="Volver al Menu", bg="#2F0070", fg="white",
              height=3, font=fuente_boton, command=volver_menu).grid(row=2, column=0, pady=10, sticky="we")

    ventana.mainloop()
