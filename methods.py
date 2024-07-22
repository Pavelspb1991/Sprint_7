import requests
from urls import Urls
from fake_data import FakerMethods


class ApiMethods:
    faker_methods = FakerMethods()

    @staticmethod
    def delete_data_courier(payload):
        login = payload['login']
        password = payload['password']
        response_login = requests.post(Urls.COURIER_LOGIN_URL, data={'login': login, 'password': password})
        courier_id = response_login.json()['id']
        response_delete = requests.delete(f"{Urls.COURIER_URL}/{courier_id}")
        return response_delete

    @staticmethod
    def create_data_courier(payload):
        response = requests.post(Urls.COURIER_URL, data=payload)
        return response

    @staticmethod
    def courier_login_success(payload):
        login = payload['login']
        password = payload['password']
        response_login = requests.post(Urls.COURIER_LOGIN_URL, data={'login': login, 'password': password})
        return response_login

    @staticmethod
    def create_courier():
        payload = {
            'login': ApiMethods.faker_methods.create_login(),
            'password': ApiMethods.faker_methods.create_password(),
            'firstName': ApiMethods.faker_methods.create_firstname()
        }
        response = requests.post(Urls.COURIER_URL, data=payload)
        return response

    @staticmethod
    def create_courier_2():
        full_payload = FakerMethods.create_payload()
        ApiMethods.create_data_courier(full_payload)
        created_login = full_payload['login']
        created_password = full_payload['password']
        return created_login, created_password

    @staticmethod
    def create_order(payload):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.ORDERS_URL, data=payload, headers=headers, timeout=5)
        return response

    @staticmethod
    def get_orders():
        response = requests.get(Urls.ORDERS_URL)
        return response
