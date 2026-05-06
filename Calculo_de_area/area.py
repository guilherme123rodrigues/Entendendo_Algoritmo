def area(altura=0, largura=0):
    return altura * largura
    
    
def erro(valor):
     try:
         r = float(input(valor))
     except (TypeError, ValueError):
         print('\033[1;31mValor incorreto\033[m')
         return False
     else:
         return r
         
resp = str(input('Menu de opçoes'))

l_n = ['Largura', 'Altura']    
lista = []

for c in l_n:
    while True:
        r = erro(f'Digite a {c} : ')
        if r != False:
            lista.append(r)
            break
        print('-'*20)

    
calc = area(lista[0], lista[1]) 
   
print(f'A areá de {lista[0]}x{lista[1]} é de {calc}m²')