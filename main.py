#-*- coding: utf-8 -*-
#/*Desenvolvido por Iovan Barros
#afim de compreeender a materia de 
#programação orientada a objetos*/
import sys

class Operacoes:

    def soma(self, x, y):
        self.soma = binarioParaDecimal(x)+ binarioParaDecimal(y)
        return print(">>>> Resultado em binario: ", decimalParaBinario(self.soma))


    def subtracao(self, x, y):
        if y > x:
            print("O segundo numero precisa ser menor")
            return calculadoraBinaria()
        else:
            self.subtracao= binarioParaDecimal(x) - binarioParaDecimal(y)
        return print(">>>> Resultado em binario: ", decimalParaBinario(self.subtracao))

    def multiplicacao(self, x, y):
        self.multi = binarioParaDecimal(x) * binarioParaDecimal(y)
        return print(">>>> Resultado em binario: ", decimalParaBinario(self.multi))

    def divisao(self, x, y):
        if y > x:
            print("O segundo numero deve ser menor que o primeiro")
            calculadoraBinaria()
        else:
            self.divi = binarioParaDecimal(x)/binarioParaDecimal(y)
            rounded = int(self.divi)
        return print(">>>> Resultado em binario: ", decimalParaBinario(rounded))

def binarioParaDecimal(valor):
    n = 0
    for i in str(valor):
        if i > '1':
            print("Somente aceitamos 0 ou 1")
            print("Encerrando o programa")
            calculadoraBinaria()
            quit()
        if i == '1':
            n+=1
    return n

def decimalParaBinario(valor):
    if valor == 0:
        return ''
    else:
        return decimalParaBinario(valor // 2) + str(valor % 2)

def calculadoraBinaria():
    calculadora = Operacoes()

    print("===============================")
    print("Bem-vindo a calculadora binaria")
    print("===============================")
    print("1- Soma")
    print("2- Subtracao")
    print("3- Multiplicacao")
    print("4- Divisao")
    print("5- Sair")
    print("===============================")


    operacao = input("Escolha uma operacao: ")

    if operacao == '5':
        print("Encerrando o programa")
        quit()
    else:
        pass

    try:
        numero1 = int(input("Primeiro numero: "))
        numero2 = int(input("Segundo numero: "))
    except ValueError:
        print("Somente aceitamos 0 ou 1")

    while operacao !='5':

        if operacao == '1':
            calculadora.soma(numero1,numero2)
            calculadoraBinaria()
            break
        elif operacao == '2':
            calculadora.subtracao(numero1,numero2)
            calculadoraBinaria()
            break
        elif operacao == '3':
            calculadora.multiplicacao(numero1,numero2)
            calculadoraBinaria()
            break
        elif operacao == '4':
            calculadora.divisao(numero1,numero2)
            calculadoraBinaria()
            break

        if operacao not in str("1,5"):
             print("Operacao nao encontrada.")
             print("Encerrando programa")
             quit()

calculadoraBinaria()
