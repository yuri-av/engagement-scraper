from selenium.webdriver.common.by import By

class InstagramLocators:
    LIKES = (By.CSS_SELECTOR, "span.like-count-class") # Usa CSS Selectors
    REPOSTS = (By.CSS_SELECTOR, "span.share-count-class")
    VIEWS = (By.CSS_SELECTOR, "span.view-count-class")

class TikTokLocators:
    LIKES = (By.CSS_SELECTOR, '[data-e2e="like-count"]')
    REPOSTS = (By.CSS_SELECTOR, '[data-e2e="share-count"]')
    VIEWS = (By.CSS_SELECTOR, '[data-e2e="video-views"]')

class FacebookLocators:
    # FB es el más complejo y suele requerir selectores por texto o posición
    LIKES = (By.CSS_SELECTOR, 'span[role="toolbar"] div') 
    REPOSTS = (By.CSS_SELECTOR, 'div[aria-label="Enviar este post"]')
    VIEWS = (By.CSS_SELECTOR, 'span.views-class')