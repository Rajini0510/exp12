from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

time.sleep(2)
driver.get("http://localhost:5000")

assert "Hello World" in driver.page_source
print("✅ Test Passed: 'Hello World' found on page")

driver.quit()