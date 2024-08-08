from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome() 
driver.get("https://www.demoblaze.com/index.html")
time.sleep(2)
driver.maximize_window()

# Entrar 
driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("AnaSacotoITSQMET")
driver.find_element(By.ID, "loginpassword").send_keys("instituto2024")
driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

time.sleep(3)

# Elegir productos
driver.find_element(By.LINK_TEXT, "Sony vaio i7").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Add to cart").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()

# Volver a la página principal
driver.find_element(By.ID, "nava").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Nokia lumia 1520").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Add to cart").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()

# Paso 4: Realizar Pedido
driver.find_element(By.ID, "cartur").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
time.sleep(2)

# Llenar el formulario de pedido
driver.find_element(By.ID, "name").send_keys("Ana Sacoto")
driver.find_element(By.ID, "country").send_keys("Ecuador")
driver.find_element(By.ID, "city").send_keys("Cuenca")
driver.find_element(By.ID, "card").send_keys("1543125635461586")
driver.find_element(By.ID, "month").send_keys("007")
driver.find_element(By.ID, "year").send_keys("2029")
driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]").click()

time.sleep(3)

driver.find_element(By.ID, "logout2").click()
time.sleep(2)

driver.quit()
