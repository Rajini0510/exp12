from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options
options = Options()
options.add_argument("--headless")  # run without UI (important inside Docker)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Create WebDriver instance
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://127.0.0.1:5000")
print("Page title is:", driver.title)

driver.quit()
