# # Enter your code here. Read input from STDIN. Print output to STDOUT
# #input - input of int
# #input of names with number
# # hel = input("Enter phone"), input("Enter name")
# # Enter phone5675
# # Enter name45666
# #list of dictionaries
# # import re

# # def phonebook_entry(phone_book,name):
# #     start  = 0
# #     while start<len(phone_book):
# #         if name == phone_book[start]['name']:
# #             print(f"{phone_book[start]['name']}={phone_book[start]['phone_number']}")
# #         else:
# #             print('Not Found')
# #         start+=1
# # if __name__=='__main__':
# #     first_entry = []
# #     n = int(input().strip())
# #     for i in range(0,n):
# #        register= {'name':input("Enter name"),'phone_number':input("Enter phone")}
# #        first_entry.append(register)
# #     any_name = input("Enter a name to check in phonebook")
# #     if re.fullmatch(r"[a-zA-Z]+",any_name):
# #         phonebook_entry(first_entry,str(any_name))     

# # Enter your code here. Read input from STDIN. Print output to STDOUT
# #input - input of int
# #input of names with number
# # hel = input("Enter phone"), input("Enter name")
# # Enter phone5675
# # Enter name45666
# #list of dictionaries
# import re

# def phonebook_entry(phone_book,names_of_people):
#     start  = 0
#     while start<len(names_of_people):
#         if names_of_people[start] != phone_book['name']:
#            print('Not Found')
#         if names_of_people[start] == phone_book['name']:
#             print(f"{phone_book['name']}={phone_book['phone_number']}")
#         # if name != phone_book[start]['name']:
#         #    print('Not Found')
#         #decided to put the inputs all stored in list to capture the order. making now 2 list, I converted the phonebook to dictinary and added elements using update method.
#         start+=1
    
# if __name__=='__main__':
#     first_entry = {}
#     inputs = []
#     n = int(input().strip())
#     for i in range(0,n):
#        register= {'name':input(),'phone_number':input()}
#        first_entry.update(register)
#     for i in range(0,3):
#       any_name = (input())
#       if re.fullmatch(r"[a-zA-Z]+",any_name):
#         #  pass
#         inputs.append(any_name)
#     # for z in inputs:
#     # print(inputs)
#     phonebook_entry(first_entry,inputs)  
 
#     #   pass
           
# Enter your code here. Read input from STDIN. Print output to STDOUT
#input - input of int
#input of names with number
# hel = input("Enter phone"), input("Enter name")
# Enter phone5675
# Enter name45666
#list of dictionaries
# import re

# def phonebook_entry(phone_book,name):
#     start  = 0
#     while start<len(phone_book):
#         if name == phone_book[start]['name']:
#             print(f"{phone_book[start]['name']}={phone_book[start]['phone_number']}")
#         else:
#             print('Not Found')
#         start+=1
# if __name__=='__main__':
#     first_entry = []
#     n = int(input().strip())
#     for i in range(0,n):
#        register= {'name':input("Enter name"),'phone_number':input("Enter phone")}
#        first_entry.append(register)
#     any_name = input("Enter a name to check in phonebook")
#     if re.fullmatch(r"[a-zA-Z]+",any_name):
#         phonebook_entry(first_entry,str(any_name))     

# Enter your code here. Read input from STDIN. Print output to STDOUT
#input - input of int
#input of names with number
# hel = input("Enter phone"), input("Enter name")
# Enter phone5675
# Enter name45666
#list of dictionaries
import re
 #need to capture the value of the name and check if the name matches the name in the phonebook
 #using map ,means we will still loop
def phonebook_entry(phone_book,names_of_people):
    # for name_and_number in phone_book:
    #         for name in names_of_people:        
    #             if name != phone_book[name_and_number]['name']:
    #                 print('Not Found')
    #             elif name ==  phone_book[name_and_number]['name']:
    #                 print(f"{phone_book[name_and_number]['name']}={phone_book[name_and_number]['phone_number']}")

    #h

    start  = 0
    # want to compare the names in the list of names if there are in the phone_book
    while start<len(phone_book):  #checking all names  
            #not sustainable as when one element satisfies the conditon it is being printed
            print(phone_book[start]['name'])
            if names_of_people != phone_book[start]['name']:
               print('Not Found')  #get elements using recursion 
            if names_of_people == phone_book[start]['name']: 
                print(f"{phone_book[start]['name']}={phone_book[start]['phone_number']}")
        # if name != phone_book[start]['name']:
        #    print('Not Found')
        #decided to put the inputs all stored in list to capture the order. making now 2 list, I converted the phonebook to dictinary and added elements using update method.
            start+=1
    # https://prutor.ai/taking-multiple-inputs-from-user-in-python/
if __name__=='__main__':
    first_entry = []
    inputs = []
    n = int(input().strip())
    for i in range(0,n):  #using update with same key is causing reassignment
        name,phone_number = input().split()
        register= {'name':name,'phone_number':int(phone_number)}
        first_entry.append(register)
   
    try:
        for i in range(0,3):
            any_name = (input())
            if re.fullmatch(r"[a-zA-Z]+",any_name):
                inputs.append(any_name)
        print(first_entry)
        print(any_name) #holds last element
        phonebook_entry(first_entry,any_name)  
    except:
        pass
           