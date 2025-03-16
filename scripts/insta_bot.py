import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import yaml
import os

# Configurar el registro
log_path = os.path.join(os.path.dirname(__file__), '../logs/bot.log')
logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cargar configuraciones y credenciales
config_path = os.path.join(os.path.dirname(__file__), '../config/config.yaml')
credentials_path = os.path.join(os.path.dirname(__file__), '../config/credentials.yaml')

with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

with open(credentials_path, 'r') as file:
    credentials = yaml.safe_load(file)

# Configuración de opciones para Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--mute-audio")

# Ruta del chromedriver
chromedriver_path = 'C:/Users/Vinay/Downloads/chromedriver_win32/chromedriver.exe'
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Ventana para aceptar entradas: usuario, contraseña y hashtags
user = credentials['username']
passw = credentials['password']
hash = input("Enter hashtags separated by comma: ")

# Abriendo la página de inicio de sesión de Instagram
logging.info('Abriendo la página de inicio de sesión de Instagram')
driver.get(config['instagram']['base_url'] + config['instagram']['login_url'])
sleep(5)

# Ingresar nombre de usuario y contraseña
logging.info('Ingresando nombre de usuario y contraseña')
username = driver.find_element(By.NAME, 'username')
username.send_keys(user)
password = driver.find_element(By.NAME, 'password')
password.send_keys(passw)

# Encontrar y hacer clic en el botón de inicio de sesión
logging.info('Haciendo clic en el botón de inicio de sesión')
button_login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
button_login.click()
sleep(5)

# Hacer clic en el botón "Not Now" para desactivar las notificaciones
logging.info('Haciendo clic en el botón "Not Now" para desactivar las notificaciones')
not_now_buttons = driver.find_elements(By.XPATH, '//button[contains(text(), "Not Now")]')
for button in not_now_buttons:
    try:
        button.click()
        sleep(2)
    except:
        continue

# Procesar hashtags
hashtag_list = hash.split(',')
for hashtag in hashtag_list:
    logging.info(f'Procesando hashtag: {hashtag}')
    driver.get(f"{config['instagram']['base_url']}{config['instagram']['explore_url']}{hashtag}/")
    sleep(5)

    # Hacer clic en la primera miniatura
    first_thumbnail = driver.find_element(By.XPATH, '//div[contains(@class, "_9AhH0")]')
    first_thumbnail.click()
    sleep(3)

    for _ in range(1, 200):
        sleep(randint(3, 7))
        
        # Intentar encontrar y hacer clic en el botón de "Me gusta"
        try:
            like_button = driver.find_element(By.XPATH, '//span[@aria-label="Like"]')
            like_button.click()
            logging.info('Foto marcada con "Me gusta"')
        except Exception as e:
            logging.error(f"Error al dar 'Me gusta': {e}")
            continue

        sleep(randint(3, 7))

        # Probabilidad de comentar
        comm_prob = randint(1, 4)
        if comm_prob == 1:
            comment_text = "Really cool!"
        elif comm_prob == 2:
            comment_text = "Nice work :)"
        elif comm_prob == 3:
            comment_text = "Nice gallery!!"
        else:
            comment_text = "So cool! :)"

        # Intentar encontrar y hacer clic en el cuadro de comentarios
        try:
            comment_box = driver.find_element(By.XPATH, '//textarea[@aria-label="Add a comment…"]')
            comment_box.click()
            comment_box.send_keys(comment_text)
            sleep(2)
            comment_box.send_keys(Keys.ENTER)
            logging.info(f'Comentario publicado: {comment_text}')
        except Exception as e:
            logging.error(f"Error al comentar: {e}")
            continue

        sleep(randint(22, 28))

        # Intentar encontrar y hacer clic en el botón "Next"
        try:
            next_button = driver.find_element(By.LINK_TEXT, 'Next')
            next_button.click()
            sleep(randint(25, 29))
        except Exception as e:
            logging.error(f"Error al ir a la siguiente foto: {e}")
            break

# Cerrar el navegador
logging.info('Cerrando el navegador')
driver.quit()