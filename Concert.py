import time

global victory
victory = 0

def main():
    global victory 
    if victory == 3:
        print "You & your friends made it to the show! Victory is yours!"
        return 0;

    print "The show starts in one hour. In order to achieve victory you must\nsuccessfully complete each of the following:\nA.) Get a ride\nB.) Get a ticket\nC.) Get your friends.\nWhat do you do?\n"
    
    first_choice = raw_input(">")

    if first_choice == "a":
        ride()
    elif first_choice =="b":
        tickets()
    else:
        if first_choice =="c":
            friends()

    print "Thanks for playing!\n"

    print "Press 'q' to quit."

    sixth_choice = raw_input(">")

    if sixth_choice =="q":
        exit()
    return 0;


def ride():
    global victory
    print "Alright, you can:\nA.) Take the bus \nB.) Steal a car \nC.) Beg your ex for a lift. \nWhich is the best bad idea?\n"
    second_choice = raw_input(">")
    if second_choice == "a":
        print "Great, you made it to the show! Too bad you forgot your friends. \nBetter go back for them.\n"
        victory = victory + 1
        time.sleep(3)
        main()
    elif second_choice =="b":
        print "Dang, this Pinto is the only car around. Guess I'll have to see if I get her going. \nI hope I don't blow up.\nYou blew up.\n"
        time.sleep(3)
        main()
    else:
        if second_choice =="c":
            print "Phone goes straight to voicemail. \nMust be on a date...Maybe I should start walking, but I'll never make it in time!\n"
            time.sleep(3)
            main()
    return victory;


    

def tickets():
    global victory
    print "Let's find a ticket!\nDo you want to: \nA.) Meet the scalper from Craigslist \nB.) Pick up friends instead and hope one of them has an extra ticket \nC.) Fight The Man! I'm sneaking in.\n"
    third_choice = raw_input(">")
    if third_choice =="a":
        print "You meet the scalper in a dimly lit parking lot. \nHe doesn't have any tickets, but now he does have your wallet.\n"
        time.sleep(3)
        main()
    elif third_choice =="b":
        print "Relying on friends, eh? You're supposed to be the responsible one of the bunch. \nOdds are not in your favor.\n"
        time.sleep(3)
        main()
    else:
        if third_choice == "c":
            print "You made it! Front row!\n"
            victory += 1
            time.sleep(3)
            main()
    return victory;



def friends():
    global victory       
    print "Let's get the band back together!\nWho should we pick up first? \nA.) Jade, working at the record store. \nB.) Tommy, at his mom's house. \nC.) Try to find Bart.\n"
    fourth_choice = raw_input(">")

    if fourth_choice =="a":
        print "Jade puts on a Pink Floyd album to mellow out. \nYou get a little too mellow and sleep through the show.\n"
        time.sleep(3)
        main()

    elif fourth_choice =="b":
        print "Tommy's mom has made pizza, but only offers it to you if you agree to be home by 11:00pm. \nDo you accept? \nA.) Yes, but we might miss the encore. \nB.) No, but what are we gonna do?"

        fifth_choice = raw_input(">")

        if fifth_choice =="a":
            print "Good call! The band no longer rocks as hard as they used to and the show was over by 10:30.\n"
            victory += 1
            time.sleep(3)
            main()

        else:
            if fifth_choice =="b":
                print "Without snacks you ran out of energy trying to get to the show.\n"
                time.sleep(3)
                main()

    else:
        if fourth_choice =="c":
            print"Bart's nowhere to be found and you lost track of time and missed the show.\nThis was the farewell tour!\n"
            time.sleep(3)
            main()
        
    return victory;
  

main()
