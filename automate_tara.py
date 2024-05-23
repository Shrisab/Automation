from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_and_set_options(memberID, memberDob, service_value="select2-selection__arrow"):
    # URL of the login page
    login_url = 'https://taradev.deerhold.com'
    
    # Initialize the WebDriver (Chrome in this example)
    driver = webdriver.Chrome()
    

    # Load the login page
    driver.get(login_url)
    
    # Fill in the login form
    member_id_field = driver.find_element(By.NAME, 'memberId')  # Update with actual field name
    dob_field = driver.find_element(By.NAME, 'memberDob')  # Update with actual field name
    member_id_field.send_keys(memberID)
    dob_field.send_keys(memberDob)
    
    # Submit the login form
    dob_field.send_keys(Keys.RETURN)
    
    # Wait for the dashboard to load
    time.sleep(5)
    
    # URL of the dashboard page (if needed)
    dashboard_url = 'https://taradev.deerhold.com/dashboard'
    driver.get(dashboard_url)

    # Use WebDriverWait to wait until the dropdown is present
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    
    # Find and set the "Select Billing Code Type" dropdown to its default value
    # billing_code_type_select = Select(driver.find_element(By.NAME, 'select2-procedure_code_type-container'))
    # billing_code_type_select.select_by_value('default_value')
    
    # Find and set the "Select Billing Code Type" dropdown to its default value
    # billing_code_type_select = wait.until(EC.presence_of_element_located((By.NAME, 'select2-procedure_code_type-container')))
    # billing_code_type_select = Select(billing_code_type_select)
    # billing_code_type_select.select_by_value('default_value')  # Update with the actual default value
    

    # Set the value for "Select your service"
    # service_select = Select(driver.find_element(By.NAME, 'select2-select_procedure_code1-container'))
    # service_select.select_by_visible_text(service_value)
    
    # Wait for the "Select your service" dropdown and set its value
    service_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-labelledby="select2-select_procedure_code1-container"]')))
    service_select.click()  # Click to activate the dropdown
    
    # Type the search query into the dropdown
    search_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field')))
    search_input.send_keys(service_value)
    
    # Wait for the search results to appear and select the appropriate option
    desired_option = wait.until(EC.presence_of_element_located((By.XPATH, f'//li[contains(text(), "{service_value}")]')))
    desired_option.click()  # Click the desired option
    

    # Click the "The least expensive option" button
    # least_expensive_button = driver.find_element(By.NAME, 'theleastexpensiveoption')
    # least_expensive_button.click()
    
    # Click the "The least expensive option" button
    least_expensive_button = wait.until(EC.element_to_be_clickable((By.NAME, 'theleastexpensiveoption')))  # Update with actual field name or ID
    least_expensive_button.click()

    # Wait for the results to load
    time.sleep(5)
    
    # Get the page source or any other necessary information
    page_source = driver.page_source
    print(page_source)
    
    # Close the browser
    driver.quit()

if __name__ == '__main__':
    memberID = '123456'
    memberDob = '01/01/1980'
    service_value = '99214 - Office O/P Est Mod 30-39 Min'
    login_and_set_options(memberID, memberDob, service_value)
