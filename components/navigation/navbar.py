import time

from playwright.sync_api import Page
from components.modals.search_modal import SearchModal
from page_factory.button import Button
from page_factory.input import Input
from page_factory.link import Link


class Navbar:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_modal = SearchModal(page)
        self.search_button = Button(
            page, locator="//div[@class='search_icon']//img", name='Search')
        self.search_input = Input(
            page, locator="//input[@type='search']", name='Find'
        )

    def open_search(self, text_in_input):
        self.search_button.should_be_visible()
        self.search_button.hover_click()
        self.search_modal.modal_is_opened(text_in_input)

