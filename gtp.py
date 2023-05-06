# print("Which Operation Do You want to Perform?")
# print("===============================================")
# print("Addition")
# print("Subtraction")
# print("Division")
# print("Multiplication")
# print("===============================================")

# num_1 = input("Enter First number: ")
# num_2 = input("Enter Second number: ")
# oper = input("Which Operation?")

# if oper == "Addition":
#     print("Total = "+ str(int(num_1)+int(num_2)))

# elif oper == "Subtraction":
#     print("Total = "+ str(int(num_1)-int(num_2)))

# elif oper == "Division":
#     print("Total = "+ str(int(num_1)/int(num_2)))

# elif oper == "Multiplication":
#     print("Total = "+ str(int(num_1)*int(num_2)))


# items = [
#     {"item1":["Milo"]},
#     {"price":"$20"}    
# ]
# def mall(buy):
#     for buy in items[0]["item1"]:
#         print("AI: ",items[1]["price"])

# while True:
#     select = input("Select Item You Want: ")
#     mall(select)

# Drinks = [
#     {"item1":["coke","malt","milk"]},
#     {"price":["Drink and fire"]}
# ]

# train = [
#     {"item":[]},
#     {"price":[]}
# ]

# def selection(select):
#     if select in Drinks[0]["item1"]:
#         index = (0, len(Drinks[1]["price"])-1)
#         print("AI: ",Drinks[1]["price"][index])
#         return None
    
#     ques = input("Train me: ")
#     ans = input("Train me: ")
#     train[0]["item"].append(ques)
#     train[0]["price"].append(ans)


# while True:
#     buy = input("Enter an item: ")
#     selection(buy)

# students = [
#     {"question":["students and their place of birth"]}
# ]

train = [
    {"item":[]},
    {"price":[]}
]

item_db = [
    {"items":["Milo"]},
    {"prices":15},
    {"items":["Milk"]},
    {"prices":12},
    {"items":["Nido"]},
    {"prices":10}
]
# names = [
#     {"name":"NAMES ===========================================", "town":"TOWNS"},
#     {"name":"Fadahunsi Paul----------------------------------","town":"Kokoben"},
#     {"name":"Frederick Boat----------------------------------","town":"Boadi"}
# ]

def selection(select):
    if select in item_db[0]["items"]:
        print("AI: ", item_db[1]["prices"])
        return None

    elif select in item_db[2]["items"]:
        print("AI: ", item_db[3]["prices"])
        return None
    
    elif select in item_db[4]["items"]:
        print("AI: ", item_db[5]["prices"])
        return None

    elif select in train[0]["item"]:
        print("AI: ", train[1]["price"])
        return None
    
    ques = input("Add me: ")
    ans = input("Add Ans: ")
    train[0]["item"].append(ques)
    train[1]["price"].append(ans)

while True:
    ask = input("Ask a question: ")
    selection(ask)