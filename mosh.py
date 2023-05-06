# print("Hello World")
# price = 10
# print (price)

# name = "John Smith"
# age = 20
# new_patient = True

# print(name,age,new_patient)

# mul = 2**2
# print(mul)
# he = 'Hello :'.title()
# print("M" in he)

# import math
# print(math.log(8))

# is_cold = False
# is_hot = True
# if is_cold:
#     print("It's a cold Day \n Don't Forget To wear Warm clothes")
# elif is_hot:
#     print("It's a Hot Day \n Drink plenty water")
# else:
#     print("It's a Lovely Day")
# print("Happy Day")

#good_credit = True
#high_income = False
#criminal_record = True
#if good_credit or high_income:
#    print("Eligible For Loan")
#if good_credit and not criminal_record:
#    print("Eligible")
#else:
#    print("not Eligible")

# temp = int(input("Enter Temperature"))
# if temp >= 30:
#     print("It's a hot Day")
# elif temp <=10:
#     print("It's a cold Day")
# else:
#     print("it's Neither hot nor cold")
# name = "Fadahunsi Paul"
# if len(name) < 3:
#     print("name can be at least three Characters Long")
# elif len(name) > 50:
#     print("Name Can be a maximum of 50 Characters")
# else:
#     print("Name looks good") 

# weight = int(input("Weight :"))
# unit = input("(L)bs Or (K)g ?").upper()

# if unit == 'L':  
#     converted = weight*0.45
#     print(f"Your weight in Lbs is{converted}")
# else:
#     converted = weight / 0.45
#     print(f"Your weight in Kg is {converted}")
# else:
#     print("Invalid")

#While loops
# number = 2

# while number <= 10:
#     print("#" * number)
#     number+=1
# print("Nice")

#Guessing Game
# guess_count = 0
# guess_num = 9
# num_of_guesses = 3
# while guess_count < num_of_guesses:
#     guess_count += 1
#     guess = int(input("Guess :"))
#     if guess == guess_num:
#         print("You won")
#         break
# else:
#     print("Out Of guesses")


# hello = ""
# started = False

# while True:
#     hello = input("> ").lower()
#     if hello == "start":
#         if started:
#             print("car Already started")
#         else:
#             started =True
#             print("car Started")
#     elif hello == "stop":
#         if not started:
#             print("Car is Already stopped")
#         else:
#             started = False
#             print("Car stopped")
#     if hello == 'help':
#         print("""
# Start - to start car
# stop - to stop car
# quit - to quit
#         """)
#     elif hello == "quit":
#             break
# else:
#     print("I don't understand That")


# prices = [10, 20 ,30]
# total = 0
# for price in prices:
#     total += price
# print(total)
    
# numbers = [5, 2, 5, 2, 2]
# for number in numbers:
#     print("x"* numbers[0])
#     break
# for numb in numbers:
#     print("x"* numbers[1])
#     break
# for numbe in numbers:
#     print("x"* numbers[2])
#     break
# for num in numbers:
#     print("x"* numbers[3])
#     break
# for numer in numbers:
#     print("x"* numbers[4])
#     break

# for nums in numbers:
#     result = ''
#     for number in range(nums):
#         result += "x"
#     print(result)
# numbers = [2, 2, 2, 2, 2, 6, 6]
# for nums in numbers:
#     results = ' '
#     for numbers in range(nums):
#         results += "x"
#     print(results)
    
# hi = ['jim', 'jey', 'jer']
# print(hi[0].replace('j','k'))

# numbers = [95, 99, 15, 20]
# max = numbers[0]
# for num in numbers:
#     if max < num:
#         max = num
# print(max) 

# my_list = [
#     [1, 4, 5],
#     [6, 7, 9],
#     [2, 3, 1]
# ]
# total = 0
# # my_list[2][2] = 16
# # print(my_list[2][2])
# for my in my_list:
#     for list in my:
#         total+= list
# print(total)
        
# number = [1, 2, 7, 8, 7, 9, 2]
# num_2 = []
# for num in number:
#     if num not in num_2:
#         num_2.append(num)
# print(num_2)
# names = ["Paul", "Dafa", "Fada", "Hunsi"]
# name1,name2,name3,name4 = names
# print(name2)

# phone = int(input('Phone :'))
# my_dict = {
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four",
#     "5":"Five"
# }
# container = ""
# for dict in my_dict:
#     container += my_dict.get(dict, "!") + " "
# print(container)

#Def Function
# def my_func(name, name_2,Name_3):
#     print(f"Hi {name} {name_2} {Name_3}")

# print("Hello Dear")
# my_func("Fadahunsi",Name_3="Paul", name_2="Ayodele")
# print("How're You Doing")

# try:
#     age = int(input("Age :"))
#     print(age) 
#     income = 30_000
#     risk = income / age
# except ZeroDivisionError:
#     print("Invalid age Input")
# except ValueError:
#     print("Invalid value")
# def me(bro):
#     print(bro*bro)
# me(4)

# numbers = [1, 4, 3]
# numbers.count()
# print(numbers)

# class Name:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print('MY name is Fadahunsi Paul \nI am 20 years old')
#     def draw(self):
#         print("Today is my Mom's Birthday \nShe's 60 Years Today")

# Name1=Name(50,30)
# Name1.x = 50 
# Name1.y = 30
# print(Name1.x,Name1.y)  

# class  Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Talk")

# Paul = Person()
# Paul.talk()
# name1 = Person("Fadahunsi Paul")
# print(name1.name)
# name1.talk()

# MUltiple Classes

class names:
    def name(self):
        print("Fadahunsi")
class paul(names):
    def daf(self):
        print("Is a Human Baing")
class dafa(names):
    def fad(self):
        print("Is a Boy")

paul1 = paul()
paul1.name()
# paul1.daf()
# dafa1 = dafa()
# dafa1.name()
# dafa1.fad() 

# dafa1 = dafa()
# dafa1.name()
# dafa1.fad() 

class Person:
    def __init__(self, name,name_2):
        self.name = name
        self.name_2 = name_2
    def talk(self):
        print("Talk")
     

name1 = Person("Fadahunsi Paul","Ayodele")
print(name1.name)
print(name1.name_2)
name1.talk() 

#Multiple Class using Pass

# class Person:
#     def name(self):
#         print("dafa")
# class Side(Person):
#     pass
# class men(Person):
#     pass

# side1 = Side()
# side1.name()
# man = men()
# man.name()

def find_max(nums):
    max = nums[0]
    for num in nums:
        if max < num:
            max = num
    return max

