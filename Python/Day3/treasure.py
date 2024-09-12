print("welcome to the treasure island")
choose_1 = input("Do you want to go left or right?\n")
if choose_1 == 'left':
    choose_2 = input("do you want to swim or wait for the boat?\n")
if choose_2 == 'wait':
    choose_3 = input("which door do you want to choose?Red, Yellow or Green\n")
if choose_3 != 'Red' and choose_3 != 'Yellow':
    print("You Win!!!!!")
else:
    print("Game over")