import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

def main():

    #acessa o navegador na pasta
    service = Service(executable_path="C:/Users/2160044544/OneDrive - Grupo Casas Bahia S.A/Área de Trabalho/AutoPontuacao/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    #--------------------Tela de login---------------------

    # 1. Acessar a página e colar o número do pedido
        # driver.get("URL_AQUI")
    driver.get("http://admin.casasbahia.com.br/Site/Login.aspx")

    # 2. Preenche o campo usuario
    campo_usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_Conteudo_ctrLogin_UserName")))
    campo_usuario.send_keys("brunod.silva")

    # 3. Preenche o campo senha
    campo_senha = driver.find_element(By.ID, "ctl00_Conteudo_ctrLogin_Password")
    campo_senha.send_keys("SiL1195vA.")

    # 4. Clica no botão de login
    Botão_login = driver.find_element(By.ID, "ctl00_Conteudo_ctrLogin_Login")
    Botão_login.click()

    #--------------------Página inicial---------------------

    #menu_principal = driver.find_element(By.NAME, "Controle de Vendas")
    #ActionChains(driver).move_to_element(menu_principal).perform()

    #controle_de_vendas = WebDriverWait(driver, 5).until(
    #    EC.element_to_be_clickable((By.ID, "AspNet-Menu-Link"))
    #)



    input("Pressione ENTER para fechar o navegador...")
    driver.quit()


def fluxo_correto(resultado):
    pass


def fluxo_divergente(resultado):
    pass


if __name__ == "__main__":
    main()
