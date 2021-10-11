import sys

def solution(x, y):
    tab = {}
    x, y = int(x), int(y)
    def recurse(a, b):
        key = '{}{}'.format(a, b)
        if key in tab:
            return tab[key]
        if x == a and y == b:
            tab[key] = 0
            return 0 
        
        if x < a or y < b:
            tab[key] = -1
            return -1
        
        l = 1 + recurse(a+b, b)
        r = 1 + recurse(a, a+b)

        if r == 0 and l == 0:
            tab[key] = -1
            return -1
        ret = r if r > l else l
        tab[key] = ret
        return ret

    rounds = recurse(1, 1)
    print(tab)
    if rounds != -1:
        return rounds

    return "impossible"

#print(solution('4', '7'))
#print(solution('2', '1'))
print(solution(sys.argv[1], sys.argv[2]))
