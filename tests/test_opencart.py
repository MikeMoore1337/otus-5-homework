from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 1)
    wait.until(EC.title_is("Your Store"))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class='btn btn-default btn-lg']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(1) > .dropdown-toggle")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[title='MacBook']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-ex1-collapse")))


def test_catalog(browser):
    browser.get(browser.url + "/desktops")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.title_is("Desktops"))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='HP Banner']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-sort")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#compare-total")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-inverse.btn-block.btn-lg.dropdown-toggle")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://www.opencart.com']")))


def test_card_product(browser):
    browser.get(browser.url + "/laptop-notebook/macbook-pro")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.title_is("MacBook Pro"))
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@class='atc_s addthis_button_compact'])[1]")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content .fa-heart")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[class='list-unstyled'] li h2")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='#tab-description']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='#tab-description']")))


def test_login(browser):
    browser.get(browser.url + "/admin")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.title_is("Administration"))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[title='OpenCart']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Forgotten Password'])[1]")))


def test_el_admin(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.title_is("Register Account"))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-lastname")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-telephone")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-confirm")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='agree']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Continue']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='content'] p a")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-right")))
