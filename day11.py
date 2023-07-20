#PRINT A STAR IN PYTHON
#line by line
   #
#create a variable and assign it 1*1
#create another variable and assign 1*2
##create another variable and assign 1*4
#create another variable and assign 1*6
#create another variable and assign 1*8
#create another variable and assign 1*10
#print them in the new lines
'''one = 1 * 'x'
one_ = 2 * 'x'
one_3 = 4 * 'x'
one_4fr = 6 * 'x'
one_5789 = 8 * 'x'
one_65432 = 10 * 'x'
print(f'''  
'''      {one_65432}
         {one_5789}
          {one_4fr}
           {one_3}
            {one_}
            {one}
           {one}
          {one_}
         {one_3}
        {one_4fr}
       {one_5789}
      {one_65432}
    '''     ''')
'''
#now hour glass shape 
'''  a b c
       d
     e f g
'''

'''
z
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
input - 2 d array printed values of 6 by 6, output - maximum sum of values falling in hour 
hour glass shape
capture sums of all the hour glasses - then compare the maximum
hour glasses - how many hour glasses  - 16
capture them in a list and using the max function you get the largest 
how to get the hour glass shape, - 
mapped to each of the values then respond- it's like a Z999
                                                         8
                                                        675

                                                      determine the first hour glasses shape
                                                      variable 
'''  

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName,lastName,idNumber,scores):
        self.scores = scores
        super().__init__(firstName,lastName,idNumber)
    def calculate(self):
        average = sum(scores) // len(scores)
        if average in range(90,101):
            return 'O'
        elif average in range(80,91):
            return 'E'
        elif average in range(70,81):
            return 'A'
        elif average in range(55,71):
            return 'P'
        elif average in range(40,56):
            return 'D'
        elif average in range(0,41):
            return 'T'
        
            
        
    
    #   Class Constructor
    #create parameters for child class Student then
    #create a function that calculates the average mark - total over number of input given
    #create a variable and assign it the calculation of total divide by number of items.
    #After getting the average mark, have the range of vlaues listed then using if statements compare the variable if it's in that range
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())