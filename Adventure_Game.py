import random
import time

def rules(): 
    print()
    print("-------------------------------------")
    print("RULES:")
    print("1. You are a detective uncovering a murder.")
    print("2. Explore the mansion and find clues in order.")
    print("3. You'll face puzzles and discover secrets.")
    print("4. After discovering the back exit in the dining room, you can choose to quit early.")
    print("5. Use input carefully and remember what you read.")
    print("-------------------------------------")
    
def introduction(): 
    print("-------------------------------------")
    print("### Welcome to the Adventure Game! ###")
    print("-------------------------------------")
    print("Here are the required information and rules:")
    print("-------------------------------------")
    print("You are the detective who is trying to uncover")
    print("the hidden truth about a murder. The truth lies")
    print("in this mansion and your goal is to find it by")
    print("exploring different places, obtaining tools, and")
    print("working hard. Good luck to you adventurer!!")
    print("-------------------------------------")
    rules()
    print()
    print("-------------------------------------")
    print("And the adventure starts:")
    print()
    print("You are at the entrance of the mansion.")
    print("You are observing the mansion from outside and")
    print("it has a front door to the east. What will you do?")
    print("You know that you have no option but to enter.")

def areas_to_cover():
    print("Areas in the mansion:")
    print(", ".join(room_tracker.keys()))

def foyer(): 
    print()
    print("-------------------------------------")
    
    current_room = "foyer"
    room_tracker[current_room] += 1

    if room_tracker[current_room] == 1:
        print("You are in the foyer now (the small hallway of entrance).")
        print("You see that there is one more door in front of you.")
        print("When you go through that door as well, you see that") 
        print("it leads to the library.")
    else:
        print("You are in the foyer again.")

    validity = False
    while not validity:
        action = input("Where do you want to go? (option: library): ").lower()
        if action == "library":
            library()
            validity = True
        else:
            print("Invalid input, please enter again.")
    
def library(): 
    current_room = "library"
    room_tracker[current_room] += 1

    if room_tracker[current_room] == 1:
        print()
        print("-------------------------------------")
        print("You are in the dusty, old library now...")
        print("Everywhere is filled with cobwebs. You observe the place.")
        print("Now, there are 2 bookshelves (bs1, bs2) in the north and south")
        print("and 2 new doors in north and east each leading")
        print("to yet unknown places.")
    else:
        print("You are back to library.")

    
    print()
    print("(Hint: Start from inside of the library.)")
    while True:
        print("\nWhere would you like to go?")
        if found_key:
            print("Options: bs1, bs2, north, east, south, west (foyer)")
        else:
            print("Options: bs1, bs2, north, east, west (foyer)")
            print("South wall looks really empty.")

        decision = input("Enter your choice: ").lower().strip()

        if decision == "bs1":
            bs1()
        elif decision == "bs2":
            bs2()
        elif decision == "north":
            storage1()
        elif decision == "east":
            dining_room()
        elif decision == "west":
            foyer()
        elif decision == "south":
            if found_key:
                secret_passage()
            else:
                print("You inspect the south wall again, but can't find a way through.")
        else:
            print("Invalid input. Try again.")
                             
def bs1(): 
    current_room = "bs1"
    room_tracker[current_room] += 1

    if room_tracker[current_room] == 1:
        print()
        print("-------------------------------------")
        print("You are now observing the bookshelf in the north.")
        print("At first glance, you cannot see anything different, but;")
        print("when you decide look more carefully, you see a scraped ")
        print("message that says 'the thing that I ALWAYS forget is in")
        print("the north' looks like this is reminder of the late ")
        print("homeowner to themself. Then you decide to observe the other bookshelf as well.")
        
        for i in range(12):
            print(".", end= " ")
            time.sleep(1)
    else:
        print("Your other clue probably lies in second bookshelf. Going to second bookshelf.")
        for i in range(3):
            print(".", end= " ")
            time.sleep(1)

    bs2()

def bs2(): 
    current_room = "bs2"
    room_tracker[current_room] += 1

    if room_tracker[current_room] == 1:
        print()
        print("-------------------------------------")
        print("You think to yourself 'this bookshelf looks so strange' as")
        print("there are piles of books scattered and looks like they tried")
        print("hide something. When you search what is underneath you find a")
        print("hidden locked drawer. Then you connect the clues that you found")
        print("in two bookshelves and say 'Our next destination is north.' ...")
        
        for i in range(15):
            print(".", end= " ")
            time.sleep(1)

    else:
        print("You are at the second bookshelf again.")
        if found_key == False:
            print("Your only clue is storage 1, going to storage 1.")

            for i in range(4):
                print(".", end= " ")
                time.sleep(1)
    
            storage1()
    
        else:
            print("You are back to the second bookshelf, and you look at the")
            print("key's shape and realize it fits to the lock. So, you try it out.")
            print("Nice work! The drawer is now open. And there is only one note which")
            print("says 'Message lies in the walls of dining room.' clearly everything")
            print("is designed to keep their belonging safe...")
            print("You decide to try the door in east, which you believe to be the dining.")
            for i in range(14):
                print(".", end= " ")
                time.sleep(1)
            dining_room()       

