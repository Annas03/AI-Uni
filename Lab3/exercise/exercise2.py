# You have collected information about cities in your province. You decide to store each city’s name, population, and mayor in a file. Write a python program to accept the data for a number of cities from the keyboard and store the data in a file in the order in which they’re entered.

cityData = []
while(True):
    city = input("Enter city name:")
    population = input("Enter population:")
    mayor = input("Enter mayor name:")
    cityData.append({"city":city, "population":population, "mayor":mayor})
    more_data = input("Do you want more data to be added(Y=yes or N=no):")
    if(more_data == 'N' or more_data == 'n'):
        break

f = open("cityData.txt", "w")
f.write("City  Population  Mayor \n")
for i in range(len(cityData)):
    f.write(cityData[i]["city"]+" ")
    f.write(" "+cityData[i]["population"]+ " ")
    f.write(" "+cityData[i]["mayor"]+"  \n")
f.close()

# Write a python program to create a data file student.txt and append the message “Now we are AI students”s

f = open("student.txt", 'a')
f.write("Now we are AI students's \n")
f.close()