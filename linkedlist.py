# # #creat a linked list and traverse through it and find mth to last element
# # #input-integer eg 4 and linked list 
# # #output- element from the last element
# # #create a node 
# # #create linked list
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
    
#     def __repr__(self):
#         return self.data
    
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def __repr__(self):
#         node = self.head
#         nodes = []
#         while node is not None:
#             nodes.append(node.data)
#             node = node.next
#         nodes.append("None")
#         return " -> ".join(nodes)    
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data
    
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printMfromLast(self,n):
        temp = self.head
        length = 0
        while temp is not None:
            temp = temp.next
            length +=1
        if n > length:  # If entered location is greater
                       # than length of linked list
            print('Location is greater than the' +
                  ' length of LinkedList')
            return    
        temp = self.head
        for i in range(0, length - 1):
            temp = temp.next
        print(temp.data)

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(17)
    llist.push(35)
    # print((llist))
    # Function call
    llist.printMfromLast(1)        
            
        

        

# Create a function and pass in a parameter
#create a base case incase number is 0 return 1
#using the else statement call the function again
#and print the output
def find_fibonacci(number):
    if(number <= 1 or number == 2):  #this is the base case,  a right edge case that stops recursion running forever
        return number
    # if number <= 1:
    #    return number
    else:
        return (find_fibonacci(number - 1) + find_fibonacci(number - 2))
# if __name__ == "main":
#     number= 9
print(find_fibonacci(6))
ans=12
# if ans <= 0:
#    print("Plese enter a positive integer")
# else:
#     print("Fibonacci sequence:")
#     for i in range(int(ans)):
#             fibo_list = []
#             fibo_list.append(find_fibonacci(i))
#     print(fibo_list[0])
#print(find_fibonacci(7))
# print(type(find_fibonacci(7 - 2)))
# print(ans)

        