def storage1(): 
    current_room = "storage1"
    room_tracker[current_room] += 1
    
    if room_tracker[current_room] == 1:
        global found_key
        print()
        print("-------------------------------------")
        print("You realize there is a number '1' indicated on the top of the door.")
        print("When you open the screaky old door you realize it is actually a")
        print("storage. It is covered with more cobwebs and dirt than the library.")
        print("You wonder what the late homeowner always forgets and makes a note.")
        print("You take a look around, but; cannot seem to find anything.")
        
        for i in range(13):
            print(".", end = " ")
            time.sleep(1)

        continuing = True
        while continuing:
            choice = input("Would you like to search more thoroughly? (yes/no): ").lower()
            if choice == "yes":
                print("AHA! That's what was needed. A KEY! You think this is probably for the drawer.")
                print("Therefore, you go back to bookshelf number 2 in the library.")
                
                found_key = True
                continuing = False

                for i in range(4):
                    print(".", end = " ")
                    time.sleep(1)
                    
                bs2()
            elif choice == "no":
                print("You couldn't find anything... You may have to look around all over again.")
            else:
                print("Please enter a valid input.")
    else:
        print("You have already found what you needed in this room.")
        print("Returning back to library.")
        for i in range(4):
            print(".", end = " ")
            time.sleep(1)
        library()

    pass

def dining_room(): 
    current_room = "dining"
    room_tracker[current_room] += 1

    if room_tracker[current_room] == 1:
        print("This is the first meeting with the empty and lonely dining room.")
        print("There are 2 doors in here. The one in the west says 'Back Exit' .")
        print("The other room is in the north, and number '2' is written on it.")
        print("'Probably this is the second storage, other than that")
        print("there is nothing but an old candle holder on the table...")
        print("Seriously, why is it standing there just by itself?")
        print("Anyways, let's check the walls.' you say. ")
        global back_exit_discovered
        back_exit_discovered = True
        
        for i in range(14):
            print(".", end= " ")
            time.sleep(1)

        print()
        print("After checking the walls by knocking and looking at them,")
        print("you have found a strange noise coming from the south wall.")
        print("The sound tells you that, this wall is different from the others")
        print("like it has something behind it, but; you cannot reach there.")

        for i in range(10):
            print(".", end= " ")
            time.sleep(1)

        print()
    else:
        print("You are in the dining room again.")
        print("Your only clue is second storage.")
        
    print("You decide to go the possible second storage. ")
    print("When you open the door, the only thing you can see is a mini table")
    print("and a note on it that says 'Haven't you suspected anything?' then")
    print("you realize and say 'Candle holder!' and go to check the candle holder.")
    print("There is a key and a note that says 'South wall of library is empty.' .")
    print("You suspect and decide to go and check it.")
        
    for i in range(15):
        print(".", end= " ")
        time.sleep(1)

    print()
    secret_passage()

def secret_passage():
    print("You are in the library again, and you are facing the wall.")
    print("You check every single part of the wall.")
    print("There it is! You have just found a very small keyhole.")
    print("When you insert the key in the wall, it starts to open itself.")

    for i in range(9):
        print(".", end= " ")
        time.sleep(1)

    print()
    print("You enter the room and see that there is mechanism to unlock")
    print("the next door in the west. You know this is it. There is nothing")
    print("else left to discover in this old house of mystery.")
    print("There is a question written on the door. 'To enter the hidden study,")
    print("speak the title of the book whose name tells no lies.")

    continuing = True
    while continuing:
        answer = input("1. Endless Dream\n" 
        "2. Whispered Secrets\n"
        "3. The Honest Truth\n"
        "4. Shadow of Deceit\n >>").strip().lower()
        
        if answer in ["3", "the honest truth"]:
            print("YES! You did it! You have opened the hidden study!")
            continuing = False
            hidden_study()
        else:
            print("Nothing happens. 'I guess I gave a wrong answer.' ")

def hidden_study(): 

    print("-------------------------------------")
    print("As you enter the only room that you haven't found until now, you know that the truth is close.")
    print("As you piece together the final clues, the truth emerges — chilling and clear.")
    print("It wasn’t an accident.The victim, Eleanor Marlowe, had uncovered damning secrets about her family’s")
    print("fortune — secrets that would have ruined them. The night of her death, she had planned to meet")
    print("with a journalist. But someone got to her first. The killer was not a stranger… it was her own brother, Gregory.")
    print("Driven by greed, he lured Eleanor to the hidden study, claiming he needed help confronting their past.")
    print("There, under the watchful eyes of dusty portraits and forgotten books, he silenced her forever.")
    print("He staged the scene to look like an accident — a fall down the grand staircase — and buried")
    print("the real story beneath layers of deception. But truth doesn’t stay buried. Not forever.")
    print("And not with you on the case. You found the hidden study. You read the forgotten diary. You saw through the lies.")
    print("Now, the world will know what really happened that night. Justice will follow.")
    print("And the mansion, once full of silence and shadows, will finally rest.")
    print(".")
    print(".")
    print(".")
    print("YOU DID IT!!! THE TRUTH IS FINALLY HERE!")

    for i in range(30):
        print("-", end = "")
        time.sleep(1)

    print()
    print("Good job detective, you have successfully uncovered the mystery and finished the game.")
    print("As you have finished the game by completing everything, you may properly exit now.")

def main(): 

    introduction()
    global current_room
    current_room = "foyer"    
    foyer()

    while True:
        if back_exit_discovered:
            action = input("What do you want to do next? (type 'quit' to leave or continue exploring): ").lower()
            if action == "quit":
                print("You decided to leave the mansion. Maybe next time you'll discover more...")
                break
            else:
                print("Continuing your investigation.")


inventory = []
room_tracker = {"foyer": 0, "library": 0, "bs1": 0, "bs2": 0, "storage1": 0, "dining": 0, "secret_passage": 0, "hidden_study": 0}
current_room = ""
found_key = False # bookshelf 2
back_exit_discovered = False

if __name__ == '__main__':
    main()