def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
	
def factorial(b):
#    if a >= b:
#        print ('a must smaller than b')
#        break
    sum = 1
    for num in range(1,(b + 1)):
        sum = num * sum
        print (sum)
    return sum

#用递归算阶乘
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
pow = 128
print ('%d power is '% pow, power(2,pow))

print ('factorial is ', factorial(10))

print ('fact is ', fact(10))