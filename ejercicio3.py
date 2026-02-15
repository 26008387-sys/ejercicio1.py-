import random
n1 = int(input("Ingrese un número positivo mayor a 5: "))            # (1) Leer un número positivo mayor a 5
aleatorio1 = random.randint(1, n1)                                   # (2) Generar número aleatorio entre 1 y n1, y desplegarlo
print(f"Primer número aleatorio (1 a {n1}): {aleatorio1}")
n2 = int(input("Ingrese un número positivo mayor a 30: "))           # (3) Leer un segundo número positivo mayor que 30
aleatorio2 = random.randint(0, n2)                                   # (4) Generar número aleatorio entre 0 y n2, y desplegarlo
print(f"Segundo número aleatorio (0 a {n2}): {aleatorio2}")
producto = aleatorio1 * aleatorio2                                   # (5) Multiplicar ambos números aleatorios y desplegar el resultado
print(f"Resultado de la multiplicación: {producto}")
division = producto / 3                                              # (6) Dividir el producto dentro de 3 y desplegar el resultado
print(f"Resultado de la división entre 3: {division}")
