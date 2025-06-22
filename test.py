from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.binary_location = "/usr/bin/chromium"
opts.add_argument("--auto-open-devtools-for-tabs")
opts.add_argument("--start-maximized")
opts.add_argument("--disable-blink-features=AutomationControlled")

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=opts)

# Cargar Instagram (PRUEBA REAL)
driver.get("https://www.instagram.com")
