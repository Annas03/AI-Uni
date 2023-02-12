## Write a Python program to swap 4 variables values

def swap_func():
    a = input("a:")
    b = input("b:")
    c = input("c:")
    d = input("d:")

    # swapping a and d values
    temp1 = d
    d = a
    a = temp1

    # swapping b and c values
    temp2 = b
    b = c
    c = temp2

    print("a:"+a+" b:"+b+" c:"+c+" d:"+d)

## Write a Python program to convert temperatures to and from celsius,Fahrenheit

def temp_convert():
    temp = input("Temperature: ")
    res = input('"C" to convert into Celcius or "F" to convert into Fahrenheit: ')
    if res.lower() == 'f':
        conv_temp = int(temp)*(9/5) + 32
        print("Temp: "+str("{:.1f}".format(conv_temp))+"°F")
    elif res.lower() == 'c':
        conv_temp = (int(temp) - 32) * 5/9
        print("Temp: "+ str("{:.1f}".format(conv_temp))+"°C")
    else:
        temp_convert()

## Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 

def num_strings(strings_list):
    count = 0
    for strings in strings_list:
        if len(strings) >=2 and strings[0] == strings[-1]:
            count+=1
    return count
# print(num_strings(['abc', 'xyz', 'aba', '1221']))

## Write a Python script to concatenate following dictionaries to create a new one

def concatenate_dicts():
    dic1 = {1:10, 2:20}
    dic2 = {3:30, 4:40}
    dic3 = {5:50, 6:60}
    return {**dic1, **dic2, **dic3}

## Write a list comprehension which, from a list, generates a lowercased version of each string that has length greater than five

def list_comp(string_list):
    res_list = []
    for string in string_list:
        if len(string) > 5:
            res_list.append(string.lower())
    return res_list

# print(list_comp(["Abcd", "ANNAS Baig"]))

## Write a Python program to print a specified list after removing the 0th, 4th and 5th elements

def filtered_list(given_list):
    if len(given_list) <= 5:
        return
    given_list.pop(5)
    given_list.pop(4)
    given_list.pop(0)
    print(given_list)

# filtered_list(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink'])


def isMatch(s, p):
    i = 0
    j = 0
    while(i < len(s) and j<len(p)):
        if s[i] == p[j]:
            i+=1
            j+=1
            continue
        else:
            if p[j] == '.':
                i+=1
                j+=1
                continue
            elif p[j] == '*':
                if s[i] == p[j-1] or p[j-1] == '.':
                    i+=1
                else:
                    j+=1
            else:
                return False
    if i!=len(s):
        return False
    return True

print(isMatch("aa", "a*"))