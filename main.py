import PySimpleGUI as sg
from main_page import mainPage
from sign_up_page import signUpPage
from calc_calorie import calc_calorie

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

def main():

    #先程確認して決めたテーマカラーを設定
    sg.theme('BlueMono')

    """
    ・sg.Imageで画像部品をのせられる
    ・sg.Textでテキスト部品をのせられる
    ・sg.InputTextでテキスト入力エリアをのせる(画像Pathを表示させる部分)
    ・sg.FileBrowseでWindowsでよく見るファイル選択画面を出せる(InputTextの横に置けばtextを自動入力してくれる)
    ・sg.Submitはいわゆる「決定ボタン」。今回はOCR開始ボタンとして使った
    ・sg.MLineはテキスト出力エリア
    ・keyは、後でイベントを追加する時に参照する変数名
    ・後は省略できるが、サイズやフォントも各命令で指定出来る
    """

    #GUIタイトルと全体レイアウトをのせたWindowを定義する
    window = signUpPage()

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
                window["inst_old"].Update('年齢を入力してください(整数じゃなければいけません)')
                continue
            elif not values["input_height"].isdigit():
                window["input_height"].Update('')
                window["inst_height"].Update('年齢を入力してください(整数じゃなければいけません)')
                continue
            elif not values["input_weight"].isdigit():
                window["input_weight"].Update('')
                window["inst_weight"].Update('年齢を入力してください(整数じゃなければいけません)')
                continue
            status.set(values)
            window.close()
            window = mainPage(status)
        elif event == "-calcurate-":
            print(type(values["input_METs"]))
            print(values["input_hour"])
            print(values["input_minute"])
            calorie = calc_calorie(float(values["input_METs"]),
            float(handleTime(values["input_hour"],values["input_minute"])),
            float(status.weight))
            window["result"].Update(str(calorie) + ' kcal')
    window.close()

if __name__ == "__main__":
    main()