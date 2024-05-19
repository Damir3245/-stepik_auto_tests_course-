import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждем, пока цена дома не станет $100
    wait = WebDriverWait(browser, 12)
    price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажимаем на кнопку "Book"
    button = browser.find_element(By.ID, "book")
    button.click()
    # Считываем значение переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)

    # Вычисляем математическую функцию от x
    result = math.log(abs(12*math.sin(x)))



    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.CSS_SELECTOR,"#answer")
    answer_input.send_keys(str(result))



# Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
    submit_button.click()
finally:

 time.sleep(10)
browser.quit()