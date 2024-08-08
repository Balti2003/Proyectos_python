#Importamos los modulos necesarios

from tkinter import messagebox, Label, Tk, ttk  # Importar los componentes necesarios de la biblioteca tkinter para crear la interfaz gráfica
from time import strftime  # Importar la función strftime del módulo time para obtener la hora actual
from pygame import mixer  # Importar el módulo mixer de pygame para reproducir audio

ventana = Tk()  # Crear una nueva ventana de Tkinter
ventana.config(bg='black')  # Configurar el color de fondo de la ventana a negro
ventana.geometry('500x250')  # Establecer el tamaño de la ventana a 500x250 píxeles
ventana.title('Alarma')  # Establecer el título de la ventana a "Alarma"
ventana.minsize(width=500, height=250)  # Establecer el tamaño mínimo de la ventana

mixer.init()  # Inicializar el mezclador de pygame para manejar la reproducción de audio

lista_horas = []  # Crear una lista vacía para almacenar los valores de las horas
lista_minutos = []  # Crear una lista vacía para almacenar los valores de los minutos
lista_segundos = []  # Crear una lista vacía para almacenar los valores de los segundos

for i in range(0, 24):  # Recorrer los números del 0 al 23 (horas)
    lista_horas.append(i)  # Añadir cada número a la lista_horas

for i in range(0, 60):  # Recorrer los números del 0 al 59 (minutos)
    lista_minutos.append(i)  # Añadir cada número a la lista_minutos

for i in range(0, 60):  # Recorrer los números del 0 al 59 (segundos)
    lista_segundos.append(i)  # Añadir cada número a la lista_segundos

# Crear y configurar etiquetas para horas, minutos y segundos
texto1 = Label(ventana, text='Hora', bg='black', fg='magenta', font=('Arial', 12, 'bold'))  
texto1.grid(row=1, column=0, padx=5, pady=5)  # Colocar la etiqueta en la cuadrícula

texto2 = Label(ventana, text='Minutos', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
texto2.grid(row=1, column=1, padx=5, pady=5)

texto3 = Label(ventana, text='Segundos', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
texto3.grid(row=1, column=2, padx=5, pady=5)

# Crear y configurar los cuadros combinados para seleccionar horas, minutos y segundos
combobox1 = ttk.Combobox(ventana, values=lista_horas, style="TCombobox", justify='center', width='12', font='Arial')
combobox1.grid(row=2, column=0, padx=15, pady=5)  # Colocar el cuadro combinado en la cuadrícula
combobox1.current(0)  # Establecer el valor seleccionado por defecto al primer elemento de la lista

combobox2 = ttk.Combobox(ventana, values=lista_minutos, style="TCombobox", justify='center', width='12', font='Arial')
combobox2.grid(row=2, column=1, padx=15, pady=5)
combobox2.current(0)

combobox3 = ttk.Combobox(ventana, values=lista_segundos, style="TCombobox", justify='center', width='12', font='Arial')
combobox3.grid(row=2, column=2, padx=15, pady=5)
combobox3.current(0)

# Crear un estilo personalizado para los cuadros combinados
style = ttk.Style()
style.theme_create('combostyle', parent='alt', settings={'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'red',  # Color de fondo del elemento seleccionado
                                       'fieldbackground': 'gold',  # Color de fondo del campo
                                       'background': 'blue'  # Color de fondo del cuadro combinado
                                       }}})
style.theme_use('combostyle')  # Aplicar el estilo personalizado a los cuadros combinados

# Establecer opciones predeterminadas para los elementos de la lista de cuadros combinados
ventana.option_add('*TCombobox*Listbox*Background', 'white')  # Establecer el color de fondo de la lista
ventana.option_add('*TCombobox*Listbox*Foreground', 'black')  # Establecer el color de primer plano de la lista
ventana.option_add('*TCombobox*Listbox*selectBackground', 'green2')  # Establecer el color de fondo del elemento seleccionado
ventana.option_add('*TCombobox*Listbox*selectForeground', 'black')  # Establecer el color de primer plano del elemento seleccionado

# Crear etiquetas y un cuadro combinado para establecer el número de repeticiones de la alarma
alarma = Label(ventana, fg='violet', bg='black', font=('Radioland', 20))  
alarma.grid(column=0, row=3, sticky="nsew", ipadx=5, ipady=20)  # Colocar la etiqueta en la cuadrícula

repetir = Label(ventana, fg='white', bg='black', text='Repetir', font='Arial')
repetir.grid(column=1, row=3, ipadx=5, ipady=20)

cantidad = ttk.Combobox(ventana, values=(1, 2, 3, 4, 5), justify='center', width='8', font='Arial')
cantidad.grid(row=3, column=2, padx=5, pady=5)
cantidad.current(0)  # Establecer el valor seleccionado por defecto al primer elemento de la lista

def obtener_tiempo():
    # Obtener los valores de tiempo seleccionados en los cuadros combinados
    x_hora = combobox1.get()
    x_minutos = combobox2.get()
    x_segundos = combobox3.get()

    # Obtener la hora actual
    hora = strftime('%H')  # Obtener la hora actual
    minutos = strftime('%M')  # Obtener los minutos actuales
    segundos = strftime('%S')  # Obtener los segundos actuales

    # Formatear la hora actual y actualizar la etiqueta de la hora
    hora_total = (hora + ' : ' + minutos + ' : ' + segundos)
    texto_hora.config(text=hora_total, font=('Radioland', 25))

    # Formatear la hora de la alarma y actualizar la etiqueta de la alarma
    hora_alarma = x_hora + ' : ' + x_minutos + ' : ' + x_segundos
    alarma['text'] = hora_alarma

    # Comprobar si la hora actual coincide con la hora de la alarma
    if int(hora) == int(x_hora):
        if int(minutos) == int(x_minutos):
            if int(segundos) == int(x_segundos):
                mixer.music.load("audio.mp3")  # Cargar el archivo de audio para la alarma (el archivo debe llamarse audio.mp3 y debe estar en el mismo directorio del programa)
                mixer.music.play(loops=int(cantidad.get()))  # Reproducir el archivo de audio con el número de repeticiones especificado
                messagebox.showinfo(message=hora_alarma, title="Alarma")  # Mostrar un mensaje cuando se alcance la hora de la alarma

    texto_hora.after(100, obtener_tiempo)  # Programar la función obtener_tiempo para que se ejecute de nuevo después de 100 milisegundos

# Crear una etiqueta para mostrar la hora actual
texto_hora = Label(ventana, fg='green2', bg='black')
texto_hora.grid(columnspan=3, row=0, sticky="nsew", ipadx=5, ipady=20)

obtener_tiempo()  # Llamar a la función obtener_tiempo para iniciar el bucle de comprobación de la hora

ventana.mainloop()  # Iniciar el bucle de eventos de Tkinter para mostrar la ventana