from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def fetch_data_with_selenium(url):
    """Selenium kullanarak URL'den veri çekme"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup
    finally:
        driver.quit()
