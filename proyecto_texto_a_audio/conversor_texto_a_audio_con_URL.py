#Conversor de texto a audio con una url de internet.

#Importamos librerias necesarias.
import nltk
from newspaper import Article
from gtts import gTTS

nltk.download("punkt") #Descargar el paquete 'punkt' de nltk, que es necesario para el tokenizador de frases.

def obtener_contenido_desde_url(url):
    """
    Esta función toma una URL como entrada, descarga el contenido del artículo 
    y lo analiza para extraer el texto completo.
    """
    try:
        article = Article(url) #Crear un objeto de artículo usando la URL proporcionada.
        article.download()  #Descargar el contenido del artículo.
        article.parse() #Analizar el contenido del artículo para extraer el texto.
        return article.text
    
    except Exception as e:
        print(f"Error al obtener el artículo: {e}") #Imprimir un mensaje de error si ocurre algún problema durante la descarga o el análisis.
        return None
    

def texto_a_voz(texto, archivo_salida='articulo_proporcionado.mp3'):
    """
    Esta función convierte el texto proporcionado en un archivo de audio llamado articulo_proporcionado en formato MP3
    usando el servicio Google Text-to-Speech.
    """
    if texto:
        try:
            tts = gTTS(text=texto, lang='es')  #Crear un objeto gTTS para convertir el texto a voz, especificando el idioma (español en este caso).
            tts.save(archivo_salida) #Guardar el resultado como un archivo MP3.
            print(f'Archivo guardado como "{archivo_salida}"')
            
        except Exception as e:
            print(f"Error al convertir texto a voz: {e}") #Imprimir un mensaje de error si ocurre algún problema durante la conversión o el guardado.
    else:
        print("No se proporcionó texto para convertir.") #Imprimir un mensaje si no se proporciona texto para convertir.
    

def main():
    """
    Función principal del programa que solicita al usuario la URL de un artículo,
    extrae el contenido y lo convierte en un archivo de audio.
    """
    url = input('Por favor, introduce la URL del artículo: ')
    print("Esto puede tardar unos segundos...")
    
    contenido = obtener_contenido_desde_url(url) #Obtener el contenido del artículo desde la URL proporcionada.
    
    if contenido: #Si el contenido se obtuvo correctamente, convertirlo a voz.
        texto_a_voz(contenido)
    else:
        print("No se pudo obtener contenido del artículo.")


# Ejecutar la función principal si el script se ejecuta directamente.
if __name__ == "__main__":
    main()
