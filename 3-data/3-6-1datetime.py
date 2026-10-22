import datetime
# you have to call everything as datetime.datetime or datetime.date or datetime.timedelta
# the first datetime is the package, the second is the module
#from datetime import datetime, date, timedelta
# then you can just call datetime(), date(), timedelta() without the prefix

# datetime module is in the python standard library


# they are equal, but python does not know that

# today's date
today = datetime.date.today()

# add 30 days to today
today_plus_30 = today + datetime.timedelta(days=30)

# print the dates
print("Today's date:", today)
print("Today's date plus 30 days:", today_plus_30)

# date -> string is called formating a string 
# string -> date is called parsing 

strftime_format = "%B %d, %Y"  # April 08, 2007
strptime_format = "%Y-%m-%d"  # 2007-04-08

date_string = datetime.datetime.strftime(today, "%A, %B %w, %Y")
print("Today's date in string:", date_string)

mybirthday = "Apr 8, 2007"
mybirthday2 = "2007-04-08"

mybirthday3 = datetime.datetime.strptime(mybirthday, "%b %d, %Y")
born_on = datetime.datetime.strftime(mybirthday3,"%A")
print("I was born on a", born_on)
