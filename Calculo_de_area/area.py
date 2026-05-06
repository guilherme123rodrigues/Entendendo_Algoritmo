from rich import Console

console = Console()

def area(altura=0, largura=0):
    return altura * largura
    
    
def erro(valor):
     try:
         r = float(input(valor))
     except (TypeError, ValueError):
         console.print('[bold red italic]Valor incorreto[/]')
         return False
     else:
         return r
         
resp = str(input('[bold blue italic]Menu de opçoes[/]'))

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