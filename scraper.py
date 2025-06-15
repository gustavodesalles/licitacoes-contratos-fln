import json
import requests

url = 'https://transparencia.e-publica.net/epublica-portal/rest/florianopolis/compras/licitacao/form?ano=2025&entidade=2002'

headers = {
  'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

registros = []

with open('responses/response_licitacoes_2018-2024.json', 'r') as f:
    data = json.load(f)
    # anos = ['2015', '2016', '2017']
    ids_licitacao = []

    # print(len(data))
    for item in data['rows']:
        # if item['numero'][-4:] in anos:
            id_licitacao = item['id']
            ids_licitacao.append(id_licitacao)

    for id_licitacao in ids_licitacao:
        payload = json.dumps({
            "id": id_licitacao,
            "mode": "INFO"
        })
        # response = requests.post(url, headers=headers, data=payload)

        retry = True
        while retry:
            response = requests.post(url, headers=headers, data=payload)
            if response.status_code == 200:
                retry = False
                registro = response.json()['pojo']
                registros.append(registro)
                print(id_licitacao)
# print(len(registros))

with open(f'licitacoes_2018-2024.json', 'w') as f:
    json.dump(registros, f)