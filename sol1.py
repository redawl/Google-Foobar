def solution(data, n):
    
    dictionary = {}
    def count(x):
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
        return x

    def check(x):
        if dictionary[x] > n:
            return False
        else:
            return True
    any(list(map(count, data)))
    return list(filter(check, data))
