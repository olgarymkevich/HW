from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем, что запрос api ключа возвращает статус 200 и в результате содержится слово key"""

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем, что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее, используя этот ключ,
    запрашиваем список всех питомцев и проверяем, что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='овчарка', age='2', pet_photo='images/dog.jpg'):
    """Проверяем, что можно добавить питомца с корректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] == pet_photo

def test_delete_pet_with_valid_data(pet_id=''):
    """Проверяем возможность удаления питомца"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Барбоскин", "овчарка", '2', "images/dog.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()

def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age='5'):
    """Проверяем возможность обновления информации о питомце"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
        assert result['animal_type'] == animal_type
        assert result['age'] == age
    else:
        raise Exception("There is no my pets")

def test_add_new_pet_simple_with_valid_data(name='Барбоскин', animal_type='овчарка', age='2'):
    """Проверяем, что можно добавить питомца с корректными данными (но без фото)"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age

def test_add_photo_pet_with_valid_data(pet_photo='images/dog.jpg'):
    """Проверяем, что можно добавить фото питомца с корректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet_simple(auth_key, "Барбоскин", "овчарка", '2')
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_photo_pet(auth_key, pet_id, pet_photo)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert result['pet_photo'] == pet_photo
# 1.1
def test_unsuccessful_get_api_key_with_invalid_email(email=invalid_email, password=valid_password):
    """ Проверяем, что запрос api ключа возвращает статус 403 и в результате нет ключа"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result

# 2.2
def test_unsuccessful_get_api_key_with_invalid_password(email=valid_email, password=invalid_password):
    """ Проверяем, что запрос api ключа возвращает статус 403 и в результате нет ключа"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
# 3.3
def test_unsuccessful_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """ Проверяем, что запрос api ключа возвращает статус 403 и в результате нет ключа"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
# 4.4
def test_unsuccessful_add_new_pet_with_invalid_age(name='Дог', animal_type='двортерьер', age='-2', pet_photo='images/dog.jpg'):
    """Проверяем, что нельзя добавить питомца с некорректными данными (отрицательным возрастом).
    На данный момент здесь присутствует баг. Ожидается статус ответа 400, а приходит 200. Питомец с
    некорректными данными добавлен на сайт."""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

# 5.5
def test_unsuccessful_add_new_pet_with_invalid_name(name='', animal_type='овчарка', age='2', pet_photo='images/dog.jpg'):
    """Проверяем, что нельзя добавить питомца с некорректными данными (имя - пустая строка).
    На данный момент здесь присутствует баг. Ожидается статус ответа 400, а приходит 200. Питомец с
    некорректными данными добавлен на сайт."""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

# 6.6
def test_unsuccessful_add_new_pet_with_invalid_photo(name='Барбоскин', animal_type='овчарка', age='2', pet_photo='images/video.mp4'):
    """Проверяем, что нельзя добавить питомца с некорректными данными (видео вместо фото).
    На данный момент здесь присутствует баг. Ожидается статус ответа 400, а приходит 200. Питомец с
    некорректными данными добавлен на сайт."""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

# 7.7
def test_unsuccessful_add_new_pet_simple_with_invalid_animal_type(name='Барбоскин', animal_type='', age='2'):
    """ Проверяем, что нельзя добавить питомца с некорректными данными (тип животного - пустая строка).
    На данный момент здесь присутствует баг. Ожидается статус ответа 400, а приходит 200. Питомец с
    некорректными данными добавлен на сайт."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    assert status == 400

# 8.8
def test_unsuccessful_add_new_pet_simple_with_invalid_age(name='Барбоскин', animal_type='овчарка', age=''):
    """ Проверяем, что нельзя добавить питомца с некорректными данными (возраст - пустая строка).
    На данный момент здесь присутствует баг. Ожидается статус ответа 400, а приходит 200. Питомец с
    некорректными данными добавлен на сайт."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    assert status == 400

# 9.9
def test_unsuccessful_update_self_pet_info_age(name='Дог', animal_type='двортерьер', age='-5'):
    """Проверяем, что нельзя изменить возраст питомца на отрицательный.
    На данный момент здесь присутствует баг. Ожидается статус ответа 400, а приходит 200.
    Возраст питомца изменен на отрицательный."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 400
        assert result['age'] != age
    else:
        raise Exception('There is no my pets')
# 10.10
def test_unsuccessful_update_self_pet_info_name(name='', animal_type='двортерьер', age='5'):
    """Проверяем, что нельзя изменить имя питомца на пустую строку.
    На данный момент здесь присутствует баг. Ожидается статус ответа 400, а приходит 200.
    Имя питомца изменено."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 400
        assert result['name'] != name
    else:
        raise Exception('There is no my pets')


