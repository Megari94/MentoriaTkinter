import tkinter as tk

#------FUNCION AUXILIAR--------
#def saludar():
	#entrada y siempre se le coloca .get()
	#nombre = entrada.get()
	#etiqueta.config(text=f"Hola! {nombre}")

ventana = tk.Tk()

#title()
ventana.title("MentoriaTk")

#geometry()
ventana.geometry("900x200")

#Colores
ventana.config(bg="#EDC0B7")

#Label() --> que es la etiqueta
#pack() --> aca se coloca la etiqueta

#etiqueta = tk.Label(ventana, text="Hola Chicos :D")
#etiqueta = tk.Label(ventana, text="Decime tu nombre")
#etiqueta.pack()

#entrada = tk.Entry(ventana)
#entrada.pack()

#boton = tk.Button(ventana, text="Saludo", command=saludar) #command llama a la funcion
#boton.pack()


#-------------SUMA DE DOS VALORES-----------------------

def sumar():
	try:
		num1 = float(entrada1.get())
		num2 = float(entrada2.get())
		resultado = num1 + num2
		etiquetaResultado.config(text=f"Resultado: {resultado}")
	except ValueError:
		etiquetaResultado.config(text=f"Ingresa numeros validos")

#Label y entrada para numero 1
tk.Label(ventana, text="Numero 1", bg="#EDC0B7").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

#Label y entrada para numero 2
tk.Label(ventana, text="Numero 2").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana, text="Sumar", command=sumar, bg="#EDDBB7")
boton.pack()

#Etiqueta donde muestre el resultado

etiquetaResultado = tk.Label(ventana, text="Resultado", bg="#E38CAC")
etiquetaResultado.pack()


ventana.mainloop()