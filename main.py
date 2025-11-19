import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

senha_caracteres = int(input("Digite o tamanho da sua senha: "))

senha = ""

for i in range(senha_caracteres):
    senha += random.choice(caracteres)

print("Sua senha gerada é:", senha)
