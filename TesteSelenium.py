import time
import subprocess
import pandas as pd
from unittest import result

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

def consultar_pedido_ponto(driver, numero_pedido): 
    
    #--------------------Tela de login---------------------
    
    # 1.1. Acessar a página de login
    driver.get("http://admin.pontofrio.com.br/Site/Login.aspx")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "ctl00_Conteudo_ctrLogin_UserName")))

    # 1.2. Preenche o campo usuario
    campo_usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_Conteudo_ctrLogin_UserName")))
    campo_usuario.send_keys("brunod.silva")

    # 1.3. Preenche o campo senha
    campo_senha = driver.find_element(By.ID, "ctl00_Conteudo_ctrLogin_Password")
    campo_senha.send_keys("SiL1195vA.")

    # 1.4. Clica no botão de login
    Botão_login = driver.find_element(By.ID, "ctl00_Conteudo_ctrLogin_Login")
    Botão_login.click()

    #--------------------Página inicial---------------------
    
    # 2.1. Valida o login validando algum objeto que existe na página inicial
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Controle de Vendas']")))
    
    # 2.2. Acessa a página de consulta de pedidos
    Pagina_inicial =  driver.find_element(By.XPATH, "//a[@title='Controle de Vendas']")
    
    # 2.3. Move o mouse para o elemento "Controle de Vendas" e clica na opção "Compras"
    ActionChains(driver).move_to_element(Pagina_inicial).perform()
    opcao_compras = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Compras']")))
    opcao_compras.click()

    #--------------------Página de Compra Consulta---------------------

    # 3.1. Abre o filtro para consultar o numero do pedido
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00_Conteudo_AjaxFiltro")))
    filtro = driver.find_element(By.ID, "ctl00_Conteudo_imgabrefecha")
    filtro.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00_Conteudo_AjaxFiltro")))
    filtro = driver.find_element(By.ID, "ctl00_Conteudo_imgabrefecha")
    filtro.click()

    # 3.2. Preenche o campo de compra com o número do pedido
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "ctl00_Conteudo_btnFiltrar")))
    campo_pedido = driver.find_element(By.ID, "ctl00_Conteudo_tbxIdCompra_txtId")
    campo_pedido.send_keys(numero_pedido)

    # 3.3. Clica no botão de pesquisar
    botao_pesquisar = driver.find_element(By.ID, "ctl00_Conteudo_btnFiltrar")
    botao_pesquisar.click()

    # 3.4. Clica no link do pedido para abrir a tela de detalhes
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00_Conteudo_rptCompra_ctl01_lnkCompraDetalhe")))
        
    except TimeoutException:
        return None 
           
    Click_pedido = driver.find_element(By.ID, "ctl00_Conteudo_rptCompra_ctl01_lnkCompraDetalhe")
    Click_pedido.click()

    #--------------------Validação de Elegibilidade---------------------
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00_Conteudo_Tabs_Panel1_lblParceiro")))
    
    # 4.1. Valida o parceiro
    Parceiro = driver.find_element(By.ID, "ctl00_Conteudo_Tabs_Panel1_lblParceiro")
    Parceiro_texto = Parceiro.text.strip()
    
    # 4.2. Valida a midia
    Midia = driver.find_element(By.ID, "ctl00_Conteudo_Tabs_Panel1_lblMidia")
    Midia_texto = Midia.text.strip()
    
    # 4.3. Valida a campanha
    Campanha = driver.find_element(By.ID, "ctl00_Conteudo_Tabs_Panel1_lblCampanha")
    Campanha_texto = Campanha.text.strip()
    
    if Parceiro_texto == "b2b_livelo" and Midia_texto == "livelo" and Campanha_texto == "livelo_acumulo":
        resultado = "Elegível"
        return resultado
    
    else:
        resultado = "Não Elegível"
        return resultado


