import random as rdm

palavras = {
    'animal': [
        'cachorro', 'gato', 'elefante', 'leao', 'tigre', 'girafa', 'zebra',
        'macaco', 'pinguim', 'golfinho', 'tartaruga', 'coelho', 'raposa',
        'urso', 'lobo', 'cobra', 'aguia', 'coruja', 'rinoceronte', 'hipopotamo'
    ],

    'fruta': [
        'banana', 'maca', 'abacate', 'uva', 'kiwi', 'laranja', 'limao',
        'morango', 'manga', 'pera', 'melancia', 'abacaxi', 'ameixa',
        'cereja', 'framboesa', 'pessego', 'figo', 'caju'
    ],

    'objeto': [
        'cadeira', 'mesa', 'computador', 'telefone', 'teclado', 'mouse',
        'janela', 'porta', 'garrafa', 'caneta', 'lapis', 'caderno',
        'mochila', 'relógio', 'espelho', 'ventilador', 'televisao'
    ],

    'lugar': [
        'cidade', 'praia', 'montanha', 'floresta', 'deserto', 'ilha',
        'aeroporto', 'hospital', 'escola', 'universidade', 'biblioteca',
        'restaurante', 'cinema', 'parque', 'castelo', 'estadio'
    ],

    'profissao': [
        'medico', 'engenheiro', 'professor', 'programador', 'advogado',
        'arquiteto', 'jornalista', 'designer', 'cozinheiro', 'bombeiro',
        'policial', 'piloto', 'cientista', 'fotografo', 'musico'
    ],

    'linguagem de programacao': [
        'python', 'java', 'javascript', 'typescript', 'csharp', 'ruby',
        'php', 'go', 'rust', 'kotlin', 'swift', 'scala', 'haskell'
    ],

    'verbo': [
        'correr', 'pular', 'pensar', 'comer', 'beber', 'dormir', 'escrever',
        'ler', 'programar', 'viajar', 'nadar', 'cantar', 'dançar',
        'construir', 'aprender', 'ensinar'
    ],

    'adjetivo': [
        'feliz', 'triste', 'rapido', 'lento', 'forte', 'fraco', 'inteligente',
        'corajoso', 'curioso', 'calmo', 'nervoso', 'gentil', 'agressivo',
        'criativo', 'preguicoso'
    ]
}

categoria = rdm.choice(list(palavras.keys()))
palavra = rdm.choice(palavras[categoria])

descoberta = False
tentativas = 6
descobrir = ['_'] * len(palavra)
letras = set()

print(f"Categoria: {categoria}")


def validar_letra(letra):
    """Valida a letra que o usuário chuta no loop
    Só será True quando for apenas uma letra e faça parte do alfabeto"""
    if len(letra) != 1:
        print('Insira apenas uma letra!')
        return False
    if not letra.isalpha():
        print('Insira uma letra válida!')
        return False
    return True

def adicionar_letra(letter, word, incognita):
    """Atualiza a palavra não-descoberta pra conter a letra na posição exata
    que ela está na palavra "word" passada"""
    for index, let in enumerate(word):
        if letter == word[index]:
            incognita[index] = letter
    print(f'A letra {letter} estava na palavra!\n{"".join(incognita)}')
    return

# Loop principal do jogo, não encerra enquanto o usuário não descobrir a palavra ou esgotar tentativas
while not descoberta and tentativas > 0:
    letra = input('Insira uma letra: ').strip().lower()
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

    ## Checa se o usuário descobriu a palavra
    if (''.join(descobrir)) == palavra:
        descoberta = True
        print('Parabéns, você acertou a palavra')
        break




