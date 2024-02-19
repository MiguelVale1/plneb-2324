# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:34:55 2024

@author: MV
"""
import unidecode

anagramas={}

filename="C:\\Users\\migue\\OneDrive\\Ambiente de Trabalho\\Processamento de Linguagem Natural\\TPCs\\TPC1\\CIH Bilibgual Medical Glossary-English-Spanhish.txt"
file= open(filename)
frase= file.read()
splice = list(range(33, 65)) + list(range(91, 97)) + list(range(123, 127))#numeros ascii que não são letras minúsculas
for i in splice:
    frase = frase.replace(chr(i),' ')#remover tudo que não é uma letra
frase=set(unidecode.unidecode(frase.lower()).split())#remover sinais e colocar a string em diminutivo

def sort(palavra):
    return ''.join(sorted(palavra))#criar a string palavra a partir da lista de todas as letras ordenadas

for palavra in frase:
    if sort(palavra) in anagramas:#se a palavra ordenada já existisse nas keys
        anagramas[sort(palavra)].append(palavra)#adicionar
    else:
        anagramas[sort(palavra)]=[palavra]#criar
for i in anagramas:
    print(i+':'+ str(anagramas[i]))#print