import pytest
import requests
from faker import Faker
from data.data import TestData
from utils.driver_factory import DriverFactory

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    # Настройка драйверов браузеров
    driver = DriverFactory.get_driver(request.param)

    # Раскрытие окна драйвера
    driver.maximize_window()

    yield driver

    # Закрытие браузера после теста
    driver.quit()

fake = Faker()

@pytest.fixture
def created_user():
    # Создание нового пользователя без авторизации и выдача его данных
    email = f"{fake.random_int()}_{fake.email()}" # Генерируем уникальный email
    password = fake.password()
    name = fake.name()

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(TestData.CREATE_USER_API_URL, json=payload)

    return {
        "email": email,
        "password": password,
        "name": name,
        "response": response
    }

@pytest.fixture
def authorized_user(logged_in_user):
    # Удаление пользователя после теста

    yield logged_in_user

    headers = {"Authorization": logged_in_user["accessToken"]}
    requests.delete(TestData.DELETE_USER_API_URL, headers=headers)