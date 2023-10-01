import PySimpleGUI as sg

def mainPage(status):
    frame1 = sg.Frame("カロリー計算",
        [
            #MED入力
            [
                sg.Text('運動強度(METs)を数値で入力してください', font=('メイリオ',20),key="inst_METs")
            ],
            [
                sg.Text("運動強度(METs)", font=('メイリオ',20)),
                sg.InputText('', key='input_METs', enable_events=True, size=(5,1))
            ],
            #運動時間入力
            [
                sg.Text('運動時間を入力してください', font=('メイリオ',20),key="inst_time")
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
                sg.Text('', key="result",font=('メイリオ',20)),
            ],
        ], size=(800, 700),relief=sg.RELIEF_FLAT,font=('Noto Serif CJK JP',30)
    )

    frame2 = sg.Frame('登録情報', 
    [
        [
            sg.Text("名前: " + status.name, font=('メイリオ',20))
        ],
        [
            sg.Text("年齢: " + status.old + " 歳", font=('メイリオ',20))
        ],
        [
            sg.Text("性別: " + status.gender, font=('メイリオ',20))
        ],
        [
            sg.Text("身長: " + status.height + " cm", font=('メイリオ',20))
        ],
        [
            sg.Text("体重: " + status.weight + " kg", font=('メイリオ',20))
        ],
    ], size=(300,700),relief=sg.RELIEF_FLAT,font=('Noto Serif CJK JP',30)
    )
    layout =  [[frame1, frame2]]
    
    return sg.Window("カロリー計算", layout, finalize=True)
