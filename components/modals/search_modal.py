from playwright.sync_api import Page
from page_factory.button import Button
from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.title import Title


class SearchModal:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.search_input = Input(
            page, locator="//input[@placeholder='Search']", name='Search'
        )

        self.submit_button = Button(
            page, locator="//button[@id='searchsubmit']", name='Submit'
        )
    def modal_is_opened(self, text):
        self.search_input.should_be_visible()
        self.search_input.should_have_text(text)

    def find_result(self, search_data: str) -> None:
        self.search_input.should_be_visible()
        self.search_input.fill(search_data, validate_value=True)
        self.submit_button.hover_click()




