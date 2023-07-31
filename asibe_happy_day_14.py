class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    def computeDifference(self):
        a.sort()
        self.maximumDifference = a[-1] - a[0]
        return self.maximumDifference
    
 #input - array of elementes
    #a variable holding maximum difference
    #output - a maximum difference between any of the two values from the array
    #process, sort the list
    #find last and first index then find the maximum difference through subtracting the two
    #use def main to run the file
    #
    
    
