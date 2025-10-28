import tkinter as tk
from tkinter import messagebox

def eliminar_tarea_ventana():
    ventana = tk.Tk()
    ventana.title("Eliminar Tarea")
    ventana.geometry("500x370")
    ventana.resizable(False, False)
    ventana.config(bg="#B3BBFF")
    ventana.columnconfigure(0, weight=1)
    fuente_boton = ("Aptos", 12, "bold")

    tk.Label(
        ventana,
        text="¿Qué tarea quieres eliminar?",
        bg="#B3BBFF",
        font=("Aptos", 14)
    ).grid(row=0, column=0, pady=5)

    listbox_tareas = tk.Listbox(ventana, font=("Arial", 12))
    listbox_tareas.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

    scrollbar = tk.Scrollbar(listbox_tareas, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox_tareas.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox_tareas.yview)

    def cargar_tareas():
        listbox_tareas.delete(0, tk.END)
        try:
            with open("tareas.txt", "r", encoding="utf-8") as f:
                tareas = f.readlines()
            if tareas:
                for tarea in tareas:
                    listbox_tareas.insert(tk.END, tarea.strip())
            else:
                listbox_tareas.insert(tk.END, "No hay tareas guardadas.")
        except FileNotFoundError:
            listbox_tareas.insert(tk.END, "No hay tareas guardadas.")

    cargar_tareas()

    def eliminar_tarea():
        seleccion = listbox_tareas.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "No se seleccionó ninguna tarea")
            return
        tarea_a_eliminar = listbox_tareas.get(seleccion[0])
        try:
            with open("tareas.txt", "r", encoding="utf-8") as f:
                tareas = f.readlines()
        except FileNotFoundError:
            messagebox.showinfo("Info", "No hay tareas guardadas.")
            return

        tareas_restantes = [tarea for tarea in tareas if tarea.strip() != tarea_a_eliminar]
        with open("tareas.txt", "w", encoding="utf-8") as f:
            f.writelines(tareas_restantes)

        messagebox.showinfo("Éxito", f"Tarea '{tarea_a_eliminar}' eliminada correctamente.")
        cargar_tareas()

    # Volver al menú
    def volver_menu():
        ventana.destroy()
        from menu import menu_ventana
        menu_ventana()

    tk.Button(ventana, text="Eliminar Tarea", bg="#2F0070", fg="white",
              height=3, font=fuente_boton, command=eliminar_tarea).grid(row=2, column=0, pady=5, sticky="we")

    tk.Button(ventana, text="Volver al Menu", bg="#2F0070", fg="white",
              height=3, font=fuente_boton, command=volver_menu).grid(row=3, column=0, pady=10, sticky="we")

    ventana.mainloop()
