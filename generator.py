import argparse
import secrets



number_list = ['0','1','2','3','4','5','6','7','8','9']
letters_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase_letters_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_characters_list = ['!','@','#','$','%','^','&','*','','(',')','_','-','=','+','[',']','{','}',';',':','|',',','.','<','>','/','?']


password = ''

# init parse
parser = argparse.ArgumentParser(description='Generate a random password')

# arguments needed

# password length
parser.add_argument('password_length', type=int, help='The length of the password')

# wether to include numbers
parser.add_argument("-n",  action='store_const', const=True, dest='include_numbers', help="Include numbers")

# wether to include uppercase letters
parser.add_argument("-u",  action='store_const', const=True,  dest='include_uppercase_letters', help="Include uppercase letters")

# wether to include special characters
parser.add_argument("-s", action='store_const', const=True, dest='include_special_characters', help="Include special characters")

args = parser.parse_args()

for i in range(args.password_length):
    list_selector = secrets.randbelow(4)
    if list_selector < 1 and args.include_uppercase_letters:
        n = secrets.randbelow(len(uppercase_letters_list)-1)
        password += uppercase_letters_list[n]
    elif list_selector < 2 and args.include_special_characters:
        n = secrets.randbelow(len(special_characters_list)-1)
        password += special_characters_list[n]
    elif list_selector < 3 and args.include_numbers:
        n = secrets.randbelow(len(number_list)-1)
        password += number_list[n]
    else:
        n = secrets.randbelow(len(letters_list)-1)
        password += letters_list[n]

print(f'Your generated password is:\n\n{password}')