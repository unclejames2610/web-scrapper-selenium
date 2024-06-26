import requests
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Origin server IP address
origin_ip = "172.64.150.207"

# Headers to mimic a real browser request, including the Host header
headers = {
    "Host": "visa.vfsglobal.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "http://visa.vfsglobal.com/gbr/en/aut/login",
    "Accept-Language": "en-US,en;q=0.9",
}

# URL to the resource on the origin server
url = f"http://{origin_ip}/gbr/en/aut/login"

# Initialize a session
session = requests.Session()

# Send a GET request to the login page
response = session.get(url, headers=headers)

# Prepare login payload
login_payload = {
    "username": "amehsolomon.aso@gmail.com",
    "password": "Qwertyuiop@2024"
}

# Send POST request to login
login_url = f"http://{origin_ip}/gbr/en/aut/login"
response = session.post(login_url, data=login_payload, headers=headers)

# Check if login was successful
if "login failed" in response.text.lower():
    print("Login failed")
else:
    print("Login successful")

# Extract cookies from requests session to pass to Selenium
cookies = session.cookies.get_dict()

# Set up Chrome options and add arguments
options = ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--start-maximized')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument(f'--host-resolver-rules=MAP visa.vfsglobal.com {origin_ip}')

# Initialize undetected Chrome WebDriver
driver = Chrome(driver_executable_path="/home/sco/Documents/Bots/sellenium/chromedriver",options=options)

# Load the page via Selenium
driver.get("http://visa.vfsglobal.com/gbr/en/aut/login")

# Add cookies to Selenium
for name, value in cookies.items():
    driver.add_cookie({'name': name, 'value': value, 'domain': 'visa.vfsglobal.com'})

# Reload the page to apply cookies
driver.refresh()

# Wait for the necessary elements and interact with them
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

# Add this if you need to click a checkbox before signing in
# checkbox = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="challenge-stage"]/div/label/input'))
# )
# checkbox.click()

# Click the Sign In button
signInBtn = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button'))
)
signInBtn.click()

time.sleep(50)  # Wait for manual inspection or further steps

driver.quit()
