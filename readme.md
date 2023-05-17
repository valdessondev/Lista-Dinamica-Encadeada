
# Lista-Dinamica-Encadeada

Este repositório contém a implementação de uma Lista Dinâmica Encadeada em Python. O objetivo é fornecer uma estrutura de dados flexível que permite a adição e manipulação de elementos de forma eficiente.

## Conteúdo

- [ldse.py](ldse.py): Implementação da Lista Dinâmica Encadeada.
- [show.py](show.py): Exemplo de uso da Lista Dinâmica Encadeada.

## Utilização

### ldse.py

O arquivo `ldse.py` contém a implementação da classe `ElementList`, que representa a Lista Dinâmica Encadeada. A classe possui os seguintes métodos:

- `append(value)`: Adiciona um elemento ao final da lista.
- `__len__()`: Retorna o tamanho da lista.
- `__getitem__(index)`: Retorna o elemento na posição `index`.
- `__setitem__(index, value)`: Define o valor do elemento na posição `index`.

A seguir está um exemplo de uso:

```python
from ldse import ElementList

instance = ElementList()
print(len(instance))
instance.append(5)
x = instance[0]
print(x)
```

### show.py

O arquivo `show.py` demonstra a utilização da Lista Dinâmica Encadeada importando o módulo `ldse`. Neste exemplo, é criada uma instância da classe `ElementList`, adicionado um elemento e obtido o tamanho da lista.

```python
import ldse

instance = ldse.ElementList()
print(instance._size)
instance.append(5)
x = len(instance)
print(x)
```

## Colaboradores

- [valdessondev](https://github.com/valdessondev) no readme e o demais conteúdos foi: [elioenays](https://github.com/elioneays)
