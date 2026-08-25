import math

print("Olá" + " Python")

# Solicitando o nome do usuário
nome = input("Qual é o seu nome? ")
print("Olá, " + nome + "! Prazer em conhecê-lo.")

# Solicitando a idade do usuário
idade = input("Quantos anos você tem? ")
# Convertendo a entrada para float para permitir cálculos futuros
altura = float(input("Qual é a sua altura em metros? ")) 
print(f"Você tem {idade} anos e sua altura é {altura:.2f} metros.")

a = 10
b = 3
print("A soma de a e b é: " + str(a + b))
print("A subtração de a e b é: " + str(a - b))
print("A multiplicação de a e b é: " + str(a * b))
print("A divisão de a e b é: " + str(a / b))
print("O resto da divisão de a por b é: " + str(a % b))
print("A potência de a elevado a b é: " + str(a ** b))
print("A divisão inteira de a por b é: " + str(a // b))

pessoa = {
    "nome": nome,
    "idade": idade,
    "altura": altura
}

print("Informações da pessoa:")
nome = pessoa["nome"]
idade = pessoa["idade"]
altura = pessoa["altura"]

nome = input("Digite o nome da pessoa: ")
idade = input("Digite a idade da pessoa: ")
altura = float(input("Digite a altura da pessoa: "))

for chave, valor in pessoa.items():
    print(chave + ": " + str(valor))
    
    
def raiz_quadrada(num1):
    raiz_quadrada = math.sqrt(num1)
    return raiz_quadrada

raiz_quadrada(16)
print("A raiz quadrada de 16 é: " + str(raiz_quadrada(16)))