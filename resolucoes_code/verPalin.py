#é um palíndromo?
# Recebendo a palavra do usuário
palavra = input("Digite uma palavra: ")

# Removendo espaços e convertendo a palavra para minúsculas (opcional, se você quiser considerar palavras case-insensitive)
palavra = palavra.replace(" ", "").lower()

# Invertendo a palavra
palavra_invertida = palavra[::-1]

# Verificando se a palavra é um palíndromo
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
