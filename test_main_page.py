import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()



link = "http://selenium1py.pythonanywhere.com/"
# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"


# task 4.3.11
@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
        self.product.delete()
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, self.link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.should_be_login_link()      # проверяем, если ли линка на форму логина
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.should_be_login_link()

# task 4.3.10
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_basket_page_link()
    page.go_to_basket_page()         # переходим в корзину
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message() # проверяем что есть сообщение о том, что корзина пуста
    basket_page.should_be_empty_basket() # проверяем что корзина пуста



