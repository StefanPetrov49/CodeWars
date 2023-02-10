def tower_builder(n_floors):
    result = []
    result.append(" " * n_floors + ("*" * 1) + "*" + ("*" * 1) + " " * n_floors)
    for i in range(1, n_floors):
        result.append(" " * (n_floors - i) + ("*" * i) + "*" + ("*" * i) + (n_floors - i))
    return result


print(tower_builder(3))
