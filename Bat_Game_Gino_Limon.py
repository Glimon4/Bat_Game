#######################################
### Text Adventure Game: The Riddle ###
### Author: Gino Limon Rioja        ###
### Email: g.rioja@student.hult.edu ###
### Masters in Business Analytics   ###
#######################################

from sys import exit
#menu function
def menu_fu():
    #importing package
    from time import sleep
    #defining function for space on dialogue
    def d_space():
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        #end of d_space
    d_space()
    #iniciationg & printing menu art looping each line
    menu_art = """
            __   __                     ___      _
           |  | |  |      /|           |   |   _/ \_
           |  | |  |  _  | |__         |   |_-/_____\-_     _
         __|  | |  |_| | | |  |/\_     |   |  \     /  |___|
        |  |  | |  | | __| |  |   |_   |   |   |___|   |   |
        |  |  |^|  | ||  | |  | ()| |__|   |   |   |   |   |
        |  |  |||  | ||  | |  |/||| /\ |   |   |   |   |   |
        ~~~~~~~~~~~~~~~~~~~~___\||___~~~~~~~~~~~~~~~~~~~~~~~~
       ~ ~~  ~ ~~ ~~~ ~ ~ ~~\_________/~    ~  ~  ~~~~ ~~~ ~~
     ~~ ~_______________________~~~   ~~  ___________________~
       ~|Type "Start" to inciate|~~~ ~~~~|Type "Over" to exit|~
    ~ ~ |_______________________|~ ~ ~~ ~|___________________|~~
    """
    for line in menu_art.split('\n'):
        print(f"{line}")
        sleep(0.2)
    d_space()
    #input for interaction with player
    menu_loop = True
    m1 = input('\n\t>')
    d_space()
    #if statement for user responsse with loop
    while menu_loop:
        m1 = m1.casefold()
        if 'start' in m1 or 'go' in m1 or 'let' in m1 or 'iniciate' in m1:
            #sending to intro
            print("Okey :D")
            d_space()
            menu_loop = False
            entrance_fu()
        elif 'over' in m1:
            print("\t\t\t END :)")
            menu_loop = False
            exit(0)
        else:
            m1 = input('\n\t>')
            d_space() #end of menu_loop
    #end of menu function & calling intro_fu
#entrance function
def entrance_fu():
        #impotying packages
    import pandas            as pd
    import matplotlib.pyplot as plt
    import seaborn           as sns
    import numpy             as np
    from time import sleep
    sleep(.5)
        #setting pandas print opts
    pd.set_option('display.max_rows',500)
    pd.set_option('display.max_columns',500)
    pd.set_option('display.width',1000)
        #file import
    file = 'Python/Projects Py/Bat_Game_Gino_Limon/Bat_Text_Game_2.xlsx'
    #reading file
    b_game = pd.read_excel(file)
    #soft coding column to read from
    column_name = 'Dialogue'
    #looping with column name
    for row in b_game[column_name]:
        print(row)
        sleep(0.6)
    input( '\t\t Press Enter to play\n\n\t>')
    intro_fu()
    #end of entrance & calling intro_fu
#intro function
def intro_fu():
    #import packages
    from time import sleep
    #defining function for space on dialogue
    def d_space():
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        #end of s_space
    #declaring count down
    intro_count = 3
    #looping while intro_count is greater than one
    while intro_count > 0:
        print(f"\t\t\t\t{intro_count}")
        intro_count -= 1
        sleep(0.5)
    d_space()
    print("\t\tWelcome to the riddle...")
    d_space()
    sleep(.5)
    #print intro logo stored as a string
    intro_art = """
                   .-''''-..              
                 .' .'''.   `.            
                /    \   \    `.          
                \    '   |     |          
                 `--'   /     /           
                      .'  ,-''            
                      |  /                
                      | '                 
                      '-'                 
                     .--.                 
                    /    \                
                    \    /                
                     `--' 
    """
    # split the ASCII art into lines and print each line with a delay
    for line in intro_art.split('\n'):
        print(f"\t{line}")
        sleep(0.2) #adjust the delay time as needed
    #calling the d_space function
    d_space()
    sleep(.6)
    #user interaction comand enter to continue
    input( '\t\tPress Enter to continue\n\n\t>')
    d_space()
    sleep(.6)
    #iniciate dialogue with explanation
    print("\tLet's see if you are as smart as you think...\n")
    d_space()            
    print("\tI am going to give you 3 chances to solve each riddle")
    sleep(.5)
    print("\taditionally I will offer you the option to get a hint")
    sleep(.5)
    print("\tif you fail on your first answer, and a give up option")
    sleep(.5)
    print("\tUsing the 'Hint' option will take away one of your chances")
    sleep(.5)
    print("\tyou decide what to do...")
    sleep(.5)
    print("\tLet's start")
    sleep(.5)
    d_space()
    input( '\t\tPress Enter to continue\n\n\t>')
    d_space()
    #asking the usef if it wants to continue on a conditional
    int_q = input( "\t Type 'no' to forfeit or press enter to continue\n\n\t>")
    int_q = int_q.casefold()
    d_space()
    #if no input by the user goes in to loser function
    if 'no' in int_q:
        #redirecting to loser function
        loser_fu()
    elif int_q == '':
        print("\t\t Let's go!")
        sleep(0.5)
        scene_1()
    else:
        print("\t\t If you didn't wanted to play\n")
        sleep(.5)
        print("\t\t you should learn to follow instructions\n")
        sleep(.5)
        print("\t\t Therefore, welcome to the game")
        sleep(.5)
        d_space
        scene_1()
    #end intro & calling scene_1
