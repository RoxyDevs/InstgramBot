from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def create_driver(chromedriver_path):
    """Crea y configura un driver de Selenium para Chrome"""
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--mute-audio")

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver

def navigate_to_hashtag(driver, base_url, hashtag):
    """Navega a la página de un hashtag específico en Instagram"""
    url = f"{base_url}/explore/tags/{hashtag}/"
    driver.get(url)
    sleep(5)

def click_first_thumbnail(driver):
    """Hace clic en la primera miniatura de la página del hashtag"""
    try:
        first_thumbnail = driver.find_element(By.XPATH, '//div[contains(@class, "_9AhH0")]')
        first_thumbnail.click()
        sleep(3)
        return True
    except Exception as e:
        print(f"Error al hacer clic en la primera miniatura: {e}")
        return False

def click_next_button(driver):
    """Hace clic en el botón 'Next' para ir a la siguiente publicación"""
    try:
        next_button = driver.find_element(By.LINK_TEXT, 'Next')
        next_button.click()
        sleep(randint(2, 5))
        return True
    except Exception as e:
        print(f"Error al hacer clic en el botón 'Next': {e}")
        return False