'''
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
faça um programa, na linguagem que desejar, que calcule e retorne:

• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
'''

import json # Importanto biblioteca Python para o tratamento de arquivos JSON
from modulos.titulo import titulo

#Conversão da lita JSON para um dicionário Python
with open("dados.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)


media_mensal = 0
soma = 0
maior_faturamento = 0
menor_faturamento = 0


#Fazendo a soma do faturamento mensal.
cont = 0
dia = 0
for i in dados:
    soma += dados[cont]['valor']
    if dados[cont]['valor'] > maior_faturamento:
        maior_faturamento = dados[cont]['valor']
        dia_maior = dados[cont]['dia']

    elif dados[cont]['valor'] < maior_faturamento:
        menor_faturamento = dados[cont]['valor']
        dia_menor = dados[cont]['dia']

    cont += 1


#Fazendo a média do faturamento mensal, desconsiderando os dias em que o faturamento foi 0
cont = 0 # Reiniciando o contador para um novo looping
dias_validos = 0
for d in dados:
    if dados[cont]['valor'] > 0:
        dias_validos += 1
    cont += 1
media_mensal = soma / dias_validos


#Verificação de quantas vezes e quais dias o faturamento diário foi maior que a média de faturamento mensal.
cont = 0 #Reiniciando o contador para um novo looping
maior_que_a_media = 0
dias_maiores = []
for c in dados:
    if dados[cont]['valor'] > media_mensal:
        maior_que_a_media += 1
        dias_maiores.append(dados[cont]['dia'])
    cont += 1


#Verificação para exibição correta do primeiro dia do mês.
if dia_maior == 1:
    dia_maior = '1º'
elif dia_menor == 1:
    dia_menor = '1º'


titulo('Faturamentos')
print(f'O maior faturamento foi de R${maior_faturamento:.2f} no dia {dia_maior}')
print(f'O menor faturamento foi de R${menor_faturamento:.2f} no dia {dia_menor}')
print(f'O faturamento mensal médio foi de R${media_mensal:.2f}.')
print(f'O faturamento diário, superou o faturamento mensal {maior_que_a_media} vezes, nos dias {str(dias_maiores)[1:-1]}.')


