
# ==========================================
# CITIZEN ASSIST AI
# Global Solution GS26_2
# Ciencia da Computacao - FIAP
# A regra será: 
#  - o cidadão poderá ser encaminhado para agendamento presencial quando o serviço exigir atendimento presencial, a documentação estiver completa e houver disponibilidade de agendamento.
#  - o cidadão poderá ser encaminhado para agendamento online quando o serviço não exigir atendimento presencial, a documentação estiver completa e houver disponibilidade de agendamento.
# ==========================================


# FUNCAO PARA RECEBER ENTRADAS
def perguntar(mensagem):

    while True:

        print("\n" + mensagem)
        print("1 - Sim")
        print("0 - Nao")

        try:

            opcao = int(input("Digite sua opcao: "))

            if opcao == 1 or opcao == 0:
                return opcao

            else:
                print("Digite apenas 1 ou 0.")

        except ValueError:
            print("Entrada invalida! Digite um numero.")


# MENU PRINCIPAL
def menu():

    print("\n================================")
    print("        CITIZEN ASSIST AI")
    print("================================")

    A = perguntar("O servico exige atendimento presencial?")

    B = perguntar("A documentacao esta completa?")

    C = perguntar("Existe disponibilidade de agendamento?")

    D = perguntar("O servico permite atendimento online?")

    return A, B, C, D


# EXPRESSAO BOOLEANA ORIGINAL
def regra_original(A, B, C, D):
    return int((not (A) and B and C and D)or(A and B and C and not (D)))


# EXPRESSAO BOOLEANA SIMPLIFICADA
def calcular(A, B, C, D):
    return int(B and C and (A != D))

# RESULTADO DO ATENDIMENTO
def orientacao(A, B, C, D):

    X = calcular(A, B, C, D)

    print("\n================================")
    print("     RESULTADO DO ATENDIMENTO")
    print("================================")

    if X == 1:
        print("Todas as condicoes foram atendidas.")
        print("Voce pode prosseguir para a proxima etapa.")
        if A == 0 and D == 1:
            print("Orientacao: atendimento online.")

        elif A == 1 and D == 0:
            print("Orientacao: atendimento presencial.")

    else:
        print("Nao foi possivel prosseguir com o atendimento.")
        print("\nVerifique os seguintes requisitos:")

        if B == 0:
            print("- A documentacao esta incompleta.")

        if C == 0:
            print("- Nao existe disponibilidade de agendamento.")

        if A == D:
            print("- A combinacao da modalidade de atendimento nao atende a regra.")

    print("\n================================")
    print("INFORMACOES IMPORTANTES")
    print("================================")
    print("Este sistema fornece orientacoes demonstrativas.")
    print("Nao representa um canal oficial do governo.")
    print("Nao confirma a concessao de servicos ou direitos.")


# EXIBICAO DA EXPRESSAO
def expressao_booleana():

    print("\n================================")
    print("       EXPRESSAO BOOLEANA")
    print("================================")

    print("Expressao original:")
    print("X = A'.B.C.D + A.B.C.D'")

    print("\nForma canonica:")
    print("X = Soma de mintermos (7, 14)")

    print("\nExpressao simplificada:")
    print("X = B.C.(A'.D + A.D')")

    print("\nRepresentacao XOR:")
    print("X = B.C.(A XOR D)")


# TABELA-VERDADE PARA CONFERENCIA
def tabela_verdade():

    print("\n================================")
    print("          TABELA-VERDADE")
    print("================================")

    print("A B C D | X")
    print("----------------")

    for A in range(2):
        for B in range(2):
            for C in range(2):
                for D in range(2):
                    X = calcular(A, B, C, D)
                    print(A, B, C, D, "|", X)

# VALIDACAO DAS 16 COMBINACOES
def validar():
    print("\n================================")
    print("     VALIDACAO DAS COMBINACOES")
    print("================================")

    total = 0
    erros = 0

    for A in range(2):
        for B in range(2):
            for C in range(2):
                for D in range(2):
                    original = regra_original(A, B, C, D)
                    simplificada = calcular(A, B, C, D)

                    executado = int( B and C and (A != D) )
                    total += 1

                    if original == simplificada == executado:
                        print(
                            A, B, C, D, "|", original,"|", simplificada,"| OK")

                    else:
                        print(A, B, C, D, "|", original,"|", simplificada,"| ERRO")
                        erros += 1

    print("\nTotal de combinacoes:", total)
    print("Total de erros:", erros)

    if erros == 0:
        print("\nTodas as combinacoes foram validadas!")

    else:
        print("\nExistem erros na validacao.")

# EXECUCAO PRINCIPAL
def main():

    while True:

        print("\n================================")
        print("         CITIZEN ASSIST AI")
        print("================================")

        print("1 - Realizar atendimento")
        print("2 - Exibir expressao booleana")
        print("3 - Exibir tabela-verdade")
        print("4 - Validar as 16 combinacoes")
        print("0 - Encerrar programa")

        try:

            opcao = int(input("\nEscolha uma opcao: "))

            if opcao == 1:
                A, B, C, D = menu()
                orientacao(A, B, C, D)

            elif opcao == 2:
                expressao_booleana()

            elif opcao == 3:
                tabela_verdade()

            elif opcao == 4:
                validar()

            elif opcao == 0:
                print("\nEncerrando Citizen Assist AI...")
                break

            else:
                print("\nOpcao invalida!")

        except ValueError:

            print("\nDigite apenas numeros.")


# INICIAR PROGRAMA
if __name__ == "__main__":

    main()
