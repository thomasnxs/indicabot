import time
import pickle
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Função para salvar os cookies em um arquivo
def salvar_cookies(driver, caminho_arquivo="cookies.pkl"):
    cookies = driver.get_cookies()
    with open(caminho_arquivo, "wb") as arquivo:
        pickle.dump(cookies, arquivo)

# Função para carregar os cookies de um arquivo
def carregar_cookies_arquivo(driver, caminho_arquivo="cookies.pkl"):
    try:
        with open(caminho_arquivo, "rb") as arquivo:
            cookies = pickle.load(arquivo)
            for cookie in cookies:
                driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(3)
    except FileNotFoundError:
        print("Arquivo de cookies não encontrado. Será necessário fazer o login manualmente.")

# CONFIGURAÇÕES DO NAVEGADOR BRAVE
options = Options()
options.add_argument("--start-maximized")
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# ADICIONAR O PERFIL PADRÃO DO USUÁRIO
options.add_argument(r"--user-data-dir=C:\Users\Thomas\AppData\Local\BraveSoftware\Brave-Browser\User Data")
options.add_argument("--profile-directory=Default")

# CAMINHO DO CHROMEDRIVER
service = Service("C:/Users/Thomas/Desktop/Projetos Curso ReactNative/indicabot/chromedriver.exe")

# LER A PLANILHA
df = pd.read_excel("dados.xlsx")
print(f"Iniciando bot com {len(df)} cadastros...")

cadastros_feitos = 0

for index, row in df.iterrows():
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 20)

    driver.get("https://atituseducacao.beeviral.app/cadastro/atitus#iFrameWidgetDesign")

    # Tempo para login manual na primeira vez
    if index == 0:
        print("Tempo para fazer login manual. O script aguardará 5 segundos...")
        time.sleep(2)#se der b.o muda essa merda pra 5

    carregar_cookies_arquivo(driver)
    time.sleep(3) #se der bomba muda essa merda pra 4

    try:
        # Esperar o iframe carregar e mudar para ele
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

        # Preencher os campos com espera explícita
        wait.until(EC.presence_of_element_located((By.NAME, "NM_PEOPLE_DI"))).send_keys(row["Nome"])  # Nome
        driver.find_element(By.NAME, "9200").send_keys(row["Email"])  # Email
        driver.find_element(By.NAME, "9199").send_keys(str(row["Telefone"]))  # Telefone
        driver.find_element(By.NAME, "12145").send_keys(row["Curso de Interesse"])  # Curso de Interesse
        driver.find_element(By.NAME, "12391").send_keys(row["Campus"])  # Campus
        
        # Preencher campo de "Sua indicação veio de uma atlética?" com "Sim"
        driver.find_element(By.NAME, "15747").send_keys("Sim")
        
        # Preencher campo "Nome da Atlética" com o valor da última coluna (Nome da Atlética)
        driver.find_element(By.NAME, "15748").send_keys(row["Nome da Atlética"])  # Nome da Atlética

        time.sleep(0.5)

        # Clicar no botão de envio
        botao = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#btnRegisterWidget_text")))
        botao.click()

        print(f"[{index + 1}/{len(df)}] Cadastro realizado para: {row['Nome']}")

        # Esperar mais alguns segundos para garantir que o cadastro foi registrado
        time.sleep(3)  # Garantir tempo para o envio ser processado

        if index == 0:
            salvar_cookies(driver)
            print("Cookies salvos para uso nas próximas execuções.")

    except Exception as e:
        print(f"Erro no cadastro {index + 1}: {e}")

    driver.quit()
    cadastros_feitos += 1
    time.sleep(2)

print(f"\nTodos os {cadastros_feitos} cadastros foram finalizados com sucesso!")
