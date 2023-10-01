import PySimpleGUI as sg
import math
from main_page import mainPage
from sign_up_page import signUpPage
from calc_calorie import calc_calorie
from log_background import log_data
from calorieScore import CalorieScore
from calorie_score_data import calorieData

def handleTime(hour, minute):
    time = float(hour) + float(minute)/60
    return time

class Status():
    name = "名無さん"
    gender = ""
    old = 20
    height = 160.0
    weight = 50.0

    def set(self, values):
        if values["input_name"]:
            self.name = values["input_name"]
        if values["input_gender"] != "男性" and values["input_gender"] != "女性":
            self.gender = "不明"
        else:
            self.gender = values["input_gender"]
        self.old = values["input_old"]
        self.height = values["input_height"]
        self.weight = values["input_weight"]

status = Status()
logData = log_data()
cd = calorieData()

def main():

    #先程確認して決めたテーマカラーを設定
    sg.theme('BlueMono')


    #GUIタイトルと全体レイアウトをのせたWindowを定義する
    window = signUpPage()
    window.Maximize()
    goal = 0
    #GUI表示実行部分
    while True:
        # ウィンドウ表示
        event, values = window.read()

        #クローズボタンの処理
        if event is None:
            print('exit')
            break
        elif event == "-enroll-":
            if not values["input_old"].isdigit():
                window["input_old"].Update('')
                window["inst_old"].Update('年齢を入力してください(数値じゃなければいけません)')
                continue
            elif not values["input_height"].isdigit():
                window["input_height"].Update('')
                window["inst_height"].Update('身長を入力してください(数値じゃなければいけません)')
                continue
            elif not values["input_weight"].isdigit():
                window["input_weight"].Update('')
                window["inst_weight"].Update('体重を入力してください(数値じゃなければいけません)')
                continue
            status.set(values)
            goal = cd.calorie_goal_score(status.gender,status.old)
            window.close()
            window = mainPage(status)
            window.Maximize()
            window["goal"].Update("Goal: " + str(goal) + " kcal")
        elif event == "-calcurate-":
            if not values["input_METs"].isdigit():
                window["input_METs"].Update('')
                window["inst_METs"].Update('運動強度(METs)を数値で入力してください(数値じゃなければいけません)')
                continue
            elif not values["input_hour"].isdigit():
                window["input_hour"].Update('')
                window["inst_time"].Update('運動時間を入力してください(整数じゃなければいけません)')
                continue
            elif not values["input_minute"].isdigit():
                window["input_minute"].Update('')
                window["inst_time"].Update('運動時間を入力してください(整数じゃなければいけません)')
                continue
            #カロリー計算
            calorie = calc_calorie(float(values["input_METs"]),
            float(handleTime(values["input_hour"],values["input_minute"])),
            float(status.weight))

            #ログに格納
            logData.store_data(calorie)
            score = CalorieScore(goal, logData.total_cal)

            log_str = ""
            for d in logData.cal_data:
                log_str = log_str+ str(d) + " kcal\n"
            window["input_METs"].Update('')
            window["input_hour"].Update('')
            window["input_minute"].Update('')
            window["inst_time"].Update('運動時間を入力してください')
            window["inst_METs"].Update('運動強度(METs)を数値で入力してください')
            window["result"].Update(log_str)
            window["score"].Update("Score: " + str(score))
            window["total_calorie"].Update('消費カロリー: ' + str(math.floor(logData.total_cal*10)/10) + " kcal")
    window.close()

if __name__ == "__main__":
    main()