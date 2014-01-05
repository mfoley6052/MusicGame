from random import *
albums = 0
running = True
cash = 0
wage = 10.25
ads = 0
hype = 0.05
day = 0
price = 4.99

commands = [["h","lists commands"],["make","makes an album"],
            ["work","works at your job"], ["go","runs a day of business"],
            ["ad","buys an ad"],["set","set the price of your albums"],
            ["exit","exit game"]]
def getCommand(albums,cash,wage,ads,hype,day,price,running):
    cpa = 0.35
    pIn = raw_input("Enter a command, h for command list: ")
    if pIn.lower() == "h":
        print commands
    elif pIn.lower() == commands[1][0]:
        if cash >= cpa:
            albums += 1
            cash -= cpa
            day += 1
            print "Made album"
            print "Albums: ",albums
        else:
            print "Not enough cash!"
    elif pIn.lower() == commands[2][0]:
        day +=1
        cash += wage
    elif pIn.lower() == commands[3][0]:
        for i in range(albums):
            if random() <= hype:
                albums -= 1
                cash += price
                print "Sold album"
                print "Cash: ",cash
    
    #.
    #.
    #.
    elif pIn.lower() == commands[len(commands)-1][0]:
        running = False
    return albums,cash,wage,ads,hype,day,price,running
        
while running == True:
    albums,cash,wage,ads,hype,day,price,running = getCommand(albums,cash,wage,ads,hype,day,price,running)
    
