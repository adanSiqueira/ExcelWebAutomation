from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import openpyxl

def preencher_campo(driver, campo_id, valor, wait, timeout=10):
    """Limpa e preenche um campo identificado pelo ID, esperando até estar presente e clicável."""
    try:
        campo = wait.until(EC.element_to_be_clickable((By.ID, campo_id)))
        campo.clear()
        campo.send_keys(valor if valor is not None else "")
    except TimeoutException:
        print(f"[ERRO] Timeout ao tentar preencher o campo {campo_id}")
    except Exception as e:
        print(f"[ERRO] Problema ao preencher o campo {campo_id}: {e}")

def clicar_botao_por_xpath(driver, wait, xpath, timeout=10):
    """Espera até o botão estar clicável e o clica."""
    try:
        botao = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        botao.click()
    except TimeoutException:
        print(f"[ERRO] Timeout ao tentar clicar no botão com xpath {xpath}")
    except Exception as e:
        print(f"[ERRO] Problema ao clicar no botão com xpath {xpath}: {e}")

def main(arquivo):
    workbook = openpyxl.load_workbook(arquivo)
    sheet_products = workbook['Produtos']

    # options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920,1080")

    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.get("https://cadastro-produtos-devaprender.netlify.app/")

    wait = WebDriverWait(driver, 15) 

    try:
        for row in sheet_products.iter_rows(min_row=2):
            # 1ª página
            elementos_com_id = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id]")))
            ids = [el.get_attribute("id") for el in elementos_com_id]

            preencher_campo(driver, ids[0], row[0].value, wait)  # nome_produto
            preencher_campo(driver, ids[1], row[1].value, wait)  # descricao
            preencher_campo(driver, ids[2], row[2].value, wait)  # categoria
            preencher_campo(driver, ids[3], row[3].value, wait)  # codigo_produto
            preencher_campo(driver, ids[4], row[4].value, wait)  # peso
            preencher_campo(driver, ids[5], row[5].value, wait)  # dimensoes

            clicar_botao_por_xpath(driver, wait, "//button[contains(text(), 'Próximo')]")

            # 2ª página
            elementos_com_id = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id]")))
            ids = [el.get_attribute("id") for el in elementos_com_id]

            preencher_campo(driver, ids[0], row[6].value, wait)  # preco
            preencher_campo(driver, ids[1], row[7].value, wait)  # quantidade_em_estoque
            preencher_campo(driver, ids[2], row[8].value, wait)  # data_de_validade
            preencher_campo(driver, ids[3], row[9].value, wait)  # cor
            preencher_campo(driver, ids[4], row[10].value, wait) # tamanho
            preencher_campo(driver, ids[5], row[11].value, wait) # material

            clicar_botao_por_xpath(driver, wait, "//button[contains(text(), 'Próximo')]")

            # 3ª página
            elementos_com_id = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id]")))
            ids = [el.get_attribute("id") for el in elementos_com_id]

            preencher_campo(driver, ids[0], row[12].value, wait)  # fabricante
            preencher_campo(driver, ids[1], row[13].value, wait)  # pais_origem
            preencher_campo(driver, ids[2], row[14].value, wait)  # observacoes
            preencher_campo(driver, ids[3], row[15].value, wait)  # codigo_de_barras
            preencher_campo(driver, ids[4], row[16].value, wait)  # localizacao_armazem

            clicar_botao_por_xpath(driver, wait, "//button[contains(text(), 'Concluir')]")

            # Espera alerta e aceita
            try:
                alerta = wait.until(EC.alert_is_present())
                alerta.accept()
            except TimeoutException:
                print("[AVISO] Nenhum alerta apareceu após concluir.")

            # Clica no botão "Adicionar Mais Um" para novo cadastro
            clicar_botao_por_xpath(driver, wait, "//button[contains(@class, 'btn-primary') and contains(text(), 'Adicionar Mais')]")

        driver.quit()
        print("Todos os produtos foram cadastrados com sucesso!")
        return True

    except Exception as e:
        print(f"[ERRO] Erro geral na automação: {e}")
        driver.quit()
        return False

# if __name__ == "__main__":
#     main()