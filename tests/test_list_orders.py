import allure
from methods import ApiMethods


class TestOrdersListGet:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверяются код и тело ответа.')
    def test_orders_list_get_success(self):
        with allure.step('Получение списка заказов'):
            response = ApiMethods.get_orders()
        with allure.step('Проверка кода ответа'):
            assert (response.json()['orders']) is not None
            assert 'id' in response.json()['orders'][0]
