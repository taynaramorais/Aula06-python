def inverso(numero): 
    try:
        divisao = 1/float(numero)
        print(f'1 / {numero} = {divisao}')
    except ZeroDivisionError: 
        print(f"Não é possível calcular a divisão por 0.")
    except ValueError:
        print(f"O valor precisa ser um número!")
    except TypeError:
        print(f"É necessário inserir um valor!")
    print('Desenvolvido por Taynara.')

#valor = 5
#valor = 0
#valor = 'teste'
resultado = inverso(valor)