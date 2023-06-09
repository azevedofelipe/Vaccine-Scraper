from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


download_dir = "/Users/Felipe/Desktop/Projects/vacina_scrape/Downloads/"

options = Options()
options.add_experimental_option('prefs',  {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
    }
)
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

browser.get("http://tabnet.datasus.gov.br/cgi/dhdat.exe?bd_pni/cpnibr.def")
browser.maximize_window()

# Creates webdriver wait period for browser (5 seconds)
wait = WebDriverWait(browser,10)

# Click all the option elements to fill the form properly using their XPATH
Linha = browser.find_element(By.XPATH, "/html/body/center[2]/div[@class='container']/form/div[@class='borda']/div[@class='corpoperiodo']/div[@class='linha']/select[@id='L']/option[3]").click()
Coluna = browser.find_element(By.XPATH, value="/html/body/center[2]/div[@class='container']/form/div[@class='borda']/div[@class='corpoperiodo']/div[@class='coluna']/select[@id='C']/option[5]").click()
Medidas = browser.find_element(By.XPATH, value="/html/body/center[2]/div[@class='container']/form/div[@class='borda']/div[@class='corpoperiodo']/div[@class='conteudo']/select[@id='I']/option[2]").click()

# Prepares for opening second window
original_window = browser.current_window_handle
assert len(browser.window_handles) == 1

# Clicks button to open second window
Mostra = browser.find_element(By.XPATH, value="/html/body/center[2]/div[@class='container']/form/div[@class='selecoes']/div[@class='input']/div[@class='botoes']/input[1]").click()

wait.until(EC.number_of_windows_to_be(2))

# Loops through until new window handle found and switches to it
for window_handle in browser.window_handles:
    if window_handle != original_window:
        browser.switch_to.window(window_handle)
        break

wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/center[2]/div[@class='nivel2']/table[@class='escondido']/tbody/tr/td[2]/a")))


CSV = browser.find_element(By.XPATH, "/html/body/center[2]/div[@class='nivel2']/table[@class='escondido']/tbody/tr/td[2]/a").click()
time.sleep(5)
browser.quit()

