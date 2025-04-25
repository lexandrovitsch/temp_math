def build_correspondence_graph(f, g):
    """Строит граф соответствия (возвращает пары вершин)"""
    return f.union(g)

def is_fully_defined(corr, domain):
    """Проверяет всюду определенность (каждый элемент domain имеет образ)"""
    domain_in_corr = {x for (x, y) in corr}
    return domain_in_corr == domain

def is_functional(corr):
    """Проверяет функциональность (каждый x имеет не более одного образа)"""
    x_values = [x for (x, y) in corr]
    return len(x_values) == len(set(x_values))

def is_surjective(corr, codomain):
    """Проверяет сюръективность (каждый y из codomain имеет прообраз)"""
    y_values = {y for (x, y) in corr}
    return y_values.issuperset(codomain)

def is_injective(corr):
    """Проверяет инъективность (разные x имеют разные образы)"""
    y_values = [y for (x, y) in corr]
    return len(y_values) == len(set(y_values))

def is_bijective(corr, domain, codomain):
    """Проверяет биективность (одновременно инъективно и сюръективно)"""
    return (is_functional(corr) and 
            is_injective(corr) and 
            is_surjective(corr, codomain) and 
            is_fully_defined(corr, domain))

def analyze_correspondence(f, g, domain, codomain):
    """Анализирует свойства соответствий"""
    print("Граф соответствия f ∪ g:")
    graph = build_correspondence_graph(f, g)
    print(graph)
    
    print("\nСвойства соответствия f:")
    print(f"Всюду определенное: {is_fully_defined(f, domain)}")
    print(f"Функциональное: {is_functional(f)}")
    print(f"Сюръективное: {is_surjective(f, codomain)}")
    print(f"Инъективное: {is_injective(f)}")
    print(f"Биективное: {is_bijective(f, domain, codomain)}")
    
    print("\nСвойства соответствия g:")
    print(f"Всюду определенное: {is_fully_defined(g, domain)}")
    print(f"Функциональное: {is_functional(g)}")
    print(f"Сюръективное: {is_surjective(g, codomain)}")
    print(f"Инъективное: {is_injective(g)}")
    print(f"Биективное: {is_bijective(g, domain, codomain)}")