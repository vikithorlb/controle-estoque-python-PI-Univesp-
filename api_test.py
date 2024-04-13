import requests
from datetime import datetime

def obter_data_hora_formatada():
    agora = datetime.now()
    return agora.strftime("%Y-%m-%d %H:%M:%S")

# Verifica se estamos no GitHub Actions
if 'GITHUB_ACTIONS' in os.environ:
    # Se estivermos no GitHub Actions, usar a URL do ambiente de CI
    url = 'https://exemplo-ci.com/api'
else:
    # Caso contrário, usar a URL local para testes
    url = 'http://127.0.0.1:5000'

try:
    response = requests.get(url)

with open('log.txt', 'a') as file:
    file.write(f'{obter_data_hora_formatada()} - ')
    if response.status_code == 200:
        file.write('Teste da API bem-sucedido!\n')
    else:
        file.write(f'Falha ao testar a API: {response.status_code}\n')

