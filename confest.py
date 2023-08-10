from selenium import webdriver
import pytest

# После завершения теста, который вызывал фикстуру,
# выполнение фикстуры продолжится со строки, следующей за строкой со словом yield
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("C:\Users\jktcz\Downloads\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()