from selenium.webdriver import Remote, ChromeOptions  
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection  
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
  
AUTH = 'brd-customer-hl_28952d2b-zone-scraping_browser1:jrt76axd2n0k'  
SBR_WEBDRIVER = f'https://{AUTH}@zproxy.lum-superproxy.io:9515'  
  
def main():  
    print('Connecting to Scraping Browser...')  
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')  
    with Remote(sbr_connection, options=ChromeOptions()) as driver:  
        print('Connected! Navigating to https://visa.vfsglobal.com/gbr/en/aut/login ...')  
        driver.get('https://visa.vfsglobal.com/gbr/en/aut/login')  

        print('Navigated! Scraping page content...') 

        # WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, "mat-input-0"))
      
        # )
        # input_element = driver.find_element(By.ID, "mat-input-0")
        # input_element.clear()
        # input_element.send_keys("amehsolomon.aso@gmail.com" + Keys.ENTER)
        # WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, "mat-input-1"))
      
        # )
        # input_element2 = driver.find_element(By.ID, "mat-input-1")
        # input_element2.clear()
        # input_element2.send_keys("Qwertyuiop@2024")
        # input_element2.send_keys(Keys.RETURN)


                # Wait until the email input field is visible
        email_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="username"]'))
        )
        print("Email field located.")

        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="password"]'))
        )
        print("Password field located.")

        email_field.send_keys("amehsolomon.aso@gmail.com")
        password_field.send_keys("Qwertyuiop@2024")
        password_field.send_keys(Keys.RETURN)
    

  
if __name__ == '__main__':  
   main()
