def solution(l):
  length = len(l)
  count = 0
  for i in range(1, length - 1):
    curr = l[i]
    left = 0
    for x in l[0:i]:
      if curr % x == 0: left += 1
    right = 0
    for x in l[i + 1:]:
      if x % curr == 0: right += 1
    count += left * right

  return count

print(solution([1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6]))
