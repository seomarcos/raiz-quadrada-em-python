import math

# Insira o número do qual você deseja calcular a raiz quadrada
numero = 16

try:
    raiz_quadrada = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é", raiz_quadrada)
except ValueError:
    print("Não é possível calcular a raiz quadrada de um número negativo")
