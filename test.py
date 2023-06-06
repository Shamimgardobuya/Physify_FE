import unittest
# from print import printing
from conditionals import checking_n
# from person import Person
from loops import check_multiple


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
    # def testing_person_created(self):
    #     #create your object
    #     object_one = Person(-1)
    #     self.assertEqual(object_one.amIOld(),print("Age is not valid, setting age to 0"))
    #     self.assertEqual(object_one.yearPasses(),1)
    def test_check_multiple(self):
        #Arrange, Act, Assert
        user_input = 2
        b = {
           " 2 x 1" :"= 2",
           " 2 x 2" :"= 4",
           " 2 x 3" :"= 6",
            "2 x 4" :"= 8",
            "2 x 5" :"= 10",
            "2 x 6" :"= 12",
            "2 x 7" :"= 14",
            "2 x 8" :"= 16",
            "2 x 9" :"= 18",
            "2 x 10" :"= 20 "   
        }      

        
        # self.assertIn(check_multiple(user_input),b)
        self.assertEquals(check_multiple(user_input),b)


#arrange,act assert, - having all values of n, so check n with function by calling, use assertequal
if __name__ =='__main__':
    unittest.main()