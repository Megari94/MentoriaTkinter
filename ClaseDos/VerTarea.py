import tkinter as tk
from tkinter import messagebox
import os

ventana = tk.Tk()
ventana.title("Ver Tarea")
ventana.geometry("500x370")
ventana.resizable(False, False)
ventana.config(bg="#B3BBFF")
ventana.columnconfigure(0, weight=1)  # Permitir que la columna 0 se expanda
fuente_boton = ("Aptos", 12, "bold")

#Etiqueta o Label donde indicamos la accion que se puede realizar
tk.Label(
	ventana,
	text="Tareas existentes",
	bg="#B3BBFF",
	font=("Aptos", 14)
	).grid(
		row=0, column=0, pady=5
	)

text_tareas = tk.Text(
	ventana,
	height=10,
	font=("Arial", 12)
	)
text_tareas.grid(
	row=1, column=0, padx=10, pady=5, sticky="we"
	)

ventana.rowconfigure(1, weight=1)#Hacer que el Text se pueda redimensionar verticalmente con la ventana

#Funcion para cargar las tareas desde archivo

def cargar_tareas():
	text_tareas.delete(1.0, tk.END)
	try:
		# "w" → escribir (borra lo que había antes)
		# "a" → agregar (append)
		# "r" → leer y escribir
		# "x" → crear un archivo nuevo (falla si ya existe)
		#with solo sin open o close abre el archivo y cierra al finalizar el bloque por lo que es mas seguro colocarle la accion
		with open("tareas.txt", "r", encoding="utf-8") as f: #utf Permite leer caracteres especiales correctamente
			tareas= f.readlines()  #Lee todas las lineas del archivo de texto

		if tareas: #si hay tareas en el archivo
			for idx, tarea in enumerate(tareas, start=1):
				text_tareas.insert(tk.END, f"{idx}.{tarea}")
		else:
			#Si el archivo esta vacio
			text_tareas.insert(tk.END, "No hay tareas guardadas")
	except FileNotFoundError:
		#Si no existe archivo txt
		text_tareas.insert(tk.END, "No hay tareas guardadas")
#llamar a la funcion para que me muestre de manera automatica la ventana con las tareas
cargar_tareas()

#Funcion Para volver al Menu
def volver_menu():
	ventana.destroy()
	os.system("python menu.py")

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
		row=2, column=0, pady=10, sticky="we"
	)
	


#Iniciacion de ventana
ventana.mainloop()