#loser function
def loser_fu():
    #import packages
    from time import sleep
    #defining function for space on dialogue
    def d_space():
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        #end of s_space
    d_space()
    #image to show on the loser function
    loser_art = """ 
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ::::I'll guess this is the end of Batman and Gotham city:::
    :::::::::::::::::::::::::::::::::::::::::::::-'    `-::::::
    ::::Game Over!::::::::::::::::::::::::::::-'          `::::
    :::::::::::::::::::::::::::::::::::::::-  '   /(_M_)\  `:::
    :::::::::::::::::::::::::::::::::::-'        |       |  :::
    ::::::::::::::::::::::::::::::::-         .   \/~V~\/  ,:::
    ::::::::::::::::::::::::::::-'             .          ,::::
    :::::::::::::::::::::::::-'                 `-.    .-::::::
    :::::::::::::::::::::-'                  _,,-::::::::::::::
    ::::::::::::::::::-'                _,--:::::::::::::::::::
    ::::::::::::::-'               _.--::::::::::::::::::::::##
    :::::::::::-'             _.--:::::::::::::::::::::::::::##
    ::::::::'    ##     ###.-::::::###:::::::::::::::::::::::##
    ::::-'       ###_.::######:::::###::::::::::::::#####:#####
    :'         .:###::########:::::###::::::::::::::#####:#####
         ...--:::###::########:::::###:::::######:::#####:#####
    _. --:::##:::###:#########:::::###:::::######:::#####:#####
    '#########:::###:#########::#########::######:::#####:#####
    :#########:::#############::#########::######:::###########
    ##########:::########################::####################
    ########## He will be missed ##############################
    ########################################################### 
    """
    for line in loser_art.split('\n'):
        print(f"{line}")
        sleep(0.2) #adjust the delay time as needed
    d_space()
    print("\t\t\t END\n")
    input( '\tPress Enter to go to the main menu\n\n\t>')
    d_space()
    menu_fu()
    #end loser function & calling menu_fu
