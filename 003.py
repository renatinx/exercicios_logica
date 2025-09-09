"""
faça um programa que peça dois numeros e imprima a soma
"""

def new_func():
    num1 = int (input("digite um numero : "))
    num2 = int (input("digite um segundo numero : "))

    soma = num1 + num2 

    print(f"a soma entre {num1} e {num2} é {soma}, .")


for i in range(100): 
    new_func()