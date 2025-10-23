from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def fetch_article_text(url: str) -> str:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(3)  

    # Adjust this selector based on MoEngage article page structure:
    # For example: article content might be in <div class="article-body"> or <article> tag
    try:
        element = driver.find_element(By.CSS_SELECTOR, ".article-body, .article-content, article")
        text = element.text
    except:
        text = driver.find_element(By.TAG_NAME, "body").text

    driver.quit()
    return text
