from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Obtener la ruta al controlador de Selenium para Microsoft Edge basado en Chromium
driver_path = EdgeChromiumDriverManager().install()

# Configurar las opciones de Microsoft Edge basado en Chromium
options = webdriver.EdgeOptions()

# Inicializar el navegador Microsoft Edge basado en Chromium
driver = webdriver.Edge(service=Service(executable_path=driver_path), options=options)

url = "https://www.google.com/maps/search/veterinarias/"
driver.get(url)
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for the elements to be present
#link_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div//div//div//div//div//div//div//div//div//div//div//div//a//@href')))
# Aquí puedes realizar acciones adicionales en la página
# Encontrar todos los elementos de enlace de las veterinarias
link_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@class, "hfpxzc")]')))
href_values = [element.get_attribute('href') for element in link_elements]

name = [element.get_attribute('accessible_name') for element in link_elements]


# Cerrar el navegador
driver.quit()








# Cerrar el navegador
driver.quit()