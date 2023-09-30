from enum import Enum
import PySimpleGUI as sg

# def culCalorie(weight, height, old):
#     calorie = ((0.0481 * weight + 0.0234 * height - 0.0138 * old - 0.4235) * 1000 ) / 4186
#     return calorie

def main():
    # weight = input("体重を入力してください")
    # height = input("身長を入力してください")
    # old = input("年齢を入力してください")
    # print("身長 = " + str(height) + "cm")
    
    sg.theme("DarkBlue")

    layout=[[sg.Text("これはPySimpleGUIのテストです。")],
            [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)]]

    window=sg.Window("test",layout)

    while True:
        event,values=window.read()
        if event == sg.WIN_CLOSED:
            break

    #画面を閉じます。
    window.close()

    # gender = Gender.Male
    # if gender == Gender.Male:
    #     print("あなたは男性です")
    # else:
    #     print("あなたは女性です")

if __name__ == "__main__":
    main()