from playwright.sync_api import Page

from page_factory.title import Title
from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.result_title = Title(
            page, locator='//span[text()="Search results for \'{search_data}\'"]', name='Search title'
        )

    def text_search_present(self, text, search_data):
        self.result_title.should_be_visible(search_data=search_data)
        self.result_title.should_have_text(
            text, search_data=search_data
        )
