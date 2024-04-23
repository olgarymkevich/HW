from selenium.webdriver.common.by import By

class AuthLocators:

    auth_page_right = (By.ID, 'page-right')
    auth_page_left = (By.ID, 'page-left')

    auth_logo = (By.CLASS_NAME, 'what-is-container__logo-container')

    btn_tab_phone = (By.ID, "t-btn-tab-phone")
    btn_tab_email = (By.ID, "t-btn-tab-mail")
    btn_tab_login = (By.ID, "t-btn-tab-login")
    btn_tab_ls = (By.ID, "t-btn-tab-ls")

    tab_phone = (By.XPATH, '//*[@id="t-btn-tab-phone"]/span')
    tab_email = (By.XPATH, '//*[@id="t-btn-tab-mail"]/span')
    tab_login = (By.XPATH, '//*[@id="t-btn-tab-login"]/span')

    auth_username = (By.XPATH, '//*[@id="username"]')
    auth_password = (By.XPATH, '//*[@id="password"]')
    auth_btn = (By.CSS_SELECTOR, 'button[type="submit"]')

    auth_form_error = (By.ID, 'form-error-message')
    auth_forgot_pass = (By.ID, 'forgot_password')
    auth_reg = (By.XPATH, '//*[@id="kc-register"]')

    reg_logo = (By.CLASS_NAME, 'what-is-container__logo-container')
    reg_page_right = (By.ID, "page-right")
    reg_page_left = (By.ID, "page-left")

    auth_first_name = (By.XPATH, '//input[@class="rt-input__input rt-input__input--rounded rt-input__input--orange"][@name="firstName"]')
    auth_last_name = (By.XPATH, '//input[@class="rt-input__input rt-input__input--rounded rt-input__input--orange"][@name="lastName"]')

    auth_city = (By.XPATH, '//input[@class="rt-input__input rt-select__input rt-input__input--rounded rt-input__input--orange"]')
    auth_email = (By.XPATH, '//input[@id="address"]')
    auth_phone = (By.XPATH, '//input[@id="address"]')
    auth_pass = (By.XPATH, '//*[@id="password"]')
    auth_pass_conf = (By.XPATH, '//*[@id="password-confirm"]')
    auth_reg_btn = (By.CSS_SELECTOR, 'button[type="submit"]')


