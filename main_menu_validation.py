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
    username_field.send_keys("Admin")

    # Enter the password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin123")

    # Click the login button
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()

    # Wait for the dashboard to load and confirm successful login
    dashboard_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h6[text()="Dashboard"]'))
    )
    print("Login successful:", dashboard_header.text == "Dashboard")

    # Validate main menu items
    main_menu_items = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard",
                       "Directory", "Maintenance", "Buzz"]
    for item in main_menu_items:
        menu_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//span[text()="{item}"]'))
        )
        print(f"Menu item '{item}' is present:", menu_item is not None)

    # Navigate to the Admin page
    admin_menu_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[text()="Admin"]'))
    )
    admin_menu_item.click()

    # Validate all options on the Admin page
    admin_page_options = ["User Management", "Job", "Organization", "Qualifications", "Nationalities",
                          "Corporate Branding", "Configuration"]
    for option in admin_page_options:
        admin_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//span[text()="{option}"]'))
        )
        print(f"Admin option '{option}' is present:", admin_option is not None)

finally:
    # Close the browser
    driver.quit()
