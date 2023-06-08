# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def string_value(word):
    if word in range(0,100000000000000000):
        return "Please try a word not an integer"
    i = 0
    new_even = []
    new_odd = []
    while i<len(word):
        if i%2 == 0: 
            new_even.append(word[i])
            even_caharacters = "".join(new_even)
        if i%2 !=0:
            new_odd.append(word[i])
            odd_caharacters = "".join(new_odd)

        i+=1
    print(f"{even_caharacters} {odd_caharacters}")
    return f"{even_caharacters} {odd_caharacters}"

        # even = i%2 ==  #this results to TypeError: not all arguments converted during string formatting - mixing f data types but also in the first iteration the value even only had one argument to check, but now in the second iteration, even did not have another place to store the value of the  even index belonging to the second argument.
             
if __name__ == '__main__':
    number_of_test = int(input("Enter the number of words "))
    for i in range(0,number_of_test):

        enter_word = (input("Enter a word "))
        if re.fullmatch(r"[a-zA-Z]+",enter_word):
            string_value(str(enter_word))
