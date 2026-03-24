from pywinauto import Application
import time
import pyperclip 

# 1. Configuración de datos
contacto = input('Nombre del contacto/grupo: ')
mensaje = input('Mensaje a enviar: ')
cantidad = int(input('¿Cuántas veces?: '))

try:
    # 2. Conectar y FORZAR la ventana al frente
    print("Conectando con WhatsApp...")
    app = Application(backend="uia").connect(title_re=".*WhatsApp.*", timeout=10)
    ventana = app.window(title_re=".*WhatsApp.*")
    
    # Esto asegura que la ventana sea la activa en Windows
    ventana.set_focus()
    time.sleep(2)

    # 3. Ir al buscador (Usamos CTRL + N para "Nuevo Chat" que es más directo)
    print(f"Buscando a: {contacto}")
    ventana.type_keys("^n") 
    time.sleep(1.5)
    
    # Escribimos el nombre
    ventana.type_keys(contacto, with_spaces=True)
    time.sleep(2)

    # Seleccionamos con ENTER el primer resultado
    ventana.type_keys("{ENTER}")
    time.sleep(1.5)

    # 4. Enviar los mensajes usando Pegar (Ctrl + V)
    print("Enviando mensajes...")
    pyperclip.copy(mensaje)

    for i in range(cantidad):
        # Pegamos y damos Enter
        ventana.type_keys("^v{ENTER}")
        time.sleep(0.3) 

    print("¡Listica la Vuelta Patron!")

except Exception as e:
    print(f"Ocurrió un problema: {e}")
    print("TIP: Asegúrate de que WhatsApp esté abierto y que NO estés en una llamada.")