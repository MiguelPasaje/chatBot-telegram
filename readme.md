# Chat Bot de Telegram

Este chatbot de Telegram es un proyecto simple que puedes usar como punto de partida para crear tu propio bot de Telegram. Sigue estos pasos para configurar y ejecutar el bot:

### Instalación de Dependencias

Primero, asegúrate de tener todas las dependencias necesarias instaladas ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

Crea un archivo llamado config.py en el mismo directorio que tu script principal. En config.py, define una variable TOKEN y asigna el token que obtuviste de BotFather:

```bash
TOKEN = 'TU_TOKEN_AQUI'
```
## Token
busca en telegram `BotFather` y sigue las instrucciones para tener tu bot

### Ejecución del Bot

```bash
python mi_chatbot.py

```
#### Uso
Este bot está configurado para responder a los comandos /start y /help con mensajes predeterminados. Puedes personalizar las respuestas y agregar funcionalidades adicionales según tus necesidades.

### Referencias
- <a href="https://core.telegram.org/api">Api Telegram Bot </a>

- <a href="https://pytba.readthedocs.io/en/latest/quick_start.html">Quick start</a>
libreria para desarrollar el funcionamiento del bot en python.

- <a href="https://github.com/eternnoir/pyTelegramBotAPI#getting-started">pyTelegramBotAPI
</a> repositorio github