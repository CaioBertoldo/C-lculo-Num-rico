import sympy as sp

def simpson(f, a, b, n):
    # Verifica se o número de iterações é par
    if n % 2 != 0:
        return None
    
    # Calcular valor de h, largura de cada subintervalo do intervalo de integração
    h = (b -  a) / n
    soma = f(a) + f(b)
    
    # Percorrer subintertvalos de índices ímpares
    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)
        
    # Percorrer os subintervalos de índices pares
    for i in range(2, n - 1, 2):
        soma += 2 * f(a + i * h)
        
    integral = h * soma / 3
    return integral    

# Main

exp = input("Expressão: ")
exp = sp.sympify(exp)

a = float(input("Limite inferior: "))
b = float(input("Limite superior: "))
n = int(input("Número de iterações: "))

# Define a função a ser a partir da expressão lida
f = lambda x: exp.subs('x', x)

# Calcular a integral pelo método de simpson
integral = simpson(f, a, b, n)

# Resultado
print(f"Aproximação de {sp.simplify(integral):.5f}")
