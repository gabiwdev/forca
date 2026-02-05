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

