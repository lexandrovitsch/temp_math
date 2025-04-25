def relation_from_matrix(matrix, elements):
    """Создает отношение из матрицы"""
    relation = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                relation.add((elements[i], elements[j]))
    return relation

def inverse_relation(relation):
    """Обратное отношение"""
    return {(y, x) for (x, y) in relation}

def relation_composition(r, s):
    """Композиция отношений r и s: r ∘ s = {(a,c) | ∃b: (a,b)∈s ∧ (b,c)∈r}"""
    return {(a, c) for (a, b1) in s for (b2, c) in r if b1 == b2}

def relation_intersection(r, s):
    """Пересечение отношений"""
    return r & s

def relation_union(r, s):
    """Объединение отношений"""
    return r | s

def relation_difference(r, s):
    """Разность отношений"""
    return r - s

def relation_symmetric_diff(r, s):
    """Симметрическая разность отношений"""
    return r ^ s

def print_relation_operations(delta_matrix, tau, rho, elements):
    """Выполняет операции над бинарными отношениями"""
    delta = relation_from_matrix(delta_matrix, elements)
    
    print("1) δ ∪ τ:")
    print(relation_union(delta, tau))
    
    print("\n2) τ \\ δ:")
    print(relation_difference(tau, delta))
    
    print("\n3) δ ∩ τ:")
    print(relation_intersection(delta, tau))
    
    print("\n4) ρ ∘ τ:")
    print(relation_composition(rho, tau))
    
    print("\n5) τ ∩ ρ:")
    print(relation_intersection(tau, rho))