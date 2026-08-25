import requests 


paramns = input("Digite o nome do pokemon: ")
resposta = requests.get(f'https://pokeapi.co/api/v2/pokemon/{paramns}')

dados = resposta.json()

print(dados['name'])
print(dados['weight'])
print(dados['height'])
print(dados['types'][0]['type']['name'])