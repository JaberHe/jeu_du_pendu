import getpass

# Entrer un mot mais afficher seulement des _
play = True
while play == True:
    nb_trials = 9
    word = getpass.getpass("entrez un mot : ")
    if word == "/stop":
        play = False
        break
    list_word = list(word)
    list_word_hidden = list("_"*len(word))
    word_hidden = " ".join(list_word_hidden)
    print(word_hidden)

    
    # Demander une lettre pour vérification + vérification

    while nb_trials > 0 :
        letter = input("entrez une lettre (pour arreter le jeu écrivez: /stop) :")

        if letter == word :
            print('vous avez gagné')
            print('- '*50)
            print("")
            print("nouvelle partie")
            print("")
            print("- "*50)
            break

        elif letter in list_word :
            while letter in list_word :
                ind_letter = list_word.index(letter)
                list_word_hidden.pop(ind_letter)
                list_word_hidden.insert(ind_letter,letter)
                word_hidden2 = " ".join(list_word_hidden)
                list_word.pop(ind_letter)
                list_word.insert(ind_letter,"-")
            print(word_hidden2)
        elif letter == "/stop":
            play = False
            break
        
        elif not letter in list_word :
            print('faux!')
            nb_trials -= 1
            print(f'il vous reste {nb_trials} essais')
            
        if "_" not in list_word_hidden:
            print('vous avez gagné')
            print('- '*50)
            print("")
            print("nouvelle partie")
            print("")
            print("- "*50)
            break   
    if nb_trials == 0:
        print("vous avez perdu")
        print(f'le mot était : {word}')
        nb_trials = 9
        print('- '*50)
        print("")
        print("nouvelle partie")
        print("")
        print("- "*50)
