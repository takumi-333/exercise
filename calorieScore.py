import math
def CalorieScore(goal,cal):
    if(goal >= cal):
        score = (cal / goal) * 9000
    
    else:
        score = 9000 + (cal - goal)/3
    
    return math.floor(score)