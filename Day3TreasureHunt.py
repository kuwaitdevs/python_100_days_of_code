print("""
            ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
          ¶¶¶    ¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
        ¶¶¶  ¶¶  ¶¶ ¶¶¶¶ ¶¶¶¶   ¶¶¶¶¶¶ ¶¶¶¶¶
      ¶¶¶  ¶¶¶  ¶¶  ¶¶¶¶ ¶¶¶¶   ¶¶¶¶¶¶  ¶¶¶¶¶¶
    ¶¶¶   ¶¶¶   ¶¶ ¶¶¶¶¶ ¶¶¶¶    ¶¶¶¶¶¶   ¶¶¶¶¶
   ¶¶   ¶¶¶¶¶  ¶¶  ¶¶¶¶¶ ¶¶¶¶    ¶¶¶¶¶¶¶    ¶¶¶¶¶
 ¶¶    ¶¶¶¶¶   ¶¶  ¶¶¶¶¶ ¶¶¶¶     ¶¶¶¶¶¶     ¶¶¶¶¶¶
¶¶¶¶¶     ¶¶  ¶¶  ¶¶¶¶¶¶ ¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
  ¶¶¶¶¶¶¶    ¶¶¶  ¶¶¶¶¶¶ ¶¶¶¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
   ¶¶¶   ¶¶¶¶¶¶          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
     ¶¶  ¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶
       ¶¶ ¶¶¶ ¶¶         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶   ¶¶¶¶
        ¶¶  ¶¶ ¶¶  ¶¶¶¶¶ ¶¶¶      ¶¶¶¶   ¶¶¶
          ¶¶ ¶¶ ¶¶  ¶¶¶¶ ¶¶¶     ¶¶¶¶  ¶¶¶
           ¶¶ ¶¶ ¶¶ ¶¶¶¶  ¶¶    ¶¶¶¶  ¶¶¶
             ¶¶ ¶ ¶¶ ¶¶¶  ¶¶   ¶¶¶¶ ¶¶¶
               ¶ ¶ ¶¶ ¶¶  ¶¶  ¶¶¶¶ ¶¶¶
                ¶¶  ¶  ¶  ¶¶  ¶¶¶¶¶¶
                  ¶  ¶    ¶¶ ¶¶¶¶¶¶
                   ¶¶ ¶   ¶¶¶¶¶¶¶
                     ¶¶¶  ¶¶¶¶¶¶
                      ¶¶¶ ¶¶¶¶
                        ¶¶¶¶¶
                          ¶""")
print("Welcome to Treasure Hunt!")
print("Your mission is to find a buried treasure using a map.")
print("Throughout your trip you will face obstacles.")
print("Chose your action by typing 1 or 2 based on what you see fit.")
print("You started your journey and came across a huge swamp.")
print("What will you do?")
print("1. Walk across it")
print("2. Go around it")
answer = int(input())

if answer == 2:
    print("You arrived at a mountain and you want to cross it.")
    print("What will you do?")
    print("1. Climb it to the other side")
    print("2. Dig a tunnel to the other side")
    answer = int(input())

    if(answer == 2):
        print("The tunnel collapsed. Game over.")
    else:
        print("You got to the other side.")
        print("You found a village and you are starving.")
        print("What will you do?")
        print("1. Beg for food")
        print("2. Work hard at a stable to afford food")
        answer = int(input())

        if(answer == 2):
            print("You worked too hard after climbing a mountain and you died. Game over.")
        else:
            print("Villagers gave you money to afford food.")
            print("You ate and you feel better.")
            print("A villager asks about your journey.")
            print("What will you do?")
            print("1. Lie and hide that you are seeking a treasure.")
            print("2. Share the truth about your objective.")
            answer = int(input())

            if(answer == 2):
                print("The villager turns out to be the king of the land. He likes your honesty and rewards you with a lot of money. You win.")
            else: 
                print("The villager turns out to be the king of the land. He spots the treasure map in your pocket. He orders the guards to behead you for lying to him. Game over.")

else:
    print("You tried your best but you got rapped in the swamp and died. Game over.")