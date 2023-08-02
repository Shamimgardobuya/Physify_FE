var array = [9, 2, 5, 6, 4, 3, 7, 10, 1, 12, 8, 11];

// Basic implementation (pivot is the first element of the array)
//create a function that takes in the global variable
function quicksort(array) {
    if (array.length == 0){
        return []
    }
    var left = [], right = [], pivot = array[0];
    array.forEach(element => {
        if(array[element] < pivot){
            left.push(array[element])
        }
        else if(array[element]>pivot){
            right.push(array[element]);
        }
    })   
   
    return quicksort(left).concat(pivot,quicksort(right));
}

console.log(quicksort(array))