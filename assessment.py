# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

# Input - story with attrubutes such as length,moral lessons and age group, StoryTeller and Translator.
# Output- recording oral stories and translate to different languages
#advise with Linda.
#create a class Story with attributes such as length, moral lesson, age group
#have a function of the story teller and translator, take in story object and return the relevant story and meaning.

# class Story:
#     def __init__(self,length,moral_lesson,age_group,name):
#         self.length = str(length)
#         self.moral_lesson = moral_lesson
#         self.age_group = age_group
#         self.initial_language = ""
#         self.name = name
#     def tell_story(self,name_story_teller):
#         return f"Hi, my name is {name_story_teller}, and am here to tell you a story of {self.name} and why {self.moral_lesson}."

#     def translate_story(self,translator_name,new_language):  #have object of story in initial language, replace the characters of story from databases
#         new_language = "Hapo zamani za kale, paliondekea sungura mmoja kwa jina kasi. Alipenda kukimbia sana hadi wanyama wote wakamfahamu na mienendo yake. Siku moja aliamua kuchangamua wanyama wote mpaka kobe kwa mchezo wa kukimbia."
#         # new_language = self.length.replace(self.length, new_language)
#         hadithi = self.length.replace(self.length, new_language)
#         return f"Kwa majina naitwa {translator_name}, hadithi ndiyo hii {hadithi}"

# story_one = Story("Hare and the tortoise","Once upon a time, there lived a hare who liked to run. All animals knew about his passion. One day he decided to challenge all the animals including Tortoise to a running competition.","Hurry hurry has no blessings",range(5,10))
# print(story_one.tell_story("Jack"))
# print(story_one.translate_story("Musa","Kiswahili"))


  #-deduct 1 , - 4mks 
# class Story:
#      def __init__(self,content,length,moral_lessons,age_group):
#          self.content=content
#          self.length=length  #1
#          self.moral_lessons=moral_lessons   #2mks +3 
#          self.age_group = age_group

#      def colonialiasm(story):
#          pass
#      def Myths(story):
#          pass

# class StoryTeller:
#     def __init__(self, name, language, culture): 
#         self.name = name
#         self.language = language   #2
#         self.culture = culture
#     def colonialism(self):
#         pass
#     def Myths(self):
#         pass


# class Translator:
#     def translate(story,language): #3
#         stories = {self.content},language
#         return stories

# class Recipe:
#     def __init__(self, food, ingredients, prep_time, cooking_method, nutritional_info):
#         self.food = food
#         self.ingredients = ingredients
#         self.prep_time = prep_time
#         self.cooking_method = cooking_method
#         self.nutritional_info = nutritional_info #2 # 3MKS

# recipe1 = Recipe("chicken","onions,tomato","30mis","fry","protein")
# class MoroccanRecipe(Recipe):                                          
#     def __init__(self,ingredients, prep_time, cooking_method, nutritional_info, spices):
#       super().__init__(ingredients, prep_time, cooking_method, nutritional_info)
#       self.spices = spices

#     def display_recipe(self):    
#      super().display_recipe()
#      return {self.spices}

# class EthiopianRecipe(Recipe):
#     def __init__(self,ingredients, prep_time, cooking_method, nutritional_info,nut,spicess):
#      super().__init__(ingredients, prep_time, cooking_method, nut,nutritional_info)
#      self.spicess = spicess

#     def display_recipe(self):
#     #  super().display_recipe()
#      return {self.spicess}
# recipe2 = EthiopianRecipe("chicken","onions,tomato","30mis","fry","protein","pili")
# recipe2.display_recipe()
# print(recipe2.display_recipe())

# class NigerianRecipe(Recipe):
#     def __init__(self,ingredients, prep_time, cooking_method, nutritional_info, plantain):
#      super().__init__(ingredients, prep_time, cooking_method, nutritional_info)
#      self.plantain = plantain

#     def display_recipe(self):
#      super().display_recipe()
#      return {self.plantain}

    
# class Product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price =price
#         self.quantity=quantity
#     def calculate_total():
#         price = 2000
#         quantity = 5
#         product = price * quantity

# Question 6
# class Student:
#     def __init__(self,name,age,grades):
#         self.name=name 
#         self.age=age
#         self.grades=grades
#     def calculate_average(self):
#         total_grades = sum{self.grades}
#         avg = total_grades/len{self.grades}
#         return avg
    
#     def display_info(self):
#         return f" {self.name} {self.age} {self.grades}"

#     def pass(self):
#     average = self.calculate_average()
#     return average

# Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.

# input - destination and data,, passenger information ,
# outout- generate booking confirmation
#         manage passenger information
# process   - create class flight, a destinantion and date as attributes- 
#passenger - name, destination, date 
#booking - if flight > 5 then fool if not, book
#create a function in passenger returning passemger information like flight 
# if dictionary of the flight is more than 5 or has been booked 5 times
# class FlightBooking:
#     def __init__(self):
#         self.flights = []
        
