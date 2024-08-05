#Conversor de texto a audio utilizando un archivo existente en la computadora

#Importamos las librerias necesarias

from gtts import gTTS #gTTS se utiliza para convertir texto a audio usando Google Text-to-Speech

# Abrimos el archivo "libro.txt" en modo lectura ("r"), leemos su contenido,
# y reemplazamos los saltos de línea ("\n") con espacios para obtener un texto continuo.
archivo = open("libro.txt", "r").read().replace("\n", " ")

# Especificamos el idioma que usará gTTS para la conversión. En este caso, "es" para español.
language = "es"

# Creamos un objeto gTTS para la conversión de texto a voz.
# Pasamos el texto del archivo, el idioma y la velocidad del habla (slow=False para una velocidad normal).
speech = gTTS(text = str(archivo), lang = language, slow = False)

# Guardamos el audio generado como un archivo MP3 llamado "archivo_a_audio.mp3".
speech.save("archivo_a_audio.mp3")
print("Archivo guardado como archivo_a_audio.mp3")