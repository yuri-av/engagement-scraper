from src.locators import InstagramLocators, TikTokLocators, FacebookLocators

# Cambiamos el nombre para que coincida con el Roadmap 
def obtener_metricas(driver, url):
    """
    Extrae las métricas usando Selenium y los Locators [cite: 25-26].
    """
    if "instagram.com" in url:
        locs = InstagramLocators
    elif "tiktok.com" in url:
        locs = TikTokLocators
    elif "facebook.com" in url:
        locs = FacebookLocators
    else:
        return None

    try:
        # Extraemos los datos del DOM [cite: 26, 30]
        return {
            "likes": int(driver.find_element(*locs.LIKES).text.replace('.', '')),
            "reposteos": int(driver.find_element(*locs.REPOSTS).text.replace('.', '')),
            "visualizaciones": int(driver.find_element(*locs.VIEWS).text.replace('.', ''))
        }
    except Exception as e:
        print(f"⚠️ Error al parsear: {e}")
        return None