# def search_flight(self,destination,date):
#     available_flights = []
#     for flight in self.flights:
#         if flight.destination == destination and flight.date == date:
#             available_flights.append(flight)  #how are they availble
#             return available_flights
             

# def reserve_seat(self,flight,customer):
#     return f"{customer} reserved seat in {self.flight}"

# class Book:
#     def __init__(self, title, author, available):
     
#         self.title = title
#         self.author = author
#         self.available= available

# class LibraryCatalog:
#     def __init__(self):
#      self.books = []

#     def new_book(self, book):
#         self.books.append(book)

#     def search_by_title(self,title):   #book can be passed as string-used a book object created 
#         books = []
#         for book in self.books:
#             if book.title.lower() == title.lower():
#              books.append(book)
#         return books

#     def search_by_author(self, author):
#         books = []
#         for book in self.books:
#             if book.author.lower() == author.lower():
#                 books.append(book)
#             return books
        
# class Story:
#     def __init__(self,story,moral,age_group,language):
#         self.story=story
#         self.moral=moral
#         self.age_group=age_group
#         self.language=language
    
#     def details(self):
#         return f'{self.moral} means alot to {self.age_group}'

# class Storyteller(Story):
#     def __init__(self, story,name):
#        self.story=story
#        self.name=name

#     def Teller(self):
#         return f'{self.name} is the best story teller of {self.story.moral} for {self.story.age_group} age group'
     

# class Translator(Story):
#     def __init__(self,story,language ,languages):
#         self.story=story
#         self.language=language
#         self.languages=languages

#     def translate(self):
#         if {self.language} in {self.languages}:
#             return "Language can be translated"
#         else:
#             return"Language not found"



# Ndabaga= Story("a woman was the bravest among all","being brave","12 years and above","English")
# print (Ndabaga.details())

# Marcus=Storyteller(Ndabaga,"Marcus")
# print( Marcus.Teller())

# Chinese=Translator(Ndabaga,"English",("English","Chinese","French"))
# print(Chinese.translate())


class Specie:
    def __init__(self,name,movement):
        self.name=name
        self.movement=movement

    def diet(self,diet):
        return f'{self.name} eats {diet}' 

    def lifespan(self,life):
        return f'{self.name} lives for {life}' 
class Predator(Specie):
    def __init__(self,animal,type):
           self.animal=animal
           self.type=type
    def preference(self):
        return f'{self.animal} is of {self.type}' 

class Prey(Specie):
    def __init__(self,animal,prey):
     self.animal=animal
     self.prey=prey

    def food(self): 
        return f'{self.animal.animal} eats {self.prey}'

# Lion=Predator("Lion","Mammal")
# print(Lion.preference())

# Antelope= Prey(Lion,"Antelope")
# print(Antelope.food())
# print("">> - Kevine"")

class AncestralStory:
    def __init__(self,length,lessons,agegroup,title): 
        self.length=length
        self.lessons=lessons
        self.agegroup=agegroup
        self.title=title
        
       
    
class Story(AncestralStory):
    def __init__(self,title,length):
        self.length=length
        self.title=title
    def record_story(self):
        
        return f"this story is called {self.title} " 
class StoryTeller(AncestralStory):
    def __init__(self,narrator):
       self.narrator=narrator
    def get_storyteller(self):
        
        return f"This story will be narrated by {self.narrator}"      
        
class Translator(AncestralStory): 
    def __init__(self,languageone, languagetwo ): 
         self.languageone=languageone
         self.languagetwo=languagetwo
    
    def translate_story(self):
        return f"Translate this story from {self.languageone} to {self.languagetwo} "   
    
    
# story1=AncestralStory("long","Obey your parents","children","The Hare and the Hyena")  
# print(story1) 
# story2=Story("The Ogre","short")
# print(story2.record_story())
# story3=StoryTeller("Mzee")
# print(story3.get_storyteller())
# story4=Translator("Kikuyu","English")
# print(story4.translate_story())

class Product:
    def __init__(self,name):
        self.name=name
        # self.price=price
        # self.quantity=quantity
        
    def calculate_total(self,price,quantity):
      a=  price*quantity
    #   return "the orange is "
      return a
        
# prod1=Product("Orange")  
# print(prod1.calculate_total(35,7))

# prod2=Product("Socks")  
# print(prod2.calculate_total(300,9))

# prod3=Product("pen")  
# print(prod3.calculate_total(40,10))

