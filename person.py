counter = 1
class Person:
    
    def __init__(self,initialAge):
        self.initialAge = initialAge
        self.age_of_person = []
       
        # Add some more code to run some checks on initialAge
        #using constraints such as as- 1-4 and then -5 to 30
        #print "Age is not valid, setting age to 0."
        if initialAge in range(1,5) or initialAge < 1:
            print("Age is not valid, setting age to 0")  
        # self.age_of_person.append(self.initialAge)
    def amIOld(self):
                # Do some computations in here and print out the correct statement to the console
                #old when age is >= 18
                if self.initialAge >= 18:
                    print("You are old")
                elif self.initialAge < 13 :
                    print("You are young")
                elif self.initialAge  >= 13 and self.initialAge < 18 :
                    print("You are a teenager")
    def yearPasses(self):
                
                self.age_of_person.append(self.initialAge)
                count = self.age_of_person.count(self.initialAge)
                if count > 1 :  #
                  self.initialAge = self.initialAge + count
                  print(self.age_of_person, count)
                  return  self.initialAge
                else:
                    return self.age_of_person[0]
                #if same person is called twice, increase the age by 1 year.
                

                # for i in range(0,90):
                      #want ot store the original age value and always increament by 1

                      #replace this as new age
                    #   return self.initialAge + 1
                # if self.initialAge != original_Age[0]:   
                #     return original_Age[0] + 1
                # else:
                #     return original_Age[0] + 1
                #capture initial object
                ##still not recognizing object
                # def __iter__(self):
                #     self.counter = 1
                #     self.max = 90
                #     return self

                # def __next__(self):
                #     increase = self.initial
                #     if fib > self.max:
                #         raise StopIteration
                #     self.a, self.b = self.b, self.a + self.b
                #     return fib
                #looping effect- continue adding until range is met
                #hold history of added age
                #problem is it will always return 1  and not record the initial age
                #how to keep record of the initial value
                # increase = self.initialAge + 1
                # if self.initialAge == increase:
                #       return increase
                # Increment the age of the person in here

t = int(input())  #6
for i in range(0, t): #0, 6 
    age = int(input())       #6  
    p = Person(age)  
    p.amIOld()    # for first age user input
    for j in range(0, 3): #iteration will happen thrice
        print(p.yearPasses())
    print(p.yearPasses())
    p.amIOld()
    print("")

# person = Person(18)  #age changes
# # print(person.yearPasses())  #17 19
# print(person.yearPasses())# orginal_age as 17
# print(person.yearPasses())# original age 18 + 1 

#how to capture previous object passed