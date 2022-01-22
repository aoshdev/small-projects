from selenium import webdriver

path = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.google.com.au/")

print(driver.title)

driver.close() # close tab
driver.quit() # close brower