# prod4=Product("Bread")  
# print(prod4.calculate_total(65,3))
books=[" "]
class LibraryCatalog:
    def __init__(self,title,author,available,year):
        self.title=title
        self.author=author
        self.available=available    #1mk
        self.year=year
        
        
    def add_new_book(self):
        newbook="The river between"
        for i in newbook:                   #1mk
            if i not in books:
                books.append(i)
        return books
    def search_books(self):
        for book in books:
         if book in books:   #1mk
            return f"{self.title} authored by {self.author} is available" 
         else:
             return f"{self.title} by {self.author} is not available" 
                                           #1mk
    def display_book_details(self):
         return f"The book {self.title} has been written by {self.author} in the year {self.year}."
    
# book1=LibraryCatalog("The River and The Source","Margaret Ogolla","is available",1994)    
# print(book1.display_book_details())  
# print(book1.add_new_book())   
# print(book1.search_books()) 

class FlightBooking:
    def __init__(self,destination,date,seat,passenger,id):
        self.destination=destination
        self.date=date
        self.seat=seat
        self.passenger=passenger
        self.id=id
    def booking_confirmations(self):
        return f"This seat number {self.seat}, has been booked for {self.passenger} of id number {self.id}"
    def manage_passenger(self):
        return f"THis is {self.passenger} of id number {self.id} and will sit at seat number {self.seat}"
    def available_flights(self):
        return f"The flight to {self.destination} is available on date {self.date}"
    
flight=FlightBooking("Mombasa","11th November",24,"Purity Wanjiku","38907645")
# print(flight.manage_passenger())  
# print(flight.available_flights())  
# print(flight.booking_confirmations())

# class AncestralStories():
#     def__init__(self,length,lessons,agegroup)
#     self.length=length
#     self.lessons=lessons
#     self.agegroup=agegroup
    



# warStory=AncestralStories("long","courage","young people")
# print(warStory)

# class StoryTeller(AncestralStories):
#     def__init__(self,length,lessons,agegroup,speed,languages)
#     super(self,length,lessons,agegroup)
#     self.speed=speed
#     self.languages=languages
        

#     languagesSpoken(self):
#         if(this.languages.length>=2):
#             print("This storyteller has translator capabilities");



# class Recipe():
#     def__init__(self,ingredients,preparationtime,cookingmethod,nutritionalinfo):
#         self.ingredients=ingredients
#         self.preparationtime=preparationtime
#         self.cookingmethod=cookingmethod
#         self.nutritionalinfo=nutritionalinfo

    
#     timeForPreparation(self):

#     if(self.preparationtime>=3):
#             print("this cuisine takes a long time to prepare")
        
#     else:
#             print("This cuisine can be prepared within a reasonable amount of time")
    
    

# MoroccanRecipe=Recipe(["dhania","onions","cinammon"],2,"frying","Rich in vitamins")
# EthiopianRecipe=Recipe(["chilli","wheat","cumin"],4,"baking","Rich in protein")
# NigerianRecipe=Recipe(["tomatoes","cassava","cardamon"],2,"boiling","Rich in iron")

# print(MoroccanRecipe)
# print(EthiopianRecipe)
# print(NigerianRecipe)
# MoroccanRecipe.timeForPreparation()
# EthiopianRecipe.timeForPreparation()
# NigerianRecipe.timeForPreparation()
# class Product():
#     constructor(name,price,quantity)
#         self.name=name;
#         self.price=price;
#         self.quantity=quantity;

    
#     totalValue()
#         total= this.price*this.quantity
#         return total
    
# soap = Product("geisha",25,5)
# soap.totalValue()
# flour = Product("exe",120,6)
# flour.totalValue()
# fish = Product("tuna",60,3)
# fish.totalValue()
# fruits = Product("pears",20,8)
# fruits.totalValue()

# class Student():
#     def__init__(self,name,age,grades)
#         self.name=name
#         self.age=age
#         self.grades=grades
    
#     average_grade(self):
#         total=0
#         for ( g in self.grades)
#             total+=g;
#             print(total);
        
#         averagetotal/(this.grades.length)
#         print(average);
        
    
#     display_total(self):
#        print("This student's name is f{self.name} and they are f{self.age} years old and they have an average grade of ${this.averageGrade()}");
    
#     passMark(self):
#         if(this.averageGrade()>=60):
#             print("The student has passed");

class Story:
    def __init__(self, length, moral_lesson, age_group):
        self.length = length
        self.moral_lesson = moral_lesson
        self.age_group = age_group

class StoryTeller(Story):
    def __init__(self, name, language):
        super().__init__("length","moral_lesson","age_group")
        self.name= name
        self.language = language


    def tell_story(self, story):
        print(f"{self.name} is telling a story in {self.language}:")
        

class Translator(StoryTeller):
    def __init__(self, name, language, target_language):
        super().__init__(name, language)
        self.target_language = target_language
        self.language = language


    def translate_story(self, story):
        print(f"{self.name} is translating a story from {story.language} to {self.target_language}:")


