def union(a, b):
    """Объединение множеств"""
    return a | b

def intersection(a, b):
    """Пересечение множеств"""
    return a & b

def difference(a, b):
    """Разность множеств (a - b)"""
    return a - b

def complement(a, universal):
    """Дополнение множества до универсума"""
    return universal - a

def symmetric_difference(a, b):
    """Симметрическая разность"""
    return a ^ b

def bitmask(s, universal):
    """Битовая шкала множества"""
    return [1 if x in s else 0 for x in sorted(universal)]

def print_set_operations(a, b, universal):
    """Выполняет и печатает все операции над множествами"""
    print(f"Множество A: {a}")
    print(f"Множество B: {b}")
    print(f"Объединение A ∪ B: {union(a, b)}")
    print(f"Пересечение A ∩ B: {intersection(a, b)}")
    print(f"Разность A \\ B: {difference(a, b)}")
    print(f"Разность B \\ A: {difference(b, a)}")
    print(f"Дополнение A^d: {complement(a, universal)}")
    print(f"Дополнение B^d: {complement(b, universal)}")
    print(f"Симметрическая разность A ⊕ B: {symmetric_difference(a, b)}")
    print(f"Битовая шкала A: {bitmask(a, universal)}")
    print(f"Битовая шкала B: {bitmask(b, universal)}")