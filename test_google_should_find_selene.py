import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def browser_open():
    browser.open('https://google.com')
    browser.driver.maximize_window()



def test_successful_search(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_unscessful_search(browser_open):
    browser.element('[name="q"]').should(be.blank).type('sdfsfesfsfef').press_enter()
    browser.element('[class="card-section"]').should(have.text('Страницы, содержащие все слова запроса, не найдены.'))