class Recipe:
    def __init__(self,name,country,ingredients,preparationTime,cookingMethod,nutritionalInformation):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.preparationTime = preparationTime
        self.cookingMethod = cookingMethod
        self.nutritionalInformation = nutritionalInformation
    def display_recipe(self):
        return f"Name:{self.name}\nIngredients:{self.ingredients}\nPreperation Time:{self.preparationTime}"
        
class KikuyuRecipe(Recipe):
    def __init__(self, name, country, ingredients, preparation_time, cooking_method, nutrition_information, spices, serving_suggestion):
        super().__init__(name, country, ingredients, preparation_time, cooking_method, nutrition_information)
        self.spices = spices
        self.serving_suggestion = serving_suggestion

    def print_recipe(self):
        return f"{super().display_recipe()}\nSpice Used:{self.spices}\nServing Suggestion:{self.serving_suggestion}"
      



# recipe1 = Recipe("Chocolate Cake","Africa","butter,sugar,flour,eggs","1hour","Oven","Strong")
# print(recipe1.display_recipe())

# kikuyurecipe1 = KikuyuRecipe("White Rice","Kenya","oil","2hours","Boiling","Strong","BlackPepper","Withpeas")
# print(kikuyurecipe1.print_recipe())


# story = Story("Welcome back", "SHHH", "Drink coffee and code")
# storyteller = StoryTeller("Goretti", "Python")
# storyteller.tell_story(story)

# translator = Translator("Maria", "Spanish", "French")
# translator.translate_story(story)

class Species:
    def __init__(self, name, diet, lifespan, migration_pattern):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan
        self.migration_pattern = migration_pattern

class Predator(Species):
    def __init__(self, name, diet, lifespan, migration_pattern, hunting):
        super().__init__(name, diet, lifespan, migration_pattern)
        self.hunting= hunting


class Prey(Species):
    def __init__(self, name, diet, lifespan, migration_pattern, running):
        super().__init__(name, diet, lifespan, migration_pattern)
        self.run = running


# species1= Species("cheetah ","meat","20years","done")
# predator1 = Predator ("lions", "meat", "25 years ", "seasonal", "yes ")
# prey1 = Prey('gazelle', 'grass','4-6 months ', 'yearly',"no")
# print (species1.name,species1.lifespan)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value_product(self):
        return self.price * self.quantity
    
product1 = Product("pen",20,95)
product2 = Product("rubber",10,95)
product3 = Product("pencil",15,95)
product4 = Product("book",100,95)
# print(product1.total_value_product())

# total = product1.total_value_product()+ product2.total_value_product() +product3.total_value_product()+product4.total_value_product()
# print(total)

# class Student:
#     def __init__(self, name, age,*grades):
#         self.name = name
#         self.age = age
#         self.grades = list(grades)

#     def calculate_average_grade(self):
#         return sum(self.grades) / len(self.grades)

#     def display_student_information(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Grades: {self.grades}")

#     def determine_if_passed(self):
#         average_grade = sum(self.grades) / len(self.grades)
#         if average_grade >= 60:
#             return True
#         else:
#             return False
        
# student1 = Student("Goretti",20, [80, 70, 90])
# student2 = Student("Gladys", 22, [50, 60, 70])
# student3 = Student("Irene",24,[90,88,95])
# print(student1.calculate_average_grade())
# print(student1.determine_if_passed())
# print(student1.display_student_information())

# print(student2.calculate_average_grade())
# print(student2.determine_if_passed())
# print(student2.display_student_information())

# from fnmatch import translate


# class Story:
#      def __init__(self, title, content, length, moral_lessons, age_group):
#         self.title = title
#         self.content = content
#         self.length = length
#         self.moral_lessons = moral_lessons
#         self.age_group = age_group

# # class StoryTeller:
# #     def __init__(self, name, language, age_group):
# #         self.name = name
# #         self.language = language
# #         self.age_group = age_group
    
# #     def tell_story(self, story):
# #         print(f"{self.name} is telling a {story.title} story which is a  {self.language} story to {self.age_group} children")

# class Translator:
#     def __init__(self, name, original_language, translated_language):
#         self.name = name
#         self.original_language = original_language
#         self.translated_language = translated_language
    
#     def translate(self, story):
    
#         translated_content = translate(story.content)
        
#         translated_story = Story(
#             title = story.title,
#             content = translated_content,
#             length = story.length,
#             moral_lessons = story.moral_lessons,
#             age_group = story.age_group
#         )
        
#         return translated_story
# story1 = Story(
#     "Mwangi, the brave boy","A boy that went searching for his beloved dog in the deadly forest","20 pages", "Bravery and courage", "5-10 years")

