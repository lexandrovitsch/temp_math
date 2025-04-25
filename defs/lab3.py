def relation_matrix(relation, universal):
    """Создает матрицу бинарного отношения"""
    size = len(universal)
    universal_sorted = sorted(universal)
    matrix = [[0]*size for _ in range(size)]
    
    for (x, y) in relation:
        i = universal_sorted.index(x)
        j = universal_sorted.index(y)
        matrix[i][j] = 1
    
    return matrix

def is_reflexive(matrix):
    """Проверяет рефлексивность"""
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            return False
    return True

def is_irreflexive(matrix):
    """Проверяет антирефлексивность"""
    for i in range(len(matrix)):
        if matrix[i][i] != 0:
            return False
    return True

def is_symmetric(matrix):
    """Проверяет симметричность"""
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def is_antisymmetric(matrix):
    """Проверяет антисимметричность"""
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and matrix[i][j] == 1 and matrix[j][i] == 1:
                return False
    return True

def is_transitive(matrix):
    """Проверяет транзитивность"""
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                for k in range(n):
                    if matrix[j][k] and not matrix[i][k]:
                        return False
    return True

def check_relation_properties(relation, universal):
    """Проверяет все свойства бинарного отношения"""
    matrix = relation_matrix(relation, universal)
    
    print("Матрица бинарного отношения:")
    for row in matrix:
        print(row)
    
    properties = {
        "Рефлексивность": is_reflexive(matrix),
        "Антирефлексивность": is_irreflexive(matrix),
        "Симметричность": is_symmetric(matrix),
        "Антисимметричность": is_antisymmetric(matrix),
        "Транзитивность": is_transitive(matrix),
    }
    
    print("\nСвойства отношения:")
    for prop, value in properties.items():
        print(f"{prop}: {'Да' if value else 'Нет'}")