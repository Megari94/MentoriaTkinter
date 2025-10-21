import tkinter as tk

ventana = tk.Tk()
ventana.title("Agregar Tarea")
ventana.geometry("500x370")
ventana.config(bg="#B3BBFF")
ventana.columnconfigure(0, weight=1)  # Permitir que la columna 0 se expanda
fuente_boton = ("Aptos", 12, "bold")

ventana.mainloop()