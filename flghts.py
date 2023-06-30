#Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.   
#input- destination and date
#output - available flights based on input
         #reserver seat for customer
        #manage passenger information
      # generate booking 
#process - create a dictionary holding the total destinations together with their data, and capacity with 3 as maximum
#create a function that checks for available flights when taking in destination and date and returns an available date
#Reserving seat function takes from available flgihts- shows a list of the available list to the user, using an input function the user is able to chose the right seat for them
#booking - now update dictionary and return the right statement in the passenger information
from datetime import datetime
flights = {"flight1":{"destination":"Lamu",'date': datetime(year=2023,month=7,day= 9,hour = 4,minute = 33,second = 6),"capacity":2},"flight2":{"destination":"Mombasa",'date': datetime(year=2023,month=7,day= 19,hour = 3,minute = 12,second = 16),"capacity":0}}
def available_flight(destination,date):
    flights_=flights.values()
    for flight in flights_:
        if flight['destination'] == destination and flight['capacity'] < 3 and date == flight['date']:
            return f"Your flight is available on {date} to {destination}"
        else:
            return "Sorry no flights are available"
print(available_flight('Lamu',datetime(year=2023,month=7,day= 9,hour = 4,minute = 33,second = 6)))
#use string formating to make it readable



 