planets = [
    {"question":["Name the nine planets","What are the planets in the solar system?"]},
    {"answer":["Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto"]}
]

verb = [
    {"question":["What is a verb?","Define a verb","What is the meaning of a verb"]},
    {"answer":["A verb is a doing word or an action word.", "A verb simply means any action or thing we PERFORM or do"]},
    {"verb_example":["Examples of a verb"]},
    {"verb_answer":["Dancing, Walking, eating, Reading, Writing", "Praying, Weeding, Clapping,Typing, Sleeping;and any word which ends with ""ING"]}
]

noun =[
    {"question":["What is a noun?","What is the meaning of a noun?","Define a noun"]},
    {"answer":["A noun is a name of a Person an Animal,Place,Thing,Idea,Quality,etc","Any object or thing that has a name is a noun"]},
    {"quest":["Examples of noun"]}, 
    {"ansr":["Animals:Dog,Cat,Horse,Mouse,etc""Places:kumasi,Canada,USA,Accra,ect""Things:Ball,Chair,Table,Cup,Book"]}
] 

foods = [
    {"food_ques":["Ghanaian foods","Local Ghanaian foods","Foods from Ghana"]},
    {"food_ans":["Banku,Fufu,Ampesi","Waakye,Tuozaafi,Konkonte","RiceBall,Tubaani,Apapransa"]}
]

regions = [
    {"question":["Regions in Ghana and their Capital"]},
    {"que":["How many Countries are in Africa?"]},
    {"que_ans":"There are 58 Countries in Africa"},
]
reg = [ 
        {"Region":"REGIONS" "-----------------------------",   "Capital":"CAPITAL"},
        {"Region":"(1).GREATER ACCRA    REGION      ---",      "Capital":"ACCRA"},
        {"Region":"(2)ASHANTI           REGION      ---",      "Capital":"kUMASI"},
        {"Region":"(3)UPPER   WEST      REGION      ---",      "Capital":"WA"},
        {"Region":"(4)UPPER  EAST       REGION      ---",      "Capital":"BOLGATANGA"},
        {"Region":"(5)NORTH   EAST      REGION      ---",      "Capital":"NALERIGU"}, 
        {"Region":"(6)SAVANNAH          REGION      ---",      "Capital":"DAMANGO"},
        {"Region":"(7)NORTHERN          REGION      ---",      "Capital":"TAMALE"},
        {"Region":"(8)BONO-AHAFO        REGION      ---",      "Capital":"SUNYANI"},
        {"Region":"(9)EASTERN           REGION      ---",      "Capital":"KOFORIDUA"},
        {"Region":"(10)CENTRAL          REGION      ---",      "Capital":"CAPE-COAST"},
        {"Region":"(11)BONO-EAST        REGION      ---",      "Capital":"TECHIMAN"},
        {"Region":"(12)VOLTA            REGION      ---",      "Capital":"HO"},
        {"Region":"(13)WEWSTERN         REGION      ---",      "Capital":"SECINDI-TAKORADI"},
        {"Region":"(14)WESTERN-NORTH    REGION      ---",      "Capital":"SSEFWI WIAWSO"},
        {"Region":"(15)AHAFO            REGION      ---",      "Capital":"AHAFO-GOASO"},
        {"Region":"(16)OTI              REGION      ---",      "Capital":"DAMBAI"}
        
]


train = [
    {"user":[]},
    {"response":[]}
]


import random

def gtp(user_in):
    #funtion for 

    if user_in in foods[0]["food_ques"]:
        ans_index = random.randint(0,len(foods[1]["food_ans"])-1)
        print("AI: ",foods[1]["food_ans"][ans_index])
        return None

    elif user_in in noun[0]["question"]:
        ans_index = random.randint(0, len(noun[1]["answer"])-1) 
        print("AI: ", noun[1]["answer"][ans_index]) 
        return None
    
    elif user_in in noun[2]["quest"]:
        ans_index = (0, len(noun[3]["answer"]))
        print("AI: ",noun[3]["answer"])

    elif user_in in planets[0]["question"]:
        ans_index = random.randint(0, len(planets[1]["answer"])-1)
        print("AI: ", planets[1]["answer"][ans_index])
        return None 

    elif user_in in verb[0]["question"]:
        ans_index = random.randint(0, len(verb[1]["answer"])-1)
        print("AI: ", verb[1]["answer"][ans_index])
        return None
    
    elif user_in in train[0]["user"]:
        ans_index = random.randint(0, len(train[1]["response"])-1)
        print("AI: ", train[1]["response"][ans_index])
        return None

    elif user_in in regions[1]["que"]:
        ind = (0, len(regions[2]["que_ans"]))
        print("AI: ",regions[2]["que_ans"])
        return None
    
    elif user_in in regions[0]["question"]:
        for index, city in enumerate(reg):
            print(index+1, city["Region"],city["Capital"])
        return None

    #Adding undeclared Functions
    ques = input("Add Up - Question :") 
    reply = input("Add Up - Answer:")
    train[0]["user"].append(ques)
    train[1]["response"].append(reply)

    #Executing console
while True:
    question= input("Ask: ")
    gtp(question)