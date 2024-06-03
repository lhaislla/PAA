class FibHeapNode:
    """
    Classe que representa um nó no Heap de Fibonacci.

    Atributos:
        key: Chave do nó.
        degree: Grau do nó (número de filhos diretos).
        mark: Indicador se o nó já perdeu um filho desde que se tornou filho de seu pai atual.
        parent: Nó pai.
        child: Qualquer um dos filhos do nó.
        left: Ponteiro para o nó à esquerda na lista de raízes ou de filhos.
        right: Ponteiro para o nó à direita na lista de raízes ou de filhos.
    """
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.mark = False
        self.parent = None
        self.child = None
        self.left = self  # Apontador para o nó à esquerda
        self.right = self  # Apontador para o nó à direita


class FibHeap:
    def __init__(self):
        self.min = None
        self.root_list = None
        self.n = 0

    def make_fib_heap(self):
        self.min = None
        self.root_list = None
        self.n = 0

    def fib_heap_insert(self, x):
        x.degree = 0
        x.parent = None
        x.child = None
        x.mark = False
        if self.min is None:
            self.root_list = x
            self.min = x
        else:
            x.left = self.min
            x.right = self.min.right
            self.min.right.left = x
            self.min.right = x
            if x.key < self.min.key:
                self.min = x
        self.n += 1

    def fib_heap_union(self, H1, H2):
        H = FibHeap()
        H.make_fib_heap()

        if H1.min is None:
            H.min = H2.min
            H.root_list = H2.root_list
        elif H2.min is None:
            H.min = H1.min
            H.root_list = H1.root_list
        else:
            H.root_list = H1.root_list
            H.min = H1.min if H1.min.key < H2.min.key else H2.min

            H1_min_right = H1.min.right
            H2_min_left = H2.min.left

            H1.min.right = H2.min
            H2.min.left = H1.min

            H1_min_right.left = H2_min_left
            H2_min_left.right = H1_min_right

        H.n = H1.n + H2.n
        return H

    def fib_heap_extract_min(self):
        z = self.min
        if z is not None:
            # Adicionar os filhos de z à lista de raízes
            if z.child is not None:
                children = self._get_children(z)
                for child in children:
                    self._add_to_root_list(child)
                    child.parent = None

            # Remover z da lista de raízes
            self._remove_from_root_list(z)

            # Atualizar o mínimo de H
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self._consolidate()

            self.n -= 1

        return z

    def _consolidate(self):
        # Inicializa o array de listas vazias
        D = [None] * (self.n.bit_length() + 1)

        # Percorre a lista de raízes
        root_nodes = self._get_root_nodes()
        for w in root_nodes:
            x = w
            d = x.degree
            while D[d] is not None:
                y = D[d]
                if x.key > y.key:
                    x, y = y, x
                self._fib_heap_link(y, x)
                D[d] = None
                d += 1
            D[d] = x

        self.min = None
        for i in range(len(D)):
            if D[i] is not None:
                self._add_to_root_list(D[i])
                if self.min is None or D[i].key < self.min.key:
                    self.min = D[i]

    def _fib_heap_link(self, y, x):
        # Remove y da lista de raízes
        self._remove_from_root_list(y)

        # Torna y um filho de x
        if x.child is None:
            x.child = y
            y.left = y.right = y
        else:
            y.left = x.child
            y.right = x.child.right
            x.child.right.left = y
            x.child.right = y
        y.parent = x
        x.degree += 1
        y.mark = False

    def fib_decrease_key(self, x, k):
        if k > x.key:
            raise ValueError("Nova chave é maior que a chave atual")

        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)
        if x.key < self.min.key:
            self.min = x

    def _cut(self, x, y):
        # Remove x da lista de filhos de y
        if x == x.right:
            y.child = None
        else:
            x.left.right = x.right
            x.right.left = x.left
            if y.child == x:
                y.child = x.right
        y.degree -= 1

        # Adiciona x à lista de raízes
        self._add_to_root_list(x)

        x.parent = None
        x.mark = False

    def _cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def fib_heap_delete(self, x):
        self.fib_decrease_key(x, float("-inf"))
        self.fib_heap_extract_min()

    def _get_children(self, x):
        children = []
        if x.child is not None:
            current = x.child
            children.append(current)
            current = current.right
            while current != x.child:
                children.append(current)
                current = current.right
        return children

    def _add_to_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
            node.left = node.right = node
        else:
            node.left = self.root_list
            node.right = self.root_list.right
            self.root_list.right.left = node
            self.root_list.right = node

    def _remove_from_root_list(self, node):
        if node == self.root_list:
            if node.right == node:
                self.root_list = None
            else:
                self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left

    def _get_root_nodes(self):
        nodes = []
        if self.root_list is not None:
            current = self.root_list
            nodes.append(current)
            current = current.right
            while current != self.root_list:
                nodes.append(current)
                current = current.right
        return nodes
    def __str__(self):
        if self.min is None:
            return "FibHeap(min=None, root_list=None, n=0)"

        nodes = self._get_root_nodes()
        nodes_str = ", ".join(str(node.key) for node in nodes)
        return f"FibHeap(min={self.min.key}, root_list=[{nodes_str}], n={self.n})"


if __name__ == "__main__":
    # Criando H1
    heap1 = FibHeap()
    node1 = FibHeapNode(10)
    heap1.fib_heap_insert(node1)

    node2 = FibHeapNode(15)
    heap1.fib_heap_insert(node2)

    # Criando H2
    heap2 = FibHeap()
    node3 = FibHeapNode(5)
    heap2.fib_heap_insert(node3)

    node4 = FibHeapNode(8)
    heap2.fib_heap_insert(node4)

    # Union
    union_heap = heap1.fib_heap_union(heap1, heap2)
    print(union_heap)

   

    # Verificando o mínimo da heap unida
    print("Mínimo:", union_heap.min.key)  # Deve imprimir o mínimo entre 5 e 10

    # Remoção do mínimo
    min_node = union_heap.fib_heap_extract_min()
    print("Mínimo após remoção:", union_heap.min.key)  # Deve imprimir o próximo mínimo

    # Decrease key
    node1.key = 3
    union_heap.fib_decrease_key(node1, 3)
    print("Novo mínimo após decrease key:", union_heap.min.key)

    # Delete
    union_heap.fib_heap_delete(union_heap.min)
    print("Mínimo após delete:", union_heap.min.key)  # Deve imprimir o próximo mínimo
