import re

char_list1 = ["a-z"]
char_list2 = ["A-Z"]
char_list3 = ["0-9"]
password = input("Enter password:")

print(len(password))

if len(password)<6 or len(password)>16:
    print("\nInvalid length, min length 6 characters max 16.")
else:
    regex = re.compile('[@_!"#$%^&\'*+,-.()<=@>?/\|}{~:;^_`]') 
    if(regex.search(password) == None):
        print("\nNo special characters, password invalid.")
    else: 
        if (characters in char_list1 for characters in password) and (characters in char_list2 for characters in password) and (characters in char_list3 for characters in password):
            print("\nValid password created successfully.")
        else:
            print("\nInvalid password.")
#matched_list = [characters in char_list for characters in password]

#password_contains_chars = all(matched_list)

#print(password_contains_chars)
