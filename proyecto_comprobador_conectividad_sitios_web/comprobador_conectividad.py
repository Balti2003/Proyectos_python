#Importamos los modulos necesarios

import tkinter as tk #para crear interfaces gráficas de usuario
from tkinter import messagebox #para mostrar mensajes emergentes
# Importamos urlopen para abrir URLs y URLError, HTTPError para manejar errores de URL
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

# Definimos la función que comprueba la conectividad de un sitio web

def comprobar_conectividad():
    # Obtenemos el texto ingresado en el campo de entrada (la URL)
    url = entrada_url.get()

    # Verificamos si la URL no está vacía
    if not url:
        # Si está vacía, mostramos un mensaje de error al usuario
        messagebox.showerror("Error", "Por favor, ingrese una dirección web.")
        return  # Salimos de la función si no hay URL

    try:
        # Intentamos abrir la URL proporcionada por el usuario
        respuesta = urlopen(url)
        # Obtenemos el código de estado HTTP de la respuesta
        codigo_estado = respuesta.getcode()

        # Comprobamos si el código de estado es 200 (OK)
        if codigo_estado == 200:
            # Si es 200, mostramos un mensaje indicando que el sitio está funcionando
            messagebox.showinfo("Conectividad", f"El sitio web {url} está funcionando correctamente.")
        else:
            # Si el código no es 200, mostramos un mensaje de advertencia con el código de estado
            messagebox.showwarning("Conectividad", f"El sitio web {url} no está disponible. Código de estado: {codigo_estado}")

    # Capturamos excepciones HTTPError que indican problemas HTTP
    except HTTPError as e:
        # Mostramos un mensaje de error con el código y la razón del error HTTP
        messagebox.showerror("Error HTTP", f"Error HTTP: {e.code} - {e.reason}")
    # Capturamos excepciones URLError que indican problemas de conexión
    except URLError as e:
        # Mostramos un mensaje de error con la razón del problema de conexión
        messagebox.showerror("Error de Conexión", f"Error de conexión: {e.reason}")


# Creamos la ventana principal de la aplicación usando tkinter
ventana = tk.Tk()
# Establecemos el título de la ventana principal
ventana.title("Comprobador de Conectividad de Sitios Web")

# Creamos una etiqueta para indicar al usuario que ingrese una dirección web
etiqueta_url = tk.Label(ventana, text="Ingrese la dirección web:")
# Colocamos la etiqueta en la ventana con un margen vertical
etiqueta_url.pack(pady=5)

# Creamos un campo de entrada donde el usuario puede escribir la URL
entrada_url = tk.Entry(ventana, width=50)
# Colocamos el campo de entrada en la ventana con un margen vertical
entrada_url.pack(pady=5)

# Creamos un botón que, al ser presionado, llama a la función comprobar_conectividad
boton_comprobar = tk.Button(ventana, text="Comprobar Conectividad", command=comprobar_conectividad)
# Colocamos el botón en la ventana con un margen vertical
boton_comprobar.pack(pady=20)

# Iniciamos el bucle principal de la aplicación para que la ventana permanezca abierta
ventana.mainloop()
