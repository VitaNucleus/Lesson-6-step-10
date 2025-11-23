import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
def test_stepik_page(browser):
    browser.get(link)
    checked_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-add-to-basket'))
    )
    assert checked_button, 'Button does not exist'