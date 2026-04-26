"""Lista de Tarefas To-Do - Versão Aprimorada e Testável."""

from datetime import datetime


# ──────────────────────────────────────────────
# Estrutura de dados
# ──────────────────────────────────────────────

def criar_tarefa(descricao: str, prioridade: str = "normal") -> dict:
    """Cria e retorna um dicionário representando uma tarefa."""
    if not descricao or not descricao.strip():
        raise ValueError("Descrição não pode ser vazia.")
    if prioridade not in ("baixa", "normal", "alta"):
        raise ValueError(f"Prioridade inválida: '{prioridade}'.")
    return {
        "descricao": descricao.strip(),
        "prioridade": prioridade,
        "concluida": False,
        "criada_em": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }


# ──────────────────────────────────────────────
# Operações sobre tarefas
# ──────────────────────────────────────────────

def adicionar_tarefa(tarefas: list, descricao: str, prioridade: str = "normal") -> None:
    """Adiciona uma nova tarefa à lista."""
    tarefas.append(criar_tarefa(descricao, prioridade))


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


def concluir_tarefa(tarefas: list, indice: int) -> None:
    """Marca a tarefa no índice informado como concluída."""
    if not (0 <= indice < len(tarefas)):
        raise IndexError(f"Índice {indice} fora do intervalo.")
    tarefas[indice]["concluida"] = True


def excluir_tarefa(tarefas: list, indice: int) -> dict:
    """Remove e retorna a tarefa no índice informado."""
    if not (0 <= indice < len(tarefas)):
        raise IndexError(f"Índice {indice} fora do intervalo.")
    return tarefas.pop(indice)


def limpar_concluidas(tarefas: list) -> int:
    """Remove todas as tarefas concluídas. Retorna a quantidade removida."""
    antes = len(tarefas)
    tarefas[:] = [t for t in tarefas if not t["concluida"]]
    return antes - len(tarefas)


# ──────────────────────────────────────────────
# Utilitários (apenas para uso interativo)
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


def _menu_adicionar(tarefas: list) -> None:
    """Solicita dados ao usuário e chama adicionar_tarefa."""
    descricao = input("Descrição da tarefa: ").strip()
    if not descricao:
        print("⚠  Descrição não pode ser vazia.")
        return
    print("Prioridade: [1] Baixa  [2] Normal  [3] Alta")
    opcao = input("Escolha (padrão = Normal): ").strip()
    mapa = {"1": "baixa", "2": "normal", "3": "alta"}
    prioridade = mapa.get(opcao, "normal")
    adicionar_tarefa(tarefas, descricao, prioridade)
    print(f"✔  Tarefa '{descricao}' adicionada com prioridade {prioridade}.")


def _menu_concluir(tarefas: list) -> None:
    """Solicita índice ao usuário e chama concluir_tarefa."""
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        num = int(input("Número da tarefa a concluir: "))
        concluir_tarefa(tarefas, num)
        print(f"✔  Tarefa '{tarefas[num]['descricao']}' marcada como concluída.")
    except (ValueError, IndexError) as e:
        print(f"⚠  {e}")


def _menu_excluir(tarefas: list) -> None:
    """Solicita índice ao usuário e chama excluir_tarefa."""
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        num = int(input("Número da tarefa a excluir: "))
        removida = excluir_tarefa(tarefas, num)
        print(f"🗑  Tarefa '{removida['descricao']}' excluída.")
    except (ValueError, IndexError) as e:
        print(f"⚠  {e}")


# ──────────────────────────────────────────────
# Loop principal
# ──────────────────────────────────────────────

def main() -> None:
    """Ponto de entrada do programa."""
    tarefas: list = []

    acoes = {
        "0": _menu_adicionar,
        "1": listar_tarefas,
        "2": _menu_concluir,
        "3": _menu_excluir,
        "4": lambda t: print(f"🧹  {limpar_concluidas(t)} tarefa(s) removida(s)."),
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