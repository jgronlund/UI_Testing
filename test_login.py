import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up Chrome WebDriver
driver = webdriver.Chrome()  # Or webdriver.Firefox()

# Start the Flask app manually before running this script
driver.get("http://127.0.0.1:5000/login")

def test_successful_login():
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("1234")
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()
    
    time.sleep(1)  # Let the page load
    assert "Dashboard" in driver.title or "Welcome" in driver.page_source
    print("Successful login test passed")

def test_failed_login():
    driver.get("http://127.0.0.1:5000/login")
    driver.find_element(By.NAME, "username").send_keys("wronguser")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()

    time.sleep(1)
    assert "Invalid credentials" in driver.page_source
    print("Failed login test passed")

# Run tests
test_successful_login()
test_failed_login()

# Quit driver
driver.quit()
