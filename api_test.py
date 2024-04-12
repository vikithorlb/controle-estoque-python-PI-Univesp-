import requests
from datetime import datetime

def obter_data_hora_formatada():
    agora = datetime.now()
    return agora.strftime("%Y-%m-%d %H:%M:%S")

url = 'http://127.0.0.1:500'

response = requests.get(url)

with open('log.txt', 'a') as file:
    file.write(f'{obter_data_hora_formatada()} - ')
    if response.status_code == 200:
        file.write('Teste da API bem-sucedido!\n')
    else:
        file.write(f'Falha ao testar a API: {response.status_code}\n')

