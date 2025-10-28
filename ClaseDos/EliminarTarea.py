import tkinter as tk
from tkinter import messagebox
import os

ventana = tk.Tk()
ventana.title("Eliminar Tarea")
ventana.geometry("500x370")
ventana.resizable(False, False)
ventana.config(bg="#B3BBFF")
ventana.columnconfigure(0, weight=1)  # Permitir que la columna 0 se expanda
fuente_boton = ("Aptos", 12, "bold")


#Etiqueta o Label donde indicamos la accion que se puede realizar
tk.Label(
	ventana,
	text="¿Que tarea quieres Eliminar?",
	bg="#B3BBFF",
	font=("Aptos", 14)
	).grid(
		row=0, column=0, pady=5
	)

#ListBox para eliminar
listbox_tareas= tk.Listbox(
	ventana,
	font=("Arial", 12)
	)
listbox_tareas.grid(
	row=1, column=0, padx=10, pady=5, sticky="nsew"
	)

scrollbar = tk.Scrollbar(listbox_tareas, orient=tk.VERTICAL)  # Creamos scrollbar vertical
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Ubicación del scrollbar dentro del listbox
listbox_tareas.config(yscrollcommand=scrollbar.set)  # Conectar scrollbar al listbox
scrollbar.config(command=listbox_tareas.yview)  # Conectar listbox al scrollbar

#cargar tarea
def cargar_tareas():
    listbox_tareas.delete(0, tk.END)  # Limpiar lista antes de cargar
    try:
        # Abrir archivo "tareas.txt" en modo lectura con codificación utf-8
        with open("tareas.txt", "r", encoding="utf-8") as f:
            tareas = f.readlines()  # Leer todas las líneas del archivo

        if tareas:  # Si hay tareas
            for tarea in tareas:
                listbox_tareas.insert(tk.END, tarea.strip())  # Insertar cada tarea eliminando saltos de línea
        else:
            listbox_tareas.insert(tk.END, "No hay tareas guardadas.")  # Si archivo vacío
    except FileNotFoundError:
        listbox_tareas.insert(tk.END, "No hay tareas guardadas.")  # Si no existe el archivo

# Cargar las tareas al abrir la ventana
cargar_tareas()

#Funcion para eliminar la tarea que sea seleccionada
def eliminar_tarea():
	#curselection devuelve una tupla con los indices de los elementos seleccionados
    seleccion = listbox_tareas.curselection()  # Obtener índice de tarea seleccionada
    if not seleccion:  # Si no se seleccionó ninguna tarea
        messagebox.showwarning("Atención", "No se seleccionó ninguna tarea")
        return

    #get(indice), como es una tupla lo que se devolvio, yo quiero solo el primer numero, por eso uso seleccion[0]
    tarea_a_eliminar = listbox_tareas.get(seleccion[0])  # Obtener texto de la tarea seleccionada

    try:
        with open("tareas.txt", "r", encoding="utf-8") as f:
            tareas = f.readlines()  # Leer todas las tareas del archivo
    except FileNotFoundError:
        messagebox.showinfo("Info", "No hay tareas guardadas.")  # Si no existe el archivo
        return

    # Filtrar la tarea seleccionada para eliminarla
    #tarea.strip() elimina espacios y saltos de linea y se compara con tarea_a_eliminar y si no coincide la tarea se mantiene
    tareas_restantes = [tarea for tarea in tareas if tarea.strip() != tarea_a_eliminar] 

    # Guardar las tareas restantes en el archivo
    with open("tareas.txt", "w", encoding="utf-8") as f:
        f.writelines(tareas_restantes)

    # Mostrar mensaje de éxito
    messagebox.showinfo("Éxito", f"Tarea '{tarea_a_eliminar}' eliminada correctamente.")
    cargar_tareas()  # Recargar lista para actualizar Listbox

#Funcion Para volver al Menu
def volver_menu():
	ventana.destroy()
	os.system("python menu.py")

#Boton para eliminar tarea
tk.Button(
    ventana,
    text="Eliminar Tarea",  # Texto del botón
    bg="#2F0070",  # Color de fondo
    fg="white",  # Color del texto
    height=3,  # Altura
    font=fuente_boton,  # Fuente
    command=eliminar_tarea  # Función al hacer clic
).grid(
    row=2, column=0, pady=5, sticky="we"  # Ubicación y estirado horizontal
)

#Boton para volver al menu
tk.Button(
	ventana,
	text="Volver al Menu",
	bg="#2F0070",
	fg="white",
	height=3,
	font=fuente_boton,
	command=volver_menu
	).grid(
		row=3, column=0, pady=10, sticky="we"
	)

ventana.mainloop()