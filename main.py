''' story exposition: you are in the middle of a wasteland, escape by navigating
through different circumstances and collect materials'''

''' set up all the variables and numbers, including x and y coordinates to 
simulate a 2 dimentional space, you health which is set to 5, your stamina 
which is set to 8, and also an inventory which holds the things you gather'''

# while loop:
   
    # allow input for move forward, backwards, left, and right
    # allow input for attack, search, hide, defend, use, inventory and quit
    # increase x by 1 if right, focus -1 
    # increase y by 1 if forward, focus -1
    # increase x by -1 if left, focus -1 
    # increase y by -1 if right, focus -1
        
        # if x and y both equal to 1, -2, or -2
            # attackers appear and try to kill you
            # if you say attack
                # they take 2 damage, you take 1
                # if their health reaches 0
                    # they die and this location will be cleared
            # if you say defend
                ''' they take no damage, you take 0.5 but the next attack you do 
                doubles in damage'''
            # if you say hide
                # if your focus is below 5:
                    # they find you and you take 4 damage
                # if your focus is above 5:
                    ''' they can't find you and you walk away free but the point 
                    don't get cleared, also gain 1 health and 1 focus''' 
            # if you say anything else
                # says invalid action or can't be done as of right now
        
        # if coordinates equals to either (-1,0) or (3,-3)
            # loot on the ground
            # if you say search
                # if the coords is (-1, 0)
                    '''you get a monke bar(+2 health and focus), a first aid(
                    full health and focus) and 2 water bottle(each +2 focus)'''
                # if the coords is (3, -3)
                    # you get a key 
        
        # if the coords is (0, -3)
        '''a door appears in front of you,if you can open it you are sure you 
        will find salvation, but do you have the key?'''
            # if you have a key
                # you win the game
            # if you don't 
                # the door is locked, need key
    
    '''if your input is inventory while not at a special location, shows 
    everything in inventory along with your health, your focus stays hidden'''    
    ''' you can use items by opening the inventory any time if you are not in a 
    special location'''   
            
    # if your health reaches 0 you die, end loop
    # if your focus reaches 0 you die, end loop    
    # if your input is quit, end loop        
           
            
            
            
            
            
            