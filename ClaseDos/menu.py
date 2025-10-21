import tkinter as tk
from PIL import Image, ImageTk
import os

ventana = tk.Tk()#crear ventana principal
ventana.title("Menu del Block")#titulo de la ventana aparece en la barra superior
ventana.geometry("500x370")#tamaño de la ventana ancho x alto cuando ejecuto es el tamaño incial
#tamaño fijo ventana.resizable(False, False) #Deshabilitar cambio de tamaño de la ventana
ventana.resizable(False, False) #Deshabilitar cambio de tamaño de la ventana
ventana.config(bg="#B3BBFF")#configuracion de la ventana color de fondo

fuente_boton = ("Aptos", 12, "bold") #Definir fuente para los botones, para reutilizar

#Logo

imagen = Image.open("logo.png") #Abrir imagen, esta en la misma carpeta que menu.py en mismo nivel del archivo
imagen = imagen.resize((500, 100)) #Redimensionar imagen
logo = ImageTk.PhotoImage(imagen) #Crear objeto PhotoImage para usar en Tkinter

#Mostrar logo en Label

label_logo = tk.Label(ventana, image=logo, bg="#B3BBFF")#Crear label para mostrar el logo con fondo igual al de la ventana
label_logo.grid(row=0, column=0, sticky="we", pady=(0, 10))# grid para organizar el logo en fila 0 columna 0, ocupa todo el ancho con sticky west east, y con un padding vertical de 10 pixeles

#Funciones de los botones mas adelante Y SIEMPRE VAN PRIMERO QUE LOS BOTONES
def agregar_tarea():
    ventana.destroy() #Cerrar ventana actual
    os.system("python AgregarTarea.py")#Ejecutar script AgregarTarea.py que esta en el mismo nivel que menu.py

#Botones

tk.Button(
    ventana,
    text="Agregar Tarea",
    bg="#2F0070",
    fg="white",
    height=3,
    font=fuente_boton, #Usar la fuente definida anteriormente arriba
    command=agregar_tarea #Asignar la funcion agregar_tarea al boton
).grid(row=1, column=0, sticky="we", pady=5)

tk.Button(
    ventana,
    text="Ver Tareas",
    bg="#2F0070",
    fg="white",
    height=3,
    font=fuente_boton,
).grid(row=2, column=0, sticky="we", pady=5)

tk.Button(
    ventana,
    text="Eliminar Tareas",
    bg="#2F0070",
    fg="white",
    height=3,
    font=fuente_boton,
).grid(row=3, column=0, sticky="we", pady=5)

ventana.mainloop() 