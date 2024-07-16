import pytest
from fake_data import DataForOrder
import allure
from methods import ApiMethods
import json


class TestCreateOrder:

    @allure.title("Test create order")
    @allure.description("Test create order with valid data")
    @pytest.mark.parametrize("order_data", [DataForOrder.order_data_black_scooter,
                                            DataForOrder.order_data_grey_scooter,
                                            DataForOrder.order_data_two_color_scooters,
                                            DataForOrder.order_data_empty_color_scooter])
    def test_create_order(self, order_data):
        with allure.step('Создание заказа'):
            order_data = json.dumps(order_data)
            response_order = ApiMethods.create_order(order_data)
        with allure.step('Проверка статус кода = 201'):
            assert response_order.status_code == 201
            assert 'track' in response_order.text