#scene 1 function
def scene_1():
    #importing package
    from time import sleep
    #defining function for space on dialogue
    def d_space():
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        #end of d_space
    #defining horse riddle
    def horse_riddle():
        d_space()
        print("\tA cowboy rode in to town on Friday,")
        sleep(.5)
        print("\the stayed for 3 nights and then left on Friday")
        sleep(.5)
        print("\thow is this possible?\n")
        sleep(.5)
        d_space()
        #end of horse riddle
    #defining joke riddle
    def joke_riddle():
        d_space()
        print("\tI can be cracked")
        sleep(.5)
        print("\tI can be made")
        sleep(.5)
        print("\tI can be told")
        sleep(.5)
        print("\tI can be played")
        sleep(.5)
        print("\tWhat am I?")
        sleep(.5)
        d_space()
        #end of joke riddle
    #defining variables for art
    s_bati_logo = """
      ._/\/\_.
     (        )
      `'-\/-'`
    """
    l_bati_logo = """
           _,    _   _    ,_
      .o888P     Y8o8Y     Y888o.
     d88888      88888      88888b
    d888888b_  _d88888b_  _d888888b
    8888888888888888888888888888888
    8888888888888888888888888888888
    YJGS8P"Y888P"Y888P"Y888P"Y8888P
     Y888   '8'   Y8P   '8'   888Y
      '8o          V          o8'
    """
    horse_art = """
                .''
      ._.-.___.' (`\
     //(        ( `'
    '/ )\ ).__. ) 
    ' <' `\ ._/'\
       `   \     \
    """
    joke_art = """
        _  ____  _  __ _____
       / |/  _ \/ |/ //  __/
       | || / \||   / |  \  
    /\_| || \_/||   \ |  /_ 
    \____/\____/\_|\_\\____|
    """
    d_space()
    #iniciationg & printing menu art looping each line
    for line in s_bati_logo.split('\n'):
        print(f"\t\t\t{line}")
        sleep(0.2)
    d_space()
    #defining variable for loop
    bati_logo_loop = True
    #input for interaction with player
    bati_logo_q = input( "\t\tWho's logo is this?\n\t>")
    d_space()
    #if statement for user responsse with loop for bati logo question
    while bati_logo_loop:
        bati_logo_q = bati_logo_q.casefold()
        if 'batman' in bati_logo_q or 'bat man' in bati_logo_q or 'bat' in bati_logo_q or 'person' in bati_logo_q:
            #continuing with response
            print("\t\tThat's right it's the Batman")
            #iniciationg & printing menu art looping each line
            for l_line in l_bati_logo.split('\n'):
                print(f"\t\t{l_line}")
                sleep(0.2)
            d_space()
            #dialogue
            print("""The so called Gotham city "Super Hero" I preffer to call him "Hindrance\n""")
            d_space()
            bati_logo_loop = False
        else:
            print("oh... I see you are kind of blind. no worries here is it enhanced\n")
            sleep(.5)
            #iniciationg & printing menu art looping each line
            for l_line in l_bati_logo.split('\n'):
                print(f"\t\t{l_line}")
                sleep(0.2)
            bati_logo_q = input( "\t\tNow, again... Whos logo is this?\n\t>")
    input( "\t\tLet's Go Press Enter to Continue\n\t>")
    #starting horse riddle
    chances_horse = 3
    #calling riddle function
    horse_riddle()
    horse_input = input( "\t>")
    horse_input = horse_input.casefold()
    sleep(.5)
    #loop for horse riddle
    while chances_horse > 0:
        chances_horse -= 1
        #conditional for loop
        if "friday" in horse_input:
            print("\t\tCorrect! you got it :)")
            for h_line in horse_art.split('\n'):
                print(f"\t\t{h_line}")
                sleep(0.2)
            #sum 1 chance to check if it passed or not
            chances_horse += 1
            break
            #end of correct answer
        #elif for hints
        elif "hint" in horse_input:
            #hint (here)
            print("\tThe Horse's name it's not saturday\n")
            sleep(.5)
            print(f"""\t\tChances = {chances_horse}\n""")
            sleep(.5)
            #calling riddle function
            horse_riddle()
            horse_input = input( "\t>")
            horse_input = horse_input.casefold()
            sleep(.5)
            #end of hint option
        #elif give up
        elif "give" in horse_input or "up" in horse_input:
            print("\t\t\tReally ?")
            sleep(.5)
            print("\t\t\tFail then")
            sleep(.5)
            print("\t\t The Horse's Name it's Friday ;)")
            for h_line in horse_art.split('\n'):
                print(f"\t\t{h_line}")
                sleep(0.2)
            d_space()
            #substracting 3 chances to check if it passed or not
            chances_horse -= 3
            break
            #end of give up option
        #else option inviting for hint or give up
        else:
            #else loop to exit in case chances runs out
            if chances_horse > 0:
                print("\t\tSorry but no, that is wrong")
                sleep(.5)
                print("\t\tIf you need a 'Hint', type(hint)")
                sleep(.2)
                print("\t\tIf you give up: type (give up)\n")
                sleep(.2)
                print(f"""\t\tYou have {chances_horse} chances left""")
                sleep(.5)
                #caling riddle function
                horse_riddle()
                horse_input = input( "\t>")
                horse_input = horse_input.casefold()
                sleep(.5)
            elif chances_horse == 0:
                print("\t\tFail!, you run out of opportunities")
                sleep(.5)
                print(f"""\t\tYou have {chances_horse} chances left\n""")
                sleep(1)
                print("\t\tThe Horse's name it's Friday")
                sleep(.5)
                d_space()
                break
            else:
                print('Something wrong Horse Loop')
                print(f"""Chances = {chances_horse}""")
        #end of loop for horse riddle
    sleep(.5)
    input( '\tReady for next? press enter to continue\n\t>') 
    d_space()
    #end of horse riddle
    #----------------------------------------------------------------------
    #starting joke riddle
    chances_joke = 3
    #calling riddle function
    joke_riddle()
    joke_input = input( "\t>")
    joke_input = joke_input.casefold()
    sleep(.5)
    #loop for joke riddle
    while chances_joke > 0:
        chances_joke -= 1
        #conditional for loop
        if "joke" in joke_input:
            print("\t\tCorrect! you got it :)")
            for j_line in joke_art.split('\n'):
                print(f"\t\t{j_line}")
                sleep(0.2)
            #sum 1 chance to check if it passed or not
            chances_joke += 1
            break
            #end of correct answer
        #elif for hints
        elif "hint" in joke_input:
            #hint (here)
            print("\tIt's the clown!\n")
            sleep(.5)
            print(f"""\t\tChances = {chances_joke}\n""")
            sleep(.5)
            #calling joke function
            joke_riddle()
            joke_input = input( "\t>")
            joke_input = joke_input.casefold()
            sleep(.5)
            #end of hint option
        #elif give up
        elif "give" in joke_input or "up" in joke_input:
            print("\t\t\tCommon this one was easy")
            sleep(.5)
            print("\t\t\tFail...")
            sleep(.5)
            print("\t\t\tA Joke")
            sleep(.5)
            print("\t\t\tTudum tsss...")
            for j_line in joke_art.split('\n'):
                print(f"\t\t{j_line}")
                sleep(0.2)
            d_space()
            #substracting 3 chances to check if it passed or not
            chances_joke -= 3
            break
            #end of give up option
        #else option inviting for hint or give up
        else:
            #else loop to exit in case chances runs out
            if chances_joke > 0:
                print("\t\tNope, is wrong")
                sleep(.5)
                print("\t\tRemember need a 'Hint', type(hint)")
                sleep(.2)
                print("\t\tWanna give up: type (give up)\n")
                sleep(.2)
                print(f"""\t\tYou have {chances_joke} chances left""")
                sleep(.5)
                #calliing riddle function
                joke_riddle()
                joke_input = input( "\t>")
                joke_input = joke_input.casefold()
                sleep(.5)
            elif chances_joke == 0:
                print("\t\tFail!, you run out of opportunities")
                sleep(.5)
                print(f"""\t\tYou have {chances_joke} chances left\n""")
                sleep(.5)
                print("\t\tThe answer is a Joke :)")
                sleep(.5)
                d_space()
                break
            else:
                print('Something wrong Joke Loop')
                print(f"""Chances = {chances_joke}""")
        #end of loop for joke riddle
    sleep(.5)
    input( '\tReady for next? press enter to continue\n\t>') 
    d_space()
    #end of joke riddle
    #----------------------------------------------------------------------
    print("To continue at least you have to figure out one of the 2 riddles\n")
    sleep(.5)
    print("\t\tLet's see so far...")
    sleep(1)
    print("\t\t\t\t...")
    sleep(.5)
    print("\t\t\t\t...")
    sleep(1)
    #conditional statement to see if user passes to next scene
    if chances_horse > 0 or chances_joke > 0:
        print("\t\tCongrats you can go to next level!!! :D")
        sleep(1)
        #iniciate scene_2
        scene_2()
    #conditional if passed
    else:
        print("It seems you fail :(")
        sleep(1)
        #loser function
        loser_fu()
    #end of scene_1
