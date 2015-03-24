import simplegui
import random
#Battle the Kraken  

print
print"The Kraken is attacking your ship, try to guess the cannon to fire to hit it"
    
    
    
def new_game():
    global health
    health=20
    global kraken_health
    kraken_health=8
    print
    print 
    print
    print 

    print "new game started"
    print
    print
    print 
    print
    print 
    print
    print
    print
    print
    print 
    print
    print 
    print
    print
    print
    print
    print 
    print
    print 
    print
    print
    print
        
new_game()        
        
        
def hit():
    global swing
    global kraken_health
    global health
    swing=random.randint(1,4)
    if kraken_health>0 and health>0:
        
    
    
    
        if swing==cannon:
            print
            print "Kraken Hit!!"
            kraken_health=kraken_health-1
            print
            print "Kraken health is "+ str(kraken_health)
        else:
            print
            print "Kraken Missed!! Ship Damaged!"
            health=health-1
            print
            print"Ship Health is "+str(health)
    elif kraken_health<=0:
        print
        print "Kraken killed, you win!!!"
    else:
        print
        print "Your ship sank, hit new game to try again"

def cannon4():
    global cannon
    cannon=4
    hit()
def cannon3():
    global cannon
    cannon=3
    hit()
def cannon2():
    global cannon
    cannon=2
    hit()
def cannon1():
    global cannon
    cannon=1
    hit()
frame= simplegui.create_frame("Battle", 200, 200)
frame.add_button("cannon 1", cannon1, 100)
frame.add_button("cannon 2", cannon2, 100)
frame.add_button("cannon 3", cannon3, 100)
frame.add_button("cannon 4", cannon4, 100)

frame.add_button("New Game", new_game, 100)
