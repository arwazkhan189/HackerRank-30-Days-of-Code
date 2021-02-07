class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        self.__elements.sort()
        a=self.__elements[0]
        b=self.__elements[len(self.__elements)-1]
        self.maximumDifference=abs(a-b)
    

    
    
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
