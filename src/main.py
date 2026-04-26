"""Lista de Tarefas To-Do - Versão Aprimorada."""

from datetime import datetime


# ──────────────────────────────────────────────
# Estrutura de dados
# ──────────────────────────────────────────────

def criar_tarefa(descricao: str, prioridade: str = "normal") -> dict:
    """Cria e retorna um dicionário representando uma tarefa."""
    return {
        "descricao": descricao,
        "prioridade": prioridade,
        "concluida": False,
        "criada_em": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }


# ──────────────────────────────────────────────
# Operações sobre tarefas
# ──────────────────────────────────────────────

def adicionar_tarefa(tarefas: list) -> None:
    """Solicita dados ao usuário e adiciona uma nova tarefa à lista."""
    descricao = input("Descrição da tarefa: ").strip()
    if not descricao:
        print("⚠  Descrição não pode ser vazia.")
        return

    print("Prioridade: [1] Baixa  [2] Normal  [3] Alta")
    opcao_prioridade = input("Escolha (padrão = Normal): ").strip()
    mapa = {"1": "baixa", "2": "normal", "3": "alta"}
    prioridade = mapa.get(opcao_prioridade, "normal")

    tarefas.append(criar_tarefa(descricao, prioridade))
    print(f"✔  Tarefa '{descricao}' adicionada com prioridade {prioridade}.")


def listar_tarefas(tarefas: list) -> None:
    """Exibe todas as tarefas formatadas com índice, prioridade e status."""
    if not tarefas:
        print("📭  Nenhuma tarefa cadastrada.")
        return

    icones_prioridade = {"baixa": "🔵", "normal": "🟡", "alta": "🔴"}
    print(f"\n{'─'*55}")
    print(f"  {'#':<4} {'Status':<10} {'Prior.':<6} {'Criada em':<17} Descrição")
    print(f"{'─'*55}")

    for i, t in enumerate(tarefas):
        status = "✔ feita" if t["concluida"] else "○ aberta"
        icone = icones_prioridade.get(t["prioridade"], "🟡")
        print(f"  {i:<4} {status:<10} {icone:<6} {t['criada_em']:<17} {t['descricao']}")

    print(f"{'─'*55}")
    total = len(tarefas)
    concluidas = sum(1 for t in tarefas if t["concluida"])
    print(f"  {concluidas}/{total} tarefas concluídas.\n")


def concluir_tarefa(tarefas: list) -> None:
    """Marca uma tarefa como concluída pelo índice informado."""
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        num = int(input("Número da tarefa a concluir: "))
        if not _indice_valido(tarefas, num):
            return
        if tarefas[num]["concluida"]:
            print("ℹ  Tarefa já estava concluída.")
        else:
            tarefas[num]["concluida"] = True
            print(f"✔  Tarefa '{tarefas[num]['descricao']}' marcada como concluída.")
    except ValueError:
        print("⚠  Digite um número válido.")


def excluir_tarefa(tarefas: list) -> None:
    """Remove uma tarefa da lista pelo índice informado."""
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        num = int(input("Número da tarefa a excluir: "))
        if not _indice_valido(tarefas, num):
            return
        removida = tarefas.pop(num)
        print(f"🗑  Tarefa '{removida['descricao']}' excluída.")
    except ValueError:
        print("⚠  Digite um número válido.")


def limpar_concluidas(tarefas: list) -> None:
    """Remove todas as tarefas já concluídas."""
    antes = len(tarefas)
    tarefas[:] = [t for t in tarefas if not t["concluida"]]
    removidas = antes - len(tarefas)
    print(f"🧹  {removidas} tarefa(s) concluída(s) removida(s).")


# ──────────────────────────────────────────────
# Utilitários
# ──────────────────────────────────────────────

def _indice_valido(tarefas: list, num: int) -> bool:
    """Verifica se o índice informado é válido para a lista."""
    if 0 <= num < len(tarefas):
        return True
    print(f"⚠  Índice {num} fora do intervalo (0–{len(tarefas) - 1}).")
    return False


def exibir_menu() -> None:
    """Imprime o menu principal."""
    print("\n╔══════════════════════════╗")
    print("║      LISTA DE TAREFAS    ║")
    print("╠══════════════════════════╣")
    print("║  0 · Adicionar tarefa    ║")
    print("║  1 · Listar tarefas      ║")
    print("║  2 · Concluir tarefa     ║")
    print("║  3 · Excluir tarefa      ║")
    print("║  4 · Limpar concluídas   ║")
    print("║  5 · Sair                ║")
    print("╚══════════════════════════╝")


# ──────────────────────────────────────────────
# Loop principal
# ──────────────────────────────────────────────

def main() -> None:
    """Ponto de entrada do programa."""
    tarefas: list = []

    acoes = {
        "0": adicionar_tarefa,
        "1": listar_tarefas,
        "2": concluir_tarefa,
        "3": excluir_tarefa,
        "4": limpar_concluidas,
    }

    while True:
        exibir_menu()
        opcao = input("Sua escolha: ").strip()

        if opcao == "5":
            print("👋  Até logo!")
            break
        elif opcao in acoes:
            acoes[opcao](tarefas)
        else:
            print("⚠  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
