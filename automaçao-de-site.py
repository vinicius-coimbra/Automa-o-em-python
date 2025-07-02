from selenium  import webdriver
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
 
navegador = webdriver.Chrome(service=servico)

navegador.get("https://dlp.hashtagtreinamentos.com/python/minicurso/minicurso-automacao/inscricao?curso=python&origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M&utm_campaign=programacao&utm_content=python%2Fminicurso%2Fminicurso-automacao%2Finscricao&conversion=lespy-Jul-25")

navegador.find_element("xpath", '//*[@id="firstname"]').send_keys("vinicius")
navegador.find_element("xpath", '//*[@id="email"]').send_keys("vctellesfigueiredo@gmail.com")
navegador.find_element("xpath", '//*[@id="phone"]').send_keys("21341444")

input("")