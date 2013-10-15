from random import randint
player = 0
comp = 0
turn = 0
crimenum = 1
print "Welcome to the Prisoner's Dilemma"
print "You and your partner have been caught on a bank robbing spree. You are sequestered in separate interogation rooms. You will each be given the chance to confess to or deny each individual robbery on your 30-bank spree. If you both deny a crime you will each receive one year added to your sentences. If you both confess to a crime you will each receive 2 years added to your sentences. If one of you confesses and the other does not the confessor will have 0 years added to his sentence while his partner receives 3 more years."

for turn in range(1, 31):
    print "Crime #" + str(crimenum)
    ratornot = raw_input("Do you confess to this crime?")
    def randomnum():
        return randint(0,2)
    if ratornot == "Yes" or ratornot == "yes" or ratornot == "No" or ratornot == "no":
        if randomnum() == 0 and (ratornot == "Yes" or ratornot == "yes"):
            player = player + 2
            comp = comp + 2
            crimenum = crimenum + 1
            print "Both you and your partner confessed. You both receive 2 year sentences."
            print "Your Sentence: " + str(player)
            print "Partner's Sentence: " + str(comp)
            
        elif randomnum() == 0 and (ratornot == "No" or ratornot == "no"):
            player = player + 2
            comp = comp + 2
            crimenum = crimenum + 1
            print "Your opponent has confessed. You receive 3 years. He receives no sentence."
            print "Your Sentence: " + str(player)
            print "Partner's Sentence: " + str(comp)
                
        elif randomnum()== 1 and (ratornot == "Yes" or ratornot == "yes"):
            player = player + 0
            comp = comp + 3
            crimenum = crimenum + 1
            print "You confessed and your partner denied the crime. He receives 3 years. You receive no sentence."
            print "Your Sentence: " + str(player)
            print "Partner's Sentence: " + str(comp)
                
        elif randomnum() == 1 and (ratornot == "No" or ratornot == "no"):
            player = player + 1
            comp = comp + 1
            crimenum = crimenum + 1
            print "Both you and your opponent denied the crime. You each receive 1 year."
            print "Your Sentence: " + str(player)
            print "Partner's Sentence: " + str(comp)
    else:
        print "Please enter Yes or No."#!/usr/bin/env python

