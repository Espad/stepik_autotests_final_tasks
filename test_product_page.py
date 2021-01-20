import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage



# pytest -v --tb=line --language=en test_main_page.py
links = [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
]
links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]

@pytest.mark.need_review
@pytest.mark.parametrize("link", links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_cart() # добавляем товары в корзину
    page.solve_quiz_and_get_code() # выполняем условие из задания
    # time.sleep(180)

    page.check_product_name() # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    page.check_basket_price() # Стоимость корзины совпадает с ценой товара.



links = [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
]

@pytest.mark.xfail
@pytest.mark.parametrize("link", links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_cart() # добавляем товары в корзину
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.parametrize("link", links)
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.parametrize("link", links)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_cart() # добавляем товары в корзину
    page.should_disappeared() # Проверяем, что пропало сообщение о добавлении в корзину


links = [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
]


@pytest.mark.login_guest
@pytest.mark.parametrize("link", links)
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link):
        #
        self.link = link
        self.login = str(time.time()) + "@email.com"
        self.password = "123ASD@@3d!"
        self.browser = browser
        page = LoginPage(self.browser, self.link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()
        page.should_be_login_page()      # проверяем, что перешли на страницу с авторизацией
        page.register_new_user(self.login, self.password) # регистрируем нового пользователя
        page.should_be_authorized_user() # проверяем, что пользователь авторизован

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        page = ProductPage(self.browser, self.link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.add_to_cart() # добавляем товары в корзину
        page.solve_quiz_and_get_code() # выполняем условие из задания
        # time.sleep(180)

        page.check_product_name() # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        page.check_basket_price() # Стоимость корзины совпадает с ценой товара.

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, self.link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


links = [
    "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
]

@pytest.mark.parametrize("link", links)
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_link()

@pytest.mark.need_review
@pytest.mark.parametrize("link", links)
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()
    page.should_be_login_page()      # проверяем, что перешли на страницу с авторизацией

@pytest.mark.need_review
@pytest.mark.parametrize("link", links)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_basket_page_link()
    page.go_to_basket_page()         # переходим в корзину
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message() # проверяем что есть сообщение о том, что корзина пуста
    basket_page.should_be_empty_basket() # проверяем что корзина пуста



