"""Testes unitários para o módulo main.py"""

import pytest
from __main__ import (
    criar_tarefa,
    adicionar_tarefa,
    concluir_tarefa,
    excluir_tarefa,
    limpar_concluidas,
)


# ─────────────────────────────────────────────
# criar_tarefa
# ─────────────────────────────────────────────

class TestCriarTarefa:

    def test_cria_com_campos_corretos(self):
        tarefa = criar_tarefa("Estudar DevOps")
        assert tarefa["descricao"] == "Estudar DevOps"
        assert tarefa["prioridade"] == "normal"
        assert tarefa["concluida"] is False
        assert "criada_em" in tarefa

    def test_cria_com_prioridade_alta(self):
        tarefa = criar_tarefa("Deploy urgente", "alta")
        assert tarefa["prioridade"] == "alta"

    def test_cria_com_prioridade_baixa(self):
        tarefa = criar_tarefa("Organizar pastas", "baixa")
        assert tarefa["prioridade"] == "baixa"

    def test_erro_descricao_vazia(self):
        with pytest.raises(ValueError, match="vazia"):
            criar_tarefa("")

    def test_erro_descricao_somente_espacos(self):
        with pytest.raises(ValueError, match="vazia"):
            criar_tarefa("   ")

    def test_erro_prioridade_invalida(self):
        with pytest.raises(ValueError, match="inválida"):
            criar_tarefa("Tarefa X", "urgente")


# ─────────────────────────────────────────────
# adicionar_tarefa
# ─────────────────────────────────────────────

class TestAdicionarTarefa:

    def test_adiciona_uma_tarefa(self):
        tarefas = []
        adicionar_tarefa(tarefas, "Ler documentação")
        assert len(tarefas) == 1
        assert tarefas[0]["descricao"] == "Ler documentação"

    def test_adiciona_multiplas_tarefas(self):
        tarefas = []
        adicionar_tarefa(tarefas, "Tarefa 1")
        adicionar_tarefa(tarefas, "Tarefa 2")
        adicionar_tarefa(tarefas, "Tarefa 3")
        assert len(tarefas) == 3

    def test_nova_tarefa_nao_concluida(self):
        tarefas = []
        adicionar_tarefa(tarefas, "Tarefa nova")
        assert tarefas[0]["concluida"] is False


# ─────────────────────────────────────────────
# concluir_tarefa
# ─────────────────────────────────────────────

class TestConcluirTarefa:

    def test_marca_tarefa_como_concluida(self):
        tarefas = []
        adicionar_tarefa(tarefas, "Fazer PR")
        concluir_tarefa(tarefas, 0)
        assert tarefas[0]["concluida"] is True

    def test_nao_afeta_outras_tarefas(self):
        tarefas = []
        adicionar_tarefa(tarefas, "Tarefa A")
        adicionar_tarefa(tarefas, "Tarefa B")
        concluir_tarefa(tarefas, 0)
        assert tarefas[1]["concluida"] is False

    def test_erro_indice_negativo(self):
        tarefas = []
        adicionar_tarefa(tarefas, "Tarefa A")
        with pytest.raises(IndexError):
            concluir_tarefa(tarefas, -1)

    def test_erro_indice_fora_do_range(self):
        tarefas = []
        adicionar_tarefa(tarefas, "Única tarefa")
        with pytest.raises(IndexError):
            concluir_tarefa(tarefas, 5)

    def test_erro_lista_vazia(self):
        with pytest.raises(IndexError):
            concluir_tarefa([], 0)


# ─────────────────────────────────────────────
# excluir_tarefa
# ─────────────────────────────────────────────

class TestExcluirTarefa:

    def test_remove_tarefa_correta(self):
        tarefas = []
        adicionar_tarefa(tarefas, "Remover esta")
        removida = excluir_tarefa(tarefas, 0)
        assert removida["descricao"] == "Remover esta"
        assert len(tarefas) == 0

    def test_lista_diminui_em_um(self):
        tarefas = []
        adicionar_tarefa(tarefas, "T1")
        adicionar_tarefa(tarefas, "T2")
        excluir_tarefa(tarefas, 0)
        assert len(tarefas) == 1

    def test_erro_indice_invalido(self):
        tarefas = []
        adicionar_tarefa(tarefas, "Tarefa")
        with pytest.raises(IndexError):
            excluir_tarefa(tarefas, 99)


# ─────────────────────────────────────────────
# limpar_concluidas
# ─────────────────────────────────────────────

class TestLimparConcluidas:

    def test_remove_apenas_concluidas(self):
        tarefas = []
        adicionar_tarefa(tarefas, "Feita")
        adicionar_tarefa(tarefas, "Pendente")
        concluir_tarefa(tarefas, 0)
        limpar_concluidas(tarefas)
        assert len(tarefas) == 1
        assert tarefas[0]["descricao"] == "Pendente"

    def test_retorna_quantidade_removida(self):
        tarefas = []
        adicionar_tarefa(tarefas, "T1")
        adicionar_tarefa(tarefas, "T2")
        adicionar_tarefa(tarefas, "T3")
        concluir_tarefa(tarefas, 0)
        concluir_tarefa(tarefas, 1)
        removidas = limpar_concluidas(tarefas)
        assert removidas == 2

    def test_sem_concluidas_nao_remove_nada(self):
        tarefas = []
        adicionar_tarefa(tarefas, "Pendente")
        removidas = limpar_concluidas(tarefas)
        assert removidas == 0
        assert len(tarefas) == 1

    def test_lista_vazia_retorna_zero(self):
        tarefas = []
        assert limpar_concluidas(tarefas) == 0