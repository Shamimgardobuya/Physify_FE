'''Find a “pivot” item in the array.
This item is the basis for comparison for a single round.
Start a pointer (the left pointer) at the first item in the array.
Start a pointer (the right pointer) at the last item in the array.
While the value at the left pointer in the array is less than the pivot value, move the left pointer to the right (add 1). Continue until the value at the left pointer is greater than or equal to the pivot value.
While the value at the right pointer in the array is greater than the pivot value, move the right pointer to the left (subtract 1). Continue until the value at the right pointer is less than or equal to the pivot value.
If the left pointer is less than or equal to the right pointer, then swap the values at these locations in the array.
Move the left pointer to the right by one and the right pointer to the left by one.
If the left pointer and right pointer dont meet, go to step 1.'''


def quicksort(my_array,left_index,right_index):
     if(left_index<right_index):
          #calculate pivot index
          pivot_index = partition(my_array,left_index,right_index)
          #sort left sub_array
          quicksort(my_array,left_index,pivot_index)
          #sort rigth sub_array
          quicksort(my_array,pivot_index+1,right_index)

def partition(my_arr,left_index,right_index):
    pivot_index = (left_index + right_index) /2
    pivot_value = my_arr[int(pivot_index)] #pivot
    # left_index - pointer  at the first item in the array
    # right_index = pointer at the last item in the array.
    while (True):
            while (my_arr[left_index] < pivot_value):# block supposed to be within the loop
                left_index +=1  #increamenting the index
            while (my_arr[right_index] > pivot_value): #novement backwards
                right_index -=1
            if (left_index >=right_index):return right_index
                #Move the left pointer to the right by one and the right pointer to the left by one.
            #swapping time for values at right and left index
            temporary_start = my_arr[left_index]
            my_arr[left_index] = my_arr[right_index]
            my_arr[right_index] = temporary_start
            # elif left_pointer != right_pointer:
            #    return quicksort(my_arr)
if __name__ == '__main__':
    array = [12, 11, 15, 10, 9, 1, 2, 3, 13, 14, 4, 5, 6, 7, 8]
    quicksort(array, 0, len(array) - 1)
    print(array)









