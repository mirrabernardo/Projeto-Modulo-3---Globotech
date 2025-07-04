class _Node:
    __slots__ = ('key', 'value', 'left', 'right')

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class ArvoreBinariaBusca:
    """
    Árvore de Busca Binária (BST) para chaves inteiras.
    Complexidades:
        inserir: O(h) onde h = altura da árvore (médio O(log n), pior O(n))
        buscar:  O(h)
        remover: O(h)
        percurso_em_ordem: O(n)
    """
    def __init__(self):
        self._root = None

    def inserir(self, key: int, value):
        # Insere ou atualiza o valor associado à chave.
        self._root = self._insert(self._root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return _Node(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            # Atualiza o valor se a chave já existir
            node.value = value
        return node

    def buscar(self, key: int):
        # Retorna o valor associado à chave, ou None se não existir.
        node = self._root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None

    def remover(self, key: int):
        # Remove o nó com a chave especificada.
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            # Caso 1: nó sem filhos ou um único filho
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Caso 2: nó com dois filhos
            # Encontrar o sucessor (menor na subárvore direita)
            succ = self._min_node(node.right)
            node.key, node.value = succ.key, succ.value
            node.right = self._remove(node.right, succ.key)
        return node

    def _min_node(self, node):
        # Retorna o nó de menor chave na subárvore.
        current = node
        while current.left:
            current = current.left
        return current

    def percurso_em_ordem(self):
        # Retorna lista de (chave, valor) em ordem crescente de chaves.
        result = []
        self._inorder(self._root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.key, node.value))
            self._inorder(node.right, result)

