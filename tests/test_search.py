import os
import time

import allure
import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage


class TestSearch:
    @allure.feature("Search")
    @allure.story("Buy Product")
    @allure.description("""
           This  test verifies the search process on the website.

           Steps:

           1. Navigate to the product website.
           2. Hover the mouse pointer to the search image.
           3. Click  the search image.
           4. Fill search input
           5. Hover the mouse pointer to the submit button.
           6. Click the submit button.

           Expected result:
           -the page with  result of search is opend.
       """)
    @pytest.mark.parametrize('search_data, text_in_input', [('Elena', "")])
    def test_search(
        self,
        search_data: str,
        text_in_input: str,
        browser
    ):
        TEXT_SEARCH_LINE_RESULT = "Search results for '{search_data}'".format(search_data=search_data)
        print(TEXT_SEARCH_LINE_RESULT)
        URI = ""
        home_page = HomePage(browser)
        home_page.open(URI)
        home_page.navbar.open_search(text_in_input)
        home_page.navbar.search_modal.find_result(
             search_data
         )
        search_page = SearchPage(browser)
        search_page.text_search_present(TEXT_SEARCH_LINE_RESULT, search_data)
        print(os.getenv("ROOT_DIR"))

