from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Bright Data Authentication
AUTH = 'brd-customer-hl_28952d2b-zone-scraping_browser1:jrt76axd2n0k'
SBR_WEBDRIVER = f'https://{AUTH}@zproxy.lum-superproxy.io:9515'

def main():
    print('Connecting to Scraping Browser...')
    
    # Set up Chrome options
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--start-maximized')
    
    # Connect to the Bright Data WebDriver
    driver = Remote(
        command_executor=SBR_WEBDRIVER,
        options=options
    )
    
    print('Connected! Navigating to https://visa.vfsglobal.com/gbr/en/aut/login ...')
    driver.get('https://visa.vfsglobal.com/gbr/en/aut/login')

    print('Navigated! Scraping page content...')

    try:
        # Wait until the email input field is visible
        email_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="username"]'))
        )
        print("Email field located.")

        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="password"]'))
        )
        print("Password field located.")

        # Simulate typing for email
        email = "amehsolomon.aso@gmail.com"
        driver.execute_script("arguments[0].focus();", email_field)
        for char in email:
            driver.execute_script(f"arguments[0].value += '{char}';", email_field)
            time.sleep(0.1)

        time.sleep(2)  # Adding a small delay before entering password

        # Simulate typing for password
        password = "Qwertyuiop@2024"
        driver.execute_script("arguments[0].focus();", password_field)
        for char in password:
            driver.execute_script(f"arguments[0].value += '{char}';", password_field)
            time.sleep(0.1)

        time.sleep(2)  # Adding a small delay before submitting the form

        # Find and click the submit button
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(5)  # Wait for a while to observe the result
        driver.quit()

if __name__ == '__main__':
   main()