# # Create an instance of StoryTeller
# storyteller1 = StoryTeller("Kamau Maina", "Kikuyu", "5-10 years")

# # Tell the story
# storyteller1.tell_story(story1)

# # Create an instance of Translator
# translator1 = Translator("Translator1", "Kikuyu", "English")

# # Translate the story
# translated_story = translator1.translate(story1)

# # Output the translated story
# # print(f"Translated story: {translated_story.title}: {translated_story.content}")
# story2 = Story("Jamba Nene", "a boy that met an ogre in the deadly forest", "40 pages", "obedience", "11-15 years")

# # Create an instance of StoryTeller
# storyteller2 = StoryTeller("Wambui Muriithi", "Kikuyu", "11-15 years")

# # Tell the story
# storyteller2.tell_story(story2)

# # Create an instance of Translator
# translator2 = Translator("Translator2", "Kikuyu", "English")

# # Translate the story
# translated_story = translator2.translate(story2)

# Output the translated story
# print(f"Translated Story: {translated_story.title}: {translated_story.content}")



# Create an instance of Story2

class Recipe:
    def __init__(self,ingridients,preparationTime,cookingMethod,nutritionalInformation):
       self.ingridients=ingridients
       self.preparationTime=preparationTime
       self.cookingMethod=cookingMethod
       self.nutritionalInformation=nutritionalInformation

  
    def getgetCookingTime(self):
        print(f'{self.__class.____.name}{self.language}')


class MoroccanRecipe (Recipe):
     time="1hour and 40 minutes"


class EthiopianRecipe  (Recipe):
     time="2 hours 40 minutes"


class  NigerianRecipe (Recipe):
     time="4hours 50 minutes"
# moroccanRecipe= MoroccanRecipe("garlic,pepper,cheese,fry,smooth skin")
# moroccanRecipe.getCookingTime()


# ethiopianRecipe=EthiopianRecipe("Sugar,spice,lemons ,steam,strong teeth")
# ethiopianRecipe.getCookingTime()

# nigerianRecipe=NigerianRecipe("water,lemons,salad,stir-fry,great eye-sight")
# nigerianRecipe.getCookingTime()

# class Species:
#     def __init__(self,diet,typicalLifespan,migrationPatterns):
#         self.diet=diet
#         self.typicalLifespan=typicalLifespan
#         self.migrationPatterns=migrationPatterns

#     def getSpecificSpecie():
#         print(f'{self.__class.____.name__},{self.language}')


# database=[]
# listOfSpecies=Species("lion","cheetah","tiger","panther","leopard")
# listOfSpecies2=Species("gazelle","zebra","rhino","hippo","monkey")
# database.extend(listOfSpecies,listOfSpecies2)


# class Predator (Species):
#      specificSpecies=["lion","cheetah","panther","tiger","leopard"]

# class Prey (Species):
#      specificSpecies=["gazelle","zebra","rhino","hippo","monkey"]

# species=Species("food","lives up to 5years ","migrates twice a year")

# predator =Predator("Eats flesh","lives upto a maximum of 10 years ","migates once a year")
# predator.getSpecificSpecies()

# prey=Prey(" Eats herbs and grass","lives uto a maximum of 5 years","migrates thrice a year")
# prey.getSpecificSpecies()
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Grades: {", ".join(str(grade) for grade in self.grades)}')
        print(f'Average grade: {self.calculate_average_grade()}')
        print(f'Passing grade: {self.has_passed()}')

    def has_passed(self):
        return self.calculate_average_grade() >= 50

# student1 = Student('Wanjiku Kihonge', 70, [90, 35, 60])
# print(student1)
library =[]
class LibraryCatalog:
    def __init__(self,title,author,copy):
        self.title = title
        self.author = author
        self.copy = copy
        # self.description = description

    def add_book(self):
        all_infor = f"{self.title}, {self.author},{self.copy}"
        library.append(all_infor)
        
    def search_book(self,book_title):
        for item in library:
         if (book_title == item.title):
             return item.author
         
   
# book1 = LibraryCatalog(title="River",author="Margret Ogola",copy=30)
# book1.add_book()
# x = book1.search_book("Born")
# print(x)
# print(library)

# book2 = LibraryCatalog("Born","Trevor Noah",300)
# book2.add_book()
# print(library)

class FlightBoooking:
    def __init__(self, passenger_name,destination,date,total_seats):
        self.passenger_name = passenger_name
        self.destination = destination
        self.date = date
        self.total_seats = total_seats
        
    def occupy_seat(self,occupied_seats):
            self.total_seats -= occupied_seats
            return f"The total seats available for booking are {self.total_seats}"
        
    def reserve_seat(self,seat_no):
        if seat_no <= self.total_seats:
            return f"{self.passenger_name} has booked {seat_no} seats"
        if seat_no >self.total_seats:
            return f"The passenger cannot book flight since {self.total_seats} seats are left for booking"
    
        
