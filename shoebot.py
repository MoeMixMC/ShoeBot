import requests
import json
import bs4
from selenium import webdriver

def URLGenerator():
    HEADERS = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
    launchURL = "https://www.nike.com/launch"
    res = requests.get(launchURL, headers=HEADERS)
    page = bs4.BeautifulSoup(res.text, 'lxml')

##url = URLGenerator()
url = 'https://www.nike.com/launch'
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get(url)
##driver.find_element_by_xpath("//a[@class='non-dropdown-help-link small text-color-grey d-sm-ib va-sm-m ml2-sm mr2-sm']").click()
driver.find_element_by_xpath('//div[@data-qa="product-card-2"]//button[@type="button"]').click()