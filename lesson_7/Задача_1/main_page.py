from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()

    # Заполнение формы с персональными данными
    def fill_form(self, first_name, last_name, address, email, phone,
                  zip_code, city, country, job_position, company):
        self.driver.find_element(By.NAME, "first-name").send_keys(first_name)
        self.driver.find_element(By.NAME, "last-name").send_keys(last_name)
        self.driver.find_element(By.NAME, "address").send_keys(address)
        self.driver.find_element(By.NAME, "e-mail").send_keys(email)
        self.driver.find_element(By.NAME, "phone").send_keys(phone)
        self.driver.find_element(By.NAME, "zip-code").send_keys(zip_code)
        self.driver.find_element(By.NAME, "city").send_keys(city)
        self.driver.find_element(By.NAME, "country").send_keys(country)
        self.driver.find_element(By.NAME, "job-position").send_keys(
            job_position)
        self.driver.find_element(By.NAME, "company").send_keys(company)

        button = self.driver.find_element(By.CSS_SELECTOR, 'button.btn')
        ActionChains(self.driver).move_to_element(button).perform()
        button.click()

    # Вызов метода для определения, имеют ли поле ввода красный цвет,
    # если оно не заполнено
    def zip_code_red(self):
        zip_code_color = self.driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
        return zip_code_color == 'rgba(248, 215, 218, 1)'

    # Вызов метода для определения, имеют ли поля ввода зеленый цвет,
    #  если они заполнены
    def other_fields_green(self):    
        other_fields = ["#first-name", "#last-name", "#address", "#e-mail",
                    "#phone", "#city", "#country", "#job-position", "#company"]
        field_color = []
        for field in other_fields:
            field_color.append(self.driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color"))
        return field_color