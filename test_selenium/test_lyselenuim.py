from selenium import webdriver


def test_selenium():
    driver = webdriver.Chrome(r'C:\Users\liuyu\AppData\Local\chromedriver.exe')
    driver.get("https://www.baidu.com/")
