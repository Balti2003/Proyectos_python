# Importamos los módulos necesarios
import tkinter as tk  # Importa la biblioteca tkinter para la GUI
from tkinter import filedialog, messagebox  # Importa módulos para diálogos de archivo y mensajes

# Creamos la ventana principal
ventana = tk.Tk()  # Crea una nueva ventana de la aplicación
ventana.title("Editor de texto")  # Le colocamos un título a la ventana

# Creamos un campo de texto
area_texto = tk.Text(ventana, wrap="word", undo=True) # Crea un widget de texto donde el texto se ajusta automáticamente al tamaño de la ventana (wrap='word'), 'undo=True' habilita la funcionalidad de deshacer

area_texto.pack(expand=1, fill="both") #'expand=1' permite que el área de texto crezca para llenar el espacio disponible, 'fill="both"' hace que el área de texto se extienda tanto vertical como horizontalmente

# Creamos un menú
barra_menu = tk.Menu(ventana)  # Crea una barra de menú en la ventana
ventana.config(menu=barra_menu)  # Asigna la barra de menú a la ventana principal

# Función para abrir un archivo
def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivo de Texto", "*.txt"), ("Todos los archivos", "*.*")])
    # Abre un cuadro de diálogo para seleccionar un archivo a abrir 'defaultextension' asegura que los archivos se guarden con extensión .txt si el usuario no proporciona una
    
    if ruta_archivo:  # Verifica si se ha seleccionado una ruta de archivo
        try:
            with open(ruta_archivo, "r") as archivo:  # Abre el archivo en modo lectura
                area_texto.delete(1.0, tk.END)  # Elimina todo el texto actual en el área de texto
                area_texto.insert(tk.END, archivo.read())  # Inserta el contenido del archivo en el área de texto
        except Exception as e:  # Maneja cualquier error que ocurra al abrir el archivo
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")  # Muestra un mensaje de error

# Función para guardar un archivo
def guardar_archivo():
    ruta_archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")])
    # Abre un cuadro de diálogo para seleccionar una ubicación para guardar el archivo

    if ruta_archivo:  # Verifica si se ha seleccionado una ruta de archivo
        try:
            with open(ruta_archivo, "w") as archivo:  # Abre el archivo en modo escritura
                archivo.write(area_texto.get(1.0, tk.END))  # Escribe todo el texto del área de texto en el archivo
        except Exception as e:  # Maneja cualquier error que ocurra al guardar el archivo
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")  # Muestra un mensaje de error

# Añadir opciones de menú
menu_archivo = tk.Menu(barra_menu, tearoff=0)  # Crea un submenú para la barra de menú

barra_menu.add_cascade(label="Archivo", menu=menu_archivo)  # Añade el submenú "Archivo" a la barra de menú

menu_archivo.add_command(label="Abrir", command=abrir_archivo)  # Añade la opción "Abrir" al submenú y asocia la función abrir_archivo
menu_archivo.add_command(label="Guardar", command=guardar_archivo)  # Añade la opción "Guardar" al submenú y asocia la función guardar_archivo
menu_archivo.add_separator()  # Añade una línea separadora en el submenú
menu_archivo.add_command(label="Salir", command=ventana.quit)  # Añade la opción "Salir" al submenú, que cierra la aplicación

# Iniciar el bucle principal de la aplicación
ventana.mainloop()  # Inicia el bucle de eventos de Tkinter para que la ventana permanezca abierta