def calculadora():
    while True:
        # Passo 1: Receber dois números do usuário
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")

        # Passo 2: Converter os valores para float
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Por favor, insira números válidos.")
            continue

        # Passo 3: Escolher a operação
        print("\nEscolha a operação:")
        print("1: Adição (+)")
        print("2: Subtração (-)")
        print("3: Multiplicação (*)")
        print("4: Divisão (/)")

        operacao = input("Digite o número da operação que deseja realizar (1/2/3/4): ")

        # Realizar a operação escolhida
        if operacao == '1':
            resultado = num1 + num2
            print(f"\nResultado da adição: {resultado}")
        elif operacao == '2':
            resultado = num1 - num2
            print(f"\nResultado da subtração: {resultado}")
        elif operacao == '3':
            resultado = num1 * num2
            print(f"\nResultado da multiplicação: {resultado}")
        elif operacao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"\nResultado da divisão: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Operação inválida. Tente novamente.")

        # Perguntar se o usuário deseja realizar outra operação
        continuar = input("\nDeseja realizar outra operação? (s/n): ")
        if continuar.lower() != 's':
            print("Obrigado por usar a calculadora!")
            break

calculadora()
