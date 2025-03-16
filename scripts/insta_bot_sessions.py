from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

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
user = input("Enter username: ")
passw = input("Enter password: ")
hash = input("Enter hashtags separated by comma: ")

# Abriendo la página de inicio de sesión de Instagram
driver.get('https://www.instagram.com/accounts/login/')
sleep(5)

# Ingresar nombre de usuario y contraseña
username = driver.find_element(By.NAME, 'username')
username.send_keys(user)
password = driver.find_element(By.NAME, 'password')
password.send_keys(passw)

# Encontrar y hacer clic en el botón de inicio de sesión
button_login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
button_login.click()
sleep(5)

# Hacer clic en el botón "Not Now" para desactivar las notificaciones
not_now_buttons = driver.find_elements(By.XPATH, '//button[contains(text(), "Not Now")]')
for button in not_now_buttons:
    try:
        button.click()
        sleep(2)
    except:
        continue

# Función para seguir cuentas en base a hashtags
def follow_accounts_by_hashtag(hashtag, follow_limit=50):
    driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
    sleep(5)

    # Hacer clic en la primera miniatura
    first_thumbnail = driver.find_element(By.XPATH, '//div[contains(@class, "_9AhH0")]')
    first_thumbnail.click()
    sleep(3)

    followed = 0  # Contador de cuentas seguidas
    for _ in range(1, follow_limit + 1):  # Limitar el número de seguimientos por sesión
        try:
            follow_button = driver.find_element(By.XPATH, '//button[text()="Follow"]')
            follow_button.click()
            followed += 1
            sleep(randint(5, 10))
        except Exception as e:
            print(f"Error al seguir la cuenta: {e}")
            break

        try:
            next_button = driver.find_element(By.LINK_TEXT, 'Next')
            next_button.click()
            sleep(randint(5, 10))
        except Exception as e:
            print(f"Error al ir a la siguiente foto: {e}")
            break

    print(f"Total de cuentas seguidas en esta sesión: {followed}")

# Llamar a la función para seguir cuentas basadas en hashtags en varias sesiones
hashtag_list = hash.split(',')
sessions_per_day = 4  # Número de sesiones por día
follow_limit_per_session = 50  # Límites de seguimientos por sesión

for _ in range(sessions_per_day):
    for hashtag in hashtag_list:
        follow_accounts_by_hashtag(hashtag, follow_limit=follow_limit_per_session)
    # Esperar antes de la siguiente sesión
    sleep(randint(3600, 7200))  # Esperar entre 1 y 2 horas

# Cerrar el navegador
driver.quit()