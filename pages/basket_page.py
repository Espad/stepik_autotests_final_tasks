from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Empty basket message element not found on page"

        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text == "Your basket is empty. Continue shopping", \
            "Invalid Basket empty message"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM_EXIST_SELECTOR), \
            "Busket is not empty, but should be"
