from .base_page import BasePage
from .locators import AuthLocators

class AuthPage(BasePage):

    def __init__(self, driver, url="https://b2c.passport.rt.ru/auth"):
        self.driver = driver
        self.url = url
        super().__init__(self.driver, url=self.url)

        # Создаем нужные элементы

        self.email = driver.find_element(*AuthLocators.auth_username)
        self.phone = driver.find_element(*AuthLocators.auth_username)
        self.password = driver.find_element(*AuthLocators.auth_password)
        self.btn = driver.find_element(*AuthLocators.auth_btn)
        self.btn_reg = driver.find_element(*AuthLocators.auth_reg)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_phone(self, value):
        self.phone.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()

    def open_registration_page(self):
        self.btn_reg.click()

class AuthRegistration(BasePage):

    def __init__(self, driver, url=""):
        self.driver = driver
        self.url = url
        super().__init__(self.driver, url=self.url)

        # Создаем нужные элементы

        self.first_name = driver.find_element(*AuthLocators.auth_first_name)
        self.last_name = driver.find_element(*AuthLocators.auth_last_name)
        self.city = driver.find_element(*AuthLocators.auth_city)
        self.email = driver.find_element(*AuthLocators.auth_email)
        self.phone = driver.find_element(*AuthLocators.auth_phone)
        self.password = driver.find_element(*AuthLocators.auth_password)
        self.password_conf = driver.find_element(*AuthLocators.auth_pass_conf)
        self.btn = driver.find_element(*AuthLocators.auth_reg_btn)

    def enter_firstname_reg(self, value):
        self.first_name.send_keys(value)

    def enter_lastname_reg(self, value):
        self.last_name.send_keys(value)

    def enter_city_reg(self, value):
        self.city.send_keys(value)

    def enter_email_reg(self, value):
        self.email.send_keys(value)

    def enter_phone_reg(self, value):
        self.phone.send_keys(value)

    def enter_pass_reg(self, value):
        self.password.send_keys(value)

    def enter_pass_conf_reg(self, value):
        self.password_conf.send_keys(value)

    def btn_click_reg(self):
        self.btn.click()

