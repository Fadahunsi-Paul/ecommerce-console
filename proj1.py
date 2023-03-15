user_db = []
item_db = [
    {"name":"iPhone_12_pro:     ===",   "price":21_200},
    {"name":"Samsung_s20_ultra  ===",   "price":20_000},
    {"name":"iPhone_14_pro_max: ===",   "price":25_000},
    {"name":"iPhone_13_pro_max: ===",   "price":22_000},
    {"name":"Tecno_Camon_19:    ===",   "price":19_000},
    {"name":"infinix_hot_15:    ===",   "price":2_000},
    {"name":"series_8:          ===",   "price":1_800 }
]

# Query functions
def create_user(fullname, username, password):
    for user in user_db:
        if username == user["username"]:
            return False
    
    # Create the new user
    new_user = {"fullname":fullname, "username": username, "password":password}
    # Add the new user to the db
    user_db.append(new_user)
    return new_user

def get_user(username):
    for user in user_db:
        if user["username"] == username:
            return user 
    return False

def login_user(username, password):
    for user in user_db:
        if user["username"] == username and user["password"] == password:
            return user 
    return False

# Auth functions
def register():
    print("=====================================")
    print("Registration Page")
    print("=====================================")
    fullname = input("Fullname : ")
    username = input("Username : ")
    password = input("Password : ")
    # Create the user
    user = create_user(fullname, username, password)
    if user:
        login()
    else:
        print("Username not available")
        print("Try Again")
        register()

def login1():
    print("=====================================")
    print("Linking page")
    print("=====================================")
    username = input("Username : ")
    password = input("Password : ")
    user = login_user(username, password)
    if user:
        main_page()
    else:
        print("Invalid username and password provided. Please try again")
        register()

def login():
    print("=====================================")
    print("Login Page")
    username = input("Username : ")
    password = input("Password : ")
    print("=====================================")
    user = login_user(username, password)
    if user:
        main_page()
    # elif user:
    #     print("Invalid username and password provided. Please try again")
    #     login()
    else:
        login()

def slection_page():
    item_selection = print("Select items you want to buy \n")
    item_total = 0
    iphone_12_pro = input("iphone_12_pro:     ")
    if iphone_12_pro == "select":
        item_total += 21_200

    Samsung_s20_ultra = input("Samsung_s20_ultra:  ")
    if Samsung_s20_ultra == "select":
        item_total += 20_000

    iphone_14_pro_max = input("iphone_14_pro_max:  ")
    if iphone_14_pro_max == "select":
        item_total += 25_000

    iphone_13_pro_max = input("iphone_13_pro_max:  ")
    if iphone_13_pro_max == "select":
        item_total += 22_000

    Tecno_Camon_19 = input("Tecno_Camon_19:     ")
    if Tecno_Camon_19 == "select":
        item_total += 19_000

    infinix_hot_15 = input("infinix_hot_15:     ")
    if infinix_hot_15 == "select":
        item_total += 2_000

    series_8 = input("Series_8:           ")
    if series_8 == "select":
        item_total += 1_800
        print(
            " "
        )
    print("======================")
    print(f"Checkout(${item_total})")
    print("======================")
    decision = input("If You Want To Checkout Press 'Pay' or 'Dont Pay' To exit \n")
    if decision == "Pay".lower():
        print(f"Total Payment = (${item_total})")
    else:
        main_page()


def auth():
    print(" "
    
         " ")
    print("Hello You are Welcome to Dafa Phones And Accessories")
    print("""
    1. Register 2. Login
    """)
    user_input = input("Response: ")
    if user_input == "1":
        register()
    elif user_input =="2":
        login1()
    else:
        print("Wrong input")

# Main page
def main_page():
    count = 1
    for item in item_db:
        print(count, item['name'],item['price'])
        count = count +1
    print("================================")
    print("Selection Page")
    print("================================")
    slection_page()


def app():
    auth()




# Running app
app()