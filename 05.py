'''
Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

string = str(input('Digite uma palavra ou frase qualquer: '))
cont = -1
stringInversa = []

#For para percorrer a string digitada, e adicionar regressivamente cada caractere
#dentro de uma lista
for letra in range(len(string)-1, -1, -1):
    stringInversa.append(string[cont])
    string[cont]
    cont -= 1
', '.join(stringInversa)

print(f'A palavra ou frase invertida é {"".join(stringInversa)} ')
