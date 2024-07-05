from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Firefox WebDriver
driver = webdriver.Firefox()

try:
    # Launch the website
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Wait for the username field to be present, then enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys("Admin")  # Replace with the correct username if needed

    # Enter the password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin123")  # Replace with the correct password if needed

    # Click the login button
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()

    # Wait for the dashboard to load and confirm successful login
    dashboard_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h6[text()="Dashboard"]'))
    )
    print("Login successful:", dashboard_header.text == "Dashboard")

finally:
    # Close the browser
    driver.quit()
