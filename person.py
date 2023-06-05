counter = 1
class Person:
    age_of_person = []
    def __init__(self,initialAge):
        self.initialAge = initialAge
        
        if  initialAge <= 1:
            self.initialAge = 0 
            print("Age is not valid, setting age to 0.") 
        elif initialAge >30 :
             print("Age has to be in range of -5 to 30") 
            # return initialAge
        # self.age_of_person.append(self.initialAge)
    def amIOld(self):
                if self.initialAge >= 18:
                    print("You are old.")
                elif self.initialAge < 13 :
                    print("You are young.")
                elif self.initialAge  >= 13 and self.initialAge < 18 :
                    print("You are a teenager.")
    def yearPasses(self):
                
                self.age_of_person.append(self.initialAge)
                count = self.age_of_person.count(self.initialAge)
                if count == 1  :  # don't count the ones that count == 2
                  self.initialAge = self.initialAge + count 
                  return self.initialAge
                
                else:
                    if count > 1 :
                        self.initialAge = self.initialAge + 1
                        return self.initialAge
                #if same person is called twice, increase the age by 1 year.
                

              
t = int(input())  #6
for i in range(0, t): #0, 6 
    age = int(input())       #6  
    p = Person(age)  
    p.amIOld()    # for first age user input
    for j in range(0, 3): #iteration will happen thrice
       p.yearPasses()
       
        # print(j)
    #    print(p.yearPasses())
    p.amIOld()
    print("")

# person = Person(18)  #age changes
# # print(person.yearPasses())  #17 19
# print(person.yearPasses())# orginal_age as 17
# print(person.yearPasses())# original age 18 + 1 

#how to capture previous object passed


 #   print(f"List every time after increamenting {self.age_of_person, count}")
                #   print(f"This is the value of the new age {self.initialAge}")
                #   new_list = []
                #   [new_list.append(x) for x in self.age_of_person if x not in new_list]
                #   print('hello')
                #   print(new_list)
                  #loop through the list: if the element appears more than once, then remove the duplicate and return the newlist.
                #   for i in self.age_of_person:
                #        if self.age_of_person.count(self.age_of_person[i]) > 1:
                #   no_duplicate = self.age_of_person.count(self.age_of_person) > 1
                #   self.age_of_person.remove(no_duplicate)
                #             print(self.age_of_person)
                #   if self.initial remove duplicate


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
