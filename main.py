tarefas = []

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)

    elif opcao == "2":
        for i, t in enumerate(tarefas):
            print(f"{i} - {t}")

    elif opcao == "3":
        num = int(input("Número da tarefa: "))
        tarefas.pop(num)

    elif opcao == "4":
        break