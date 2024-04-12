import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    """
    Setup the Chrome driver
    Allow the page to load
    Locate the cookie and cookie count
    Start time
    Every 5 seconds, check for upgrades
    Attempt to buy the most expensive affordable upgrade
    After 2 minutes, print cookies per second
    Clean up
    """
    # Setup the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    # Allow the page to load
    time.sleep(10)  # Adjust this based on your internet speed

    # Locate the cookie and cookie count
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie_count = driver.find_element(By.ID, "cookies")

    # Start time
    start_time = time.time()
    while time.time() - start_time < 120:  # Run for 2 minutes
        cookie.click()

        # Every 5 seconds, check for upgrades
        if int((time.time() - start_time) % 5) == 0:
            try:
                # Attempt to buy the most expensive affordable upgrade
                products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
                if products:
                    # The most expensive one that is affordable appears at the bottom of the list
                    products[-1].click()
            except:
                pass  # If something goes wrong (like a timing issue), just pass

    # After 2 minutes, print cookies per second
    cookies_per_second = cookie_count.text.split(" : ")[1]
    print(f"Cookies per second: {cookies_per_second}")

    # Clean up
    driver.quit()

if __name__ == "__main__":
    main()