from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        btns = self.browser.find_elements(
            *ProductPageLocators.ADD_TO_CART_BUTTON)
        assert len(btns) > 0, "button not found"
        # test click if button exist
        btns[0].click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_NAME_BASKET_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_NAME_BASKET_MESSAGE), \
            "Success message is not disappeared"

    def check_product_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_MAIN_FORM), (
            "Book name on page is not presented")
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_BASKET_MESSAGE), (
            "Message about adding to basket is not presented")

        product_name = self.browser.find_element(
            *ProductPageLocators.BOOK_NAME_MAIN_FORM).text
        message = self.browser.find_element(
            *ProductPageLocators.BOOK_NAME_BASKET_MESSAGE).text
        assert product_name == message, 'no product name in basket add message'

    def check_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_MAIN_FORM), (
            "Price is not presented")
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_BASKET), (
            "Price message about adding is not presented")

        product_price = self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE_MAIN_FORM).text
        price_message = self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE_BASKET).text
        assert product_price == price_message, 'different product and basket prices'