#scene_2 definition
def scene_2():
    #importing package
    from time import sleep
    #defining function for space on dialogue
    def d_space():
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        #end of d_space
    #defining age riddle
    def age_riddle():
        d_space()
        print("\tWhat number goes up and doesn’t come back down?")
        d_space()
        #end of age riddle
    #defining time riddle
    def time_riddle():
        d_space()
        print("\tWhere can you add 2 to 11 and get 1?")
        d_space()
        #end of time riddle
    #defining variables for art
    age_art = """
      _  _  __   _  _  ____     __    ___  ____ 
     ( \/ )/  \ / )( \(  _ \   / _\  / __)(  __)
      )  /(  O )) \/ ( )   /  /    \( (_ \ ) _) 
     (__/  \__/ \____/(__\_)  \_/\_/ \___/(____)
    """
    time_art = """
      _______
     /  12   \
    |    |    |
    |9   |   3|
    |     \   |
    |         |
     \___6___/
    """
    d_space()
    #iniciate dialogue
    print("Great you passed the first riddles\n")
    sleep(.5)
    print("Continue like that and maybe you will save 'Batman'\n")
    sleep(.5)
    d_space()
    #starting horse riddle
    chances_age = 3
    #calling riddle function
    age_riddle()
    age_input = input( "\t>")
    age_input = age_input.casefold()
    sleep(.5)
    #loop for age riddle
    while chances_age > 0:
        chances_age -= 1
        #conditional for loop
        if "age" in age_input:
            print("\t\tCorrect! you got it :)")
            for age_line in age_art.split('\n'):
                print(f"\t\t{age_line}")
                sleep(0.2)
            #sum 1 chance to check if it passed or not
            chances_age += 1
            break
            #end of correct answer
        #elif for hints
        elif "hint" in age_input:
            #hint (here)
            print("\tYou are getting older but not younger\n")
            sleep(.5)
            print(f"""\t\tChances = {chances_age}\n""")
            sleep(.5)
            #calling riddle function
            age_riddle()
            age_input = input( "\t>")
            age_input = age_input.casefold()
            sleep(.5)
            #end of hint option
        #elif give up
        elif "give" in age_input or "up" in age_input:
            print("\t\t\tReally ?")
            sleep(.5)
            print("\t\t\tFail then")
            sleep(.5)
            print("\t\t Your Age ;)")
            for a_line in age_art.split('\n'):
                print(f"\t\t{a_line}")
                sleep(0.2)
            d_space()
            #substracting 3 chances to check if it passed or not
            chances_age -= 3
            break
            #end of give up option
        #else option inviting for hint or give up
        else:
            #else loop to exit in case chances runs out
            if chances_age > 0:
                print("\t\tSorry but no, that is wrong")
                sleep(.5)
                print("\t\tIf you need a 'Hint', type(hint)")
                sleep(.2)
                print("\t\tIf you give up: type (give up)\n")
                sleep(.2)
                print(f"""\t\tYou have {chances_age} chances left""")
                sleep(.5)
                #caling riddle function
                age_riddle()
                age_input = input( "\t>")
                age_input = age_input.casefold()
                sleep(.5)
            elif chances_age == 0:
                print("\t\tFail!, you run out of opportunities")
                sleep(.5)
                print(f"""\t\tYou have {chances_age} chances left\n""")
                sleep(1)
                print("\t\tThe Horse's name it's Friday")
                sleep(.5)
                d_space()
                break
            else:
                print('Something wrong Horse Loop')
                print(f"""Chances = {chances_age}""")
        #end of loop for age riddle
    sleep(.5)
    input( '\tReady for next? press enter to continue\n\t>') 
    d_space()
    #end of age riddle
    #----------------------------------------------------------------------
    #starting time riddle
    chances_time = 3
    #calling riddle function
    time_riddle()
    time_input = input( "\t>")
    time_input = time_input.casefold()
    sleep(.5)
    #loop for time riddle
    while chances_time > 0:
        chances_time -= 1
        #conditional for loop
        if "time" in time_input or "clock" in time_input or "watch" in time_input:
            print("\t\tCorrect! you got it :)")
            for t_line in time_art.split('\n'):
                print(f"\t\t{t_line}")
                sleep(0.2)
            #sum 1 chance to check if it passed or not
            chances_time += 1
            break
            #end of correct answer
        #elif for hints
        elif "hint" in time_input:
            #hint (here)
            print("\tConsider Hours for example\n")
            sleep(.5)
            print(f"""\t\tChances = {chances_time}\n""")
            sleep(.5)
            #calling time function
            time_riddle()
            time_input = input( "\t>")
            time_input = time_input.casefold()
            sleep(.5)
            #end of hint option
        #elif give up
        elif "give" in time_input or "up" in time_input:
            print("\t\t\tCommon keep on going!")
            sleep(.5)
            print("\t\t\tFail...")
            sleep(.5)
            print("\t\t\tTime!")
            sleep(.5)
            for t_line in time_art.split('\n'):
                print(f"\t\t{t_line}")
                sleep(0.2)
            d_space()
            #substracting 3 chances to check if it passed or not
            chances_time -= 3
            break
            #end of give up option
        #else option inviting for hint or give up
        else:
            #else loop to exit in case chances runs out
            if chances_time > 0:
                print("\t\tNope, is wrong")
                sleep(.5)
                print("\t\tRemember need a 'Hint', type(hint)")
                sleep(.2)
                print("\t\tWanna give up: type (give up)\n")
                sleep(.2)
                print(f"""\t\tYou have {chances_time} chances left""")
                sleep(.5)
                #calliing riddle function
                time_riddle()
                time_input = input( "\t>")
                time_input = time_input.casefold()
                sleep(.5)
            elif chances_time == 0:
                print("\t\tFail!, you run out of opportunities")
                sleep(.5)
                print(f"""\t\tYou have {chances_time} chances left\n""")
                sleep(.5)
                print("\t\tThe answer is Time! :)")
                sleep(.5)
                d_space()
                break
            else:
                print('Something wrong Joke Loop')
                print(f"""Chances = {chances_time}""")
        #end of loop for joke riddle
    sleep(.5)
    input( '\tReady for next? press enter to continue\n\t>') 
    d_space()
    #end of time riddle
    #----------------------------------------------------------------------
    print("To continue at least you have to figure out one of the 2 riddles\n")
    sleep(.5)
    print("\t\tLet's see so far...")
    sleep(1)
    print("\t\t\t\t...")
    sleep(.5)
    print("\t\t\t\t...")
    sleep(1)
    #conditional statement to see if user passes to next scene
    if chances_age > 0 or chances_time > 0:
        print("\t\tCongrats you can go to next level!")
        sleep(1)
        print("\t\tYou might save Batman...")
        sleep(1)
        #iniciate scene_2
        scene_3()
    #conditional if passed
    else:
        print("It seems you fail :(")
        sleep(1)
        #loser function
        loser_fu()
    #end of scene_2
