counter = 1
class Person{
    constructor(initialAge){
    this.initialAge = initialAge
    this.age_of_person = []

}
// if  (initialAge <= 1){
//     self.initialAge = 0 
//     print("Age is not valid, setting age to 0.") }
// else if( initialAge >30 ){


//      print("Age has to be in range of -5 to 30") 
//     // return initialAge
// }
amIOld(){
    if (this.initialAge >= 18){
        print("You are old.")
    }
    else if (this.initialAge < 13){
        print("You are young.")
    }
    else if( this.initialAge  >= 13 && this.initialAge < 18){
        print("You are a teenager.")
    }
}  
yearPasses(){
                
    this.age_of_person.push(this.initialAge)
    var count_of_age = 0
    this.age_of_person.filter((initialAge)=>(initialAge?count_of_age++:age_of_person))
    // count = this.age_of_person.count(this.initialAge)
    if (count_of_age == 1){ 
      this.initialAge = this.initialAge + count_of_age 
      return this.initialAge
}
    
    else{
        if (count_of_age > 1 ){
            this.initialAge = this.initialAge + 1
            return this.initialAge
    }
}
    // #if same person is called twice, increase the age by 1 year.
    
}

}
my_age = new Person(25);
console.log(my_age.yearPasses())
    
               
// t = int(input()) 
// //  #6
// for (i in range(0, t)){
// // #0, 6 
//     age = int(input())       
//     // #6  
//     p = Person(age)  
//     p.amIOld()   
//     //  # for first age user input
//     for (j in range(0, 3)){
//     // #iteration will happen thrice
//        p.yearPasses()
       
//         // # print(j)
//     // #    print(p.yearPasses())
//     p.amIOld()
//     print("")
//     }
// }