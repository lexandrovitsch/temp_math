def powerset(s):
    """Возвращает булеан (множество всех подмножеств)"""
    from itertools import chain, combinations
    s = list(s)
    return set(frozenset(x) for x in chain.from_iterable(
        combinations(s, r) for r in range(len(s)+1)))

def cartesian_product(a, b):
    """Декартово произведение двух множеств"""
    return {(x, y) for x in a for y in b}

def symmetric_diff(a, b):
    """Симметрическая разность множеств"""
    return a ^ b

def print_set_operations_lab2(a, b, c):
    """Пример выполнения операций для лабораторной работы 2"""
    print(f"Булеан P(A): {powerset(a)}")
    
    # Пример для варианта 1
    d1 = symmetric_diff(a, b)
    d2 = c - (a | b)
    d = cartesian_product(d2, d1)
    
    print(f"D1 = A △ B: {d1}")
    print(f"D2 = C \\ (A ∪ B): {d2}")
    print(f"D = D2 × D1: {d}")
    
    # Матрица бинарного отношения D
    print("\nМатрица бинарного отношения D:")
    d_list = list(d)
    elements_d1 = sorted(d1)
    elements_d2 = sorted(d2)
    
    for y in elements_d2:
        row = []
        for x in elements_d1:
            row.append(1 if (y, x) in d else 0)
        print(row)