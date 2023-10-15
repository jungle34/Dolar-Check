import requests
import json

data_inicio = "01/01/2010"
data_fim = "31/12/2023"

def dadosVenda():
    url_venda = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json&dataInicial="+str(data_inicio)+"&dataFinal="+str(data_fim)
    response_venda = requests.request("GET", url_venda)
    return json.loads(response_venda.text)

def dadosCompra():
    url_compra = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json&dataInicial="+str(data_inicio)+"&dataFinal="+str(data_fim)
    response_compra = requests.request("GET", url_compra)
    return json.loads(response_compra.text)

def dadosSelic():
    url_compra = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial="+str(data_inicio)+"&dataFinal="+str(data_fim)
    response_compra = requests.request("GET", url_compra)
    return json.loads(response_compra.text)

def variacaoMedia(dados):
    total = 0

    key = 0
    for item in dados:
        atual = item['valor']
        if key > 0:
            posterior = dados[key - 1]['valor']            
        
        
            
            variacao = float(posterior) - float(atual)
            total += variacao
        key += 1

    return (total / key)

def valorizacaoReal(dados):
    atual = float(dados[0]['valor'])
    max = float(dados[-1]['valor'])

    return (atual - max)

def valorizacaoPct(dados):
    atual = float(dados[0]['valor'])
    min = float(dados[-1]['valor'])

    return (((atual - min) / min) * 100)


def analiseCambial(dados, tipo):
    obj = {
        "variacaoMedia": variacaoMedia(dados),
        "valorizacaoReal": valorizacaoReal(dados),
        "valorizacaoPct": valorizacaoPct(dados),        
    }

    print(tipo)
    print(obj)


analiseCambial(dadosCompra(), 'Compra')
analiseCambial(dadosVenda(), 'Venda')
analiseCambial(dadosSelic(), 'Selic')





