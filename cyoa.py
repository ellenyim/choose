def main():
    print("A Pokemon Story: Choosing your Starter and having your first battle. ")

    print("\nGreetings. I am professor oak. I've seen you grow as a young self. Now, you are going to start on your \n"
          "extremely long journey. I welcome you to your home town. You see, when I was a young self like you, I\n "
          "used to go travel the world meeting all different types of trainers and pokemon. Now it's your turn. First, \n"
          "tell me, are you a boy or are you a girl? \n")
    print("1. Boy 1    2. Girl")
    choice = input("Choose your gender: ")

    print("\nGreat! Now, tell me the name you want to be called on this journey. \n")

    print("1. Red     2. Blue ")
    name = input("Choose your name: ")

    if name == 1:
        print("\n So, Red your journey to become a trainer has begun. Now it's time for you to choose your starting \n"
              "pokemon. \n")
        print("1. Bulbasaur, the grass type.   2. Charmander, the fire type.   3. Squirtle, the water type. ")
        start = input("Choose: ")
        if start == 1:
            print("\nSo you chose the grass type. Excellent choice! Your journey to become a trainer is underway.\n")
        elif start == 2:
            print("\nSo you chose the fire type. Excellent choice! Your journey to become a trainer is underway. \n ")
        else:
            print("\nSo you chose the water type. Excellent choice! Your journey to become a trainer is underway. \n")

    else:
        print("So, Blue, your journey to become a trainer has begun. Now it's time for you to choose your starting \n"
              "pokemon. \n")
        print("1. Bulbasaur, the grass type.   2. Charmander, the fire type.   3. Squirtle, the water type.")
        start = input("Choose: ")
        if start == 1:
            print("\nSo you chose the grass type. Excellent choice! Your journey to become a trainer is underway.\n")
        elif start == 2:
            print("\nSo you chose the fire type. Excellent choice! Your journey to become a trainer is underway.\n")
        else:
            print("\nSo you chose the water type. Excellent choice! Your journey to become a trainer is underway.\n")

    print("\nPlease don't forget to trust and love your partner and you will also work hard together with them. ")
    print("\nOne more thing, this is your rival, you have been feuding since you were babies, Errr, what's his name "
          "again? \n")
    print("1. Gary. 2. Arch 3. Ambi.")
    rival = input("Name: ")

    if rival == 1:
        print("\nSo, the two of you will not only travel around the region, but to catch every pokemon and go through "
              "the gyms, and then the elite four. ")
    elif rival == 2:
        print("\nSo, the two of you will not only travel around the region, but to catch every pokemon and go through "
              "the gyms, and then the elite four. ")
    else:
        print("\nSo, the two of you will not only travel around the region, but to catch every pokemon and go through "
              "the gyms, and then the elite four.")

    print(
    "\nYour adventure in this world, begins now. Also, before I forget, I have always wanted to fulfill this dream\n"
    "but could never get it done. So now, I would like both of you to fulfill my dream of completing the \n"
    "pokedex. I will give you the pokedex, a high-tech system that will record all pokemon that you encounter and \n"
    "when you catch them, it will record even more. Come back to my lab when you have completed your fulfillment. ")

    print(
    "\nAfter leaving, your rival challenges you to a battle and you can't say no, so of course your rival will choose \n"
    "the pokemon that you are weak against. ")

    if rival == 1:
        if start == 1:
            print("Hey how about a battle? I'll send out my fire type. Let's go! ")
        elif start == 2:
            print("Hey how about a battle? I'll send out my water type. Let's go! ")
        else:
            print("Hey, how about a battle? I'll send out my grass type. Let's go! ")

    if rival == 2:
        if start == 1:
            print("Hey how about a battle? I'll send out Charmander. Let's go! ")
        elif start == 2:
            print("Hey how about a battle? I'll send out Squirtle. Let's go! ")
        else:
            print("Hey, how about a battle? I'll send out Bulbasaur. Let's go! ")

    if rival == 3:
        if start == 1:
            print("Hey how about a battle? I'll send out my fire type. Let's go! ")
        elif start == 2:
            print("Hey how about a battle? I'll send out my water type. Let's go! ")
        else:
            print("Hey, how about a battle? I'll send out my grass type. Let's go! ")

    print("1. Scratch. 2. Tail whip. ")
    you = input("Choose: ")

    if you == 1:
        print("Good, using offensive moves is the key to defeating you opponent. ")
    else:
        print(
        "Keep up your defense. Defensive moves will raise your defense and your opponent's moves won't be as strong on you. ")

    print("\nOnce defeated your rival, you can do choose 2 options. ")

    print("1. Go to your rivals house and obtain a nice item. 2. Continue on to the next city. ")
    map = input("Choose: ")

    if map == 1:
        print("Your rival sister says, 'Hi neighbor, great to see you! Wow, my grandpa assigned you that big of an important task and \n"
        "you don't even have a town map. Jeez, that's lazy of him, here, why don't you take this one. \n"
        "Obtained the town map. ")
    else:
        print("The journey begins..... ")

    print("\nOn your way to Virdian City, the first thing you do is go to the Poke Mart that is the place with the blue roof. Inside \n "
    "the owner will ask, 'Are you hear from Professor Oak?' You will say yes and he will give you the Oak's Parcel. After you receive \n"
    "the parcel, you will head back to Pallet Town to give the professor his parcel. Inside the parcel contains Poke balls, where \n"
    "he gives you and your rival 5 pokeballs each to get started. Your first destination is Pewter City. ")

    print("You left Pallet Town, and you encountered a Rattata. ")
    print("1. Run Away.  2. Catch it.  3. Fight to gain experience.  ")
    choice = input("Choose: ")

    if start == 1:
        if choice == 1:
            print("You continue your journey with Bulbasaur and find better pokemon. ")
        elif choice == 2:
            print("Congrats, you caught your first pokemon. ")
        else:
            print("Your Bulbasaur gained experience. ")

        print("You made it to Viridian City again and before you leave, an old man who was before lying on the ground sick had his coffee \n"
        "already and he is 10x better. Now, he assists on how to catch a pokemon with a little computer video, called the TeachyTV. \n"
        "You move on to Viridian Forest where it contains tons of bug pokemon and your Bulbsaur has a huge disadvantage against. Good Luck! \n"
        "Next, there are also tons of trainers, so be prepared to face a whole lot of bugs. ")

        print("You arrive in Pewter City. The gym is a rock type, so Bulbasaur has a huge advantage. Make sure you have lots of potions. ")
        print("You arrive at the Gym. The battle starts. He sends out Geodude. Second is Onix. You have the first attack, what attack do you use? ")
        print("1. Tackle. 2. Growl. 3. Razor Leaf. 4. Growth. ")
        a = input("Choose: ")
        if a == 1:
            print("Wow, that did nothing, normal attacks don't match up that well on rock.")
        elif a == 2:
            print("Good, you lowered your opponent's attack. ")
        elif a == 3:
            print("Super Effective. ")
        else:
            print("increases the user's Special Attack stat by one stage.")
        print("Ok, let's just imagine that you just need a one turn and you win. Next is round 2. ")
        print("\nSecond Round. Onix. ")
        print("1. Tackle. 2. Growl. 3. Razor Leaf. 4. Growth. ")
        a = input("Choose: ")
        if a == 1:
            print("Wow, that did nothing, normal attacks don't match up that well on rock.")
        elif a == 2:
            print("Good, you lowered your opponent's attack. ")
        elif a == 3:
            print("Super Effective. One hit KO. ")
        else:
            print("increases the user's Special Attack stat by one stage.")

        print("Again, too much to actually code the whole battle so let's imagine that you need one turn and you win. ")

        print("YAY! You won your first gym battle. You earned the Boulder Badge and you received $10 (this game is in japanese yen, which will be equivalent to 900 yen.)")

    elif start == 2:
        if choice == 1:
            print("You continue your journey with Charmander and find better pokemon.")
        elif choice == 2:
            print("Congrats, you caught your first pokemon. ")
        else:
            print("Your Charmander gained experience. ")

        print("You made it to Viridian City again and before you leave, an old man who was before lying on the ground sick had his coffee \n"
        "already and he is 10x better. Now, he assists on how to catch a pokemon with a little computer video, called the TeachyTV. \n"
        "You move on to Viridian Forest where it contains tons of bug pokemon and this is the place where Charmander shines. Good Luck! \n"
        "Next, there are also tons of trainers, so be prepared to face a whole lot of bugs. ")

        print("You arrive in Pewter City. The gym is rock type and Charmander has a disadvantage. So word of advice, train Charmander to level \n"
        "13 and it will learn Metal Claw, which will be super effective against rock. Make sure you have lots of potions. ")
        print("You arrive at the Gym. The battle starts. He sends out Geodude. Second is Onix. You have the first attack, what attack do you use? ")
        print("1. Scratch. 2. Tail Whip. 3. Ember. 4. Metal Claw. ")
        b = input("Choose: ")
        if b == 1:
            print("That did nothing, cause normal type attacks don't do much on rock. ")
        elif b == 2:
            print("You weakened your opponent's defense. ")
        elif b == 3:
            print("Did some damage but not enough. ")
        else:
            print("Super effective. ")
        print("Ok, let's just imagine that you just need a one turn and you win. Next is round 2. ")
        print("\nSecond Round. Onix. ")
        print("1. Scratch. 2. Tail Whip. 3. Ember. 4. Metal Claw. ")
        b = input("Choose: ")
        if b == 1:
            print("That did nothing, cause normal type attacks don't do much on rock. ")
        elif b == 2:
            print("You weakened your opponent's defense. ")
        elif b == 3:
            print("Did some damage but not enough. ")
        else:
            print("Super effective. ")

        print("Again, too much to actually code the whole battle so let's imagine that you need one turn and you win. ")

        print("YAY! You won your first gym battle. You earned the Boulder Badge and you received $10 (this game is in japanese yen, which will be equivalent to 900 yen.)")


    else:
        if choice == 1:
            print("You continue your journey with Squirtle and find better pokemon.")
        elif choice == 2:
            print("Congrats, you caught your first pokemon. ")
        else:
            print("Your Squirtle gained experience. ")

        print("You made it to Viridian City again and before you leave, an old man who was before lying on the ground sick had his coffee \n"
        "already and he is 10x better. Now, he assists on how to catch a pokemon with a little computer video, called the TeachyTV. \n"
        "You move on to Viridian Forest where it contains tons of bug pokemon and Squirtle is average cause water against bug, okay. Good Luck! \n"
        "Next, there are also tons of trainers, so be prepared to face a whole lot of bugs. ")

        print("You arrive in Pewter City. The gym is rock type and Squirtle is the perfect match against the gym leader. Make sure you \n"
        "have lots of potions.")
        print("You arrive at the Gym. The battle starts. He sends out Geodude. Second is Onix. You have the first attack, what attack do you use? ")
        print("1. Tackle. 2. Tail Whip. 3. Bubble. 4. Withdraw.  ")
        c = input("Choose: ")
        if c == 1:
            print("Did nothing. normal against rock. ")
        elif c == 2:
            print("lower opponent's defense. ")
        elif c == 3:
            print("Super effective! ")
        else:
            print("You raise your defense. ")

        print("Ok, let's just imagine that you just need a one turn and you win. Next is round 2. ")
        print("Round 2, Onix. ")
        print("1. Tackle. 2. Tail Whip. 3. Bubble. 4. Withdraw.  ")
        c = input("Choose: ")
        if c == 1:
            print("Did nothing. normal against rock. ")
        elif c == 2:
            print("lower opponent's defense. ")
        elif c == 3:
            print("Super effective! ")
        else:
            print("You raise your defense. ")

        print("Again, too much to actually code the whole battle so let's imagine that you need one turn and you win. ")

        print("YAY! You won your first gym battle. You earned the Boulder Badge and you received $10 (this game is in japanese yen, which will be equivalent to 900 yen.)")

    print("Narrator speaking, 'I don't want to do the rest of this story/game, but here's a quick summary about what happens next, the game itself is pretty straightforward. Catch more \n"
    "pokemon, more gym battles and trainer battles, stopping bad guys, catching rare pokemon, and elite 4 + champion. The champion happens to be your rival because he is always one step \n"
    "ahead of you. Of course, your team evolves once you train. Bye. ")


    print("THE END! ")


main()
