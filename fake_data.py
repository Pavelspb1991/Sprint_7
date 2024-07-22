from faker import Faker
fake = Faker()
fakeRU = Faker('ru_RU')


class FakerMethods:
    @staticmethod
    def create_payload():
        payload = {
            'login': FakerMethods.create_login(),
            'password': FakerMethods.create_password(),
            'firstName': FakerMethods.create_firstname()
        }
        return payload

    @staticmethod
    def create_login():
        letters = fake.lexify(text='??????', letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        digits = str(fake.random_number(digits=4, fix_len=True))
        login = letters + digits
        return login

    @staticmethod
    def create_password():
        password = fake.password(length=4, lower_case=True, upper_case=True, special_chars=False)
        return password

    @staticmethod
    def create_firstname():
        first_name = fakeRU.first_name()
        return first_name

    @staticmethod
    def add_random_digits_login(payload, num_digits=3):
        payload['login'] = str(fake.random_number(digits=num_digits, fix_len=True)) + payload['login']
        return payload

    @staticmethod
    def add_random_digits_password(payload, num_digits=3):
        payload['password'] = str(fake.random_number(digits=num_digits, fix_len=True)) + payload['password']
        return payload


class DataForOrder:
    order_data_black_scooter = {
        "firstName": "Шутник",
        "lastName": "Хохмач",
        "address": "ул. Веселая, д. Смешной",
        "metroStation": 7,
        "phone": "+78006663535",
        "rentTime": 3,
        "deliveryDate": "2024-07-18",
        "comment": "Хочу, чтобы курьер пришел в костюме клоуна",
        "color": ["BLACK"]
    }

    order_data_grey_scooter = {
        "firstName": "Капитан",
        "lastName": "Очевидность",
        "address": "пер. Логичный, д. Разумный",
        "metroStation": 2,
        "phone": "+78001234567",
        "rentTime": 4,
        "deliveryDate": "2024-07-16",
        "comment": "Если что, я дома",
        "color": [
            "GREY"
        ]
    }

    order_data_two_color_scooters = {
        "firstName": "Любитель",
        "lastName": "Пиццы",
        "address": "ул. Пепперони, д. Ананас",
        "metroStation": 5,
        "phone": "+7 8009998877",
        "rentTime": 4,
        "deliveryDate": "2024-07-19",
        "comment": "Можно с собой захватить кусочек пиццы?",
        "color": [
            "BLACK",
            "GREY"
        ]
    }

    order_data_empty_color_scooter = {
        "firstName": "Соня",
        "lastName": "Засоня",
        "address": "ул. Подушкина, д. Одеяловый",
        "metroStation": 3,
        "phone": "+78007776655",
        "rentTime": 2,
        "deliveryDate": "2024-07-15",
        "comment": "Пожалуйста, звоните громче, я крепко сплю",
        "color": []
    }
