import tkinter as tk
from tkinter import messagebox
import os

ventana = tk.Tk()
ventana.title("Agregar Tarea")
ventana.geometry("500x370")
ventana.resizable(False, False)
ventana.config(bg="#B3BBFF")
ventana.columnconfigure(0, weight=1)  # Permitir que la columna 0 se expanda
fuente_boton = ("Aptos", 12, "bold")

#Etiqueta o Label donde indicamos la accion que se puede realizar
tk.Label(
	ventana,
	text="Ingrese una nueva tarea",
	bg="#B3BBFF",
	font=("Aptos", 14)
	).grid(
		row=0, column=0, pady=5
	)

#Entrada (Entry) de datos
entry_tarea= tk.Entry(
	ventana,
	width=60
	)
entry_tarea.grid(
	row=1, column=0, pady=10, padx=10, sticky="we", ipady=20
	)

#Funcion para guardar tarea
def guardar_tarea():
	tarea = entry_tarea.get().strip() #obtengo la info con get y elimino espacios al inicio y a l final.
	#Verificar no este vacio
	if tarea != "":
		with open("tareas.txt", "a", encoding="utf-8") as f: #abrir un txt en modo "agregar" y con una codificacion utf-8
			f.write(tarea + "\n") #Guardar cada tarea en una linea nueva
		entry_tarea.delete(0, tk.END) #Limpiar Entry cuando agregamos tarea
		messagebox.showinfo("Exito", "Tarea guardada correctamente")
	else:
		messagebox.showinfo("Atencion", "No se pueden guardar tareas vacias")

#Funcion Para volver al Menu
def volver_menu():
	ventana.destroy()
	os.system("python menu.py")

#Boton de guardado
tk.Button(
	ventana,
	text="Guardar Tarea",
	bg="#2F0070",
	fg="white",
	height=3,
	font=fuente_boton,
	command=guardar_tarea
	).grid(
		row=2, column=0, pady=5, sticky="we"
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
		row=3, column=0, pady=5, sticky="we"
	)
	

#Iniciacion de ventana
ventana.mainloop()