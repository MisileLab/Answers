import string

list1 = list(string.ascii_lowercase)
list2 = list(string.ascii_uppercase)

string = input()
string2 = ""

for i in string:
    try:
        string2 = string2 + list2[list1.index(i)]
    except ValueError:
        string2 = string2 + list1[list2.index(i)]

print(string2)