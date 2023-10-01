import math

def calc_calorie(mets,time,weight):

    calorie = mets*time*weight*1.05
    calorie = math.floor(calorie * 10) / 10

    return calorie