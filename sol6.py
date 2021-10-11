import random

def solution(l):
  length = len(l)
  count = 0
  for i in range(0, length):
    val = l[i]
    multiples = [ x for x in l[i + 1:] if x % val == 0 ]
    length2 = len(multiples)
    for j in range(0, length2):
      val2 = multiples[j]
      mult2 = [ x for x in multiples[j + 1:] if x % val2 == 0 ]
      count += len(mult2)
    
  return count

print(solution([1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6]))
list = []
base = 5987
for i in range(1, 2001):
  list.append(base ** i)
print(list)
print(solution(list))
