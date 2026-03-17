tarefas = []
#Lista de Tarefas To-Do
while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Lista de Tarefas")
    print("3 - Excluir tarefa")
    print("4 - Sair")
    opcao = input("Digite o número de sua escolha: ")

    # Adicionar
    if opcao == "1":
        tarefa = input("Defina a tarefa: ")
        tarefas.append(tarefa)

    # Enumerar
    elif opcao == "2":
        for i, t in enumerate(tarefas):
            print(f"{i} - {t}")

    # Deletar
    elif opcao == "3":
        num = int(input("Número da tarefa: "))
        tarefas.pop(num)

    elif opcao == "4":
        break