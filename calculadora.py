class Calculadora:
    def __init__(self):
        pass

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

    def calcular(self, operacao, a, b):
        if operacao == 'somar':
            return self.somar(a, b)
        elif operacao == 'subtrair':
            return self.subtrair(a, b)
        elif operacao == 'multiplicar':
            return self.multiplicar(a, b)
        elif operacao == 'dividir':
            return self.dividir(a, b)
        else:
            raise ValueError("Operação inválida. Use 'somar', 'subtrair', 'multiplicar' ou 'dividir'.")
        

calc = Calculadora()
print("Calculadora inicializada. Use o método 'calcular' para realizar operações.")
definir_operacao = input("Digite a operação (somar, subtrair, multiplicar, dividir): ")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
resultado = calc.calcular(definir_operacao, a, b)
print(f"O resultado da operação {definir_operacao} entre {a} e {b} é: {resultado}")        

  
    