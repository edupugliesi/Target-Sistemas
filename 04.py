'''
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
que cada estado teve dentro do valor total mensal da distribuidora.
'''

total = 67836.43 + 36678.66 + 29229.88 + 27165.48 + 19849.53

sp = (67836.43 / total) * 100
rj = (36678.66 / total) * 100
mg = (29229.88 / total) * 100
es = (27165.48 / total) * 100
outros = (19849.53 / total) * 100

print(f'O faturamento total da distruidora em todos os estados foi de R${total:.2f}')
print(f'A representatividade do estado de São Paulo foi de {sp:.2f}%')
print(f'A representatividade do estado do Rio de Janeiro foi de {rj:.2f}%')
print(f'A representatividade do estado de Minas Gerais foi de {mg:.2f}%')
print(f'A representatividade do estado de Espirito Santo foi de {es:.2f}%')
print(f'A representatividade dos outros estados foi de {outros:.2f}%')