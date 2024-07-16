import pytest
from fake_data import FakerMethods
import allure
from methods import ApiMethods


class TestCourierLogin:
    @allure.title('Проверка успешного логина курьера')
    @allure.description('Проверка статус кода = 200 и сообщения id != 0 при успешном логине курьера')
    def test_courier_login_success(self):
        with allure.step('Создание аккаунта курьера'):
            payload = FakerMethods.create_payload()
            ApiMethods.create_data_courier(payload)
        with allure.step('Логин курьера в системе'):
            response_login = ApiMethods.courier_login_success(payload)
        with allure.step('Проверка статус кода = 200 и сообщения id != 0'):
            assert response_login.status_code == 200
            assert 'id' in response_login.text
        with allure.step('Удаление аккаунта курьера'):
            ApiMethods.delete_data_courier(payload)

    @allure.title('Проверка, что при авторизации под несуществующим пользователем, запрос возвращает ошибку')
    @allure.description('Проверка статус кода = 404 и сообщения Учетная запись не найдена при неверном логине курьера')
    def test_courier_login_incorrect_values_failed(self):
        with allure.step('Логин курьера в системе'):
            payload = FakerMethods.create_payload()
            response_login = ApiMethods.courier_login_success(payload)
        with allure.step('Проверка статус кода = 404 и сообщения "Учетная запись не найдена"'):
            assert response_login.status_code == 404
            assert response_login.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Проверка, что при авторизации с неправильным паролем или логином, запрос возвращает ошибку')
    @allure.description('Проверка статус кода = 404 и сообщения Учетная запись не найдена при неверном пароле курьера')
    def test_invalid_login_or_password_failed(self):
        with allure.step('Создание аккаунта курьера'):
            payload = FakerMethods.create_payload()
            create_response = ApiMethods.create_data_courier(payload)
            assert create_response.status_code == 201 and create_response.json() == {'ok': True}
        with allure.step('Логин курьера в системе с неправильным логином'):
            modified_payload = FakerMethods.add_random_digits_login(payload.copy())
            response_login = ApiMethods.courier_login_success(modified_payload)
        with allure.step('Проверка статус кода = 404 и сообщения "Учетная запись не найдена"'):
            assert response_login.status_code == 404
            assert response_login.json()['message'] == 'Учетная запись не найдена'
        with allure.step('Логин курьера в системе с неправильным паролем'):
            modified_payload = FakerMethods.add_random_digits_password(payload.copy())
            response_login = ApiMethods.courier_login_success(modified_payload)
        with allure.step('Проверка статус кода = 404 и сообщения "Учетная запись не найдена"'):
            assert response_login.status_code == 404 and response_login.json()['message'] == 'Учетная запись не найдена'
        with allure.step('Удаление аккаунта курьера'):
            ApiMethods.delete_data_courier(payload)

    @allure.title('Проверка получения ошибки аутентификации курьера с пустым полем логина или пароля')
    @allure.description(
        'В тест по очереди передаются наборы данных с пустым логином или паролем. Проверяются код и тело ответа.')
    @pytest.mark.parametrize('values', [
        {'login': '', 'password': FakerMethods.create_password(), 'firstName': FakerMethods.create_firstname()
         }, {'login': FakerMethods.create_login(), 'password': '', 'firstName': FakerMethods.create_firstname()
             }])
    def test_courier_login_empty_values_failed(self, values):
        with allure.step('Логин курьера в системе'):
            response_login = ApiMethods.courier_login_success(values)
        with allure.step('Проверка статус кода = 400 и сообщения "Недостаточно данных для входа"'):
            assert response_login.status_code == 400
            assert response_login.json()['message'] == 'Недостаточно данных для входа'




