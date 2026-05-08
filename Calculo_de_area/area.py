def area(base=0, altura=0):
    '''
    ==================================================
                    FUNÇÃO: ÁREA
    ==================================================

    Objetivo:
        Calcular a área de um retângulo.

    Fórmula:
        A = b × h

    Onde:
        A = Área
        b = Base
        h = Altura

    Exemplo:
        Base = 5 m
        Altura = 3 m

        A = 5 × 3
        Resultado = 15 m²

    Retorno:
        Valor da área do retângulo.
    '''
    return base * altura


def perimetro(base=0, altura=0):
    '''
    ==================================================
                FUNÇÃO: PERÍMETRO
    ==================================================

    Objetivo:
        Calcular o perímetro de um retângulo.

    Fórmula:
        P = 2 × (base + altura)

    Onde:
        P = Perímetro

    Exemplo:
        Base = 5 m
        Altura = 3 m

        P = 2 × (5 + 3)
        Resultado = 16 m

    Retorno:
        Valor do perímetro do retângulo.
    '''
    return 2 * (base + altura)


# ==================================================
# FUNÇÃO DE TRATAMENTO DE ERROS
# ==================================================
def erro(valor, ty):

    '''
    Objetivo:
        Validar entradas do usuário e evitar
        erros de conversão de tipos.

    Parâmetros:
        valor -> Mensagem exibida no input.
        ty -> Tipo esperado da variável.

    Tipos aceitos:
        int
        float
        str
        bool
        etc...

    Funcionamento:
        Tenta converter o valor digitado para
        o tipo informado.

    Retorno:
        Valor convertido corretamente
        ou False em caso de erro.
    '''

    try:
        r = ty(input(valor))

    except (TypeError, ValueError):
        print('\033[1;31mValor incorreto\033[m')
        return False

    else:
        return r


# ==================================================
# MENU PRINCIPAL
# ==================================================
while True:

    resp = erro('''MENU DE OPÇÕES
[1] Calcular área
[2] Calcular perímetro
[3] Sair

Opção: ''', int)

    if resp != False:

        # Verifica se a opção escolhida existe
        if not resp in {1, 2, 3}:
            print('\033[1;31mValor inválido!\033[m')
            print('-' * 30)

        else:
            break

    else:
        print('-' * 30)


# ==================================================
# ENTRADA DOS DADOS
# ==================================================
l_n = ['Base', 'Altura']
lista = []

print('-' * 30)

if not resp == 3:

    # Solicita os valores da base e altura
    for c in l_n:

        while True:

            r = erro(f'Digite a {c}: ', float)

            if r != False:
                lista.append(r)
                break

            print('-' * 20)

print('-' * 30)


# ==================================================
# PROCESSAMENTO DOS CÁLCULOS
# ==================================================
match resp:

    case 1:
        calc = area(lista[0], lista[1])

        print(
            f'A área de {lista[0]}x{lista[1]} '
            f'é de {calc}m²'
        )

    case 2:
        calc = perimetro(lista[0], lista[1])

        print(
            f'O perímetro de {lista[0]}x{lista[1]} '
            f'é {calc}m'
        )

    case _:
        print('\033[1;33mEncerrando sistema...\033[m')
        