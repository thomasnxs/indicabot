from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Caminho para o driver do navegador (certifique-se de ter o chromedriver instalado corretamente)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Altere o caminho para o chromedriver no seu sistema

# Acesse a página de login
driver.get('https://yourwebsite.com')  # Substitua com a URL do seu site

# Defina os cookies aqui
cookies = [
    {'name': '__RequestVerificationToken', 'value': '6hAMnr1Upx-zeM68uEM0CCyTaY6qiSIk_bsCIIefAnUKxFvoTdxUtkfS5BUyG0kDmC0RQQiHmtsAUobBicF86Zi7ZAulYfat4W5Ur5LS08A1', 'domain': 'atituseducacao.beeviral.app', 'path': '/'},
    {'name': '__RequestVerificationToken', 'value': 'kSojr8gSFLyHI3Jdm8-8XQdhnAEvaBKRYXzH8v1ysC2UCq9j4wj-_juR_rLr8FA_yHlqraNXKH9Qu_7NE0kzrKdHk0bn5DQCljIHvPpdr1U1', 'domain': 'account.beeviral.app', 'path': '/'},
    {'name': 'ASP.NET_SessionId', 'value': '15sygcoyeuh2htb24nni2bk3', 'domain': 'atituseducacao.beeviral.app', 'path': '/'},
    {'name': 'ASP.NET_SessionId', 'value': 'mdbtyxtzjg42iquek1qpekxj', 'domain': 'account.beeviral.app', 'path': '/'},
    {'name': 'EWG_7510', 'value': '1125325@atitus.edu.br', 'domain': '.atituseducacao.beeviral.app', 'path': '/', 'expiry': '2025-05-16T16:58:30.139Z'},
    {'name': 'EWG_7510', 'value': '1125325@atitus.edu.br', 'domain': 'atituseducacao.beeviral.app', 'path': '/', 'expiry': '2025-11-05T18:41:37.852Z'},
    {'name': 'IDWG_7510', 'value': '2627489', 'domain': 'atituseducacao.beeviral.app', 'path': '/', 'expiry': '2025-11-05T18:41:37.852Z'},
    {'name': 'version', 'value': '2.0.0.26', 'domain': 'atituseducacao.beeviral.app', 'path': '/', 'expiry': '2025-11-05T16:57:32.339Z'},
    {'name': 'version', 'value': '2.0.0.26', 'domain': 'account.beeviral.app', 'path': '/', 'expiry': '2025-11-05T16:57:33.085Z'}
]

# Carregue os cookies no navegador
for cookie in cookies:
    driver.add_cookie(cookie)

# Atualize a página para aplicar os cookies
driver.refresh()

# Aguarde um pouco para garantir que a página seja carregada com os cookies aplicados
sleep(3)

# Agora o site deve estar carregado como se você estivesse logado
# Você pode interagir com o site normalmente
# Exemplo: acessar uma página interna ou verificar algo

# Caso deseje navegar em outra página após a autenticação:
# driver.get('https://yourwebsite.com/yourpage')

# Fecha o navegador depois de finalizar
driver.quit()
