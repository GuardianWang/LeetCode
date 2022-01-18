def calculate_gcd(a, b):
    return gcd(a, b) if a > b else gcd(b, a)

 
def gcd(a, b):
    # a >= b
    while b != 0:
        a, b = b, a % b
    return a


def calculate_lcm(a, b):
    return a * b / calculate_gcd(a, b)


print(gcd(100, 80))
print(calculate_lcm(3, 9))

