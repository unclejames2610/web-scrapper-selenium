from undetected_chromedriver import Chrome
import time


chrome = Chrome()

chrome.get("http://visa.vfsglobal.com/gbr/en/aut/login")

time.sleep(20)
chrome.close()