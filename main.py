from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="/home/sco/Documents/Bots/sellenium/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://visa.vfsglobal.com/gbr/en/aut/login")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "mat-input-0"))

)
input_element = driver.find_element(By.ID, "mat-input-0")
input_element.clear()
input_element.send_keys("amehsolomon.aso@gmail.com" + Keys.ENTER)
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "mat-input-1"))

)
input_element2 = driver.find_element(By.ID, "mat-input-1")
input_element2.clear()
input_element2.send_keys("Qwertyuiop@2024")

time.sleep(10)
# WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div/label/input'))
# )

# checkBox = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/label/input')
# checkBox.click()

# time.sleep(10)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button'))
)

signInBtn = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button')
signInBtn.click()


# /html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button

# //*[@id="challenge-stage"]/div/label/input
# input_element2.send_keys(Keys.RETURN)

# email_field = WebDriverWait(driver, 20).until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="username"]'))
#         )
# print("Email field located.")

# password_field = WebDriverWait(driver, 20).until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="password"]'))
#         )
# print("Password field located.")

# email_field.send_keys("amehsolomon.aso@gmail.com")
# password_field.send_keys("Qwertyuiop@2024")


time.sleep(50)
# password_field.send_keys(Keys.RETURN)

# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
# )

# input_element = driver.find_element(By.CLASS_NAME, "gLFyf" )
# input_element.clear()
# input_element.send_keys("ebuka udeala" + Keys.ENTER)
# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Ebuka Udeala"))
# )
# link = driver.find_element(By.PARTIAL_LINK_TEXT, "Ebuka Udeala")
# link.click()



# time.sleep(10)

# driver.quit()
