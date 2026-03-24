# 📲 WhatsApp Spammer

> 🇺🇸 [English](#-english) | 🇪🇸 [Español](#-español)

---

Script de Python para enviar múltiples mensajes automáticos a un contacto o grupo de WhatsApp Desktop desde Windows.

---

## ⚠️ Legal Notice

This script is intended **for personal and educational use only**, such as automating reminders, tests, or jokes between friends with their consent. Using this tool for spam, harassment, or any malicious activity **is your responsibility**. Use it wisely.

---

## 🧰 Requirements

- Windows 10/11
- [WhatsApp Desktop](https://www.whatsapp.com/download) installed and logged in
- Python 3.7 or higher
- `pywinauto` and `pyperclip` libraries

---

## 📦 Installation

1. Clone or download this repository:

```bash
git clone https://github.com/your-username/whatsapp-spammer.git
cd whatsapp-spammer
```

2. Install the required dependencies:

```bash
pip install pywinauto pyperclip
```

3. Make sure **WhatsApp Desktop is open** before running the script.

---

## 🚀 Usage

Run the script from the terminal:

```bash
python spammer.py
```

The script will ask for three inputs:

| Field | Description |
|---|---|
| `Contact/group name` | Exact name as it appears in WhatsApp |
| `Message to send` | The text you want to send |
| `How many times?` | Number of times the message will be sent |

### Example

```
Contact/group name: Juan Pérez
Message to send: Hello buddy!
How many times?: 5
```

---

## ⚙️ How it works

The script uses `pywinauto` to control WhatsApp Desktop and `pyperclip` to handle the clipboard:

1. **Connects** to the WhatsApp Desktop window and brings it to the front with `set_focus()`.
2. **Opens the contact search** with `Ctrl+N` (more direct than `Ctrl+F`).
3. **Types the contact name** and selects the first result with `Enter`.
4. **Copies the message** to the system clipboard with `pyperclip`.
5. **Pastes and sends** with `Ctrl+V` + `Enter` in a loop, avoiding issues with special characters or spaces.

---

## 🐛 Known Issues

- **El contacto no se encuentra:** asegúrate de escribir el nombre exactamente como aparece en WhatsApp.
- **Los mensajes se envían al chat equivocado:** espera a que WhatsApp cargue completamente antes de ejecutar. Puedes aumentar los `time.sleep()` si tu PC es lenta.
- **El script no detecta la ventana:** verifica que WhatsApp Desktop esté abierto y visible (no minimizado en la bandeja).
- **No funciona si estás en una llamada activa:** WhatsApp bloquea la navegación de chats durante llamadas.
- **Solo funciona en Windows:** tanto `pywinauto` como los atajos de teclado usados dependen de la API de Windows.

---

## 📁 Project Structure

```
whatsapp-spammer/
├── spammer.py       # Main script
└── README.md        # This file
```

---

## 🤝 Contribuciones

Si tienes mejoras, como soporte para múltiples contactos o interfaz gráfica, abre un Pull Request. ¡Todo suma!

---

*¡Lista la vueltica Patron!* 🫡