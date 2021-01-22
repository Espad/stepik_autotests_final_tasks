import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

links = [
    "http://selenium1py.pythonanywhere.com/",
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
]


# task 4.3.11
# Группировка тестов: setup 
@pytest.mark.login_guest
@pytest.mark.parametrize("link", links)
class TestLoginFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link):
        self.link = link
        self.browser = browser

    def test_guest_can_go_to_login_page(self):
        page = MainPage(self.browser, self.link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.should_be_login_link()      # проверяем, если ли линка на форму логина
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(self.browser, self.browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self):
        page = MainPage(self.browser, self.link)
        page.open()
        page.should_be_login_link()

# task 4.3.10
# Задание: наследование и отрицательные проверки
@pytest.mark.parametrize("link", links)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_basket_page_link()
    page.go_to_basket_page()         # переходим в корзину
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message() # проверяем что есть сообщение о том, что корзина пуста
    basket_page.should_be_empty_basket() # проверяем что корзина пуста



