from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
# Obtener la ruta al controlador de Selenium para Microsoft Edge basado en Chromium
driver_path = EdgeChromiumDriverManager().install()

# Configurar las opciones de Microsoft Edge basado en Chromium
options = webdriver.EdgeOptions()

# Inicializar el navegador Microsoft Edge basado en Chromium
driver = webdriver.Edge(service=Service(executable_path=driver_path), options=options)

url = "https://www.google.com/maps/search/veterinarias/"
driver.get(url)
wait = WebDriverWait(driver, 10)
link_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@class, "hfpxzc")]')))
href_values = [element.get_attribute('href') for element in link_elements]
name = [element.get_attribute('aria-label') for element in link_elements]

data = {
        'name': name,
        'href_values': href_values, 
        }
df = pd.DataFrame(data)

# Recorrer el DataFrame
for index, row in df.iterrows():
    href = row['href_values']
    
    # Abrir el enlace en una nueva pestaña
    driver.execute_script("window.open('" + href + "', '_blank')")
    # Esperar a que se cargue la página
    time.sleep(5)
    # lbl_fecha = driver.find_element('xpath', '//*[@id="main-root"]/div[2]/section/div/div/div[1]/div/div/div[2]/div/div/label')
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class,"AeaXub")]')))
    # Obtener el texto del elemento
    ubicacion = element.text
    
    xpath_abierto = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[4]/div[1]/div[2]/div/span[1]/span/span')))
    abierto  = xpath_abierto.text
    xpath_web = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[5]/a/div/div[2]/div[1]')))
    web  = xpath_web.text
    xpath_celular = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[6]/button/div/div[2]/div[1]')))
    celular  = xpath_celular.text
    
    xpath_puntuacion = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[1]/span[1]')))
    puntuacion  = xpath_puntuacion.text

    # Agregar los valores al DataFrame
    df.at[index, 'ubicacion'] = ubicacion
    df.at[index, 'abierto'] = abierto
    df.at[index, 'web'] = web
    df.at[index, 'celular'] = celular
    df.at[index, 'puntuacion'] = puntuacion

    
    # Cerrar la pestaña actual
    driver.close()
    
    # Cambiar al control de la pestaña anterior
    driver.switch_to.window(driver.window_handles[0])





df.to_excel('data.xlsx')


# Cerrar el navegador
driver.quit()