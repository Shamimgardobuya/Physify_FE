function find_fibo(number){
    if(number <=1 || number ==2){
        return number
    }
    else{
        return find_fibo(number-1) + find_fibo(number-2)
    }
}
console.log(find_fibo(5))