from fake_data import FakerMethods
import allure
import pytest
from methods import ApiMethods


class TestCourierCreate:

    @allure.title('Проверка успешного создания  аккаунта курьера с валидными данными')
    @allure.description('Проверка статус кодов и сообщений при создании и удалении аккаунта курьера')
    def test_create_and_delete_courier(self):
        with allure.step('Создание аккаунта курьера'):
            payload = FakerMethods.create_payload()
            response = ApiMethods.create_data_courier(payload)
            with allure.step('Проверка статус кода = 201'):
                assert response.status_code == 201
                assert response.json() == {'ok': True}
        with allure.step('Удаление аккаунта курьера'):
            delete_response = ApiMethods.delete_data_courier(payload)
            assert delete_response.status_code == 200
            assert delete_response.json() == {'ok': True}

    @allure.title('Проверка невозможности создания аккаунта курьера с уже существующим логином')
    @allure.description(
        'Проверка статус код = 409 и сообщения при попытке создания аккаунта с уже существующим логином')
    def test_cannot_create_duplicate_courier(self):
        with allure.step('Создание аккаунта курьера'):
            payload = FakerMethods.create_payload()
            create_response = ApiMethods.create_data_courier(payload)
            assert create_response.status_code == 201 and create_response.json() == {'ok': True}
        with allure.step('Попытка создания аккаунта с уже существующим логином'):
            create_response = ApiMethods.create_data_courier(payload)
            assert create_response.status_code == 409
            assert create_response.json() == {
                "code": 409,
                "message": "Этот логин уже используется. Попробуйте другой."
            }
        with allure.step('Удаление аккаунта курьера'):
            delete_response = ApiMethods.delete_data_courier(payload)
            assert delete_response.status_code == 200

    @allure.title('Проверка невозможности создания аккаунта курьера с пустыми данными')
    @allure.description('Проверка статус код = 400 и сообщения при попытке создания аккаунта с пустыми данными')
    @pytest.mark.parametrize('values', [
        {'login': '', 'password': FakerMethods.create_password(), 'firstName': FakerMethods.create_firstname()
         }, {'login': FakerMethods.create_login(), 'password': '', 'firstName': FakerMethods.create_firstname()
             }])
    def test_create_courier_empty_data_fields(self, values):
        with allure.step('Создание аккаунта курьера'):
            response = ApiMethods.courier_login_success(values)
        with allure.step('Проверка статус кода = 400'):
            assert response.status_code == 400
            assert response.json() == {"code": 400, 'message': 'Недостаточно данных для входа'}
