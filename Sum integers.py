def solution(queryType, query):
    hash_map = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    help_hash_map = hash_map
    for i in range(len(queryType)):
        command = queryType[i]
        if command == 'insert':
            position = query[i][0]
            value = query[i][1]
            hash_map[position] += value
        elif command == 'addToValue':
            add_value = query[i][0]
            for key, value in hash_map.items():
                if value != 0:
                    hash_map[key] += add_value
        elif command == 'addToKey':
            add_key_value = query[i][0]
            for key, value in hash_map.items():
                if value != 0:
                    help_hash_map[key + add_key_value] = value

        elif command == 'get':
            return help_hash_map[query[i]]

    print(queryType)
    print(query)


print(solution(["insert", "insert", "addToValue", "addToKey", "get"], [[1, 2], [2, 3], [2], [1], [3]]))
