import random
import time

###############değişkenler###################
fruits = "Strawberry\n","Cherry\n","Grapes\n","Walnut\n"
vegetables = "Pepper\n","Bell Pepper\n","Bread\n","Basil\n","Carrot\n","Cabbage\n","Lemon\n","Mushroom\n","Parsley\n","Eggplant\n","Mint\n","Potato\n","Cheese\n","Garlic\n","Onion\n","Tomato\n","Cucumber\n","Ginger\n"
meats = "Fish\n","Beef\n","Mince\n","chicken meat\n"
boxed_bottled = "Milk\n","Pasta\n","Sunflower Oil\n","Olive Oil\n"
spices_powders = "Salt\n","Sugar\n","Flour\n","Black Pepper\n","Baking Powder\n","Cumin\n","Lentil\n","Rice\n","Chili Pepper\n","Butter\n"

All = fruits+vegetables+meats+boxed_bottled+spices_powders
##############################################

print ( """

   _____ _____  _        ____         ___  
  / ____|  __ \| |      |___ \       / _ \ 
 | |  __| |__) | |        __) |     | | | |
 | | |_ |  ___/| |       |__ <      | | | |
 | |__| | |    | |____   ___) |  _  | |_| |
  \_____|_|    |______| |____/  (_)  \___/                                                 
       
İngilizce Projem, sürüm 2.0 -sürüm (x86_x64)
Lisans GPLv3+ : GNU GPL sürüm 3 <https://www.gnu.org/licenses/gpl-3.0.html>
telif hakkı (C) 2022 BatuHanHub 

Bu ücretsiz bir yazılımdır; değiştirmekte ve yeniden dağıtmakta özgürsünüz.
Yasaların izin verdiği ölçüde HİÇBİR GARANTİ YOKTUR.\n""" )

print("******Welcome to English Market!******\n")

team1 = str(input("Enter the name of the 1st team:"))
team2 = str(input("Enter the name of the 2nd team:"))


while True:

    difficulty = str(input('''
                   
        Difficulty levels;
      
    #############################
    type "e/E" for easy mode   (5)
    type "n/N" for normal mode (8)
    type "h/H" for hard mode   (10)
    #############################
      
        >>>'''))
    
    if difficulty == ("e" or "E"):
        length = 5
    
    elif difficulty == ("n" or "N"):
        length = 8
    
    elif difficulty == ("h" or "H"):
        length = 12
    
    elif difficulty != ("e" , "E" , "n" , "N" , "h" , "H"):
        print('''Error: write your difficulty level
          
            Difficulty levels;
      
        #############################
        type "e/E" for easy mode   *
        type "n/N" for normal mode **
        type "h/H" for hard mode   ***
        #############################
      
            ''') 
        continue 
    
    List1 = "".join(random.sample(All,length))
    List2 = "".join(random.sample(All,length))

    print("\nList of", team1, "team\n#########################\n"+List1)
    print("\nList of", team2, "team\n#########################\n"+List2)

    break

Time = 3

while Time:
    minute  = Time // 60
    second = Time % 60
    timer = "{:02d}:{:02d}".format(minute , second)
    print(timer, end="\r")
    time.sleep(1)
    Time -= 1
    
    if Time == 0:
        print("""      
  _______ _                _                   
 |__   __(_)              ( )                  
    | |   _ _ __ ___   ___|/ ___   _   _ _ __  
    | |  | | '_ ` _ \ / _ \ / __| | | | | '_ \ 
    | |  | | | | | | |  __/ \__ \ | |_| | |_) |
    |_|  |_|_| |_| |_|\___| |___/  \__,_| .__/ 
                                        | |    
                                        |_|                                 
              """)
       
input("press a key to exit...")