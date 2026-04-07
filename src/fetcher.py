from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def fetch_html(url):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Desactivalo si querés ver qué hace el navegador
    
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        return driver  # IMPORTANTE: Devolvemos el objeto driver
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None