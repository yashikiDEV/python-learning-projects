numero = input('escreva um número: ')
rodadas = input('escreva o numero de rodadas: ')

n = int(numero)
r = int(rodadas)

penultimo_n = 0
ultimo_n = 0

print(n)
n1 = n + n
print(n1)
penultimo_n += n1
ultimo_n += int(n + n1)
print(ultimo_n)

for _ in range(r):
    penultimo_n += ultimo_n
    ultimo_n += penultimo_n
    print(penultimo_n)
    print(ultimo_n)