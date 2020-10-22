import re

string = 'Teste de expressoes Teste  regulares. Teste'

# search => pega o primeiro valor que der match
# findall => retorna uma lista com todos os valores do match
# sub => faz a substituicao dos valores do match para outro valor
# compile => faz uma compilação da minha expressão regular


# <_sre.SRE_Match object; span=(0, 5), match='Teste'>
print(re.search(r'Teste', string))

print(re.findall(r'Teste', string))  # ['Teste', 'Teste', 'Teste']

# Cabecinha de expressoes Cabecinha  regulares. Cabecinha
print(re.sub(r'Teste', 'Cabecinha', string))


regExp = re.compile(r'Teste')

print(regExp.search(string))
print(regExp.sub("Abacaxi", string))
print(regExp.findall(string))
