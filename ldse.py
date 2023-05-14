'''Implementação'''


class Node():
    def __init__(self, value):
        self.data = value
        self.next = None


class ElementList():
    def __init__(self):
        self.first = None
        self._size = 0

    def append(self, value):
        if self.first:
            pointer = self.first
            while (pointer.next):
                pointer = pointer.next
            pointer.next = Node(value)
        else:
            self.first = Node(value)
        self._size = self._size + 1

    def __len__(self):
        return self._size

    '''implemente os métodos GET e SET para
        se comportarem conforme o comentario
        na descrição do método'''

    def __getitem__(self, index):
        pointer = self.first

        for i in range(index):
            if (pointer):
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            return pointer.data

        raise IndexError("List index out of range")

    def __setitem__(self, index, value):
        for i in range(index):
            if (pointer):
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            pointer.data = value
        else:
            raise IndexError("List index out of range")
