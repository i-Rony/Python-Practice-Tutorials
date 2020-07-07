def game():
    print("---------------------")
    print("=== Guessing Game ===")
    print("---------------------")

    G_count=0
    G_limit=5
    Out_of_g=False
    Guess=""
    Sec_word="Pluto"

    while Guess!=Sec_word and not(Out_of_g):
        if G_count<G_limit:
            Guess=input("Enter the Guess :")
            G_count+=1
        else:
            Out_of_g=True

    if Out_of_g:
        print ("You lose the game!")
    else:
        print ("You win!")

game()
