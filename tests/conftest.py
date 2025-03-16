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
    #Создаёт нового пользователя без авторизации и возвращает его данные.
    email = f"{fake.random_int()}_{fake.email()}" # Генерируем уникальный email
    password = fake.password()
    name = fake.name()

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(TestData.CREATE_USER_API_URL, json=payload)
    assert response.status_code == 200, f"Ошибка при создании пользователя: {response.text}"

    data = response.json()
    assert data["success"] is True, "Неуспешное создание пользователя"

    return {
        "email": email,
        "password": password,
        "name": name
    }

@pytest.fixture
def authorized_user(logged_in_user):
    # Авторизует пользователя и удаляет его после теста.
    yield logged_in_user

    # Удаляем пользователя после теста
    headers = {"Authorization": logged_in_user["accessToken"]}
    response = requests.delete(TestData.DELETE_USER_API_URL, headers=headers)
    data = response.json()
    assert data["message"] == "User successfully removed", "Пользователь не удалён"

    headers = {"Authorization": logged_in_user["accessToken"]}
    response = requests.get(TestData.ORDERS_API_URL, headers=headers)

    assert response.status_code == 200, f"Ошибка: {response.text}"
    data = response.json()