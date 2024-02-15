from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service()

chromeOptions = webdriver.ChromeOptions()
webDriver = webdriver.Chrome(service=service, options=chromeOptions)
webDriver.set_window_size(1600,900)

#credentials 
url = 'https://qa.climberrms.com'
email = 'eduardo.bernardes+test@climberhotel.com'
password = '*****'
timer = 15

webDriver.get(url)
time.sleep(timer)

login_email = webDriver.find_element(By.XPATH, "/html/body/jhi-main/climber-login/div[2]/div/jhi-login-modal/form/div[1]/input")
login_password = webDriver.find_element(By.XPATH, "/html/body/jhi-main/climber-login/div[2]/div/jhi-login-modal/form/div[2]/input")

login_email.send_keys(email)
login_password.send_keys(password)

login_email.send_keys(Keys.ENTER)

array_hotels = [
    "Ape Paulista Augusta",
    "Bavária Sport Hotel",
    "Castelo de Itaipava"
]

counter = 0

while True:
        menu_dropdown = webDriver.find_element(By.XPATH,"/html/body/jhi-main/climber-shell/climber-header/nav[2]/div/div[2]/climber-dropdown-v2")
        menu_dropdown.click()

        time.sleep(timer)
        print(array_hotels[counter])
        seletor_css = '[title*="' + array_hotels[counter] + '"]'
        print(seletor_css)
        hotels_dropdown = webDriver.find_element(By.CSS_SELECTOR, seletor_css)
        hotels_dropdown.click()
        time.sleep(timer)

        webDriver.get(url + '/pickup')
        time.sleep(timer)
        webDriver.get(url + '/pricing-distribution')
        time.sleep(timer)
        webDriver.get(url + '/overview')
        time.sleep(timer)

        counter+=1
        if counter == len(array_hotels) : counter = 0