# flight1 = FlightBoooking("Rita","Wajir",2,40)
# results = flight1.occupy_seat(40)
# results2 = flight1.reserve_seat(3)
# print(results)
# print(results2)
class Ancestral_stories:
    def __init__(self, title,moral_lessons , length, age_group):
        self.title = title
        self.moral_lessons = moral_lessons
        self.length = length
        self.age_group = age_group 
        
    def story(self):
        self.moral_lessons 
        
class Story:
    def __init__(self, name):
        self.name = name  
                       
class Story_teller:
    def __init__(self, name,story_title):
        self.name = name  
        self.story_title=story_title
        
    def tell_story(self):
        print(f"{self.name} is telling a story:")
        print(Story_teller.tell_story(self))
        
class Translator:
     def __init__(self, name,language):
        self.name = name  
        self.language=language
        
story = Story("Mzee Kobe") 
ancestral_story = Ancestral_stories("The cunning fox", "Helping others is important.", "Short", "Children")
storyteller = Story_teller("John", "The dark forest")
translator = Translator("Maria", "Spanish")
# print(translator)   #str__object

class Recipe:
    def __init__(self, name, country, ingredients, preparation_time, cooking_method):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method
        

    def display_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"Country: {self.country}")
        print("Ingredients:") 
        
        
class MoroccanRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, serving_suggestion):
        Recipe.__init__(self, name, "Morocco", ingredients, preparation_time, cooking_method)
        self.serving_suggestion = serving_suggestion

    def display_recipe(self):
        Recipe.display_recipe(self)
        print(f"Serving Suggestion: {self.serving_suggestion}") 
        
class EthiopianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, spice_level):
        Recipe.__init__(self, name, "Ethiopia", ingredients, preparation_time, cooking_method)
        self.spice_level = spice_level

    def display_recipe(self):
        Recipe.display_recipe(self)
        print(f"Spice Level: {self.spice_level}") 
        
class NigerianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_information):
        Recipe.__init__(self, name, "Nigeria", ingredients, preparation_time, cooking_method)
        self.nutritional_information = nutritional_information

    def display_recipe(self):
        Recipe.display_recipe(self)
        print("Nutritional Information:")
     
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):   
        total_grades = sum(self.grades)
        average_grade = total_grades / len(self.grades)
        return average_grade

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def has_passed(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60

# instances for the student 
# student1 = Student("Elizabeth", 21, [80, 75, 90, 95])
# student1.display_student_info()
# average_grade1 = student1.calculate_average_grade()
# print(f"Average Grade: {average_grade1}")
# print(f"Passed: {student1.has_passed()}")
class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Total Copies:", self.total_copies)
        print("Available Copies:", self.available_copies)


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, total_copies):
        book = Book(title, author, total_copies)
        self.books.append(book)

    def search_by_title(self, title):
        found_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                found_books.append(book)
        return found_books

    def search_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                found_books.append(book)
        return found_books

    def display_book_details(self, title):
        found_books = self.search_by_title(title)
        if found_books:
            for book in found_books:
                book.display_book_details()
        else:
            print("Book not found in the library.")

library = LibraryCatalog()
library.add_book("Born A Crime", "Trevor Noah", 13)

# print(library.add_book("Born A Crime", "Trevor Noah", 13))

class Recipe:
    def __init__(self,recipes):
        self.recipes=recipes

class MoroccanRecipe:

    def __init__(self,ingredients,preparationTime,cookingMethod,nutritionalInformation) :
        self.ingredients=ingredients
        self.prepationTime=preparationTime
        self.cookingMethod=cookingMethod
        self.nutritionalInformation=nutritionalInformation
    def recipe(self):
        return f"The Morrocan recipe is prepared using {self.ingredients} and is cooked using {self.cookingMethod} and has {self.nutritionalInformation}"    
class EthiopianRecipe:
    def __init__(self,ingredients,preparationTime,cookingMethod,nutritionalInformation) :
        self.ingredients=ingredients
        self.prepationTime=preparationTime
        self.cookingMethod=cookingMethod
        self.nutritionalInformation=nutritionalInformation
    def recipe(self) :
        return f"the Ethiopian recipe is prepared using {self.ingredients} and is cooked using {self.cookingMethod} and has {self.nutritionalInformation} "   
class NigerianRecipe:
    def __init__(self,ingredients,preparationTime,cookingMethod,nutritionalInformation) :
        self.ingredients=ingredients
        self.prepationTime=preparationTime
        self.cookingMethod=cookingMethod
        self.nutritionalInformation=nutritionalInformation
    def recipe(self) :
        return f"the Ethiopian recipe is prepared using {self.ingredients} and is cooked using {self.cookingMethod} and has {self.nutritionalInformation} "   

