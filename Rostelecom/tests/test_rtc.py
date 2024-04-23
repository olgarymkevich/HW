import time
from selenium.webdriver.common.by import By
from pages.locators import AuthLocators
from pages.auth_page import AuthPage
from pages.auth_page import AuthRegistration
from pages.settings import valid_email, valid_password, valid_login

#1
def test_auth_page_right(driver):
    """Проверка, что в правой части страницы авторизации отображена форма авторизации"""

    time.sleep(10)
    page = AuthPage(driver)
    assert driver.find_element(*AuthLocators.auth_page_right)
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"

#2
def test_auth_page_left(driver):
    """Проверка, что в левой части страницы авторизации
    отображены вспомогательная информация для клиента и лого Ростелеком"""

    time.sleep(10)
    page = AuthPage(driver)
    assert driver.find_element(*AuthLocators.auth_page_left)
    assert driver.find_element(By.TAG_NAME, 'h2').text == "Личный кабинет"
    assert driver.find_element(*AuthLocators.auth_logo)

#3
def test_auth_btn_tab(driver):
    """Проверка, что форма авторизации содержит меню выбора типа аутентификации"""

    time.sleep(10)
    page = AuthPage(driver)
    assert driver.find_element(*AuthLocators.btn_tab_phone)
    assert driver.find_element(*AuthLocators.btn_tab_email)
    assert driver.find_element(*AuthLocators.btn_tab_login)
    assert driver.find_element(*AuthLocators.btn_tab_ls)

#4
def test_auth_form_username(driver):
    """Проверка, что форма авторизации содержит форму ввода "Номер", "Логин", "Почта", "Лицевой счет"
    и по умолчанию выбрана форма авторизации по телефону"""

    time.sleep(10)
    page = AuthPage(driver)
    assert driver.find_element(*AuthLocators.auth_username)
    assert driver.find_element(*AuthLocators.tab_phone)

#5
def test_auth_form_password(driver):
    """Проверка, что форма авторизации содержит форму ввода "Пароль"""

    time.sleep(10)
    page = AuthPage(driver)
    assert driver.find_element(*AuthLocators.auth_password)

#6
def test_change_btn_tab_email(driver):
    """Проверка, что при вводе почты в форму ввода телефона пользователя,
    таб выбора аутентификации меняется автоматически на почту"""

    time.sleep(10)
    page = AuthPage(driver)
    page.enter_phone(valid_email)
    driver.find_element(*AuthLocators.auth_password).click()

    assert driver.find_element(*AuthLocators.tab_email)

#7
def test_change_btn_tab_login(driver):
    """Проверка, что при вводе логина в форму ввода телефона пользователя,
    таб выбора аутентификации меняется автоматически на логин"""

    time.sleep(10)
    page = AuthPage(driver)
    page.enter_phone(valid_login)
    driver.find_element(*AuthLocators.auth_password).click()

    assert driver.find_element(*AuthLocators.tab_login)

#8
def test_auth_valid_data(driver):
    """Проверка, что при вводе валидных email и пароль, идет переход в личный кабинет пользователя"""

    time.sleep(10)
    page = AuthPage(driver)
    page.enter_email(valid_email)
    page.enter_pass(valid_password)
    page.btn_click()

    assert driver.find_element(By.TAG_NAME, 'h2').text == "Рымкевич\nОльга"

#9
def test_auth_invalid_password(driver):
    """Проверка, что при вводе валидного email и невалидного пароля, переход в личный кабинет не происходит
    и отображается ошибка"""

    time.sleep(10)
    page = AuthPage(driver)
    page.enter_email(valid_email)
    page.enter_pass("12345")
    page.btn_click()

    assert driver.find_element(*AuthLocators.auth_form_error)

#10
def test_auth_invalid_email(driver):
    """Проверка, что при вводе невалидного email и валидного пароля, переход в личный кабинет не происходит
    и отображается ошибка"""

    time.sleep(10)
    page = AuthPage(driver)
    page.enter_email("test@mail.ru")
    page.enter_pass(valid_password)
    page.btn_click()

    assert driver.find_element(*AuthLocators.auth_form_error)

#11
def test_auth_invalid_data(driver):
    """Проверка, что при вводе невалидных email и пароля, переход в личный кабинет не происходит
    и отображается ошибка"""

    time.sleep(10)
    page = AuthPage(driver)
    page.enter_email("test@mail.ru")
    page.enter_pass("Oooo12345")
    page.btn_click()

    assert driver.find_element(*AuthLocators.auth_form_error)

#12
def test_btn_reg(driver):
    """Проверка, что при нажатии на ссылку регистрации, происходит переход к форме "Регистрация"""

    time.sleep(10)
    page = AuthPage(driver)
    driver.find_element(*AuthLocators.auth_reg).click()

    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"

#13
def test_forgot_password(driver):
    """Проверка, что при нажатии на ссылку "Забыл пароль", происходит переход к форме "Восстановление пароля"""

    time.sleep(10)
    page = AuthPage(driver)
    driver.find_element(*AuthLocators.auth_forgot_pass).click()

    assert driver.find_element(By.TAG_NAME, 'h1').text == "Восстановление пароля"

