import random #library to implement the pets' likes and dislikes
import re #library for Regex

#if the pygame part of my assignment doesn't get implemented, this will be seen as a prototype for the actual game.
#Prototype maynot be completed itself.

#a oop class that represents the attributes of the virtual pet
class Animal:
    def __init__(self, type, name,age,likes,dislikes,hunger,happy):
        self.type = type
        self.name = name
        self.age = age
        self.likes = likes
        self.dislikes = dislikes
        self.hunger = hunger
        self.happy = happy
    
    def name(self, n):
        self._name = n
    
    def type(self,t):
        self._type = t
    
    def likes(self,l):
        self._type = l
    
    def dislikes(self,d):
        self._type = d
    
    def hunger(self,hu):
        self._type = hu
    
    def happy(self,ha):
        self._type = ha

#Implemetation of a file - player will haev to create a file beforehand
# Players data is stored in the file
gamestats = open("gamefile.txt","w")

#Regex that allows a name: That has only 12 characters,
#allows letters from A-Z both captial and lowercase, doesn't allow numbers on it's own e.g.
#"5000" is not allowed, but "MEGATRON5000" is.
#No special characters, such as "?!£$", is allowed
Aname = input("What's the name of your animal?: ").strip()
if re.search(r"^[a-zA-Z][^0-9]{0,11}$",Aname):
    print(Aname, "is your new pet.")
    #OOP setter method for 'name' attribute
    oopn = Animal("","","","","","","")#said I needed positional arguments for 'Animals()'
    oopn.name = Aname
else:
    print("That name isn't appropriate.")

#writes name of animal to the text file
gamestats.write(f"The name of the animal is {Aname}\n")

#Changes the colour of the background to chosen colour, mostly for the implementaion of pygame
print("Displays colours blue, green, pink, yellow and purple")
Colour = input("What colour would you like?: ").lower()
if Colour == "blue":
    print("blue background")
elif Colour == "green":
    print("green background")
elif Colour == "pink":
    print("pink background")
elif Colour == "yellow":
    print("yellow background")
elif Colour == "purple":
    print("purple background")
else:
    print("Not a colour.")
#writes down the background colour to the text file
gamestats.write(f"The background colour is {Colour}\n")    

#Player can choose which animal they can look after
print("Display animals cat, dog, snake, parrot, rabbit, turtle." )
Ani = input("Which animal would you like?: ").lower()
if Ani == "cat":
    print("You have chosen a cat.")
elif Ani == "dog":
    print("You have chosen a dog.")
elif Ani == "snake":
    print("You have chosen a snake.")
elif Ani == "parrot":
    print("You have chosen a parrot.")
elif Ani == "rabbit":
    print("You have chosen a rabbit.")
elif Ani == "turtle":
    print("You have chosen a turtle.")
else:
    print("Not an option.")
#writes the animal type to the text file

gamestats.write(f"The animal is a {Ani}\n")

#A function that implements the feature of the pets likes or dislikes using the random library
#Chooses a number between 1 and 3 and assigns the number to like, dislike or neutral.
def likeordis():
    rate = (random.randrange(1,3))
    if rate == 1:
        print("Your pet likes this food!")
    elif rate == 2:
        print("Your pet thinks the food is okay.")
    else:
        print("You pet dislikes this food")

food= input("Would you like to feed your pet?: (y/n)").lower()
fbar = 0 # implement as hunger when using oop
if fbar == 5:
    print(Aname, "is full.")
else:
    if food == "y" or food == "yes":
        print("You feed your pet")
        fbar += 1
        likeordis()
    else:
        print(Aname,"is looking at you expectantly")


game= input("Would you like to play with your pet?: (y/n)").lower()
pbar = 0 # implement as hunger when using oop
if pbar >= 5:
    print(Aname,"is tired.")
else:
    if game == "y" or game == "yes":
        print("You play with your pet")
        pbar += 1
    else:
        print(Aname,"is looking at you expectantly")


        
