import random as rdm

palavras = {
    'animal': ['raposa', 'elefante', 'pinguim', 'cachorro', 'gato'],
    'construção': ['prédio', 'casa', 'loja', 'fazenda'],
    'linguagem de programação': ['python', 'java', 'javascript'],
    'fruta': ['banana', 'maça', 'abacate', 'uva', 'tomate', 'kiwi']
}

categoria = rdm.choice(list(palavras.keys()))
palavra = rdm.choice(palavras[categoria])

descoberta = False
tentativas = 6
descobrir = ['_'] * len(palavra)
letras = set()

print(f"Categoria: {categoria}")

print(palavra)
print(descobrir)

def validar_letra(letra):
    if len(letra) != 1:
        print('Insira apenas uma letra!')
        return False
    if not letra.isalpha():
        print('Insira uma letra válida!')
        return False
    return True

def adicionar_letra(letter, word, incognita):
    for index, let in enumerate(word):
        if letter == word[index]:
            incognita[index] = letter
    print(f'A letra {letter} estava na palavra!\n{"".join(incognita)}')
    return


while not descoberta and tentativas > 0:
    letra = input('Insira uma letra: ').strip().lower()
    print(letra)
    if validar_letra(letra):
        if letra in letras:
            print(f'Você já tentou a letra "{letra}".\nAs letras já tentadas foram {letras}')
            continue

        letras.add(letra)
        if letra in palavra:
            adicionar_letra(letra, palavra, descobrir)

        else:
            tentativas -= 1
            print(f'A letra {letra} não existe na palavra!\nTentativas restantes: {tentativas}')
    else:
        continue
    if (''.join(descobrir)) == palavra:
        descoberta = True
        print('Parabéns, você acertou a palavra')
        break




