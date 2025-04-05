class TestData:
    # URL тестового стенда
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    BASE_API_URL = BASE_URL + "api/"
    CREATE_USER_API_URL = BASE_API_URL + "auth/register"
    DELETE_USER_API_URL = BASE_API_URL + "auth/user"
    LOGIN_USER_API_URL = BASE_API_URL + "auth/login"
    ORDERS_API_URL = BASE_API_URL + "orders"

    # Список путей URL
    ROUTES = {
        "feed": "feed",
        "forgot_password": "forgot-password",
        "login": "login",
        "order_history": "account/order-history",
        "profile": "account/profile",
        "reset_password": "reset-password"
    }

    EMAIL_TEXT = "ya@ya.ya"

