def ex1():
    fibo_numbers = [0,1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    n -= 2
    while n:
        n -= 1
        fibo_numbers.append(fibo_numbers[-1] + fibo_numbers[-2])
    return fibo_numbers

def isPrime(number):
    if number<2:
        return False;
    if number == 2:
        return True
    if number%2 == 0:
        return False
    for i in range(3, number//2):
        if(number%i == 0):
            return False
    return True


def ex2(list):
    returnList = []
    for number in list:
        if isPrime(number):
            returnList.append(number)

#print(ex2([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def ex3(a, b):
    
