import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver

def test_show_my_pets(driver):
    # Вводим email
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.ID, 'email'))).send_keys('olgarymk@mail.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # Нажимаем на кнопку "Мои питомцы"
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()
    # Проверяем, что находимся на странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h2').text == "olgaolgaolga"

    # 1.
    # Находим число питомцев пользователя по таблице
    time.sleep(5)
    pet_count = driver.find_elements(By.XPATH, '//table[@class ="table table-hover"]/tbody/tr')
    # Находим число питомцев пользователя по статистике
    pet_amount = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    # Сравниваем число питомцев пользователя по таблице со статистикой
    assert int(pet_amount) == len(pet_count)

    # 2.
    # Находим имена, породы и возраст всех питомцев
    driver.implicitly_wait(5)
    names = driver.find_elements(By.XPATH, '//table[@class ="table table-hover"]/tbody/tr/td[1]')
    driver.implicitly_wait(5)
    breeds = driver.find_elements(By.XPATH, '//table[@class ="table table-hover"]/tbody/tr/td[2]')
    driver.implicitly_wait(5)
    ages = driver.find_elements(By.XPATH, '//table[@class ="table table-hover"]/tbody/tr/td[3]')
    # Проверяем, что у всех питомцев есть имя, возраст и порода
    for i in range(len(names)):
        assert names[i].text != ''
        assert breeds[i].text != ''
        assert ages[i].text != ''

    # 3.
    # Находим фото всех питомцев
    driver.implicitly_wait(5)
    images = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/th/img')
    # Проверяем, что хотя бы у половины питомцев есть фото
    n = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            n += 1
    assert n >= int(pet_amount)/2


    # 4.
    # Создаем пустой список имен всех питомцев
    list_names = []
    for i in range(len(names)):
        list_names.append(names[i].text)
    # Преобразуем список в множество
    set_names = set(list_names)
    # Проверяем, что у всех питомцев разные имена
    assert len(list_names) == len(set_names)


    # 5.
    # Создаем пустой список всех питомцев
    list_my_pets = []
    for i in range(len(pet_count)):
        list_my_pets.append(pet_count[i].text)
    # Преобразуем список в множество
    set_my_pets = set(list_my_pets)
    # Проверяем, что в списке нет повторяющихся питомцев
    assert len(list_my_pets) == len(set_my_pets)
        

