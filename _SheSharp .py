import os, requests, uuid, json
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client


def traduzir():
    #Dados do serviço cognitivo
    subscription = 'subscription do serviço'
    endpoint = 'https://api.cognitive.microsofttranslator.com/'

    #Qual é a API
    path = '/translate?api-version=3.0'

    #Qual idioma origem e destino
    params = '&to=pt&to=en'
    constructed_url = endpoint + path + params

    print (constructed_url)

    #Autenticação...
    headers = {
        'Ocp-Apim-Subscription-Key': subscription,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    #O que vamos traduzir
    body = [{
        'text': 'Mulheres Maravilhosas!'
    }]

    #Criar uma solicitação POST usando o módulo requests. 
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()

    #imprimir os resultados
    print(json.dumps(response, sort_keys=True, indent=4,
                    ensure_ascii=False, separators=(',', ': ')))

if __name__ == '__main__':
     traduzir()