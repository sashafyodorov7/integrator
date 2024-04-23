from selenium import webdriver

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)

browser.get("http://127.0.0.1:8000/")
assert "The install worked successfully! Congratulations!" in browser.title
