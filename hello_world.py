import math
import functools

def isNumPerfectNum(n):
    numsUntilN = list(range(1,n))
    cdLst = list(filter(lambda x : n % x ==0, numsUntilN))
    return n == sum(cdLst)


def sommeOfList(lst):
    return functools.reduce(lambda x,y : x + y, lst)

def isTrue(var):
    if type(var) == bool:
        return 1 if var else 0
    else:
        return None

def xPowerY(x,y):
    return math.pow(x,y)

if __name__ == "__main__":
    #Q1.1
    print("hello world!")
    #Q1.2
    boolVar = True
    print(isTrue(boolVar))
    print(isTrue(not boolVar))
    print(isTrue("kkk"))
    #Q1.3
    print(xPowerY(2,3))
    #Q1.4
    a,b = 2,3
    (a,b) = (b,a)
    print((a,b))
    #Q1.5
    l = []
    l.append("aba")
    l.append(5)
    print(l)
    l.reverse()
    print(l)
    #Q1.6
    print([i for i in range(2,24)])
    print(list(range(2,24)))
    #Q1.7
    num_list = list(range(1,11))
    print(num_list)
    slice_obj = slice(3,10,2)
    print(type(slice_obj))
    print(slice_obj)
    print(num_list[slice_obj])
    #Q1.8
    print(sommeOfList(num_list[slice_obj]))
    #Q1.9
    f = open("my_file.txt","w+")
    f.write("I know how to write")
    #Q1.10
    print(isNumPerfectNum(6))##true
    print(isNumPerfectNum(28))##true
    print(isNumPerfectNum(496))##true
    print(isNumPerfectNum(497))##false


