import sys, math

def solution(n):
  n = int(n)
  count = 0
  if n == 1: return 0

  while n != 1:
    if math.log(n, 2).is_integer() == True:
      return int(count + math.log(n, 2))
    elif n % 2 == 0: 
      n = n >> 1
    elif n == 3 or n % 4 == 1:
      n -= 1
    else:
      n += 1
    count += 1
  return count
      
    
  
print(solution('15'))
print(solution('4'))
print(solution('9' * 310))

