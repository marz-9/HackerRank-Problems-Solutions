num1 = int(input())
num2 = int(input())
summ=0
def solveMeFirst(summ):
    a=num1
    b=num2
    if (1<=a<=1000 and 1<=b<=1000):
        summ=a+b
        return summ
res = solveMeFirst(summ)
print(res)