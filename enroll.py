import PySimpleGUI as sg
from enum import Enum

class Gender(Enum):
    Male = 1
    Female = 2

class Status():
    name = ""
    gender = Gender.Male
    old = 20
    height = 160.0
    weight = 50.0

    def set(self, values):
        self.name = values["input_name"]
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
                sg.Text('名前を入力してください', font=('メイリオ',12))
            ],
            [
                sg.Text("名前"),
                sg.InputText('', key='input_name', enable_events=True), 
            ],
            #性別入力
            [
                sg.Text('性別を入力してください', font=('メイリオ',12))
            ],
            [
                sg.Text("性別"),
                sg.Combo(["男性","女性"], default_value="選択してください", key='input_gender', size=(30,1), enable_events=True,  readonly=True,)
            ],
            #年齢入力
            [
                sg.Text('年齢を入力してください', font=('メイリオ',12), key="inst_old")
            ],
            [
                sg.Text("年齢"),
                sg.InputText('', key='input_old', enable_events=True,), 
                sg.Text("歳"),
            ],
            #身長入力
            [
                sg.Text('身長を入力してください', font=('メイリオ',12), key="inst_height")
            ],
            [
                sg.Text("身長"),
                sg.InputText('', key='input_height', enable_events=True,), 
                sg.Text("cm")
            ],
            #体重入力
            [
                sg.Text('体重を入力してください', font=('メイリオ',12), key="inst_weight")
            ],
            [
                sg.Text("体重"),
                sg.InputText('', key='input_weight', enable_events=True,), 
                sg.Text("kg")
            ],
            #登録完了ボタン
            [
                sg.Submit(button_text='登録',
                        font=('メイリオ',8),size=(8,3),key='enroll')
            ]
        ], size=(1000, 700)
    )

    layout =  [[frame1]]
    
    return sg.Window("情報登録", layout, finalize=True)

def caloriePage():
    frame1 = sg.Frame('',
        [
            #MED入力
            [
                sg.Text('運動強度(METs)を数値で入力してください', font=('メイリオ',12))
            ],
            [
                sg.Text("運動強度(METs)"),
                sg.InputText('', key='input_METs', enable_events=True, size=(5,1))
            ],
            #運動時間入力
            [
                sg.Text('運動時間を入力してください', font=('メイリオ',12))
            ],
            [
                sg.Text("運動時間"),
                sg.InputText('', key='input_hour', enable_events=True, size=(5,1)), 
                sg.Text("時間"),
                sg.InputText('', key='input_minite', enable_events=True,size=(5,1)), 
                sg.Text("分")
            ],
            [
                sg.Text("名前" + status.name),
                sg.Text("年齢" + status.old),
                sg.Text("性別" + status.gender),
                sg.Text("身長" + status.height),
                sg.Text("体重" + status.weight),
            ]
        ], size=(1000, 700)
    )

    layout =  [[frame1]]
    
    return sg.Window("カロリー計算", layout, finalize=True)

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
        elif event == "enroll":
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
    window.close()

if __name__ == "__main__":
    main()