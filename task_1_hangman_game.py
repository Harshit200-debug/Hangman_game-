import random 
word_list=["apple","understanding","right","harshit","cruel","brilliant","mango","banana","flower","beautiful","happiness","honesty","sad","communication","radharani"]
life = 7
chosen_list = random.choice(word_list)
display = []
for i in range(len(chosen_list)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guess = input("guess a letter : ").lower()
    for position in range(len(chosen_list)):
        letter = chosen_list[position]
        if letter==guess:
            display[position]=guess
    print(display)
    if guess not in chosen_list:
        life -=1
        if life ==1:
            print("""___________________|""")
            print("""|                  |""")
            print("""|                  0""")
            print("""|                ( | )""")
            print("""|                 | |""")
            print("""|""")
            print("""|""")
            print("""|""")
        elif life == 2:
            print("""___________________|""")
            print("""|                  |""")
            print("""|                  0""")
            print("""|                ( | )""")
            print("""|                 |  """)
            print("""|""")
            print("""|""")
            print("""|""")
        elif life == 3:
            print("""___________________|""")
            print("""|                  |""")
            print("""|                  0""")
            print("""|                ( | )""")
            print("""|""")
            print("""|""")
            print("""|""")
            print("""|""")
        elif life == 4:
            print("""___________________|""")
            print("""|                  |""")
            print("""|                  0""")
            print("""|                ( | """)
            print("""|""")
            print("""|""")
            print("""|""")
            print("""|""")
        elif life == 5:
            print("""___________________|""")
            print("""|                  |""")
            print("""|                  0""")
            print("""|                  | """)
            print("""|""")
            print("""|""")
            print("""|""")
            print("""|""")
        elif life == 6:
            print("""___________________|""")
            print("""|                  |""")
            print("""|                  0""")
            print("""|""")
            print("""|""")
            print("""|""")
            print("""|""")
            print("""|""")
        elif life == 7:
            print("""___________________|""")
            print("""|                  |""")
            print("""|""")
            print("""|""")
            print("""|""")
            print("""|""")
            print("""|""")
            print("""|""")
        else:
            game_over=True
            print("try again !")
            print("you loss the game and the right word is : ")
            print(chosen_list)         
    if '_' not in display:
        game_over=True
        print("congratulation ! you win the game. ")