import PySimpleGUI as sg

class Status():
    name = "名無さん"
    gender = ""
    old = 20
    height = 160.0
    weight = 50.0

    def set(self, values):
        if (values["input_name"]):
            self.name = values["input_name"]
        if (values["input_gender"] != "男性" and values["input_gender"] != "女性"):
            self.gender = "不明"
        else :
            self.gender = values["input_gender"]
        self.old = values["input_old"]
        self.height = values["input_height"]
        self.weight = values["input_weight"]

status = Status()

def signUpPage():
    frame1 = sg.Frame('',
        [
            #名前入力
            [
                sg.Text('名前を入力してください', font=('メイリオ',20))
            ],
            [
                sg.Text("名前", font=('メイリオ',20)),
                sg.InputText('', key='input_name', enable_events=True,size=(20,3)), 
            ],
            #性別入力
            [
                sg.Text('性別を入力してください', font=('メイリオ',20))
            ],
            [
                sg.Text("性別", font=('メイリオ',20)),
                sg.Combo(["男性","女性"], default_value="選択してください", key='input_gender', size=(30,1), enable_events=True,  readonly=True,)
            ],
            #年齢入力
            [
                sg.Text('年齢を入力してください', font=('メイリオ',20), key="inst_old")
            ],
            [
                sg.Text("年齢", font=('メイリオ',20)),
                sg.InputText('', key='input_old', enable_events=True,size=(10,3)), 
                sg.Text("歳", font=('メイリオ',20)),
            ],
            #身長入力
            [
                sg.Text('身長を入力してください', font=('メイリオ',20), key="inst_height")
            ],
            [
                sg.Text("身長", font=('メイリオ',20)),
                sg.InputText('', key='input_height', enable_events=True,size=(15,3)), 
                sg.Text("cm", font=('メイリオ',20))
            ],
            #体重入力
            [
                sg.Text('体重を入力してください', font=('メイリオ',20), key="inst_weight")
            ],
            [
                sg.Text("体重", font=('メイリオ',20)),
                sg.InputText('', key='input_weight', enable_events=True,size=(15,3)), 
                sg.Text("kg", font=('メイリオ',20))
            ],
            #登録完了ボタン
            [
                sg.Submit(button_text='登録',
                        font=('メイリオ',8),size=(8,3),key='-enroll-')
            ]
        ], size=(1000, 700),relief=sg.RELIEF_FLAT
    )

    layout =  [[frame1]]
    
    return sg.Window("情報登録", layout, finalize=True, resizable=True)

def caloriePage():
    frame1 = sg.Frame("カロリー計算",
        [
            #MED入力
            [
                sg.Text('運動強度(METs)を数値で入力してください', font=('メイリオ',20))
            ],
            [
                sg.Text("運動強度(METs)", font=('メイリオ',20)),
                sg.InputText('', key='input_METs', enable_events=True, size=(5,1))
            ],
            #運動時間入力
            [
                sg.Text('運動時間を入力してください', font=('メイリオ',20))
            ],
            [
                sg.Text("運動時間", font=('メイリオ',20)),
                sg.InputText('', key='input_hour', enable_events=True, size=(5,1)), 
                sg.Text("時間", font=('メイリオ',20)),
                sg.InputText('', key='input_minute', enable_events=True,size=(5,1)), 
                sg.Text("分", font=('メイリオ',20))
            ],
            #計算ボタン
            [
                sg.Submit(button_text='計算',
                        font=('メイリオ',8),size=(8,3),key='-calcurate-')
            ],
            #計算結果
            [
                sg.Text('', key="result"),
            ],
        ], size=(500, 700),relief=sg.RELIEF_FLAT,font=('Noto Serif CJK JP',30)
        )

    frame2 = sg.Frame('登録情報', 
    [
        [
            sg.Text("名前: " + status.name, font=('メイリオ',20))
        ],
        [
            sg.Text("年齢: " + status.old, font=('メイリオ',20))
        ],
        [
            sg.Text("性別: " + status.gender, font=('メイリオ',20))
        ],
        [
            sg.Text("身長: " + status.height, font=('メイリオ',20))
        ],
        [
            sg.Text("体重: " + status.weight, font=('メイリオ',20))
        ],
    ], size=(500,700),relief=sg.RELIEF_FLAT,font=('Noto Serif CJK JP',30)
    )

    layout =  [[frame1, frame2]]
    
    return sg.Window("カロリー計算", layout, finalize=True, resizable=True)

def main():

    #先程確認して決めたテーマカラーを設定
    sg.theme('BlueMono')

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
        
        # 登録ボタンが押された時の処理
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
            window = caloriePage()
        
        elif event == "-calcurate-":
            window["result"].Update('100 kcal')
    window.close()

if __name__ == "__main__":
    main()