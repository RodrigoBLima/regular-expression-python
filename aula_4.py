import re

texto = '''
    <p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <p>Frase 4</p> <p>Frase 5</p> <div>Frase 5</div> <div></div>
'''

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto)) #GULOSO #ambiguo
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto)) #NAÃO GULOSO #não ambiguo
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto)) #uma ou n vezes, precisar ter algo
