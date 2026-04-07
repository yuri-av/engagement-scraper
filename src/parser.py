import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import InstagramLocators, FacebookLocators, TikTokLocators

def detectar_red(url):
    """Lógica para elegir qué clase de locadores usar"""
    if "instagram.com" in url:
        return InstagramLocators
    elif "facebook.com" in url:
        return FacebookLocators
    elif "tiktok.com" in url:
        return TikTokLocators
    return None

def obtener_metricas(driver, url):
    locs = detectar_red(url)
    if not locs:
        print("❌ Red social no soportada.")
        return None

    # Función interna para limpiar los números (K, M, puntos, etc.)
    def limpiar_numero(texto):
        if not texto: return 0
        texto = texto.lower().replace('.', '').replace(',', '').replace('k', '000').replace('m', '000000')
        import re
        numeros = re.findall(r'\d+', texto)
        return int(numeros[0]) if numeros else 0

    try:
        # Extraemos con bloques try individuales para que si falta uno no muera todo
        try:
            likes = limpiar_numero(driver.find_element(*locs.LIKES).text)
        except:
            likes = 0
            
        try:
            reposts = limpiar_numero(driver.find_element(*locs.REPOSTS).text)
        except:
            reposts = 0
            
        try:
            views = limpiar_numero(driver.find_element(*locs.VIEWS).text)
            if views == 0: views = 1 # Evitamos división por cero
        except:
            views = 1

        return {
            "likes": likes,
            "reposteos": reposts,
            "visualizaciones": views,
            "url": url
        }
    except Exception as e:
        print(f"⚠️ Error general al parsear: {e}")
        return None