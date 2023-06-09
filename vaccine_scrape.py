from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get("http://tabnet.datasus.gov.br/cgi/dhdat.exe?bd_pni/cpnibr.def")
browser.maximize_window()

# Click all the option elements to fill the form properly using their XPATH
Linha = browser.find_element(By.XPATH, "/html/body/center[2]/div[@class='container']/form/div[@class='borda']/div[@class='corpoperiodo']/div[@class='linha']/select[@id='L']/option[3]")
Linha.click()
Coluna = browser.find_element(By.XPATH, value="/html/body/center[2]/div[@class='container']/form/div[@class='borda']/div[@class='corpoperiodo']/div[@class='coluna']/select[@id='C']/option[5]")
Coluna.click()
Medidas = browser.find_element(By.XPATH, value="/html/body/center[2]/div[@class='container']/form/div[@class='borda']/div[@class='corpoperiodo']/div[@class='conteudo']/select[@id='I']/option[2]")
Medidas.click()

Mostra = browser.find_element(By.XPATH, value="/html/body/center[2]/div[@class='container']/form/div[@class='selecoes']/div[@class='input']/div[@class='botoes']/input[1]")
Mostra.click()

