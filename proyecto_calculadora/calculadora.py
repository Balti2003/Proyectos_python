#Importamos los modulos necesarios
import tkinter

i = 0

#---------------Funciones--------------
def click_boton(valor):
    global i
    entrada_texto.insert(i, valor) #Inserto en el indice 0 (al principio de la entrada de texto) el valor tal.
    i += 1 #Creo una variable i y la voy sumando para que cuando toco un numero se coloca en la posicion 0 y cuando toco entro se coloca en la 0+1 y asi

def borrar():
    entrada_texto.delete(0, tkinter.END) #Borra la entrada de texto desde el indice 0 hasta el final
    
    
def operaciones():
    ecuacion = entrada_texto.get() #Almaceno lo que esta en entrada_texto en la variable ecuacion
    
    resultado_ec = eval(ecuacion) #Eval es una funcion de python que hace el calculo de una cadena de caracteres, ej "5 + 10 * 2"

    entrada_texto.delete(0, tkinter.END) #Borro lo que esta en la entrada_texto
    entrada_texto.insert(0,resultado_ec) #Coloco el resultado de la ecuacion
    
    
#---------------Interfaz--------------
#Creamos la ventana
ventana = tkinter.Tk()
ventana.title("Calculadora")

#Creamos la entrada de texto
entrada_texto = tkinter.Entry(ventana, font = ("Calibri 20"))
entrada_texto.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5) #fila 0 columna 0, por debajo habra 4 columnas, padx es el espacio en x y pady el espacio en y

#Creamos los botones
boton1 = tkinter.Button(ventana, text="1", width=5, height=2, command = lambda: click_boton(1))
boton2 = tkinter.Button(ventana, text="2", width=5, height=2, command = lambda: click_boton(2))
boton3 = tkinter.Button(ventana, text="3", width=5, height=2, command = lambda: click_boton(3))
boton4 = tkinter.Button(ventana, text="4", width=5, height=2, command = lambda: click_boton(4))
boton5 = tkinter.Button(ventana, text="5", width=5, height=2, command = lambda: click_boton(5))
boton6 = tkinter.Button(ventana, text="6", width=5, height=2, command = lambda: click_boton(6))
boton7 = tkinter.Button(ventana, text="7", width=5, height=2, command = lambda: click_boton(7))
boton8 = tkinter.Button(ventana, text="8", width=5, height=2, command = lambda: click_boton(8))
boton9 = tkinter.Button(ventana, text="9", width=5, height=2, command = lambda: click_boton(9))
boton0 = tkinter.Button(ventana, text="0", width=13, height=2, command = lambda: click_boton(0))

boton_borrar = tkinter.Button(ventana, text="AC", width=5, height=2, command = lambda: borrar())
boton_parentesis_1 = tkinter.Button(ventana, text="(", width=5, height=2, command = lambda: click_boton("("))
boton_parentesis_2 = tkinter.Button(ventana, text=")", width=5, height=2, command = lambda: click_boton(")"))
boton_punto = tkinter.Button(ventana, text=".", width=5, height=2, command = lambda: click_boton("."))

boton_suma= tkinter.Button(ventana, text="+", width=5, height=2, command = lambda: click_boton("+"))
boton_resta = tkinter.Button(ventana, text="-", width=5, height=2, command = lambda: click_boton("-"))
boton_mult = tkinter.Button(ventana, text="*", width=5, height=2, command = lambda: click_boton("*"))
boton_div = tkinter.Button(ventana, text="/", width=5, height=2, command = lambda: click_boton("/"))
boton_igual = tkinter.Button(ventana, text="=", width=5, height=2, command = lambda: operaciones())

#Agregamos y posicionamos los botones en la ventana
boton_borrar.grid(row=1, column=0, padx=5 ,pady=5)
boton_parentesis_1.grid(row=1, column=1, padx=5 ,pady=5)
boton_parentesis_2.grid(row=1, column=2, padx=5 ,pady=5)
boton_div.grid(row=1, column=3, padx=5 ,pady=5)

boton7.grid(row=2, column=0, padx=5 ,pady=5)
boton8.grid(row=2, column=1, padx=5 ,pady=5)
boton9.grid(row=2, column=2, padx=5 ,pady=5)
boton_mult.grid(row=2, column=3, padx=5 ,pady=5)

boton4.grid(row=3, column=0, padx=5 ,pady=5)
boton5.grid(row=3, column=1, padx=5 ,pady=5)
boton6.grid(row=3, column=2, padx=5 ,pady=5)
boton_suma.grid(row=3, column=3, padx=5 ,pady=5)

boton1.grid(row=4, column=0, padx=5 ,pady=5)
boton2.grid(row=4, column=1, padx=5 ,pady=5)
boton3.grid(row=4, column=2, padx=5 ,pady=5)
boton_resta.grid(row=4, column=3, padx=5 ,pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5 ,pady=5)
boton_punto.grid(row=5, column=2, padx=5 ,pady=5)
boton_igual.grid(row=5, column=3, padx=5 ,pady=5)

ventana.mainloop()