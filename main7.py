from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create options for undetected_chromedriver
options = ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--start-maximized')

# Initialize undetected_chromedriver
driver = Chrome(options=options)

# Navigate to the login page
driver.get("http://visa.vfsglobal.com/gbr/en/aut/login")

# Wait for the page to load and CAPTCHA to be bypassed
time.sleep(20)  # Adjust sleep time as needed for CAPTCHA to be bypassed

# Perform login actions using Selenium
try:
    # Wait for the email input field to be present
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "mat-input-0"))
    )
    input_element = driver.find_element(By.ID, "mat-input-0")
    input_element.clear()
    input_element.send_keys("amehsolomon.aso@gmail.com" + Keys.ENTER)
    print("Email field located.")


    password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="password"]'))
        )
    print("Password field located.")

    password_field.send_keys("Qwertyuiop@2024")
    password_field.send_keys(Keys.RETURN)

    # Wait for the sign-in button to be present
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button'))
    )
    signInBtn = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button')
    signInBtn.click()
    
    print("Sign-in button clicked!")

    # Optional: wait for some time to observe the result
    time.sleep(50)

finally:
    # Close the browser
    driver.quit()
