import os
import time
import platform
import shutil
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")

def _find_binary(binary_name: str) -> str | None:
    return shutil.which(binary_name)

def _build_driver() -> webdriver.Chrome:
    system = platform.system().lower()
    chrome_opts = Options()
    chrome_opts.add_argument("--auto-open-devtools-for-tabs")
    chrome_opts.add_argument("--start-maximized")
    chrome_opts.add_argument("--disable-blink-features=AutomationControlled")

    if system == "linux":
        binary = _find_binary("chromium") or _find_binary("google-chrome")
        driver_bin = _find_binary("chromedriver")
    else:
        binary = _find_binary("chrome") or _find_binary("google-chrome")
        driver_bin = _find_binary("chromedriver")

    if not binary:
        raise RuntimeError("❌ No se encontró Chromium/Chrome en el sistema.")
    if not driver_bin:
        raise RuntimeError("❌ No se encontró chromedriver en el PATH.")

    chrome_opts.binary_location = binary
    service = Service(executable_path=driver_bin)
    return webdriver.Chrome(service=service, options=chrome_opts)

def instagram_login(driver):
    print("[→] Iniciando sesión en Instagram...")
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    try:
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys(IG_USERNAME)
        password_input.send_keys(IG_PASSWORD)
        password_input.send_keys(Keys.RETURN)
        time.sleep(6)

        try:
            not_now = driver.find_element(By.XPATH, "//button[contains(text(), 'Ahora no')]")
            not_now.click()
            time.sleep(2)
        except:
            pass

        print("[✓] Login exitoso.")
    except Exception as e:
        raise RuntimeError(f"[✗] Error en el login: {str(e)}")

def mostrar_instrucciones_script_console():
    script_path = Path("scripts/inject_console_script.js")
    if not script_path.exists():
        print("[!] Script para consola no encontrado.")
        return

    with open(script_path, "r") as f:
        script_consola = f.read()

    print("\n[✓] Inyecta este script en la consola del navegador (DevTools):\n")
    print(script_consola)
    print("\n[→] Haz clic en 'seguidores' o 'seguidos' y desplázate para cargar datos.")
    print("[↓] Luego, pulsa en 'Download XX users' para guardar el archivo CSV.")
    print("[⏳] Cuando termines, cierra el navegador para continuar.")

def get_followers(username: str) -> dict:
    url = f"https://www.instagram.com/{username}/"

    try:
        driver = _build_driver()
        instagram_login(driver)

        print(f"[→] Navegando al perfil de {username}...")
        driver.get(url)
        time.sleep(8)

        mostrar_instrucciones_script_console()

        return {"success": True, "followers": [], "count": 0}

    except Exception as e:
        return {"error": f"[followers] {type(e).__name__}: {e}"}