#14
def test_reg_page_left(driver):
    """Проверка, что в левой части страницы регистрации отображены
    логотип и продуктовый слоган кабинета"""

    time.sleep(10)
    page = AuthPage(driver)
    page.open_registration_page()

    assert driver.find_element(*AuthLocators.reg_page_left)
    assert driver.find_element(By.TAG_NAME, 'h2').text == "Личный кабинет"
    assert driver.find_element(*AuthLocators.reg_logo)

#15
def test_reg_page_right(driver):
    """Проверка наличия необходимых элементов в правой части страницы регистрации"""

    time.sleep(10)
    page = AuthPage(driver)
    page.open_registration_page()

    assert driver.find_element(*AuthLocators.reg_page_right)
    assert driver.find_element(*AuthLocators.auth_first_name)
    assert driver.find_element(*AuthLocators.auth_last_name)
    assert driver.find_element(*AuthLocators.auth_city)
    assert driver.find_element(*AuthLocators.auth_email)
    assert driver.find_element(*AuthLocators.auth_pass)
    assert driver.find_element(*AuthLocators.auth_pass_conf)
    assert driver.find_element(*AuthLocators.auth_reg_btn)

#16
def test_reg_incorrect_firstname(driver):
    """Проверка, что при попытке регистрации пользователя с некорректными данными (имя), отображается ошибка"""

    time.sleep(10)
    page = AuthPage(driver)
    page.open_registration_page()
    page = AuthRegistration(driver)
    page.enter_firstname_reg('O')
    page.enter_lastname_reg('Рымк')
    page.enter_city_reg('Москва')
    page.enter_email_reg('test@mail.ru')
    page.enter_pass_reg('Qwert12345')
    page.enter_pass_conf_reg('Qwert12345')
    page.btn_click_reg()

    assert driver.find_element(By.XPATH, '//div[1]/span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

#17
def test_reg_incorrect_lastname(driver):
    """Проверка, что при попытке регистрации пользователя с некорректными данными (фамилия), отображается ошибка"""

    time.sleep(10)
    page = AuthPage(driver)
    page.open_registration_page()
    page = AuthRegistration(driver)
    page.enter_firstname_reg('Oльга')
    page.enter_lastname_reg('Р')
    page.enter_city_reg('Москва')
    page.enter_email_reg('test@mail.ru')
    page.enter_pass_reg('Qwert12345')
    page.enter_pass_conf_reg('Qwert12345')
    page.btn_click_reg()

    assert driver.find_element(By.XPATH, '//div[2]/span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

#18
def test_reg_incorrect_email(driver):
    """Проверка, что при попытке регистрации пользователя с некорректными данными (email), отображается ошибка"""

    time.sleep(10)
    page = AuthPage(driver)
    page.open_registration_page()
    page = AuthRegistration(driver)
    page.enter_firstname_reg('Oльга')
    page.enter_lastname_reg('Рымкевич')
    page.enter_city_reg('Москва')
    page.enter_email_reg('olga')
    page.enter_pass_reg('Qwert12345')
    page.enter_pass_conf_reg('Qwert12345')
    page.btn_click_reg()

    assert driver.find_element(By.XPATH, '//span[contains(text(), "Введите телефон в формате +7ХХХХХХХХХХ '
                                         'или +375XXXXXXXXX, или email в формате example@email.ru")]')

#19
def test_reg_incorrect_short_password(driver):
    """Проверка, что при попытке регистрации пользователя с некорректными данными (слишком короткий пароль),
    отображается ошибка"""

    time.sleep(10)
    page = AuthPage(driver)
    page.open_registration_page()
    page = AuthRegistration(driver)
    page.enter_firstname_reg('Oльга')
    page.enter_lastname_reg('Рымкевич')
    page.enter_city_reg('Москва')
    page.enter_email_reg('test@mail.ru')
    page.enter_pass_reg('12345')
    page.enter_pass_conf_reg('12345')
    page.btn_click_reg()

    assert driver.find_element(By.XPATH, '//div[1]/span[contains(text(), "Длина пароля должна быть не менее 8 символов")]')

#20
def test_reg_incorrect_password(driver):
    """Проверка, что при попытке регистрации пользователя с некорректными данными (пароль), отображается ошибка"""

    time.sleep(10)
    page = AuthPage(driver)
    page.open_registration_page()
    page = AuthRegistration(driver)
    page.enter_firstname_reg('Oльга')
    page.enter_lastname_reg('Рымкевич')
    page.enter_city_reg('Москва')
    page.enter_email_reg('test@mail.ru')
    page.enter_pass_reg('12345qwert')
    page.enter_pass_conf_reg('12345qwert')
    page.btn_click_reg()

    assert driver.find_element(By.XPATH, '//span[contains(text(), "Пароль должен содержать хотя бы одну заглавную букву")]')

#21
def test_reg_incorrect_long_password(driver):
    """Проверка, что при попытке регистрации пользователя с некорректными данными (слишком длинный пароль),
    отображается ошибка"""

    time.sleep(10)
    page = AuthPage(driver)
    page.open_registration_page()
    page = AuthRegistration(driver)
    page.enter_firstname_reg('Oльга')
    page.enter_lastname_reg('Рымкевич')
    page.enter_city_reg('Москва')
    page.enter_email_reg('test@mail.ru')
    page.enter_pass_reg('12345Qwert12345qwert123456')
    page.enter_pass_conf_reg('12345Qwert12345qwert123456')
    page.btn_click_reg()

    assert driver.find_element(By.XPATH, '//span[contains(text(), "Длина пароля должна быть не более 20 символов")]')

