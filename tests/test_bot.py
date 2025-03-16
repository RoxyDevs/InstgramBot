import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import yaml
import os

class TestInstagramBot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configuración de opciones para Chrome
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--mute-audio")
        
        # Ruta del chromedriver
        chromedriver_path = 'C:/Users/Vinay/Downloads/chromedriver_win32/chromedriver.exe'
        service = Service(executable_path=chromedriver_path)
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Cargar configuraciones y credenciales
        config_path = os.path.join(os.path.dirname(__file__), '../config/config.yaml')
        credentials_path = os.path.join(os.path.dirname(__file__), '../config/credentials.yaml')

        with open(config_path, 'r') as file:
            cls.config = yaml.safe_load(file)

        with open(credentials_path, 'r') as file:
            cls.credentials = yaml.safe_load(file)
        
        # Iniciar sesión en Instagram
        cls.driver.get(cls.config['instagram']['base_url'] + cls.config['instagram']['login_url'])
        cls.driver.implicitly_wait(5)
        
        username = cls.driver.find_element_by_name('username')
        username.send_keys(cls.credentials['username'])
        password = cls.driver.find_element_by_name('password')
        password.send_keys(cls.credentials['password'])
        
        button_login = cls.driver.find_element_by_css_selector('button[type="submit"]')
        button_login.click()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        # Verificar que la URL después del inicio de sesión no sea la página de inicio de sesión
        current_url = self.driver.current_url
        self.assertNotIn('accounts/login', current_url)
    
    def test_like_post(self):
        # Navegar a una página de hashtag
        hashtag = 'test'
        self.driver.get(f"{self.config['instagram']['base_url']}{self.config['instagram']['explore_url']}{hashtag}/")
        self.driver.implicitly_wait(5)
        
        # Hacer clic en la primera miniatura
        first_thumbnail = self.driver.find_element_by_xpath('//div[contains(@class, "_9AhH0")]')
        first_thumbnail.click()
        self.driver.implicitly_wait(3)
        
        # Intentar encontrar y hacer clic en el botón de "Me gusta"
        like_button = self.driver.find_element_by_xpath('//span[@aria-label="Like"]')
        like_button.click()
        self.driver.implicitly_wait(3)
        
        # Verificar que el botón de "Me gusta" ha cambiado a "No me gusta"
        liked_button = self.driver.find_element_by_xpath('//span[@aria-label="Unlike"]')
        self.assertIsNotNone(liked_button)

if __name__ == '__main__':
    unittest.main()