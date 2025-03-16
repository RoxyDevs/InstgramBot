from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

# Procesar hashtags
hashtag_list = hash.split(',')
for hashtag in hashtag_list:
    driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
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
        except Exception as e:
            print(f"Error al dar 'Me gusta': {e}")
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
        except Exception as e:
            print(f"Error al comentar: {e}")
            continue

        sleep(randint(22, 28))

        # Intentar encontrar y hacer clic en el botón "Next"
        try:
            next_button = driver.find_element(By.LINK_TEXT, 'Next')
            next_button.click()
            sleep(randint(25, 29))
        except Exception as e:
            print(f"Error al ir a la siguiente foto: {e}")
            break

# Cerrar el navegador
driver.quit()