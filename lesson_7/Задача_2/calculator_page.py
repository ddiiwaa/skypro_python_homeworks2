from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open_page(self, url):
        # Открываем указанную страницу
        self.driver.get(url)

    def enter_delay_value(self, delay_value):
        # Находим поле ввода и вводим в него заданное значение
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def click_button(self, button_text):
        # Находим кнопку по тексту и кликаем на нее
        button_locator = f"//span[contains(@class, 'btn-outline-primary') and text()='{button_text}']"
        button = self.driver.find_element(By.XPATH, button_locator)
        button.click()

    def click_operator_button(self, operator):
        operator_locator = f"//span[contains(@class, 'operator') and text()='{operator}']"
        operator_button = self.driver.find_element(By.XPATH, operator_locator)
        operator_button.click()

    def click_equals_button(self):
        equals_locator = "//span[contains(@class, 'btn-outline-warning') and text()='=']"
        equals_button = self.driver.find_element(By.XPATH, equals_locator)
        equals_button.click()

    def get_result_text(self):
        WebDriverWait(self.driver, 6).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
        result = self.driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return result