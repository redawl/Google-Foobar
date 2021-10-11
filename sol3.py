from fractions import Fraction

def solution(x):
    # odd: R = 2 * (-P0 + 2 * (P1 - P2 + P3 - ... - P(x - 2)) + P(x - 1))
    # even: same but 2/3 at the start
    # special case for x = 2
    # not possible for x <= 1
    length = len(x)

    if length <= 1:
        return [-1,-1]

    if length == 2:
        rad = Fraction(2 * float(x[1] - x[0]) / 3).limit_denominator()
        return [rad.numerator, rad.denominator]

    ret = 0

    for i in range(1, length - 1):
        ret += 2 * ((-1)**(i - 1)) * x[i]

    ret = 2 * (ret - x[0])

    if length % 2 == 0:
        ret = float((ret + 2*x[-1])) / 3
    else:
        ret -= 2*x[-1]

    ret = Fraction(ret).limit_denominator()

    return [ret.numerator, ret.denominator]       
    
    
