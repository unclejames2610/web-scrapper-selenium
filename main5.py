import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Origin server IP address
origin_ip = "172.64.150.207"

# Headers to mimic a real browser request
headers = {
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

# Path to your ChromeDriver
service = Service(executable_path="/home/sco/Documents/Bots/sellenium/chromedriver")

# Set up Chrome options and proxy settings
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--start-maximized')
options.add_argument(f'--proxy-server=http://{origin_ip}:80')  # Set the proxy to the origin IP

# Connect to the Bright Data WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Load the page via Selenium using the origin IP proxy
driver.get(f"http://{origin_ip}/gbr/en/aut/login")

# Add cookies to Selenium
for name, value in cookies.items():
    driver.add_cookie({'name': name, 'value': value})

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

time.sleep(50)

driver.quit()
