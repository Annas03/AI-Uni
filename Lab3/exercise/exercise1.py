# a Python program to square and cube every number in a given list of integers using Lambda.
square = lambda num: num**2
cube = lambda num: num**3
num = [2, 1, 3, 9]
for i in num:
    print("Sqaure of:",i,"is",square(i))
    print("cube of:",i,"is",cube(i))


# a Python program to find if a given string starts with a given character using Lambda.
string = "Annas"
isCharPresent = lambda char: char[0]=='A'
print(isCharPresent(string))

# a Python program to extract year, month, date and time using Lambda
import datetime
curr_time = datetime.datetime.now()
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(day(curr_time), month(curr_time), year(curr_time), t(curr_time))