#also known as half interval search
#finds target value within a sorted array if not sorted one needs to sort it.
#sort array first.


array = [5,6,0,1,5,6,3]
def quicksort(array):
    if(len(array)==0):
        return []
    left_elements = []
    right_elements = []
    pivot = array[0]
    
    for i in array:
        if i < pivot:
            left_elements.append(i)
        elif i > pivot:
            right_elements.append(i)
    return quicksort(left_elements)+[pivot]+quicksort(right_elements)

# if __name__ == '__main__':
#     array = [12, 11, 15, 10, 9, 1, 2, 3, 13, 14, 4, 5, 6, 7, 8]
#     quicksort(array, 0, len(array) - 1)
#     print(array)
#create a function that takes in an array, a the size of it and a target.
#start base case
#Find if the element exists
'''Have pointers of start to represent the starting 
and end to represent the end of array for the flow of direction. 

Then find the mid of the array
If mid element is equal to element, return mid
If mid is less element, remove left side, start = mid+1
If mid is more than an element, remove right side, end = mid -1
Repeat the process n times till you find the position of the element'''
def  binary_search(arr,target,start,end):

    if start <= end:
        mid = start + (start+end) //2
        if arr[mid] == target:
            return mid
        elif(arr[mid] < target) :
            return binary_search(arr,target,mid + 1,end)
        else:
            return binary_search(arr,target,start,end = mid - 1)
        
    else:
        return 'not found'
array = [3,7,56,4,5,6,76,78,]
print(binary_search(array,5,0,len(array)-1))





