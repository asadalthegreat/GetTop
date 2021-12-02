from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome(executable_path='/Users/jordan/Projects/chromedriver')
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)
driver.implicitly_wait(4)

# open the url
driver.get('https://www.gettop.us/')
##OLD
# search = driver.find_element(By.NAME, 'icon-search')
# search.clear()
# search.send_keys('iPhone')

# wait for 4 sec
# driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Error, search button is not clickable')

# click search
# driver.find_element(By.NAME, 'nav-top-link').click()

# verify
# assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
# print('Test Passed')

driver.quit()
