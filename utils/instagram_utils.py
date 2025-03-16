from selenium.webdriver.common.by import By
from time import sleep
from random import randint

def login(driver, username, password):
    """Inicia sesión en Instagram"""
    driver.get('https://www.instagram.com/accounts/login/')
    sleep(5)
    
    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys(username)
    
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)
    
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()
    sleep(5)

def like_post(driver):
    """Da 'Me gusta' a una publicación"""
    try:
        like_button = driver.find_element(By.XPATH, '//span[@aria-label="Like"]')
        like_button.click()
        sleep(randint(2, 5))
        return True
    except Exception as e:
        print(f"Error al dar 'Me gusta': {e}")
        return False

def comment_on_post(driver, comment_text):
    """Comenta en una publicación"""
    try:
        comment_box = driver.find_element(By.XPATH, '//textarea[@aria-label="Add a comment…"]')
        comment_box.click()
        comment_box.send_keys(comment_text)
        sleep(2)
        comment_box.send_keys(Keys.ENTER)
        sleep(randint(2, 5))
        return True
    except Exception as e:
        print(f"Error al comentar: {e}")
        return False

def follow_account(driver):
    """Sigue a una cuenta"""
    try:
        follow_button = driver.find_element(By.XPATH, '//button[text()="Follow"]')
        follow_button.click()
        sleep(randint(2, 5))
        return True
    except Exception as e:
        print(f"Error al seguir la cuenta: {e}")
        return False