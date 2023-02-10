def dig_pow(n, p):
    result = 0
    for i, number in enumerate(str(n)):
        result += int(number) ** (p + i)
    if result % n == 0:
        return result // n
    return -1

print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(695, 2))

# def dig_pow(n, p):
#   s = 0
#   for i,c in enumerate(str(n)):
#      s += pow(int(c),p+i)
#   return s/n if s%n==0 else -1