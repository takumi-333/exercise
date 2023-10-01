import PySimpleGUI as sg

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
