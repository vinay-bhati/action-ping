from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def keep_app_awake(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Let the page load

        try:
            # Switch into the iframe
            iframe = driver.find_element(By.TAG_NAME, "iframe")
            driver.switch_to.frame(iframe)
            time.sleep(2)

            # Now find the input field (your email input)
            input_box = driver.find_element(By.XPATH, "//input[@type='text']")
            input_box.clear()
            input_box.send_keys("test@example.com")
            print(f"Interacted at {time.ctime()}")

            # Switch back to main page
            driver.switch_to.default_content()

        
        except Exception as e:
            print(f"No interaction performed: {e}")

    except Exception as e:
        print(f"Script error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    keep_app_awake("https://rv-cal.streamlit.app/")
    keep_app_awake("https://rv-cal-v2.streamlit.app/")
