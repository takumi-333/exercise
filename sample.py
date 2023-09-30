import PySimpleGUI as sg

def signUpPage():
    frame1 = sg.Frame('',
        [
            # テキストレイアウト
            [
                sg.Text('体重を入力してください', font=('メイリオ',12))
            ],
            #画像選択ボタン ※3つカンマ区切りで書いてるのでこれらが同じ行に配置される
            [
                sg.Text("体重"),
                sg.InputText('', key='-INPUTTEXT-', enable_events=True,), 
                sg.Text("kg")
            ],
            #OCR開始ボタン
            [
                sg.Submit(button_text='消費カロリー計算開始',
                        font=('メイリオ',8),size=(8,3),key='calorie')
            ]
        ], size=(500, 700)
    )
    layout =  [[frame1]]
    
    return sg.Window("情報登録", layout, finalize=True)

def main():

    #先程確認して決めたテーマカラーを設定
    sg.theme('Purple')

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

    window.close()


if __name__ == "__main__":
    main()