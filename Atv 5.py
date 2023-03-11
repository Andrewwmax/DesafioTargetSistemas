# Python

# string = input("Digite uma string para ser invertida: ")
string = 'invertendo'

invertida = []

# básico tamanho da string - 1,
# posição - 1 (última),
# com passo -1 (percorrendo de trás pra frente)
for i in range(len(string) - 1, -1, -1):
    invertida.append(string[i])

# converte p/ string
invertida = ''.join(invertida)

print("A string invertida:", invertida)