# Classe Pessoa com atributos nome, idade e altura

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
# Metodo

def apresentar_pessoa(pessoa):
    print(f"Olá, meu nome é {pessoa.nome}, tenho {pessoa.idade} anos.")
    
def fazer_aniversario(pessoa):
    pessoa.idade += 1
    print(f"Parabéns, {pessoa.nome}! Agora você tem {pessoa.idade} anos.")
    
# Construtor

pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

# Utilizando método para apresentar as pessoas

pessoa1.apresentar_pessoa()
pessoa2.apresentar_pessoa()

pessoa1.fazer_aniversario()