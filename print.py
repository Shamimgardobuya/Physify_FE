# # Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
# # input_string = input("Welcome to 30 Days of Code!")
# # greeting = f'''Hello, World
# #             {input_string}  '''
# # Print a string literal saying "Hello, World." to stdout.
# # # print("Say: Welcome to 30 Days of Code! ")
# # input_string = input("Hello")


# def printing(input_string):
#     # input_string = input("Hello")
#     # Print a string literal saying "Hello, World." to stdout.
#     print(f'''{input_string}.
#     Hello, World'''
#     )
# printing(input("Hello"))
# # TODO: Write a line of code here that prints the contents of input_string to stdout.
# #input is variable input_string
# #output value of the string in console
# #save value of input function
# #create variable and assgin the input function
# #inside the input function, write the string 'Welcome to 30 Days of Code !'
# #input_string = input("Welcome to 30 Days of Code!")


# # def addying_variables(number,user_double,users_string):
   
    
# #    adding_integers = number + i
# #    adding_double   = user_double + d
# #    adding_strings  = " ".join([s,users_string])
# #    printing_output = f'{adding_integers}\n{adding_double}\n{adding_strings}'

   
# #    print(printing_output)
# # addying_variables(1,4.5,"is the best place to learn and practice coding!")
# users_number = int(input())
# users_double = float(input())
# users_string = input()
# # def addying_variables(number,user_double,users_string):
    
# adding_integers = users_number + int(i)
# adding_double   = users_double + float(d)
# adding_strings  = "".join([s,users_string])
# printing_output = f'{adding_integers}\n{adding_double}\n{adding_strings}'

# print(printing_output)


def find_fibonacci(number):


    # elif(number == 1):
    #     return 1
    if(number <= 1):
         return number
    elif(number < 0):
        return 'incorrect input'
    elif(number == 2):
          return number
    else:
        return find_fibonacci(number - 1) + find_fibonacci(number - 2)

ans=13
for i in range(int(ans)):
            fibo_list = []
            fibo_list.append(find_fibonacci(i))
print(fibo_list[0])
    