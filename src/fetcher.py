import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def fetch_html(url):
    options = webdriver.ChromeOptions()
    
    # Esta línea busca automáticamente tu usuario de Windows, sea cual sea
    user_home = os.path.expanduser("~") 
    perfil_path = os.path.join(user_home, r'AppData\Local\Google\Chrome\User Data')

    options.add_argument(f"--user-data-dir={perfil_path}")
    options.add_argument("--profile-directory=Default")
    
    # Evita que TikTok detecte que es una automatización
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        return driver
    except Exception as e:
        print(f"❌ Error al iniciar navegador: {e}")
        return None