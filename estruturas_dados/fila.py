from collections import deque

class Fila:
    """
    Fila FIFO (First-In, First-Out) para processamento de itens em ordem de chegada.

    Complexidades:
        enfileirar: O(1)
        desenfileirar: O(1)
        esta_vazia: O(1)
        __len__: O(1)
    """
    def __init__(self):
        # Usamos deque para enfileirar/desenfileirar em O(1)
        self._dados = deque()

    def enfileirar(self, item):
        # Adiciona um item ao final da fila.
        self._dados.append(item)

    def desenfileirar(self):
        # Remove e retorna o item da frente da fila. Lança IndexError se vazia.
        if self.esta_vazia():
            raise IndexError("Fila vazia")
        return self._dados.popleft()

    def esta_vazia(self) -> bool:
        # Retorna True se a fila estiver vazia.
        return not self._dados

    def __len__(self) -> int:
        # Retorna o número de itens na fila.
        return len(self._dados)
