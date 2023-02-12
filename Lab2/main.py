# num = int(input("Enter a Number:"))

# if num > 0:
#     root = num**(1/2)
#     print("The root of "+str(num)+" is "+str(int(root)))
# else:
#     print("The number should be greater than 0")

# num = int(input('number:'))
# if num == 1:
#     num = 0
# if num == 0:
#     num = 1
# if num > 1 or num < 0:
#     print("Number in between")

# num = int(input("Enter a number between 10-20 or 30-40->"))
# if (num >= 10 and num <= 20) or (num >= 30 and num <= 40):
#     print("The condition has been met")
# else:
#     print("you did it wrong")

# i = 100
# while(i > 0):
#     print("Karachi, Pakistan")
#     i -= 1

# count = int(input("how many numbers you want?"))
# p_count = 0
# n_count = 0
# i = 0
# while(i<count):
#     num = int(input("Enter num:"))
#     if num >= 0:
#         p_count+=1
#     else:
#         n_count+=1
#     i+=1
# print("Positive: "+str(p_count))
# print("Negative: "+str(n_count))

# value = 'i'
# user_char = input("guess character from a to e: ")
# while(user_char != value):
#     user_char = input("Try again: ")
# print('Congratulations you guessed it')

# cube_height = int(input("height:"))
# cube_width = int(input('width:'))
# cube_depth = int(input('depth:'))
# cube_volume = cube_depth*cube_height*cube_width
# if cube_volume >= 1 and cube_volume <= 10:
#     print('Extra Small')
# elif cube_volume >= 11 and cube_volume <= 25:
#     print('Small')
# elif cube_volume >= 26 and cube_volume <= 75:
#     print('Medium')
# elif cube_volume >= 76 and cube_volume <= 100:
#     print('Large')
# elif cube_volume >= 101 and cube_volume <= 250:
#     print('Extra Large')
# elif cube_volume >= 251:
#     print('Extra-Extra Large')
# else:
#     print('Invalid size')

# time = float(input("Time taken in hours: "))
# if time>0 and time<=2:
#     print("Show me your work!")
# elif time>2 and time<=3:
#     print("Highly Efficient")
# elif time>3 and time<=4:
#     print("Improve Speed")
# elif time>4 and time<=5:
#     print("Training is required")
# elif time>5:
#     print("Plese leave the company!")
# else:
#     print("Invalid Hours")

# password = 'abc$123'
# username = input("username: ")
# userpassword = input("password: ")
# if password == userpassword.lower():
#     print("Welcome")
# else:
#     print("I don't know you!")

# countries = ['Canada', 'USA', 'Mexico', 'Austrailia']
# for country in countries:
#     print(country)

# for i in range(0,101):
#     print(i)

# multi_table = 8
# for i in range(1, 11):
#     print("8 * "+str(i)+" = "+str(8*i))

# i = 10
# while(i > 0):
#     print(i)
#     i-=1

# for i in range(1,11):
#     if i%2==0:
#         print(i)

# sum = 0
# for i in range(100, 201):
#     sum += i
# print("sum: "+str(sum))

# countries = ['Canada', 'USA', 'Mexico']
# i=0
# while(i<len(countries)):
#     print(countries[i])
#     i+=1