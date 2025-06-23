import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv

load_dotenv()

def download_stories(username: str) -> dict:
    try:
        # Ruta de la extensión
        extension_path = os.path.abspath("downloads/Instagram-Downloader-5.1.9")

        # Configuración de opciones de Chrome
        chrome_options = Options()
        chrome_options.add_argument(f"--load-extension={extension_path}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Usar Chromium directamente si estás en Linux y no tienes google-chrome
        chrome_options.binary_location = "/usr/bin/chromium"

        # Iniciar el navegador
        driver = webdriver.Chrome(options=chrome_options)

        # Abrir la página de login
        driver.get("https://www.instagram.com/accounts/login/")
        sleep(4)

        # Login
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")

        username_input.send_keys(os.getenv("IG_USERNAME"))
        password_input.send_keys(os.getenv("IG_PASSWORD"))
        password_input.submit()

        sleep(6)  # Espera a que cargue la sesión

        # Ir directo a las stories del usuario
        driver.get(f"https://www.instagram.com/stories/{username}/")
        sleep(15)

        return {
            "success": True,
            "message": "✅ Navegador abierto y extensión cargada. Descarga las stories manualmente si deseas."
        }

    except Exception as e:
        return {
            "error": f"❌ Error en el proceso: {str(e)}"
        }

