from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

    #create class MyBook
    #add extra attrubute price
    #create function display
    #using multiline strings and formatting print it rightly
class MyBook(Book):
    def __init(self,title,author,price):
        self.price = price
        super().__init__(title,author)
    def display(self):
        return f'''Title: {self.title}
                   Author: {self.author}
                   Price: {self.price}
                 '''
      #we are to display a readable way for the user
      
#Write MyBook class

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()