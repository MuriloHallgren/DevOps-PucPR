"""Arquivo principal do projeto."""

tarefas = []

#Lista de Tarefas To-Do

while True:
    print("\n0 - Adicionar tarefa")
    print("1 - Lista de Tarefas")
    print("2 - Excluir tarefa")
    print("3 - Sair")
    opcao = input("Digite o número de sua escolha: ")

    # Adicionar
    if opcao == "0":
        tarefa = input("Defina a tarefa: ")
        tarefas.append(tarefa)

    # Enumerar
    elif opcao == "1":
        for i, t in enumerate(tarefas):
            print(f"{i} - {t}")

    # Deletar
    elif opcao == "2":
        num = int(input("Número da tarefa: "))
        tarefas.pop(num)

    # Encerrar
    elif opcao == "3":
        print("Operação encerrada.")
        break
#teste