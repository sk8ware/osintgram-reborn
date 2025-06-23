import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from time import sleep

load_dotenv()
IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")

def get_followers(username: str) -> dict:
    try:
        # Configuración del navegador
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--auto-open-devtools-for-tabs")  # Abre DevTools automáticamente
        chrome_options.binary_location = "/usr/bin/chromium"  # Usa Chromium directamente

        driver = webdriver.Chrome(options=chrome_options)

        # Abrir Instagram y hacer login
        driver.get("https://www.instagram.com/accounts/login/")
        sleep(4)

        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")

        username_input.send_keys(IG_USERNAME)
        password_input.send_keys(IG_PASSWORD)
        password_input.send_keys(Keys.RETURN)

        sleep(6)

        # Navegar al perfil
        driver.get(f"https://www.instagram.com/{username}/")
        sleep(10)

        print("\n[✓] Navegador abierto con DevTools. Ve a la sección de seguidores.")
        print("[↓] Pega el script en consola y guarda el CSV cuando termines.")

        return {
            "success": True,
            "followers": [],
            "count": 0
        }

    except Exception as e:
        return {
            "error": f"❌ Error al abrir perfil o cargar el navegador: {str(e)}"
        }

