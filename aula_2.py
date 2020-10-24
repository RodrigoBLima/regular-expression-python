import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

print(re.findall('João|Maria|ad....s', texto))
print(re.findall('[Jj]oão|[Mm]aria|ad....s', texto))

print(re.findall('[a-sA-S]aria', texto))  # QUALQUER LETRA ENTRE ESSE RANGE
print(re.findall('[a-sA-S]aria|[a-sA-S]oão', texto))

print(re.findall('jOãO|MaRiA', texto, flags=re.IGNORECASE))
