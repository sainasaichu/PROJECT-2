from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Firefox WebDriver
driver = webdriver.Firefox()

try:
    # Launch the website
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Wait for the "Forgot your password?" link to be clickable and then click it
    forgot_password_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Forgot your password?"))
    )
    forgot_password_link.click()

    # Wait for the username field to be present, then enter a username to reset password
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys("Admin")  # Replace with the correct username

    # Click on the reset button
    reset_button = driver.find_element(By.XPATH, '//button[text()="Reset Password"]')
    reset_button.click()

    # Simulate waiting for an email and resetting the password (for demonstration purposes)
    # In a real scenario, you would handle the actual email verification and password reset steps
    time.sleep(5)  # Wait for a few seconds to simulate email handling

    # Enter new password
    new_password = "Admin1234"

    # Go back to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys("Admin")

    # Enter the new password
    password_field = driver.find_element(By.NAME, "Admin1234")
    password_field.send_keys(new_password)

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
