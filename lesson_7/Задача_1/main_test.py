import pytest
from selenium import webdriver
from main_page import MainPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_registration(driver):
    registration_page = MainPage(driver)
    registration_page.fill_form(
        first_name="Иван",
        last_name="Петров",
        address="Ленина, 55-3",
        email="test@skypro.com",
        phone="+7985899998787",
        zip_code="",
        city="Москва",
        country="Россия",
        job_position="QA",
        company="SkyPro"
    )

    test_red = registration_page.zip_code_red()
    assert 1 == test_red

    test_green = registration_page.other_fields_green()
    for green in test_green:
        assert green == 'rgba(209, 231, 221, 1)'

# print("Тест успешно пройден!")