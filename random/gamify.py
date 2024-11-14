def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health, time
    
    global bored_with_stars
    global tired
    global hedons_per_min 
    global star
    global starcounter
    global star_activity, star_timer, star_timer2
    
    cur_hedons = 0
    cur_health = 0
    hedons_per_min = 0
    star = False
    starcounter = 0
    star_activity = None
    star_timer = -100
    star_timer2 = -100
    time = 0
    
    bored_with_stars = False
    
    tired = False

            

def star_can_be_taken(activity):
    global starcounter, star_activity, star_timer, star_timer2, time
    if (time - star_timer2) < 120:
        return False
    else:
        return True

#cur_minutes = 0
# jump for 5 minutes
## cur_minutes is now 5
#time of last non rest activity is 5# rest for 2 minutes
## cur_minutes is now 7

def get_hedons_per_min(activity):
    global hedons_per_min, star_activity, star, tired
    if activity == "running":
        if tired == False:
            hedons_per_min = 2
        else:
            hedons_per_min = -2
    elif activity == "textbooks":
        if tired == False:
            hedons_per_min = 1
        else:
            hedons_per_min = -2
    if star_activity == activity and star == True and star_can_be_taken(activity) == True:
        hedons_per_min += 3
    return hedons_per_min
        
        
def perform_activity(activity, duration):
    global cur_hedons, cur_health, tired, star, time, star_activity, star_timer, star_timer2
    time += duration
    hedons_per_min = get_hedons_per_min(activity)
    
    if star_can_be_taken == False:
        star = False
    if activity == "running":
        if duration > 180:
            cur_health += 180 * 3
            cur_health += (duration - 180)
        elif duration <= 180:
            cur_health += duration * 3
         
        if duration < 10:
                cur_hedons += hedons_per_min * duration
        else:
            if star == True and star_activity == "running":
                if tired == False:
                    cur_hedons += hedons_per_min * 10
                    cur_hedons += (hedons_per_min - 7) * (duration - 10)
                else:
                    cur_hedons += hedons_per_min * 10
                    cur_hedons -= 2 * (duration - 10)
                    
                star_activity = None
            else:
                if tired == False:
                    cur_hedons += hedons_per_min * 10
                    cur_hedons -= hedons_per_min * (duration - 10)
                else:
                    cur_hedons += hedons_per_min * duration
    tired = True
                
    if activity == "textbooks":
        cur_health += duration * 2
    
        if star == True and star_activity == "textbooks":
            if tired == False:
                if duration <= 10:
                    cur_hedons += hedons_per_min * duration
                elif duration <= 20:
                    cur_hedons += hedons_per_min * 10
                    cur_hedons += (hedons_per_min - 3) * (duration - 10)
                else:
                    cur_hedons += hedons_per_min * 10
                    cur_hedons += (hedons_per_min - 3) * (10)
                    cur_hedons -= (duration - 20)
                    
            else:
                if duration <= 10:
                    cur_hedons += hedons_per_min * duration
                else:
                    cur_hedons += hedons_per_min * 10
                    cur_hedons += (hedons_per_min - 3) * (duration - 10)
            star_activity = None
        else:
            if tired == False:
                if duration > 20:
                    cur_hedons += hedons_per_min * 20
                    cur_hedons -= hedons_per_min * (duration - 20)
            else:
                cur_hedons += hedons_per_min * duration
    tired = True
            
    if activity == "resting" and duration >= 120:
        current_activity = "resting"
        tired = False
        
    star = False

def get_cur_hedons():
    return cur_hedons
    
def get_cur_health():
    return cur_health
    
def offer_star(activity):
    global star_activity, star, star_timer, star_timer2
    if star_can_be_taken(activity) == True:
        star_activity = activity
        star = True
        star_timer2 = star_timer
        star_timer = time
        return star_activity
    else:
        star = None
    

    
        
def most_fun_activity_minute():
    global cur_hedons, cur_health, tired, star, time, star_activity
    rest = 0
    run = get_hedons_per_min("running")
    text = get_hedons_per_min("textbooks")
    if rest > run and rest > text:
        return "resting"
    elif run > text and run > rest:
        return "running"
    else:
        return "textbooks"
    

################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    
def get_effective_minutes_left_health(activity):
    pass    

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass
            

def estimate_health_delta(activity, duration):
    pass
        
################################################################################
        
if __name__ == '__main__':
    initialize()
    '''perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
    '''
    perform_activity("running", 20)
    offer_star("running")
    perform_activity("running", 10)
    offer_star("running")
    perform_activity("running", 10)
    offer_star("running")
    perform_activity("running", 10)
    print(get_cur_hedons())  # Expected: 10 (only from first star)
    
    