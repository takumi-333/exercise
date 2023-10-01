class calorieData():
    calorie_data = {"male":{18:1500,29:1520,49:1530,69:1400,150:1290},
                    "female":{18:1100,29:1110,49:1150,69:1100,150:1020}}
    
    def calorie_gorl_score(self,gender,age):
        if(age <= 18):
            ageData = 18
        elif(age <= 29):
            ageData = 29
        elif(age <= 49):
            ageData = 49
        elif(age <= 69):
            ageData = 69
        else:
            ageData = 150

        GoalCal = self.calorie_data[gender][ageData]
        
        return GoalCal