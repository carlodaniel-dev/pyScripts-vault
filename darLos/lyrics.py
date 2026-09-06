"""
LYRICS VISUALIZER - estilo TikTok
----------------------------------
Imprime la letra de una canción línea por línea, con pausas para que
coincida con el ritmo de la música mientras grabas la pantalla.
"""

import time
import sys
import random

# ============================================
# COLORES ESTILO TERMINAL (códigos ANSI)
# ============================================
COLORES = [
    "\033[91m",  # rojo
    "\033[92m",  # verde
    "\033[93m",  # amarillo
    "\033[94m",  # azul
    "\033[95m",  # morado
    "\033[96m",  # cyan
]
RESET = "\033[0m"  # apaga el color, vuelve al color normal de la terminal

# ============================================
# EDITA ESTA LISTA CON TU PROPIA LETRA
# Cada elemento: (texto_de_la_linea, emoji, segundos_de_espera_antes)
# ============================================
letra = [
    ("Escribe aquí tu primera línea...", "✨", 1.5),
    ("Escribe aquí tu segunda línea...", "👑", 2.0),
    ("Escribe aquí tu tercera línea...", "🛡️", 2.0),
    ("Escribe aquí tu cuarta línea...", "👉💗", 1.8),
    ("Escribe aquí tu quinta línea...", "💗", 1.8),
    ("Escribe aquí tu sexta línea...", "🌙", 2.0),
]


def efecto_maquina_de_escribir(texto, delay=0.03, usar_color=False):
    """Imprime el texto letra por letra, como si se estuviera escribiendo."""
    color = random.choice(COLORES) if usar_color else ""
    reset = RESET if usar_color else ""
    if usar_color:
        sys.stdout.write(color)
        sys.stdout.flush()
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(reset)
    print()


def print_lyrics(letra, modo_maquina_de_escribir=True, usar_color=False):
    print("\n\n\n")
    for texto, emoji, espera in letra:
        time.sleep(espera)
        linea = f"{texto} {emoji}"
        if modo_maquina_de_escribir:
            efecto_maquina_de_escribir(linea, usar_color=usar_color)
        else:
            if usar_color:
                color = random.choice(COLORES)
                print(f"{color}{linea}{RESET}")
            else:
                print(linea)


if __name__ == "__main__":
    print_lyrics(letra, modo_maquina_de_escribir=True, usar_color=True)