def consultar_pedido_cb(driver, numero_pedido):

    #--------------------Página inicial---------------------
    
    # 2.1. Valida o login validando algum objeto que existe na página inicial
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Controle de Vendas']")))
    
    # 2.2. Acessa a página de consulta de pedidos
    Pagina_inicial =  driver.find_element(By.XPATH, "//a[@title='Controle de Vendas']")
    
    # 2.3. Move o mouse para o elemento "Controle de Vendas" e clica na opção "Compras"
    ActionChains(driver).move_to_element(Pagina_inicial).perform()
    opcao_compras = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Compras']")))
    opcao_compras.click()

    #--------------------Página de Compra Consulta---------------------

    # 3.1. Abre o filtro para consultar o numero do pedido
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00_Conteudo_AjaxFiltro")))
    filtro = driver.find_element(By.ID, "ctl00_Conteudo_imgabrefecha")
    filtro.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00_Conteudo_AjaxFiltro")))
    filtro = driver.find_element(By.ID, "ctl00_Conteudo_imgabrefecha")
    filtro.click()

    # 3.2. Preenche o campo de compra com o número do pedido
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "ctl00_Conteudo_btnFiltrar")))
    campo_pedido = driver.find_element(By.ID, "ctl00_Conteudo_tbxIdCompra_txtId")
    campo_pedido.send_keys(numero_pedido)

    # 3.3. Clica no botão de pesquisar
    botao_pesquisar = driver.find_element(By.ID, "ctl00_Conteudo_btnFiltrar")
    botao_pesquisar.click()

    # 3.4. Clica no link do pedido para abrir a tela de detalhes
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00_Conteudo_rptCompra_ctl01_lnkCompraDetalhe")))
        
    except TimeoutException:
        print(f"\nPedido {numero_pedido} não é Casas Bahia.")
        return None 
           
    Click_pedido = driver.find_element(By.ID, "ctl00_Conteudo_rptCompra_ctl01_lnkCompraDetalhe")
    Click_pedido.click()

    #--------------------Validação de Elegibilidade---------------------
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00_Conteudo_Tabs_Panel1_lblParceiro")))
    
    # 4.1. Valida o parceiro
    Parceiro = driver.find_element(By.ID, "ctl00_Conteudo_Tabs_Panel1_lblParceiro")
    Parceiro_texto = Parceiro.text.strip()
    
    # 4.2. Valida a midia
    Midia = driver.find_element(By.ID, "ctl00_Conteudo_Tabs_Panel1_lblMidia")
    Midia_texto = Midia.text.strip()
    
    # 4.3. Valida a campanha
    Campanha = driver.find_element(By.ID, "ctl00_Conteudo_Tabs_Panel1_lblCampanha")
    Campanha_texto = Campanha.text.strip()
    
    if Parceiro_texto == "b2b_livelo" and Midia_texto == "livelo" and Campanha_texto == "livelo_acumulo":
        resultado = "Elegível"
        return resultado
    
    else:
        resultado = "Não Elegível"
        return resultado



def main():

    # Inicia o Chrome
    service = Service(executable_path="C:\\Users\\2160044544\\OneDrive - Grupo Casas Bahia S.A\\Área de Trabalho\\AutoPontuacao\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    #--------------------Tela de login---------------------
    
    # 1.1. Acessar a página de login
    driver.get("http://admin.casasbahia.com.br/Site/Login.aspx")

    # 1.2. Preenche o campo usuario
    campo_usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_Conteudo_ctrLogin_UserName")))
    campo_usuario.send_keys("brunod.silva")

    # 1.3. Preenche o campo senha
    campo_senha = driver.find_element(By.ID, "ctl00_Conteudo_ctrLogin_Password")
    campo_senha.send_keys("SiL1195vA.")

    # 1.4. Clica no botão de login
    Botão_login = driver.find_element(By.ID, "ctl00_Conteudo_ctrLogin_Login")
    Botão_login.click()

    #---------------------Pedidos em lista---------------------

    #5.1. Lista de pedidos a serem consultados
 
    pedidos = ["518383367","517969219","517766780","518583071"] 

    for pedido in pedidos:
        resultado = consultar_pedido_cb(driver, pedido)
        
        if resultado is None:
            resultado = consultar_pedido_ponto(driver, pedido)
            
            if resultado is None:
                resultado = "Pedido não encontrado"

        print(f"Pedido {pedido}: {resultado}\n")

    input("\nPressione ENTER para fechar o navegador...")
    driver.quit()


def fluxo_correto(resultado):
    pass


def fluxo_divergente(resultado):
    pass


if __name__ == "__main__":
    main()
