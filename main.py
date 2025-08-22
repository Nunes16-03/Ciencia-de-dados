continuar = "s"

while continuar == "s":
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    if operacao == "+":
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    else:
        if operacao == "-":
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        else:
            if operacao == "*":
                resultado = num1 * num2
                print(f"Resultado: {resultado}")
            else:
                if operacao =="/":
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"Resultado: {resultado}")
                    else:
                        print("Não é possivel dividir por 0")
