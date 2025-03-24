'''
1 - Entrar na planilha e extrair o cpf do cliente.
2 - Checar status de pagamento do cpf do cliente no site https://consultcpf-devaprender.netfly.app/
3 - Verificar status "em dia" ou "atrasado":
    3.1 - Se estiver em dia, pegar data do pagamento e método de pagamento.
    3.2 - Se estiver atrasado, colocar status como "pendente".
4 - Inserir essas novas informações(nome, cpf, vencimento, status[considerando informações do item 3.1]) em nova planilha.
5 - Looping até o último cliente.
'''
import pandas as pd
import openpyxl
from selenium.webdriver.common.by import By
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#df = pd.read_excel("./dados_clientes.xlsx")
# Passo 1:
planilha_clientes = openpyxl.load_workbook("./dados_clientes.xlsx")
page_clientes = planilha_clientes["Sheet1"]

driver = webdriver.Chrome()
driver.get("https://consultcpf-devaprender.netfly.app/")

for linha in page_clientes.iter_rows(min_row=2): #percorrer linhas da planilha a partir da linha 2
    nome, valor, cpf, vencimento = linha
    # Passo 2:
    campo_pesquisa = driver.find_element(By.XPATH, "//input[@id='cpfInput']")
    sleep(2)
    campo_pesquisa.send_keys(cpf)
    sleep(2)
    # Passo 3:
    clica_button = driver.find_element(By.XPATH, "//button[@class='btn btn-custom btn-lg btn-block mt-3']")
    sleep(1)
    clica_button.click()
    sleep(4)
    checa_status = driver.find_element(By.XPATH, "//span[@id='statusLabel']")
    if checa_status.text == "em dia":
        data_paga = driver.find_element(By.XPATH, "//p[@id='paymentDate']")
        metodo_paga = driver.find_element(By.XPATH, "//p[@id='paymentMethod']")
        
        text_data_paga = data_paga.text.split()[3]
        text_metd_paga = data_paga.text.split()[3]
        
        plan_fecha = openpyxl.load_workbook("./planilha fechamento.xlsx")
        page_fecha = plan_fecha["Sheet1"]
        
        page_clientes.append([nome, valor, cpf,vencimento, "Em dia", text_data_paga, text_metd_paga])
        plan_fecha.save("./planilha fechamento.xlsx")
    else:
        plan_fecha = openpyxl.load_workbook("./planilha fechamento.xlsx")
        page_fecha = plan_fecha["Sheet1"]
        
        page_fecha.append([nome, valor, cpf, vencimento, "Pendente"])
        plan_fecha.save("./planilha fechamento.xlsx")
    campo_pesquisa.clear()
