def quicksort(l):
    '''
    Uma funçao para orderna lista
    Ela usa o metodo recursivo
    '''
    if  len(l) < 2:
        return l
    
    pivo = l[(len(l) // 2)]
    indice = (len(l) // 2)

    menores =  [x for i, x in enumerate(l) if x < pivo and i != indice]
    maiores = [x for i, x in enumerate(l) if x > pivo and i != indice]

    return  quicksort(menores) + [pivo] + quicksort(maiores)


lista = [12, 4, 3,  11, 2,  18, 20]

ordem = quicksort(lista)

print(f'Lista anterior: {lista}\nLista atual: {ordem}')
help(quicksort)