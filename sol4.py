import sys

def solution(x, y):
    x, y = int(x), int(y)

    if x == y:
        return 'impossible'

    def scale(a, b):
        ans = (((a - b) - ((a - b) % b)) / b)

        return ans if ans > 0 else 1
        

    count = 0

    while x > 1 or y > 1:
        if x > y:
            s = scale(x, y)
            x -= y * s
        elif x < y:
            s = scale(y, x)
            y -= x * s
        else: 
            break
        count += s

    if x == 1 and y == 1:
        return str(count)
    
    return 'impossible'
            

print(solution('4', '7'))
print(solution('2', '1'))
print(solution('2', '4')) 
print(solution(sys.argv[1], sys.argv[2]))
