import sys

def solution(n):
  n = int(n)
  min = 0
  max = 1

  count = 0
  
  while max < n:
    max, min = max * 2, max
    count += 1

  count += max - n if max - n < n - min - 1 else n - min - 1

  return str(count)

print(solution('15'))
print(solution('4'))
print(solution('9'  * 310))
print(solution(sys.argv[1]))