# recipe1=MoroccanRecipe("wheat","30 minutes","oven","carbs")
# print(recipe1.recipe())
# recipe2=EthiopianRecipe("maize","1 hour","boling","calcium")
# print(recipe2.recipe())
# recipe3=NigerianRecipe("bean","20 minutes","heat","calcium")
# print(recipe3.recipe())


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0


    def passed(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60
    
student1=Student("rita",20,[50,50,60,50])  
# print(student1.average_grade()) 
# student2=Student("rita",20,[50,50,50,50])  
# print(student2.average_grade())
# student3=Student("rita",20,[50,50,50,50])  
# print(student3.average_grade()) 

class Book:
    def __init__(self,title,author,book) :
        self.title=title
        self.book=book
        self.author=author
        
        
class Catalog:
  def __init__(self):
      self.books=[]
  def addBook(self,title,author,book):
      book=Book(title,author,book)
      self.books.append(Book) 
  def search(self,title):
      for x in self.books:
          if x.title==title:
            return x
          else:
              return "not found"
  def Authour(self,author):
      for x in self.books:
          if x.author==author:
              return x
          else:
              return "not found"
  def details(self):
      print(f"the {self.books} by {self.Authour} was published in 2020")
            
 
# book1=Book("Born A crime","trevor","born")
# book2=Catalog()
# # book2.addBook('born a crime', 'trevor noah')
# # book2.search("born a crime","trevor noah")
# book2.details()
# book2.Authour("Anne")
# print(book2.details()
# )

class Story:
    def __init__(self,Story,morallesson,length):
        self.story=Story
        self.morallesson=morallesson
        self.length=length
    def  story_name(self):
     return f"{self.story} of morallesson {self.morallesson} is {self.length} long"
#    // question1.The story telling requires art in which different stories are inherrited to different people.We shall have three classes which are stories,that will hold the properties for stories(moral lesson,age group and the length).The second class is f Storyteller which shall inherit properties from story but shall have a different attribute called language and it shall return the name of the storyteller.Lastly we have class Translate which shall also inherit from story and returns a statement to translate from one language to another 
class Storyteller (Story) :
   def __init__(self, Story, morallesson, length,person):
      super().__init__(Story, morallesson, length)  
      self.person=person
   def teller_ofstory(self):
         return f"{self.story} with {self.morallesson}, has {self.length} and was told by{self.person}"
class Translate(Story):
   def __init__(self, Story, morallesson, length,language):
      super().__init__(Story, morallesson, length)
      self.language=language

def change_language(self):
            #  language="English"
            if self.language=="English":
                return f"translate to English"
            else:
                return f"language remains as it is"
# story1=Story("GredyHyena","shairing","40minutes")   
# print(story1.story_name())  
# story2=Storyteller("GredyHyena","shairing","40minutes","John") 
# print(story2.teller_ofstory())

class Recipee:
   def __init__(self,ingredients,preparatipontime,cookingmethod,nutritionalinfo):
        self.ingredients=ingredients
        self.preparatipontime=preparatipontime
        self.cookingmethod=cookingmethod
        self.nutritionalinfo=nutritionalinfo
class   MorocanRecipee(Recipee):
    def morocan_food(self):
       return f"{self.ingredients} are required with a time of{self.preparatipontime} and a method of {self.cookingmethod} and thie information is {self.nutritionalinfo},"
class   EthiopianRecipee(Recipee):
     def ethipian_food(self):
       return f"{self.ingredients} are required with a time of{self.preparatipontime} and a method of {self.cookingmethod} and thie information is {self.nutritionalinfo},"
class    NigerianRecipee (Recipee):
     def nigearin_food(self):
       return f"{self.ingredients} are required with a time of{self.preparatipontime} and a method of {self.cookingmethod} and thie information is {self.nutritionalinfo},"
     
food1=EthiopianRecipe("salt","20 minutes","frying","vitamins")   
# print(food1.ethipian_food())

from typing import Any


class Species:
    def __init__(self,diet,lifespan): 
          self.diet=diet
          self.lifespan=lifespan
        
    def migrationPatterns(self):
       print (f"This{self.__class__.__name__} eats {self.diet} and has a life span of{self.lifespan} and {self.migrate}")

class Preditor(Species):
 migrate="Migrates according to the pattern of the prey"

class Prey(Species):
 migrate="Migrates according to season"

prey1=Prey("grass","10 years")
# print(prey1.migrationPatterns())
class Library:
   def __init__(self):
      
      self.books={}
      

   def add_book(self):
      book=input("Enter bookname:")
      author=input(":Enter author:")
      self.books[book]=author
   
   def details(self):
      if self.books:
         for book,author in self.books.items():
            print(f"Book:{book}  Author:{author}")
         else:("No book in the library")

# library=Library()
# print(library.add_book())
# (library.details( ))
# print(books)

class Species:
     def __init__(self, diet, lifespan, migration_patterns):
        self.diet = diet
        self.lifespan = lifespan
        self.migration_patterns = migration_patterns

class Predator(Species):
    def __init__(self, diet, lifespan, migration_patterns, hunting_method):
        super().__init__(diet, lifespan, migration_patterns)
        self.hunting_method = hunting_method

class Prey(Species):
    def __init__(self, diet, lifespan, migration_patterns, hiding_behavior):
        super().__init__(diet, lifespan, migration_patterns)
        self.hiding_behavior = hiding_behavior


        
lion = Predator("Carnivore", 12, "Seasonal", "Ambush hunting")
gazelle = Prey("Herbivore", 8, "Seasonal", "Group hiding")

# print(lion.diet) 
# print(gazelle.lifespan) 
# print(lion.hunting_method)  
# print(gazelle.hiding_behavior)  

class Artist:
    def __init__(self, name, country, musical_style, instruments):
        self.name = name
        self.country = country
        self.musical_style = musical_style
        self.instruments = instruments

class Performance:
    def __init__(self, artist, start_time, end_time):
        self.artist = artist
        self.start_time = start_time
        self.end_time = end_time

class Stage:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.performances = []

        
artist1 = Artist("Wakadinali", "Kenya", "Gengetone", ["Drums", "Guitar"])
performance1 = Performance(artist1, "19:00", "21:00")
stage1 = Stage("Main Stage", 1000)
stage1.performances.append(performance1)


# print(artist1.country)  
# print(performance1.start_time) 
# print(stage1.capacity) 
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):
        total_grades = sum(self.grades)
        return total_grades / len(self.grades)

    def display_student_info(self): 
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def determine_passing_status(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60

student1 = Student("Mitch Odede", 18, [20, 15, 90])
student2 = Student("Nova Noel", 20, [70, 65, 55])

# print("Student 1 Information:")
# student1.display_student_info()
# print("Average Grade:", student1.calculate_average_grade())
# print("Passing Status:", student1.determine_passing_status())

# print("Student 2 Information:")
# student2.display_student_info()
# print("Average Grade:", student1.calculate_average_grade())
# print("Passing Status:", student1.determine_passing_status())

class Recipe:
    def __init__(self, food, ingredients, prep_time, cooking_method, nutritional_info):
        self.food = food
        self.ingredients = ingredients
        self.preparation_time = prep_time
        self.cooking_method = cooking_method
        self.nutritional_info = nutritional_info

    def display_recipe(self):
        print(f"Recipe: " + self.food)
        print("Ingredients: " + self.ingredients)
        print("Preparation Time: " + self.preparation_time)
        print("Cooking Method: " + self.cooking_method)
        print("Nutritional Information: " + self.nutritional_info)


class KenyanRecipe(Recipe):
    def __init__(self, food, ingredients, preparation_time, cooking_method, nutritional_info,serving_method, optional_ingredients ):
        super().__init__(food, ingredients, preparation_time, cooking_method, nutritional_info)
        self.serving_method = serving_method
        self.optional_ingredients = optional_ingredients

    def display_recipe(self):
        super().display_recipe()
        print(f"Serving method:{self.serving_method}")
        print(f"Optional ingredients are: {self.optional_ingredients}")
       


# kenyan_Recipe1 = KenyanRecipe("Ugali", "Water, Wheat flour", "45 minutes", "Low heat", "Rich in carbs", "Hot", "Blueband")
# print(kenyan_Recipe1.display_recipe())

class Ancestral:
    def __init__(self,story,storyteller,translator):
        self.story=story
        self.translator=translator
        self.storyteller=storyteller
    def story_roles(self):
        return f"{self.story} is told by {self.storyteller} and has to be translated by {self.translator}"
    
class Storytype(Ancestral):
    def __init__(self, story, storyteller, translator,length,moral_lesson,age_group):
        super().__init__(story, translator, storyteller)
        self.length=length
        self.moral_lesson=moral_lesson
        self.age_group=age_group
    def type_story(self):
        if(self.length >=100 and self.age_group >=10 and self.moral_lesson=="mature"):
            return f"{self.story} that has {self.length}  pages and teaches {self.moral_lesson} belongs to children who are {self.age_group}"
        else:
            return f"{self.story} that has {self.length} pages and teaches {self.moral_lesson} belongs to children who are above {self.age_group}"
        
ancestral=Ancestral("animation","Mother","Mary")
storytype=Storytype("animation","Mary","Joseph",50,"childish",5)
print(storytype.type_story())
   





    
  

