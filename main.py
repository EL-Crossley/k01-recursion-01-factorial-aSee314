3# Put your function here


def factorial (a):
    if a == 1:
        return a
    if a > 1:
        return a * factorial(a-1)




# testing
num = int(input())
print(factorial(num))