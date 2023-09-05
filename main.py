from docx import Document
from datetime import datetime
from random import randint

document = Document('Recibo.docx')

print('='*60)
print('        ====== Gerador de Recibo ======')
print('='*60)

print('='*60)
nome = str(input('Digite o nome do cliente: '))
print('='*60)
cpf = str(input('Digite seu CPF: '))
print('='*60)
endereço = str(input('Digite seu endereço: '))
print('='*60)
valor = float(input('Digite o valor: '))
print('='*60)
descricao = str(input('Digite o serviço: '))
print('='*60)
data = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'

lista = []
for n in range(0, 4):
    lista.append(randint(1, 10))

codigo = f'{lista[0]}{lista[1]}{lista[2]}{lista[3]}'

referencias = {
    'ZZZZZZ': nome,
    'aaa': cpf[:3],
    'bbb': cpf[3:6],
    'ccc': cpf[6:9],
    'dd': cpf[9:],
    'SSSSS': endereço,
    'XXXX,XX': str(valor),
    'fffffff': descricao,
    '(Data da movimentação)': data,
    '(Número do recibo)': codigo
}

for paragrafo in document.paragraphs:
    for linha in referencias:
        paragrafo.text = paragrafo.text.replace(linha, referencias[linha])

document.save(f'Recibo - {nome}')

print('='*60)
print('O recibo foi gerado com sucesso!')
print('='*60)
