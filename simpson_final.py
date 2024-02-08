import sympy as sp


def simpson(f, a, b, n):
    # Verifica se o número de iterações é par
    if n % 2 != 0:
        return None

    # Calcular valor de h, largura de cada subintervalo do intervalo de integração
    h = (b - a) / n

    soma = f(a) + f(b)
    print("\nx               y")
    print("%.5f         %.5f" % (a, f(a)))
    ind = 0.0
    for i in range(1, n, 1):
        ind += h
        print("%.5f         %.5f" % (ind+a, f(a + i * h)))
        if i % 2 != 0:
            soma += 4 * f(a + i * h)
        elif i % 2 == 0:
            soma += 2 * f(a + i * h)

    print("%.5f         %.5f\n" % (b, f(b)))


    integral = h * soma / 3

    x = sp.symbols('x')

    return integral

# Main
exp = input("Expressão: ")
exp = sp.sympify(exp)

a = float(input("Limite inferior: "))
b = float(input("Limite superior: "))
n = int(input("Valor de Passos: "))

# Define a função a ser a partir da expressão lida
f = lambda x: exp.subs('x', x)


# Calcular a integral pelo método de simpson
integral = simpson(f, a, b, n)

# Resultado
print(f"Aproximação de {sp.simplify(integral):.5f}")
