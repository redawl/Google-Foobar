def solution(x):

    def generous(x):
        if x == 1:
            return 1
        num1 = 1
        num2 = 1
        count = 2
        total = 2
        while total < x:
            num1, num2 = num2, num1 + num2
            total += num2
            if total <= x:
                count += 1
            else:
                return count
        return count

    def greedy(x):
        num1 = 1
        total = 1
        count = 1
        while x >= total:
            num1 = num1 * 2
            total += num1
            if total <= x: 
                count += 1
            else:
                return count

        return count

    return generous(x) - greedy(x)
