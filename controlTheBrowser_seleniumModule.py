from selenium import webdriver

PATH = 'C:\Program Files (x86)\chromedriver.exe' #Must manually type (NO COPY PASTE!!)
browser = webdriver.Chrome(PATH)
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a')   
elem.click()