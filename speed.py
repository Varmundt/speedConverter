while True:
    print("\nConversor de Velocidade")
    print("1 - Converter de MPH para KMH")
    print("2 - Converter de KMH para MPH")
    print("0 - Sair")

    opcao = input("Escolha uma opção (0, 1 ou 2): ")

    if opcao == '1':
        mph = float(input("\nDigite a velocidade em MILHAS por hora (MPH): "))
        kmh = mph * 1.60934
        print("A velocidade convertida é de: {:.2f} km/h".format(kmh))

    elif opcao == '2':
        kmh = float(input("\nDigite a velocidade em QUILÔMETROS por hora (KMH): "))
        mph = kmh / 1.60934
        print("A velocidade convertida é de: {:.2f} mph".format(mph))

    elif opcao == '0':
        print("\nCalculadora Encerrada.")
        break

    else:
        print("\nINVÁLIDO! Por favor, ESCOLHA 0, 1 ou 2.")