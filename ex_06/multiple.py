def multiple(a,b):
    result = 0
    for n in range(1,1000):
        if n % a == 0 or n % b == 0:
            result += n
    return result
# multiple(3,5)