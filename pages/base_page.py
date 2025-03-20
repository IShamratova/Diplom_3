import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы по URL')
    def open_url(self, url):
        # Открытие страницы по URL
        self.driver.get(url)

    @allure.step('Поиск элемента по XPATH')
    def find_element_by_xpath(self, xpath):
        # Поиск и выдача элемента
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step('Поиск элементов по XPATH')
    def find_elements_by_xpath(self, xpath):
        # Поиск и выдача элементов
        return self.driver.find_elements(By.XPATH, xpath)

    @allure.step('Явное ожидание появления элемента по XPATH с заданным таймаутом')
    def wait_for_visibility_of_element_by_xpath_by_timeout(self, xpath, timeout):
        # Явное ожидание для загрузки страницы
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath))
        )

    @allure.step('Явное ожидание загрузки новой вкладки с заданным таймаутом')
    def wait_for_new_tab_by_timeout(self, timeout):
        # Явное ожидание появления новой вкладки
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.number_of_windows_to_be(2)
        )

    @allure.step('Явное ожидание загрузки ресурса с заданным таймаутом')
    def wait_for_loading_url_by_timeout(self, url, timeout):
        # Явное ожидание для загрузки URL
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_to_be(url)
        )

    @allure.step('Явное ожидание загрузки текста, отличающегося от переданного, с заданным таймаутом')
    def wait_for_text_differing_from_given_by_timeout(self, xpath, given_text, timeout):
        # Явное ожидание для загрузки текста
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(By.XPATH, xpath).text.strip() != str(given_text)
        )

    @allure.step('Явное ожидание загрузки текста, равному переданному, с заданным таймаутом')
    def wait_for_text_equals_to_given_by_timeout(self, xpath, given_text, timeout):
        # Явное ожидание для загрузки текста
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(By.XPATH, xpath).text.strip() == str(given_text)
        )

    @allure.step('Прокрутка страницы до элемента по XPATH')
    def scroll_to_element_by_xpath(self, xpath):
        # Поиск элемента
        element = self.driver.find_element(By.XPATH, xpath)

        # Прокрутка страницы до элемента
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Установка видимости элемента через скрипт по XPATH')
    def remove_elements_by_script(self, xpaths):

        for xpath in xpaths:
            # Поиск элемента
            element = self.driver.find_element(By.XPATH, xpath)
            # Удаление элемента
            self.driver.execute_script("arguments[0].remove();", element)

    @allure.step('Клик по элементу по XPATH')
    def click_element_by_xpath(self, xpath):
        # Поиск элемента и клик по нему
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step('Клик по элементу через скрипт по XPATH')
    def click_element_by_script_by_xpath(self, xpath):
        # Поиск элемента
        element = self.driver.find_element(By.XPATH, xpath)

        # Клик по элементу
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ввод текста в поле по XPATH')
    def set_text_to_field_by_xpath(self, xpath, text):
        # Поиск поля и ввод данных в него
        self.driver.find_element(By.XPATH, xpath).send_keys(text)

    @allure.step('Переключение на новую вкладку')
    def switch_to_new_tab(self):
        # Явное ожидание для загрузки новой вкладки
        self.wait_for_new_tab_by_timeout(10)

        # Получение списка всех вкладок
        windows = self.driver.window_handles

        # Переключение на новую вкладку
        self.driver.switch_to.window(windows[1])

    @allure.step('Проверка адреса страницы')
    def check_url(self, url):
        # Явное ожидание для загрузки новой страницы dzen
        self.wait_for_loading_url_by_timeout(url, 10)

        # Сравнение текущего URL с переданным
        assert self.driver.current_url == url

    @allure.step('Проверка нахождения текста в адресе страницы')
    def check_text_in_current_url(self, text):

        # Сравнение находится ли текст внутри текущего URL
        assert text in self.driver.current_url

    @allure.step('Перетаскивание элемента')
    def drag_n_drop_element(self, source_element_xpath, target_element_xpath):
        # Элемент перетаскивания
        source = self.find_element_by_xpath(source_element_xpath)

        # Элемент целевой области перетаскивания
        target = self.find_element_by_xpath(target_element_xpath)

        # Функция для работы перетаскивания
        drag_and_drop_js = """
        function simulateDragDrop(sourceNode, destinationNode) {
            var EVENT_TYPES = {
                DRAG_START: 'dragstart',
                DROP: 'drop',
                DRAG_END: 'dragend'
            };

            function createCustomEvent(type) {
                var event = new CustomEvent("CustomEvent");
                event.initCustomEvent(type, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function(format, data) {
                        this.data[format] = data;
                    },
                    getData: function(format) {
                        return this.data[format];
                    }
                };
                return event;
            }

            function dispatchEvent(node, type, event) {
                if (node.dispatchEvent) {
                    return node.dispatchEvent(event);
                }
                if (node.fireEvent) {
                    return node.fireEvent("on" + type, event);
                }
            }

            var dragStartEvent = createCustomEvent(EVENT_TYPES.DRAG_START);
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, dragStartEvent);

            var dropEvent = createCustomEvent(EVENT_TYPES.DROP);
            dropEvent.dataTransfer = dragStartEvent.dataTransfer;
            dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent);

            var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END);
            dragEndEvent.dataTransfer = dragStartEvent.dataTransfer;
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent);
        }
        """

        # Выполнение функции для перетаскивания элементами
        self.driver.execute_script(drag_and_drop_js + "simulateDragDrop(arguments[0], arguments[1]);", source, target)