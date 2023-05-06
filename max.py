# from mosh import find_max
# nums = [4,1,6,3,8,5,7] 
# max = find_max(nums)
# print(max)

# class Person:
#     def __init__(self,name_1,name_2):
#         self.name_1 = name_1
#         self.name_2 = name_2
#     def name1(self):
#         print("Fadahunsi Paul")


# name = Person("Ayodele","Dafahunsi")
# print(name.name_1)
# print(name.name_2)
# name.name1()
# name = Person()
# name.name1()

# Importing Random
# import random

# for i in range(3):
#     print(random.random())

# To specify range
# import random

# for i in range(3):
#     print(random.randint(10, 20))

# import random

# names = ['Dafa', 'Fada', 'Paul','Hunsi']
# name = random.choice(names)
# print(name)

# import random

# class Dice:
#     def roll(self):
#         num_1 = random.randint(1,6)
#         num_2 = random.randint(1,6)
#         return num_1,num_2
    
# num = Dice()
# print(num.roll())

# from pathlib import Path
# path = Path() 
# for file in path.glob('*'):
#     print(file)

# greetings_ds = [
#     {"user":["What's up","Hi", "Hello"]},
#     {"response":["Yeah man", "Mandem",  "Broski"]}
# ]

# fav = [
#     {"user":["Who are You?", "What is Your name?","Tell Me Your name"]},
#     {"response":["alright,I'm Paul.An Ai bot", "I am called Paul","My Name is Paul"]}
# ]

# import random

# def give(user_in):
#     if user_in in greetings_ds[0]["user"]:
#         ans_index = random.randint(0, len(greetings_ds[1]["response"])-1)
#         print("AI: ", greetings_ds[1]["response"][ans_index])
#         return None
#     elif user_in in fav[0]["user"]:
#         ans_index = random.randint(0, len(fav[1]["response"])-1)
#         print("AI: ", fav[1]["response"][ans_index])
#         return None
    
# while True:
#     user = input("Paul: ")
#     give(user)