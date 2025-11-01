from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome options (headless mode for Docker)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Setup ChromeDriver service
service = Service(ChromeDriverManager().install())

# Launch browser
driver = webdriver.Chrome(service=service, options=options)

# Wait briefly for Flask app to start
time.sleep(3)

# Visit your Flask app
driver.get("http://127.0.0.1:5000")
print("Page title is:", driver.title)

driver.quit()
