from selenium.webdriver.common.by import By

class InstagramLocators:
    # Instagram usa etiquetas de accesibilidad muy claras
    LIKES = (By.XPATH, "//section//span[contains(text(), 'Me gusta') or contains(@aria-label, 'Me gusta')]")
    REPOSTS = (By.XPATH, "//button[contains(@aria-label, 'Compartir')]")
    VIEWS = (By.XPATH, "//span[contains(text(), 'reproducciones')]")

class FacebookLocators:
    LIKES = (By.XPATH, "//*[contains(@aria-label, 'reacciones') or contains(@aria-label, 'Me gusta')]")
    REPOSTS = (By.XPATH, "//*[contains(@aria-label, 'Compartir')]")
    VIEWS = (By.XPATH, "//*[contains(text(), 'reproducciones') or contains(text(), 'Visualizaciones')]")

class TikTokLocators:
    LIKES = (By.XPATH, "//strong[@data-e2e='like-count']")
    REPOSTS = (By.XPATH, "//strong[@data-e2e='share-count']")
    VIEWS = (By.XPATH, "//strong[@data-e2e='video-views']")