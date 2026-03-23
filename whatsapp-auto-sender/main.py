from pywinauto import Application
import time

# Conectar a la aplicación de WhatsApp
app = Application(backend="uia").connect(title_re=".*WhatsApp.*")  # Busca la ventana de WhatsApp
ventana = app.window(title_re=".*WhatsApp.*")  # Obtiene la ventana principal

# Solicitar datos
cantidad = int(input('Cuantos Mensajes: '))
mensaje = input('Mensaje: ')
contacto = input('Nombre o número del contacto/grupo: ')

# 1: Buscar contacto/grupo
ventana.type_keys("^f")  # Presiona Ctrl+F para abrir la búsqueda
time.sleep(1)  
ventana.type_keys(contacto)  # Escribe el nombre/número del contacto
time.sleep(3)  

# 2: Seleccionar el primer resultado de la búsqueda
ventana.type_keys("{DOWN}")  # Presiona la flecha hacia abajo para seleccionar 
time.sleep(1)
ventana.type_keys("{ENTER}")  # Presiona Enter para abrir el chat
time.sleep(2)  

# 3: Mover el foco al campo de texto del chat
ventana.type_keys("{TAB}")  # Presiona Tab para mover el foco al campo de texto
time.sleep(1) 

# 4: Escribir y enviar los mensajes
for i in range(cantidad):
    ventana.type_keys(f"{mensaje}")  # Escribe el mensaje
    ventana.type_keys("{ENTER}")     # Presiona Enter para enviar
    time.sleep(0.5)                  # Retraso entre mensajes

print("¡Lista la vueltica Patron!")