#scene_3 definition
def scene_3():
    #importing package
    from time import sleep
    #defining function for space on dialogue
    def d_space():
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        #end of d_space
    #defining secret riddle
    def secret_riddle():
        d_space()
        print("\tIf you have me, you will want to share me.")
        sleep(.5)
        print("\tIf you share me,")
        sleep(.5)
        print("\tyou will no longer have me.")
        sleep(.5)
        print("\tWhat am I?\n")
        sleep(.5)
        d_space()
        #end of secret riddle
    #defining barber riddle
    def barber_riddle():
        d_space()
        print("\tI shave every day,")
        sleep(.5)
        print("\tbut my beard stays the same")
        sleep(.5)
        print("\tWho am I?\n")
        sleep(.5)
        d_space()
        #end of barber riddle
    #defining variables for art
    secret_art = """
      _____                    _   
     / ____|                  | |  
    | (___   ___  ___ _ __ ___| |_ 
     \___ \ / _ \/ __| '__/ _ \ __|
     ____) |  __/ (__| | |  __/ |_ 
    |_____/ \___|\___|_|  \___|\__|
    """
    barber_art = """
      /$$$$$$        /$$$$$$$                      /$$                          
     /$$__  $$      | $$__  $$                    | $$                          
    | $$  \ $$      | $$  \ $$  /$$$$$$   /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
    | $$$$$$$$      | $$$$$$$  |____  $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$
    | $$__  $$      | $$__  $$  /$$$$$$$| $$  \__/| $$  \ $$| $$$$$$$$| $$  \__/
    | $$  | $$      | $$  \ $$ /$$__  $$| $$      | $$  | $$| $$_____/| $$      
    | $$  | $$      | $$$$$$$/|  $$$$$$$| $$      | $$$$$$$/|  $$$$$$$| $$      
    |__/  |__/      |_______/  \_______/|__/      |_______/  \_______/|__/      
    """
    d_space()
    #iniciate dialogue
    print("Okey you arrived at the last two\n")
    sleep(.5)
    print("The question remains are you going to save'Batman'?\n")
    sleep(.5)
    d_space()
    #starting secret riddle
    chances_secret = 3
    #calling riddle function
    secret_riddle()
    secret_input = input( "\t>")
    secret_input = secret_input.casefold()
    sleep(.5)
    #loop for secret riddle
    while chances_secret > 0:
        chances_secret -= 1
        #conditional for loop
        if "secret" in secret_input:
            print("\t\tCorrect! you got it :)")
            for s_line in secret_art.split('\n'):
                print(f"\t\t{s_line}")
                sleep(0.2)
            #sum 1 chance to check if it passed or not
            chances_secret += 1
            break
            #end of correct answer
        #elif for hints
        elif "hint" in secret_input:
            #hint (here)
            print("\tCan I tell you something and trust that you will not share it?\n")
            sleep(.5)
            print(f"""\t\tChances = {chances_secret}\n""")
            sleep(.5)
            #calling riddle function
            secret_riddle()
            secret_input = input( "\t>")
            secret_input = secret_input.casefold()
            sleep(.5)
            #end of hint option
        #elif give up
        elif "give" in secret_input or "up" in secret_input:
            print("\t\t\tokey")
            sleep(.5)
            print("\t\t\tFail then")
            sleep(.5)
            print("\t\tIt's a Secret")
            for s_line in secret_art.split('\n'):
                print(f"\t\t{s_line}")
                sleep(0.2)
            d_space()
            #substracting 3 chances to check if it passed or not
            chances_secret -= 3
            break
            #end of give up option
        #else option inviting for hint or give up
        else:
            #else loop to exit in case chances runs out
            if chances_secret > 0:
                print("\t\tSorry but no, that is wrong")
                sleep(.5)
                print("\t\tIf you need a 'Hint', type(hint)")
                sleep(.2)
                print("\t\tIf you give up: type (give up)\n")
                sleep(.2)
                print(f"""\t\tYou have {chances_secret} chances left""")
                sleep(.5)
                #caling riddle function
                secret_riddle()
                secret_input = input( "\t>")
                secret_input = secret_input.casefold()
                sleep(.5)
            elif chances_secret == 0:
                print("\t\tFail!, you run out of opportunities")
                sleep(.5)
                print(f"""\t\tYou have {chances_secret} chances left\n""")
                sleep(1)
                print("\t\tThe Horse's name it's Friday")
                sleep(.5)
                d_space()
                break
            else:
                print('Something wrong Horse Loop')
                print(f"""Chances = {chances_secret}""")
        #end of loop for secret riddle
    sleep(.5)
    input( '\tReady for next? press enter to continue\n\t>') 
    d_space()
    #end of secret riddle
    #----------------------------------------------------------------------
    #starting barber riddle
    chances_barber = 3
    #calling riddle function
    barber_riddle()
    barber_input = input( "\t>")
    barber_input = barber_input.casefold()
    sleep(.5)
    #loop for barber riddle
    while chances_barber > 0:
        chances_barber -= 1
        #conditional for loop
        if "barber" in barber_input or "stylist" in barber_input:
            print("\t\tCorrect! you got it :)")
            for b_line in barber_art.split('\n'):
                print(f"\t\t{b_line}")
                sleep(0.2)
            #sum 1 chance to check if it passed or not
            chances_barber += 1
            break
            #end of correct answer
        #elif for hints
        elif "hint" in barber_input:
            #hint (here)
            print("\tI also cut hair\n")
            sleep(.5)
            print(f"""\t\tChances = {chances_barber}\n""")
            sleep(.5)
            #calling barber function
            barber_riddle()
            barber_input = input( "\t>")
            barber_input = barber_input.casefold()
            sleep(.5)
            #end of hint option
        #elif give up
        elif "give" in barber_input or "up" in barber_input:
            print("\t\t\tBye bye")
            sleep(.5)
            print("\t\t\tYou Fail!")
            sleep(.5)
            print("\t\t\tIt a Barber")
            sleep(.5)
            for b_line in barber_art.split('\n'):
                print(f"\t\t{b_line}")
                sleep(0.2)
            d_space()
            #substracting 3 chances to check if it passed or not
            chances_barber -= 3
            break
            #end of give up option
        #else option inviting for hint or give up
        else:
            #else loop to exit in case chances runs out
            if chances_barber > 0:
                print("\t\tNope, is wrong")
                sleep(.5)
                print("\t\tRemember need a 'Hint', type(hint)")
                sleep(.2)
                print("\t\tWanna give up: type (give up)\n")
                sleep(.2)
                print(f"""\t\tYou have {chances_barber} chances left""")
                sleep(.5)
                #calliing riddle function
                barber_riddle()
                barber_input = input( "\t>")
                barber_input = barber_input.casefold()
                sleep(.5)
            elif chances_barber == 0:
                print("\t\tFail!, you run out of opportunities")
                sleep(.5)
                print(f"""\t\tYou have {chances_barber} chances left\n""")
                sleep(.5)
                print("\t\tThe answer is a Joke :)")
                sleep(.5)
                d_space()
                break
            else:
                print('Something wrong barber Loop')
                print(f"""Chances = {chances_barber}""")
        #end of loop for barber riddle
    sleep(.5)
    input( '\tReady for next? press enter to continue\n\t>') 
    d_space()
    #end of barber riddle
    #----------------------------------------------------------------------
    print("This is the last one, at least you have to figure out one of the 2 riddles\n")
    sleep(.5)
    print("\t\tDid you saved 'Batman'?\n")
    sleep(1)
    print("\t\t\t\t...")
    sleep(.5)
    print("\t\t\t\t...")
    sleep(1)
    #conditional statement to see if user passes to next scene
    if chances_secret > 0 or chances_barber > 0:
        print("\t\tCongrats you Win!")
        sleep(1)
        #iniciate win function 
        win_input()
    #conditional if passed
    else:
        print("It seems you did not saved Batman")
        sleep(1)
        #loser function
        loser_fu()
    #end of scene_3
