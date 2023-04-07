'''
# Faça um programa que entre com o nome, idade, peso e altura de uma pessoa e 
retorne como resultado a seguinte frase: 
- Ficha do paciente:
- Idade:
- Altura:
- Peso:
- Seu IMC é de:

OBS> IMC= peso/(altura*altura)
'''

nome=input("Digite seu nome: ")
idade=input("Digite sua idade: ")
altura=float(input("Digite sua altura: "))
peso=float(input("Digite seu peso: "))
imc=peso/(altura*altura)

print("Ficha do paciente ")
print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura)
print("Peso: ", peso)
print("Valor do IMC= ",imc)
