#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is:", today)

    # TODO: print out the date's individual components
    print("Date components:", today.day, today.month, today.year)
    
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday # is", today.weekday())

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("Today is", days[today.weekday()])
    
    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today1 = datetime.now()
    print("Today's date and time is", today1)
    
    # TODO: Get the current time
    print("The current time is", datetime.time(today1))

 

  
if __name__ == "__main__":
    main()
  