#win function
def win_input():
    from time import sleep
    #dialogue
    def d_space():
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        print(f"""{'-'*70}""")
        sleep(0.1)
        #end of d_space
    d_space()
    print("Here is it")
    sleep(.5)
    print("Save and sound")
    sleep(.5)
    d_space()
    #image to show on the win function
    win_art= """ 
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡂⢸⠀⢀⣀⣤⣤⣤⣤⣄⡀⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠘⣷⡿⠋⠀⣀⣀⣀⣈⡙⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠙⠁⠔⢻⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢀⢈⠉⠹⠿⢿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣰⡁⠀⠀⠹⣿⡎⠀⣀⣹⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢹⡿⢷⣢⣤⡟⣧⣭⣶⣿⣽⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢩⠙⠶⣬⡉⠇⣿⣿⣿⣿⡟⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠆⠆⠀⡈⠓⠠⣿⣿⣿⠟⣼⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠈⣴⠀⠐⢒⣲⣼⣿⣾⣆⣷⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡀⢌⠳⢄⠈⢀⣀⣼⣿⣿⣿⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⣿⣿⣷⡀⠛⣦⡙⠳⣶⣾⣿⣿⡇⢸⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⡿⢿⣷⡄⠀⠙⢦⣤⣿⡟⠁⢱⡘⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣠⣤⣼⣿⣶⣤⣀⠽⢿⡶⠤⠾⣷⣶⣿⣿⢿⣿⣿⠿⠿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣠⣾⡿⠟⠉⣉⣠⣴⣒⣀⣤⡤⠤⠤⣤⣶⣶⣶⡶⠟⠋⠁⠀⠀⢀⠁⠀⠀⠀⠈⠉⠓⢶⣶⣮⣝⠲⣤⣉⠛⠻⢿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⣼⣿⡿⠖⠚⢉⣡⠴⠞⣉⡡⠴⢖⣫⣭⠶⢛⣿⣿⣤⣀⡀⠀⠀⠀⣸⣷⣿⡀⠀⠀⠀⣀⣼⣿⣿⣟⢿⣶⣿⣍⡓⠶⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢹⣿⣧⣴⠶⣛⡫⠵⣒⣩⡤⠶⠚⠋⠁⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢻⣿⡿⣯⣑⠒⠾⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢀⣿⣋⡵⢖⡩⠔⠚⠉⠁⠀⠀⠀⠀⡀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⠀⠈⣿⡇⠈⠻⢿⣝⡲⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢘⣿⠏⣴⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀⠙⠉⠀⠀⠀⠙⠿⠛⠛⢿⣿⣿⣿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠹⢿⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠸⣯⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⠻⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⢰⡿⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣿⠁⠈⠳⣄⠀⠀⠀⠀⠀⢹⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡀⠀⠀⠀⠀⢠⡿⣧⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣾⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⠿⣝⠛⠳⠶⠤⠤⠤⠤⠤⠤⠤⠤⠶⣿⣿⡷⠦⠤⠤⠤⠤⠤⠤⢤⣴⣿⠉⠣⠀⠀⠀⠐⠉⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⢠⣿⣿⣿⣦⡀⠀⢀⠀⠀⠀⠀⠀⢸⣏⠳⡀⠑⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⢀⠀⠀⠀⠀⢻⡟⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
    """    
    for w_line in win_art.split('\n'):
                print(f"\t\t{w_line}")
                sleep(0.1)
    d_space()
    #indication for credit conditional
    print("(yes/no) answer")
    sleep(.5)
    #credits conditional
    qw = input('Are you curious?\n>')
    d_space()
    #conditinal if s=yes
    if 'yes' in qw or 'maybe' in qw or 'perhaps' in qw:
        print("Credits:\n")
        sleep(.5)        
        #my name CODER OF THE GAME
        d_space()
        print("\t\t\tMini Game Coded by:\n")
        sleep(.5)
        print("\t\t\tGino Limon Rioja (gl)\n")
        sleep(.5)
        print("\t\t\tThank's for playing!")
        sleep(.5)
        d_space()
        sleep(3)
        #citation for art
        print("\t\tASCII Art extracted from:\n")
        sleep(.5)
        print("""
        -https://www.asciiart.eu/comics/batman
        -https://patorjk.com
        -https://emojicombos.com/batman-text-art
        -https://ascii.co.uk/art/batman
        on 1/27/2023
        """)
        sleep(.5)
        #citation for riddles
        print("\t\tRiddles extracted from:\n")
        sleep(.5)
        print("""
        -https://www.rd.com/list/easy-riddles/
        -https://icebreakerideas.com/math-riddles/
        """)
        sleep(.5)
        #character inspiration
        print("\t\tGame inpired on the Riddler from Batman\n")
        sleep(.5)
        print("""
        -https://www.dc.com/blog/2022/02/23/who-is-the-riddler
        """)
        sleep(.5)
    #else function (jumps credits) 
    else:
        print("until next time ;)")
        sleep(1)
    #variable for function loop 
    intro_continuance = True   
    #question for the user if he wants to play again
    replay = input("Do you want to play again?\n (yes/no) answer only\n>")
    #loop iniciation
    while intro_continuance:
        replay = replay.casefold()
        #loop conditional, the loop keeps you here until the user chooses to play again 
        if 'yes' in replay:
            sleep(1)
            intro_continuance = False
            menu_fu()
        elif 'no' in replay:
            print("Thanks for playing Bye :)\n")
            menu_fu()
            
        else:
            print("No matter if it's true or not, gotham law requires you to follow instructions\n")
            sleep(.5)
            replay = input("Do you want to play?\n (yes/no) answer only\n>")
#end of win function
#Launching Game
menu_fu()
print('finish here')
#end
