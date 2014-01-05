from random import *
albums = 0
running = True
cash = 0
wage = 10.25
ads = 0
adCost = 50
hype = 0.05
day = 1
price = 4.99

commands = [["h","lists commands"],["make","makes an album"],
            ["work","works at your job"], ["go","runs a day of business"],
            ["ad","buys an ad"],["display","show your current statistics"],
            ["set","set the price of your albums"],["quit","quit game"]]
def getCommand(albums,cash,wage,ads,adCost,hype,day,price,running):
    cpa = 3.50
    pIn = raw_input("Enter a command, h for command list: ")
    if pIn.lower() == commands[0][0]:
        print commands
    elif pIn.lower() == commands[1][0]:
        if cash >= cpa:
            albums += 1
            cash -= cpa
            print "Made album"
        else:
            print "Not enough cash!"
    elif pIn.lower() == commands[2][0]:
        cash += wage
    elif pIn.lower() == commands[3][0]:
        for i in range(albums):
            if random() <= hype:
                albums -= 1
                cash += price
                print "Sold album"
    elif pIn.lower() == commands[4][0]:
        if cash >= adCost:
            cash-=adCost
            ads += 1
            adCost = ((10*ads)**2)/2.0 + 50
            hype += 0.025
            print "Bought an ad"
        else:
            print "Not enough cash!"
            print "An ad costs: ",adCost
    elif pIn.lower() == commands[5][0]:
        print "Cash: ",cash
        print "Albums: ",albums
        print "Wage: ",wage
        print "Ads: ",ads
        day-=1
    
    #.
    #.
    #.
    elif pIn.lower() == commands[len(commands)-1][0]:
        running = False
    else:
        print "Unknown command :("
        day-=1
    day +=1
    return albums,cash,wage,ads,adCost,hype,day,price,running

while running == True:
    print "Day: ",day
    albums,cash,wage,ads,adCost,hype,day,price,running = getCommand(albums,cash,wage,ads,adCost,hype,day,price,running)
    
