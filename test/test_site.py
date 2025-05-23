import time
from pages.homepage import HomePage
from pages.product import ProductPage



def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    #browser.get('https://demoblaze.com/index.html#')
    #galaxy_s6 = browser.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']")
    #galaxy_s6.click()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')
    #title = browser.find_element(By.CSS_SELECTOR, 'h2')
    #assert title.text == 'Samsung galaxy s6'

def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    #browser.get('https://demoblaze.com/index.html#')
    homepage.click_monitor()
    #monitor_link = browser.find_element(By.CSS_SELECTOR, '''[onclick = "byCat('monitor')"]''')
    #monitor_link.click()
    time.sleep(2)
    homepage.check_products_count(2)
    #monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    #assert len(monitors) == 2





