"""
 Escreva um programa que inverta os caracteres de um string.
"""

word = input('Digite sua string')

total = len(word) - 1
while total >= 0:
    print(word[total], end='')
    total -= 1




