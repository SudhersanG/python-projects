class Madlibgame:
    def __init__(self):
        print("HI THERE WELCOME TO MADLIB GAME!")
        print("                                  ")
        print("-------------- :) --------------")
        print("                                  ")

    def game(self):
        noun1=input("noun1:") #power
        noun2=input("noun2:") #story
        pronoun1=input("pronoun1:") #multiverse
        pronoun2=input("pronoun2:") #universe
        adject=input("adject:") #war
        place=input("place:") #london
        name=input("name:") #youmangasor
        hero1=input("hero1:") #ironman
        hero2=input("hero2:") #captain america
        verb=input("verb:") #tony won

        madlib=f"one day i get one new {noun1}. That is power of {noun2} creating with all aspects to connect with {pronoun1}.\n Iron man now getting the whole power of {pronoun2} strength. \n Now ben10 entered in the {adject} \n of wherer irom and ben10 were both anouncced a {place}  inbetween them. \n Yeah you are right! That day came ben and tony stark were suited up. \n start fight in {name}.\n Ben transformed as {hero1} and tony suited up as {hero2}.\n {hero2} was the match decider in this one. \n fight started and they both foght trastically and hardly. {verb} finally."
        print("                                  ")
        print("                                  ")
        print(madlib)

mad=Madlibgame()
mad.game()
