import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','&',')','(','+']

print("Welcome to Random Password Generator")
ask_let=int(input("Enter how many letters you want: "))
ask_num=int(input("Enter how many numbers ypu want: "))
ask_sym=int(input("Enter how many symbols you want: "))

#easy level
#password=""
#for i in range(1,ask_let+1):
#    password=password+random.choice(letters)
#for i in range(1,ask_num+1):
#    password=password+random.choice(numbers)
#for i in range(1,ask_sym+1):
#    password=password+random.choice(symbols)
#print(password)


#hard level
password_list=[]
for i in range(1,ask_let+1):
    password_list.append(random.choice(letters))
for i in range(1,ask_num+1):
    password_list.append(random.choice(numbers))
for i in range(1,ask_sym+1):
    password_list.append(random.choice(symbols))


random.shuffle(password_list)
print(password_list)

password=""
for i in password_list:
    password+=i

print(f"Your new password is: {password}")