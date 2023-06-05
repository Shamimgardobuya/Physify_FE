import unittest
# from print import printing
from conditionals import checking_n
from person import Person
#Arrange,act, asssert, test if it prints out the input function's details
class testing_printing(unittest.TestCase):
    # def test_printing_input(self):
    #     data = input("My test")
    #     self.assertEqual(printing(data),f'''{data}.                              
    #                              Hello, World'''
    #                      )
    # def testing_conditionals(self):
    #     data =  int(input().strip())
    #     self.assertEqual(checking_n(data),"Weird")
    def testing_person_created(self):
        #create your object
        object_one = Person(-1)
        self.assertEqual(object_one.amIOld(),print("Age is not valid, setting age to 0"))
        self.assertEqual(object_one.yearPasses(),1)

#arrange,act assert, - having all values of n, so check n with function by calling, use assertequal
if __name__ =='__main__':
    unittest.main()