# Instagram Bot

Este es un bot de Instagram que aumenta tus seguidores mediante métodos orgánicos. No utiliza técnicas de seguir-dejar de seguir.

## Requisitos

- Python 3.x
- Selenium
- Chromedriver

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/RoxyDevs/InstgramBot.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd InstgramBot
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Configuración

Asegúrate de configurar tus credenciales en `config/credentials.yaml` y cualquier otra configuración en `config/config.yaml`.

### Ejecución del Bot

Para ejecutar el bot principal:
```bash
python scripts/insta_bot.py
```

Para ejecutar el bot con sesiones distribuidas:
```bash
python scripts/insta_bot_sessions.py
```

## Contribución

Si deseas contribuir a este proyecto, por favor abre un issue o crea un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.