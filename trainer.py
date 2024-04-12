from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)


driver.get("https://secure-retreat-92358.herokuapp.com")

f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email_address = driver.find_element(By.NAME, "email")

f_name.send_keys("Faaiz")
l_name.send_keys("Rehman")
email_address.send_keys("faaizrehman@gmail.com")



button = driver.find_element(By.CSS_SELECTOR, "form button")
button.send_keys(Keys.ENTER)


#closes tab
# driver.close()



