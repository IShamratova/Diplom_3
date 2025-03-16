import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы по URL')
    def open_url(self, url):
        #Открывает страницу по переданному URL
        self.driver.get(url)

    @allure.step('Поиск элемента по XPATH')
    def find_element_by_xpath(self, xpath):
        # поиск и выдача элемента
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step('Поиск элемента по XPATH')
    def find_elements_by_xpath(self, xpath):
        # поиск и выдача элемента
        return self.driver.find_elements(By.XPATH, xpath)

    @allure.step('Ожидание появления элемента по XPATH с заданным таймаутом')
    def wait_for_visibility_of_element_by_xpath_by_timeout(self, xpath, timeout):
        # явное ожидание для загрузки страницы
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath))
        )

    @allure.step('Ожидание загрузки новой вкладки с заданным таймаутом')
    def wait_for_new_tab_by_timeout(self, timeout):
        # явное ожидание появления новой вкладки
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.number_of_windows_to_be(2)
        )

    @allure.step('Ожидание загрузки ресурса с заданным таймаутом')
    def wait_for_loading_url_by_timeout(self, url, timeout):
        # явное ожидание для загрузки страницы
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_to_be(url)
        )

    @allure.step('Ожидание загрузки ресурса с заданным таймаутом')
    def wait_for_text_differing_from_given_by_timeout(self, xpath, given_text, timeout):
        # явное ожидание для загрузки страницы
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(By.XPATH, xpath).text.strip() != str(given_text)
        )

    @allure.step('Прокрутка страницы до элемента по XPATH')
    def scroll_to_element_by_xpath(self, xpath):
        # поиск элемента
        element = self.driver.find_element(By.XPATH, xpath)

        # прокрутка страницы до элемента
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Установка видимости элемента через скрипт по XPATH')
    def remove_elements_by_script(self):
        # поиск элемента
        element = self.driver.find_element(By.CSS_SELECTOR, ".Modal_modal__P3_V5")
        # удаление элемента
        self.driver.execute_script("arguments[0].remove();", element)

        # поиск элемента
        element = self.driver.find_element(By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr")
        # удаление элемента
        self.driver.execute_script("arguments[0].remove();", element)

    @allure.step('Нажатие на элемент через скрипт по XPATH')
    def click_element_by_script_by_xpath(self, xpath):
        # поиск элемента и клик по нему
        element = self.driver.find_element(By.XPATH, xpath)

        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Нажатие на элемент по XPATH')
    def click_element_by_xpath(self, xpath):
        # поиск элемента и клик по нему
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step('Ввод текста в поле по XPATH')
    def set_text_to_field_by_xpath(self, xpath, text):
        # поиск поля и ввод данных
        self.driver.find_element(By.XPATH, xpath).send_keys(text)

    @allure.step('Переключение на новую вкладку')
    def switch_to_new_tab(self):
        # явное ожидание для загрузки новой вкладки
        self.wait_for_new_tab_by_timeout(10)

        # получение списка всех вкладок
        windows = self.driver.window_handles

        # переключение на новую вкладку
        self.driver.switch_to.window(windows[1])

    @allure.step('Проверка адреса страницы')
    def check_url(self, url):
        # явное ожидание для загрузки новой страницы dzen
        self.wait_for_loading_url_by_timeout(url, 10)

        assert self.driver.current_url == url

    @allure.step('Перетаскивание элемента')
    def drag_n_drop_element(self, source_element_xpath, target_element_xpath):
        source = self.find_element_by_xpath(source_element_xpath)
        target = self.find_element_by_xpath(target_element_xpath)

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

        # Выполняем функцию с нашими элементами
        self.driver.execute_script(drag_and_drop_js + "simulateDragDrop(arguments[0], arguments[1]);", source, target)