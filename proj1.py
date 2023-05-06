user_db = []
item_collection = [] 
price_box = []
item_db = [
    {"name":"iPhone_12_pro:     ===",   "price":21_200},
    {"name":"Samsung_s20_ultra:  ===",   "price":20_000},
    {"name":"iPhone_14_pro_max: ===",   "price":25_000},
    {"name":"iPhone_13_pro_max: ===",   "price":22_000},
    {"name":"Tecno_Camon_19:    ===",   "price":19_000},
    {"name":"infinix_hot_15:    ===",   "price":2_700},
    {"name":"series_8:          ===",   "price":4_800} 
]


items = {
    "item1": "iphone_12_pro",
    "item2": "Samsung_s20_ultra",
    "item3": "iphone_14_pro_max",
    "item4": "iphone_13_pro_max",
    "item5": "Tecno_Camon_19", 
    "item6": "infinix_hot_15",
    "item7": "series_8",
}

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
    return  False

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
    if len(password) and len(username) < 5:
        print("Password Or Username shouldn't be Less Than 5 Characters")
        register()
    if create_user(fullname, username, password):
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
        print("Invalid username and password provided. Please register again")
        auth()

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

def item_box():
    buy = True 
    while buy == True:
        select = input(":").replace(':', '')
        buy = False if not select else True
        if buy:
            item_collection.append(item_db[int(select)-1])

    total_price = sum([item["price"] for item in item_collection]) 
    for item in item_collection:
        print(item["name"])
    print("TOTAL PRICE : GHc",total_price)


    print("========================")
    print("Cart :")
    print("----------")

    for collect in item_collection:
        print(collect["name"])
    print("========================")

    # print(f"Checkout(${total})")
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
    
    # print items
    for index, item in enumerate(item_db):
        print(index+1, item["name"], item["price"])

    print("================================")
    print("Select Items You Want") 
    print("================================")
    # select items
    item_box()
def app():
    auth()


# Running app
app() 