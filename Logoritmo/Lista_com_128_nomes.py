log = 2
valor = 1_000_000_000
cont = 0
 
while valor > 1:
    div = valor / log
    valor = div
    cont += 1

print(f'{cont}')
