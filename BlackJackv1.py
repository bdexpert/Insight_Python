from random import choice as rc
def total(inhand):
    # figure out num aces in hand
    aces = inhand.count(11)
    # aces are considered 11 or 1
    sumtotal = sum(inhand)
    # sum is over 21 but switch the ace to 1
    if sumtotal > 21 and aces > 0:
        while aces > 0 and sumtotal > 21:
            sumtotal -= 10
    return sumtotal
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cwin = 0  # computer counter
pwin = 0  # player counter
nchips = 100 # number of chips to begin with

while True:
    if nchips >= 1:
        nchips -= 1
    else:
        print "You do not have enough balance to continue playing."
        break
    playchipshand = 1 # number of chips bet on a hand
    print "Your initial stake for this hand is 1 chip. You now have %d chips on hand" % (nchips)
    print
    player = []
    # start with 2 cards
    player.append(rc(cards))
    player.append(rc(cards))
    pbust = False  # player busted flag
    cbust = False  # computer busted flag
    while True:
        # player's turn ...
        tp = total(player)
        print "The player has these cards %s with a total value of %d" % (player, tp)
        if tp > 21:
            print "**** Player loses! ****"
            pbust = True
            break
        elif tp == 21:
            print "Player wins **** BLACKJACK!!! ****"
            break
        else:
            inp = raw_input("Play next (y or n): ").lower()
            if 'y' in inp:
                print
                print "You have %d chips on hand. Increase stakes?" % (nchips)
                inpchips = raw_input("Enter Amount: ")
                if inpchips == "":
                    inpchips = 0
                playchips = int(inpchips)
                
                if playchips <= nchips:
                    nchips = nchips - playchips
                    playchipshand = playchipshand + playchips 
                    player.append(rc(cards))
                else:
                    print "You do not have the amount on hand."
                    break
            else:
                break
    while True:
        # computer's turn
        comp = []
        comp.append(rc(cards))
        comp.append(rc(cards))
        while True:
            tc = total(comp)                
            if tc < 21:
                comp.append(rc(cards))
            else:
                break
        print "Computer has %s with a sum total of %d" % (comp, tc)
        # to find out the winner ...
        if tc > 21:
            print "**** Computer loses!****"
            cbust = True
            if pbust == False:
                nchips = nchips + playchipshand*2
                print "You win! %d chip(s)" % (playchipshand*2) # player wins double the amount he bet
                pwin += 1
                
        elif tc > tp:
            print "Computer wins!"
            cwin += 1
        elif tc == tp:
            print "It's a draw!"
        elif tp > tc:
            if pbust == False:
                print "You win!"
                pwin += 1
            elif cbust == False:
                print "Computer wins!"
                cwin += 1
        break
    print
    print "Wins, player = %d  computer = %d" % (pwin, cwin)
    print "chips on hand = %d" % (nchips)
    exit = raw_input("Press Enter (q to quit): ").lower()
    if 'q' in exit:
        break
    print
print
print "Thanks for playing!"
