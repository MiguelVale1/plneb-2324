# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:15:36 2024

@author: MV
"""

import re

#Ficha de Expressões Regulares 1

#Frases
line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"
line4 = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
line5 = "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."

#Exercício 1
#Alínea 1.1

def match_hello(linha):
    if re.match(r"hello\b", linha):
        return True

print(match_hello(line3))
#------------------------------------------
#Alínea 1.2

def search_hello(linha):
    if re.search(r"\bhello\b", linha):
        return True
        
print(search_hello(line3))
#------------------------------------------
#Alínea 1.3

def findall_hello(linha):
    findall = re.findall(r"\bhello\b", linha, re.I) 
    return findall if len(findall)!=0 else None

print(findall_hello(line4))
#------------------------------------------
#Alínea 1.4

def sub_hello(linha):
    return re.sub(r"\bhello\b", "*YEP*", linha)
    
print(sub_hello(line4))
#------------------------------------------
#Alínea 1.5

def split_hello(linha):
    return re.split(r",", linha)

print(split_hello(line5))
#------------------------------------------
#Exercício 2

def palavra_magica(linha):
  if re.search(r"\bpor favor[.!?]$", linha):
      return True
      

print(palavra_magica("Posso ir à casa de banho, por favor?"))
print(palavra_magica("Preciso de um favor."))
#------------------------------------------
#Exercício 3

def narcissismo(linha):
    return len(re.findall(r"\beu\b", linha))

print(narcissismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."))
#------------------------------------------
#Exercício 4

def troca_de_curso(linha, novo_curso):
  return re.sub(r"LEI", str(novo_curso), linha)

print(troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.","Biomédica"))
#------------------------------------------
#Exercício 5

def soma_string(linha):
    return sum([int(i) for i in re.split(r",", linha)])

print(soma_string("4,-6,2,3,8,-3,0,2,-5,1"))
#------------------------------------------
#Exercício 6

def pronomes(linha):
    return re.findall(r"\b(eu|tu|eles?|elas?|nós|vós)\b", linha, re.I)

print(pronomes("Eu fui até a casa dele para entregar-lhe o livro que ela esqueceu, pois ele precisava dela para estudar."))
#------------------------------------------
#Exercício 7

def variavel_valida(linha):
    if re.match(r"^[a-z]\w*$", linha, re.I):
        return True

print(variavel_valida("var_20"))
#------------------------------------------
#Exercício 8

def inteiros(linha):
    return [int(i) for i in re.findall(r"-?\d+[.,]?\d*", linha) if '.' not in i and ',' not in i]

print(inteiros("13 -9 7 -21 5 -12 22 -1 12 -5 90.90 -45.54"))
#------------------------------------------
#Exercício 9

def underscores(linha):
    return re.sub(r" +", "_",linha)

print(underscores("Uma frase       completamente normal."))
#------------------------------------------
#Exercício 10

def codigos_postais(lista):
    lista_final=[]
    for codigo_postal in lista:
        lista_final.append(re.split(r"-", codigo_postal))
    return lista_final

lista = ["4700-000", "1234-567", "8541-543", "4123-974", "9481-025"]
print(codigos_postais(lista))
