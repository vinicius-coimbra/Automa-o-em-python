from selenium  import webdriver
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
 
navegador = webdriver.Chrome(service=servico)

