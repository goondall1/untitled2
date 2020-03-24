import re
import random



def ifRandLowerThenN(n):
    randNum = random.randrange(1,1000)
    return 0 if randNum > n else randNum

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def show(self):
        print("my location is %d,%d" %(self.x ,self.y))



if __name__ == '__main__':
    var = Point(2,3)
    var.show()
    var2 = Point()
    var2.show()
    print(ifRandLowerThenN(0))
    print(ifRandLowerThenN(1000))
    print(ifRandLowerThenN(10))
