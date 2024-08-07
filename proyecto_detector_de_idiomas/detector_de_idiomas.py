# Importamos las librerías necesarias
from langdetect import detect  # Para detectar el idioma del texto
import tkinter as tk  # Para crear la interfaz gráfica de usuario (GUI)
from tkinter import messagebox  # Para mostrar mensajes emergentes

# Diccionario que mapea los códigos de idioma a sus nombres completos
idiomas = {
    'en': 'Inglés',
    'es': 'Español',
    'fr': 'Francés',
    'de': 'Alemán',
    'it': 'Italiano',
    'pt': 'Portugués',
    'nl': 'Holandés',
    'ru': 'Ruso',
    'zh-cn': 'Chino (Simplificado)',
    'ja': 'Japonés',
    'ko': 'Coreano',
    'ar': 'Árabe',
    'hi': 'Hindi',
    'sv': 'Sueco',
    'fi': 'Finlandés',
    'no': 'Noruego',
    'da': 'Danés'
    # Se pueden añadir mas idiomas si es necesario
}

# Definimos una función para detectar el idioma del texto ingresado por el usuario

def detectar_idioma():
    # Obtenemos el texto del campo de entrada en la interfaz gráfica
    texto = entrada_texto.get("1.0", tk.END)
    
    # Verificamos si el texto está vacío
    if texto.strip() == "":
        # Mostramos una advertencia si no se ha ingresado texto
        messagebox.showwarning("Advertencia", "Por favor, ingrese algún texto.")
        return  # Salimos de la función si no hay texto

    try:
        # Intentamos detectar el idioma usando langdetect
        codigo_idioma = detect(texto)
        
        # Buscamos el nombre completo del idioma en el diccionario
        nombre_idioma = idiomas.get(codigo_idioma, "Idioma desconocido")
        
        # Mostramos el nombre del idioma detectado en una ventana emergente
        messagebox.showinfo("Resultado", f"El idioma detectado es: {nombre_idioma}")
    
    except Exception as e:
        # Si ocurre un error durante la detección, mostramos un mensaje de error
        messagebox.showerror("Error", f"No se pudo detectar el idioma. Error: {str(e)}")


# Creamos la ventana principal de la aplicación GUI
ventana = tk.Tk()
ventana.title("Detector de Idioma")  # Establecemos el título de la ventana

# Configuramos el tamaño de la ventana
ventana.geometry("400x300")

# Creamos una etiqueta para indicar al usuario que ingrese el texto
etiqueta = tk.Label(ventana, text="Ingrese el texto:")
etiqueta.pack(pady=10)  # Añadimos un poco de espacio vertical alrededor de la etiqueta

# Creamos un campo de texto para que el usuario ingrese el texto a analizar
entrada_texto = tk.Text(ventana, height=10, width=40)  # Especificamos el tamaño del área de texto
entrada_texto.pack(pady=10)  # Añadimos un poco de espacio vertical alrededor del campo de texto

# Creamos un botón que, al ser presionado, llamará a la función para detectar el idioma
boton_detectar = tk.Button(ventana, text="Detectar Idioma", command=detectar_idioma)
boton_detectar.pack(pady=20)  # Añadimos espacio vertical para separar el botón de otros elementos

# Iniciamos el bucle principal de la interfaz gráfica
ventana.mainloop()  # Esto mantiene la ventana abierta y esperando interacciones del usuario
