import re
import unittest


def extractNumAndSum(doubleStr):
    m = re.match(r'(\d+|-\d+)\.(\d+)',doubleStr)
    if m == None:
        print("Error: " + doubleStr + " is not a floating point number")
        return
    sum = 0
    sum += int(m.groups()[0])
    sum += int(m.groups()[1])
    print(sum)

class TestStringManipulation(unittest.TestCase):
    def test

if __name__ == '__main__':
    #extractNumAndSum("abc")
    #extractNumAndSum("20.20")
    #extractNumAndSum("0.20")
    #extractNumAndSum(".20")
    #extractNumAndSum("20.")
    #extractNumAndSum("20.20.20")
    #extractNumAndSum("-20.20")
    unittest.main()
