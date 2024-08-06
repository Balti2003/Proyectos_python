#Importamos los modulos necesarios

import tkinter as tk  # Módulo para crear interfaces gráficas de usuario
import random  # Módulo para seleccionar elementos aleatorios
import timeit  # Módulo para medir el tiempo

# Lista de frases que se usarán en el test de escritura

frases = [
    "La rapidez con la que puedes escribir esta frase será medida.",
    "Practicar con el teclado puede mejorar tu velocidad.",
    "El tiempo es oro, y la precisión es clave.",
    "Cada letra cuenta cuando estás en una competencia de escritura.",
    "Escribe tan rápido como puedas, pero sin errores.",
]

# Definimos la clase que manejará la lógica de la prueba de escritura

class PruebaEscrituraVeloz:
    def __init__(self, raiz):
        # Inicializamos la ventana principal
        self.raiz = raiz
        self.raiz.title("Prueba de Escritura Veloz")  # Establecemos el título de la ventana

        # Creamos una etiqueta con un mensaje de bienvenida
        self.etiqueta_bienvenida = tk.Label(raiz, text="Presiona el botón para comenzar el test.")
        self.etiqueta_bienvenida.pack(pady=10)  # Añadimos un poco de espacio alrededor

        # Creamos una etiqueta que mostrará la frase a escribir
        self.etiqueta_frase = tk.Label(raiz, text="", wraplength=400)
        self.etiqueta_frase.pack(pady=10)

        # Creamos un campo de entrada donde el usuario escribirá la frase
        self.campo_entrada = tk.Entry(raiz, width=50)  # Especificamos el ancho del campo de entrada
        self.campo_entrada.pack(pady=10)

        # Creamos un botón que iniciará el test
        self.boton_comenzar = tk.Button(raiz, text="Comenzar", command=self.comenzar_prueba)
        self.boton_comenzar.pack(pady=10)

        # Creamos un botón que enviará el texto escrito para verificarlo
        self.boton_enviar = tk.Button(raiz, text="Enviar", command=self.enviar_prueba)
        self.boton_enviar.pack(pady=10)

        # Creamos una etiqueta que mostrará el resultado del test
        self.etiqueta_resultado = tk.Label(raiz, text="")
        self.etiqueta_resultado.pack(pady=10)

        # Variables para almacenar la frase de prueba y el tiempo de inicio
        self.frase_prueba = ""
        self.tiempo_inicio = 0

    # Método que se ejecuta cuando se presiona el botón "Comenzar"
    
    def comenzar_prueba(self):
        # Seleccionamos una frase aleatoria de la lista
        
        self.frase_prueba = random.choice(frases) #Selecciona aleatoriamente una frase de la lista frases
        self.etiqueta_frase.config(text=self.frase_prueba)  # Mostramos la frase en la etiqueta
        self.campo_entrada.delete(0, tk.END)  # Limpiamos el campo de entrada
        self.campo_entrada.focus()  # Colocamos el cursor en el campo de entrada

        # Iniciamos el cronómetro para medir el tiempo de escritura
        
        self.tiempo_inicio = timeit.default_timer()
        self.etiqueta_resultado.config(text="")  # Limpiamos el resultado anterior

    # Método que se ejecuta cuando se presiona el botón "Enviar"
    
    def enviar_prueba(self):
        # Detenemos el cronómetro y calculamos el tiempo transcurrido
        tiempo_final = timeit.default_timer()
        tiempo_transcurrido = tiempo_final - self.tiempo_inicio

        # Obtenemos el texto escrito por el usuario
        texto_escrito = self.campo_entrada.get()
        
        # Verificamos si el texto coincide con la frase de prueba
        if texto_escrito.strip() == self.frase_prueba:
            # Si coincide, mostramos un mensaje de éxito con el tiempo tomado
            mensaje = f"¡Bien hecho! Tiempo tomado: {tiempo_transcurrido:.2f} segundos."
        else:
            # Si no coincide, mostramos un mensaje de error
            mensaje = "La frase no coincide. Inténtalo de nuevo."

        # Mostramos el resultado en la etiqueta de resultados
        self.etiqueta_resultado.config(text=mensaje)


# Creamos y ejecutamos la aplicación
if __name__ == "__main__":
    raiz = tk.Tk()  # Creamos la ventana principal de la aplicación
    app = PruebaEscrituraVeloz(raiz)  # Instanciamos la clase PruebaEscrituraVeloz
    raiz.mainloop()  # Iniciamos el bucle de eventos de tkinter